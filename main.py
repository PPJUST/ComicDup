import os.path
import time

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import satic_function
from thread_run import CompareQthread
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
        self.origin_data_dict = {}  # 原始文件数据字典，key为源文件路径，value为数据的字典

        # 实例化子线程
        self.thread_run = CompareQthread()
        self.thread_run.signal_compare_result.connect(self.accept_compare_result)
        self.thread_run.signal_stop.connect(self.accept_thread_finished)
        self.thread_run.signal_schedule.connect(self.update_schedule)

        # 设置一个定时器用于更新时间
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_thread_run_time)
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
        satic_function.print_function_info()
        # 设置启动时间
        self.start_thread_time = time.time()
        self.timer.start()
        # 更新运行时间0:00
        self.update_schedule('总耗时', '0:00')
        # 改变按钮状态
        self.set_start_button_state(mode='start')
        # 清除上一次的查重结果
        self.ui.treeWidget_show.clear()
        # 获取相似度算法设置
        similar_mode_dict = self.get_similar_mode()
        need_image_number = similar_mode_dict['image_number']
        mode_ahash = similar_mode_dict['ahash']
        mode_phash = similar_mode_dict['phash']
        mode_dhash = similar_mode_dict['dhash']
        mode_ssim = similar_mode_dict['ssim']
        # 清空临时文件夹中的图片
        satic_function.clear_temp_image_folder()
        # 获取需要检查的文件夹
        check_folder_list = []
        for path in self.folder_list:
            if path != '' and os.path.exists(path):
                check_folder_list.append(path)
        # 设置子线程参数
        self.thread_run.reset_var()
        self.thread_run.set_check_folder_list(check_folder_list)
        self.thread_run.set_need_image_number(need_image_number)
        self.thread_run.set_mode_ahash(mode_ahash)
        self.thread_run.set_mode_phash(mode_phash)
        self.thread_run.set_mode_dhash(mode_dhash)
        self.thread_run.set_mode_ssim(mode_ssim)
        # 启动子线程
        self.thread_run.start()

    def accept_thread_finished(self):
        """接收结束子线程的信号"""
        self.set_start_button_state(mode='stop')
        self.timer.stop()

    def accept_compare_result(self, similar_group_list, origin_data_dict):
        """接收子线程的结果，包括一个相似组list和源文件数据dict"""
        # 写入全局变量
        self.similar_group_list = similar_group_list
        self.origin_data_dict = origin_data_dict
        # 保存结果到xlsx
        satic_function.save_similar_result(similar_group_list, origin_data_dict)
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
                filesize_mb = round(origin_data_dict[file]['filesize'] / 1024 / 1024, 2)
                image_number = origin_data_dict[file]['image_number']
                preview_image = origin_data_dict[file]['preview']
                filetype = origin_data_dict[file]['filetype']
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
        self.thread_run.set_stop_code()

    def update_schedule(self, s_type, text):
        """刷新运行进度"""
        if s_type == '总耗时':
            self.ui.label_schedule_time.setText(text)
        elif s_type == '步骤':
            self.ui.label_schedule_step.setText(text)
        elif s_type == '子进度':
            self.ui.label_schedule_rate.setText(text)

    def update_thread_run_time(self):
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
            filesize_mb = round(self.origin_data_dict[file]['filesize'] / 1024 / 1024, 0)
            image_number = self.origin_data_dict[file]['image_number']
            preview_image = self.origin_data_dict[file]['preview']
            filetype = self.origin_data_dict[file]['filetype']
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
