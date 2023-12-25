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

        self.thread_extract_image = ThreadExtractImage()
        self.thread_extract_image.signal_schedule_extract_image.connect(self.update_schedule_rate)

        self.thread_calc_hash = ThreadCalcHash()
        self.thread_calc_hash.signal_schedule_calc_hash.connect(self.update_schedule_rate)

        self.thread_compare_image = ThreadCompareImage()
        self.thread_compare_image.signal_schedule_compare_image.connect(self.update_schedule_rate)

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
        self.ui.pushButton_start.clicked.connect(self.start_check)
        self.ui.pushButton_stop.clicked.connect(self.stop_thread)

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

    def start_check(self):
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
        # 获取相似度算法设置
        similar_mode_dict = self.get_similar_mode()
        need_image_number = similar_mode_dict['image_number']
        mode_ahash = similar_mode_dict['ahash']
        mode_phash = similar_mode_dict['phash']
        mode_dhash = similar_mode_dict['dhash']
        mode_ssim = similar_mode_dict['ssim']
        # 清空临时文件夹中的图片
        satic_function.clear_temp_image_folder()
        # 清除上一次的查重结果
        self.ui.treeWidget_show.clear()
        print('测试节点1')

        """
        第1步 检查文件夹，提取漫画文件夹和压缩包
        """
        self.ui.label_schedule_time.setText('1/4 检查文件夹')
        # 获取需要检查的文件夹
        check_folder_list = []
        for path in self.folder_list:
            if path != '' and os.path.exists(path):
                check_folder_list.append(path)
        print('测试节点2')
        # 提取文件夹中符合要求的文件夹、压缩包
        self.thread_check_folder.set_dirpath_list(check_folder_list)
        self.thread_check_folder.start()
        self.thread_check_folder.wait()
        comic_dir_dict, archive_set = self.thread_check_folder.get_result()
        # comic_dir_dict 格式：{文件夹路径:(排序后的内部图片路径), ...}
        # archive_set 格式：(压缩包路径, ...)
        print('测试节点3')
        """
        第2步 提取文件夹和压缩包中的图片
        """
        self.ui.label_schedule_time.setText('2/4 提取图片')
        self.thread_extract_image.set_comic_dir_dict(comic_dir_dict)
        self.thread_extract_image.set_archive_set(archive_set)
        self.thread_extract_image.set_need_image_number(need_image_number)
        self.thread_extract_image.start()
        self.thread_extract_image.wait()
        comic_data_dict, image_data_dict = self.thread_extract_image.get_result()
        # self.image_data_dict 图片对应的数据字典 {图片文件:{origin_path:...}, ...}
        # self.comic_data_dict 源文件对应的数据字典 {源文件/文件夹:{preview:..., filetype/image_number/filesize}, ...}
        print('测试节点4')
        """
        第3步 提取已有图片缓存
        """
        self.ui.label_schedule_time.setText('3/4 提取图片特征缓存')
        image_cache_data = satic_function.check_hash_cache()
        print('测试节点5')
        """
        第4步 计算图片特征
        """
        print('测试节点6')
        self.ui.label_schedule_time.setText('3/4 计算图片特征')
        self.thread_calc_hash.set_image_data_dict(image_data_dict)
        self.thread_calc_hash.set_comic_cache_data(image_cache_data)
        self.thread_calc_hash.set_mode_hash(mode_ahash, mode_phash, mode_dhash)
        self.thread_calc_hash.start()
        self.thread_calc_hash.wait()
        new_image_data_dict = self.thread_calc_hash.get_result()
        print('测试节点7')
        """
        第5步 保存图片缓存，只保存源文件为文件夹的图片数据
        """
        print('测试节点8')
        self.ui.label_schedule_time.setText('3/4 保存图片缓存')
        save_cache_data = {}  # {图片路径:{'filesize源文件大小':int, 'ahash':'str', ...}...}
        for image, data in new_image_data_dict.items():
            origin_path = data['origin_path']
            if os.path.isdir(origin_path):
                filesize = os.path.getsize(image)
                ahash = data['ahash']
                phash = data['phash']
                dhash = data['dhash']
                save_cache_data[image] = {'filesize': filesize, 'ahash': ahash, 'phash': phash, 'dhash': dhash}
        satic_function.update_hash_cache(save_cache_data)
        print('测试节点9')
        """
        第6步 对比图片特征
        """
        self.ui.label_schedule_time.setText('4/4 对比图片特征')
        self.thread_compare_image.set_image_data_dict(new_image_data_dict)
        self.thread_compare_image.set_mode_compare(mode_ahash=mode_ahash,
                                                   mode_phash=mode_phash,
                                                   mode_dhash=mode_dhash,
                                                   mode_ssim=mode_ssim)
        self.thread_compare_image.start()
        self.thread_compare_image.wait()
        similar_group_list = self.thread_compare_image.get_result()
        print('测试节点10')
        """
        结束
        """
        self.ui.label_schedule_step.setText('-/- 结束')
        self.ui.label_schedule_rate.setText('-/-')
        self.set_start_button_state(mode='stop')
        self.timer.stop()
        # 处理最终结果
        self.deal_compare_result(similar_group_list, comic_data_dict)

    def deal_compare_result(self, similar_group_list, comic_data_dict):
        """接收最终结果，包括一个相似组list和源文件数据dict"""
        # 写入全局变量
        self.similar_group_list = similar_group_list
        self.comic_data_dict = comic_data_dict
        # 保存结果到xlsx
        satic_function.save_similar_result(similar_group_list, comic_data_dict)
        # 显示结果在ui中
        self.ui.treeWidget_show.clear()
        group_number = 0
        for group_turple in similar_group_list:
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
                # 提取数据
                filesize_mb = round(comic_data_dict[file]['filesize'] / 1024 / 1024, 2)
                image_number = comic_data_dict[file]['image_number']
                preview_image = comic_data_dict[file]['preview']
                filetype = comic_data_dict[file]['filetype']
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
