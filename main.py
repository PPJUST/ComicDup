"""
2024.01.08调整：哈希值只使用phash，不再使用其他哈希值（影响对比哈希时的字典排序，其他代码未变动）
"""

import os.path
import time

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import satic_function
from config_function import *
from thread_calc_hash import ThreadCalcHash
from thread_check_folder import ThreadCheckFolder
from thread_compare_image import ThreadCompareImage
from thread_extract_image import ThreadExtractImage
from ui.dialog_compare_result import DialogShowComic
from ui.listwidget_folderlist import ListWidgetFolderlist
from ui.ui_main import Ui_MainWindow
from ui.widget_show_comic import WidgetShowComic


class DouDup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        """初始化设置"""
        # 设置初始变量
        self.folder_list = []  # 当前选择的文件夹
        self.start_thread_time = None
        self.similar_group_list = []  # 相似组列表，内部元素为元组
        self.comic_data_dict = {}  # 源文件对应的数据字典 {源文件/文件夹:{preview:..., filetype/image_number/filesize}, ...}

        # 实例化子线程
        self.thread_check_folder = ThreadCheckFolder()
        self.thread_check_folder.signal_schedule_check_folder.connect(self.update_schedule_rate)
        self.thread_check_folder.signal_finished.connect(self.start_check_step_2)

        self.thread_extract_image = ThreadExtractImage()
        self.thread_extract_image.signal_schedule_extract_image.connect(self.update_schedule_rate)
        self.thread_extract_image.signal_finished.connect(self.start_check_step_3)

        self.thread_calc_hash = ThreadCalcHash()
        self.thread_calc_hash.signal_schedule_calc_hash.connect(self.update_schedule_rate)
        self.thread_calc_hash.signal_finished.connect(self.start_check_step_5)

        self.thread_compare_image = ThreadCompareImage()
        self.thread_compare_image.signal_schedule_compare_image.connect(self.update_schedule_rate)
        self.thread_compare_image.signal_finished.connect(self.start_check_step_finished)

        # 设置一个定时器用于更新时间
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_runtime)
        self.timer.setInterval(1000)

        # 添加自定义控件
        self.ui.listWidget_folderlist = ListWidgetFolderlist()
        self.ui.groupBox_folderlist.layout().addWidget(self.ui.listWidget_folderlist)

        # 设置ui
        self.ui.pushButton_stop.setEnabled(False)

        """连接信号与槽函数"""
        self.ui.listWidget_folderlist.signal_folderlist.connect(self.accept_folderlist)
        self.ui.pushButton_start.clicked.connect(self.start_check_step_1)
        self.ui.pushButton_stop.clicked.connect(self.stop_thread)
        self.ui.pushButton_load_result.clicked.connect(self.load_compare_result)
        self.ui.pushButton_refresh_result.clicked.connect(self.refresh_compare_result)

    def accept_folderlist(self, folderlist):
        """接收子控件的信号"""
        satic_function.print_function_info()
        self.folder_list = folderlist

    def get_similar_mode(self):
        """获取当前选择的相似算法"""
        satic_function.print_function_info()
        similar_mode_dict = {}
        # ahash
        if self.ui.checkBox_ahash.isChecked():
            threshold = self.ui.spinBox_threshold_ahash.value()
            similar_mode_dict['ahash'] = threshold
        else:
            similar_mode_dict['ahash'] = False
        # phash
        if self.ui.checkBox_phash.isChecked():
            threshold = self.ui.spinBox_threshold_phash.value()
            similar_mode_dict['phash'] = threshold
        else:
            similar_mode_dict['phash'] = False
        # dhash
        if self.ui.checkBox_dhash.isChecked():
            threshold = self.ui.spinBox_threshold_dhash.value()
            similar_mode_dict['dhash'] = threshold
        else:
            similar_mode_dict['dhash'] = False
        # ssim
        if self.ui.checkBox_ssim.isChecked():
            threshold = self.ui.doubleSpinBox_threshold_ssim.value()
            similar_mode_dict['ssim'] = threshold
        else:
            similar_mode_dict['ssim'] = False
        # 检查图片数
        image_number = self.ui.spinBox_extract_image_number.value()
        similar_mode_dict['image_number'] = image_number

        return similar_mode_dict

    def start_check_step_1(self):
        """原神，启动！"""
        """
        准备工作
        """
        satic_function.print_function_info()
        # 设置启动时间
        self.start_thread_time = time.time()
        self.timer.start()
        # 更新运行时间0:00
        self.ui.label_schedule_time.setText('0:00')
        # 改变按钮状态
        self.set_start_button_state(mode='start')
        # 清空临时文件夹中的图片
        satic_function.clear_temp_image_folder()
        # 清除上一次的查重结果
        self.ui.treeWidget_show.clear()

        """
        第1步 检查文件夹，提取漫画文件夹和压缩包
        """
        self.ui.label_schedule_step.setText('1/6 检查文件夹')
        # 获取需要检查的文件夹
        check_folder_list = []
        for path in self.folder_list:
            if path != '' and os.path.exists(path):
                check_folder_list.append(path)
        # 提取文件夹中符合要求的文件夹、压缩包
        self.thread_check_folder.set_dirpath_list(check_folder_list)
        self.thread_check_folder.start()
        # 获取的数据
        # comic_dir_dict 格式：{文件夹路径:(排序后的内部图片路径), ...}
        # archive_set 格式：(压缩包路径, ...)

    def start_check_step_2(self, comic_dir_dict, archive_set):
        """
        第2步 提取文件夹和压缩包中的图片
        """
        # comic_dir_dict 格式：{文件夹路径:(排序后的内部图片路径), ...}
        # archive_set 格式：(压缩包路径, ...)
        # 获取相似度算法设置
        similar_mode_dict = self.get_similar_mode()
        need_image_number = similar_mode_dict['image_number']

        self.ui.label_schedule_step.setText('2/6 提取图片')
        self.thread_extract_image.set_comic_dir_dict(comic_dir_dict)
        self.thread_extract_image.set_archive_set(archive_set)
        self.thread_extract_image.set_need_image_number(need_image_number)
        self.thread_extract_image.start()
        # 获取的数据
        # image_data_dict 图片对应的数据字典 {图片文件:{origin_path:...}, ...}
        # comic_data_dict 源文件对应的数据字典 {源文件/文件夹:{preview:..., filetype/image_number/filesize}, ...}

    def start_check_step_3(self, comic_data_dict, image_data_dict):
        """
        第3步 提取已有图片缓存
        """
        # image_data_dict 图片对应的数据字典 {图片文件:{origin_path:...}, ...}
        # comic_data_dict 源文件对应的数据字典 {源文件/文件夹:{preview:..., filetype/image_number/filesize}, ...}

        self.comic_data_dict = comic_data_dict
        self.ui.label_schedule_step.setText('3/6 提取图片特征缓存')
        image_cache_data = satic_function.check_hash_cache()
        self.start_check_step_4(image_data_dict, image_cache_data)

    def start_check_step_4(self, image_data_dict, image_cache_data):
        """
        第4步 计算图片特征
        """
        # 获取相似度算法设置
        similar_mode_dict = self.get_similar_mode()
        mode_ahash = similar_mode_dict['ahash']
        mode_phash = similar_mode_dict['phash']
        mode_dhash = similar_mode_dict['dhash']

        self.ui.label_schedule_step.setText('4/6 计算图片特征')
        self.thread_calc_hash.set_image_data_dict(image_data_dict)
        self.thread_calc_hash.set_comic_cache_data(image_cache_data)
        self.thread_calc_hash.set_mode_hash(mode_ahash, mode_phash, mode_dhash)
        self.thread_calc_hash.start()

    def start_check_step_5(self, image_data_dict):
        """
        第5步 保存图片缓存，只保存源文件为文件夹的图片数据
        """
        self.ui.label_schedule_step.setText('5/6 保存图片缓存')
        save_cache_data = {}  # {图片路径:{'filesize源文件大小':int, 'ahash':'str', ...}...}
        for image, data in image_data_dict.items():
            origin_path = data['origin_path']
            if os.path.isdir(origin_path):
                filesize = os.path.getsize(image)
                ahash = data['ahash']
                phash = data['phash']
                dhash = data['dhash']
                save_cache_data[image] = {'filesize': filesize, 'ahash': ahash, 'phash': phash, 'dhash': dhash}
        satic_function.update_hash_cache(save_cache_data)
        self.start_check_step_6(image_data_dict)

    def start_check_step_6(self, image_data_dict):
        """
        第6步 对比图片特征
        """
        # 获取相似度算法设置
        similar_mode_dict = self.get_similar_mode()
        mode_ahash = similar_mode_dict['ahash']
        mode_phash = similar_mode_dict['phash']
        mode_dhash = similar_mode_dict['dhash']
        mode_ssim = similar_mode_dict['ssim']

        self.ui.label_schedule_step.setText('6/6 对比图片特征')
        self.thread_compare_image.set_image_data_dict(image_data_dict)
        self.thread_compare_image.set_mode_compare(mode_ahash=mode_ahash,
                                                   mode_phash=mode_phash,
                                                   mode_dhash=mode_dhash,
                                                   mode_ssim=mode_ssim)
        self.thread_compare_image.start()
        # 获取的数据
        # similar_group_list 相似组列表 [(源文件1,源文件2), (...)...]

    def start_check_step_finished(self, similar_group_list):
        """
        结束
        """
        self.ui.label_schedule_step.setText('-/- 结束')
        self.ui.label_schedule_rate.setText('-/-')
        self.set_start_button_state(mode='stop')
        self.timer.stop()
        self.similar_group_list = similar_group_list
        # 保存结果到xlsx
        satic_function.save_similar_result(self.similar_group_list, self.comic_data_dict)
        # 保存原始数据到本地
        save_data_pickle(self.similar_group_list, self.comic_data_dict)
        self.show_compare_result()

    def show_compare_result(self):
        """将对比结果显示在ui中"""
        self.ui.treeWidget_show.clear()
        group_number = 0
        for group_turple in self.similar_group_list:
            if len(group_turple) <= 1:  # 无相似的项不显示
                continue
            group_number += 1
            # 创建父节点
            parent_item = QTreeWidgetItem(self.ui.treeWidget_show)
            parent_item.setText(0, f'■ 相似组 {group_number} - {len(group_turple)}项')
            parent_item.setBackground(0, QColor(248, 232, 137))
            # 创建子节点
            child_item = QTreeWidgetItem(parent_item)
            # 创建自定义控件组（ScrollArea->Widget->ComicWidget)
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(30)
            for file in group_turple:
                if os.path.exists(file) and file in self.comic_data_dict:
                    # 提取数据
                    filesize_mb = round(self.comic_data_dict[file]['filesize'] / 1024 / 1024, 2)
                    image_number = self.comic_data_dict[file]['image_number']
                    preview_image = self.comic_data_dict[file]['preview']
                    filetype = self.comic_data_dict[file]['filetype']
                    # 实例化自定义控件
                    widget_comic = WidgetShowComic()
                    widget_comic.signal_del_file.connect(self.accept_signal_del_file)
                    widget_comic.signal_double_click.connect(self.show_dialog_compare_result)
                    # widget_comic.setFixedSize(125, 215)
                    widget_comic.setStyleSheet('{border: 1px solid gray;')
                    widget_comic.set_filepath(file)
                    widget_comic.set_size_and_count(f'{filesize_mb}MB/{image_number}图')
                    widget_comic.set_preview(preview_image)
                    if filetype == 'folder':
                        widget_comic.set_filetype_icon(satic_function.icon_folder)
                    elif filetype == 'archive':
                        widget_comic.set_filetype_icon(satic_function.icon_archive)
                    layout.addWidget(widget_comic)
            scroll_area = QScrollArea()
            scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(widget)
            # 将控件组设置为子节点的单元格部件
            self.ui.treeWidget_show.setItemWidget(child_item, 0, scroll_area)
            # 打开所有父节点
            self.ui.treeWidget_show.expandAll()

    def load_compare_result(self):
        """加载保存的对比结果数据"""
        similar_group_list, comic_data_dict = get_data_pickle()
        self.similar_group_list = similar_group_list
        self.comic_data_dict = comic_data_dict
        self.show_compare_result()

    def refresh_compare_result(self):
        """刷新结果，剔除不存在的项"""
        checked_similar_group_list = []
        for group_turple in self.similar_group_list:
            checked_group_list = []
            for file in group_turple:
                if os.path.exists(file):
                    checked_group_list.append(file)
            checked_similar_group_list.append(tuple(checked_group_list))

        self.similar_group_list = checked_similar_group_list
        self.show_compare_result()

    def set_start_button_state(self, mode='start'):
        """设置开始和停止按钮状态"""
        if mode == 'start':
            self.ui.pushButton_start.setEnabled(False)
            self.ui.pushButton_stop.setEnabled(True)
        elif mode == 'stop':
            self.ui.pushButton_start.setEnabled(True)
            self.ui.pushButton_stop.setEnabled(False)

    def stop_thread(self):
        """停止子线程"""
        pass

    def update_schedule_rate(self, text):
        """刷新运行进度"""
        self.ui.label_schedule_rate.setText(text)

    def update_runtime(self):
        """更新运行时间"""
        current_time = time.time()
        runtime = current_time - self.start_thread_time
        minutes, seconds = divmod(runtime, 60)
        self.ui.label_schedule_time.setText(f'{int(minutes)}:{int(seconds):02d}')

    def show_dialog_compare_result(self, path):
        """显示结果对应dialog"""
        # 找到path对应的相似组
        the_similar_group = None
        for group in self.similar_group_list:
            if path in group:
                the_similar_group = group
                break
        # 实例化dialog
        dialog = DialogShowComic()
        dialog.set_show_path_list(the_similar_group)
        dialog.signal_del_file.connect(self.accept_signal_del_file)
        dialog.exec()

    def accept_signal_del_file(self, path):
        """接收删除文件的路径信号，刷新对应的树状视图中的父节点"""
        # 找父节点对象
        find_index = 0
        find_group = None
        for group_turple in self.similar_group_list:
            if path in group_turple:
                find_group = list(group_turple)
                find_group.remove(path)
                break
            else:
                find_index += 1
        # 同步删除全局变量中的数据
        pre_split = self.similar_group_list[:find_index]
        change_split = [tuple(find_group)]
        after_split = self.similar_group_list[find_index + 1:]
        self.similar_group_list = pre_split + change_split + after_split
        # 清空子节点
        parent_item = self.ui.treeWidget_show.topLevelItem(find_index)
        while parent_item.childCount() > 0:
            child_item = parent_item.takeChild(0)
            del child_item
        # 重新设置子节点的控件
        child_item = QTreeWidgetItem(parent_item)
        # 创建自定义控件组（ScrollArea->Widget->ComicWidget)
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(30)
        for file in find_group:
            # 提取数据
            filesize_mb = round(self.comic_data_dict[file]['filesize'] / 1024 / 1024, 0)
            image_number = self.comic_data_dict[file]['image_number']
            preview_image = self.comic_data_dict[file]['preview']
            filetype = self.comic_data_dict[file]['filetype']
            # 实例化自定义控件
            widget_comic = WidgetShowComic()
            widget_comic.signal_del_file.connect(self.accept_signal_del_file)
            widget_comic.signal_double_click.connect(self.show_dialog_compare_result)
            # widget_comic.setFixedSize(125, 215)
            widget_comic.setStyleSheet('{border: 1px solid gray;')
            widget_comic.set_filepath(file)
            widget_comic.set_size_and_count(f'{filesize_mb}MB/{image_number}图')
            widget_comic.set_preview(preview_image)
            if filetype == 'folder':
                widget_comic.set_filetype_icon(satic_function.icon_folder)
            elif filetype == 'archive':
                widget_comic.set_filetype_icon(satic_function.icon_archive)
            layout.addWidget(widget_comic)
        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(widget)
        # 将控件组设置为子节点的单元格部件
        self.ui.treeWidget_show.setItemWidget(child_item, 0, scroll_area)
        # 打开所有父节点
        self.ui.treeWidget_show.expandAll()


def main():
    check_config()

    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    # 设置白色背景色
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)
    app.setWindowIcon(QIcon('icon/icon.ico'))
    show_ui = DouDup()
    show_ui.show()
    app.exec()


if __name__ == '__main__':
    main()
