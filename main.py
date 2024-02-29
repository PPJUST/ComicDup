# 主程序
import os
import time

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import ICON_START, ICON_STOP, ICON_LOAD, ICON_CACHE, ICON_information, ICON_REFRESH
from module import function_cache_comicdata
from module import function_cache_hash
from module import function_cache_similargroup
from module import function_config
from module import function_normal
from ui.dialog_cache_setting import DialogCacheSetting
from ui.dialog_info import DialogInfo
from ui.listwidget_folderlist import ListWidgetFolderlist
from ui.thread_compare import ThreadCompare
from ui.treewidget_similar_comics import TreeWidgetSimilarComics
from ui.ui_main import Ui_MainWindow


class ComicDup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        """初始化设置"""
        # 初始化
        self.start_time_run = None  # 查重任务开始运行的时间
        function_cache_hash.check_hash_cache_exist()

        # 定时器，用于更新运行时间
        self.timer_runtime = QTimer()
        self.timer_runtime.timeout.connect(self.update_runtime)
        self.timer_runtime.setInterval(1000)  # 刷新时间1秒

        # 添加自定义控件
        self.listWidget_folderlist = ListWidgetFolderlist()
        self.listWidget_folderlist.signal_folderlist.connect(self.drop_folders)
        self.ui.groupBox_folderlist.layout().addWidget(self.listWidget_folderlist)

        self.treeWidget_similar_comics = TreeWidgetSimilarComics()
        self.ui.groupBox_comics.layout().addWidget(self.treeWidget_similar_comics)

        # 实例化子线程
        self.thread_compare = ThreadCompare()
        self.thread_compare.signal_start_thread.connect(lambda: self.set_ui_with_thread_state(state='start'))
        self.thread_compare.signal_finished.connect(self.compare_thread_finished)
        self.thread_compare.signal_schedule_step.connect(self.update_schedule_step)
        self.thread_compare.signal_schedule_rate.connect(self.update_schedule_rate)

        # 设置ui属性
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.spinBox_thread_number.setEnabled(False)
        self.ui.pushButton_refresh_result.setEnabled(False)
        self.ui.pushButton_start.setIcon(QIcon(ICON_START))
        self.ui.pushButton_stop.setIcon(QIcon(ICON_STOP))
        self.ui.pushButton_refresh_result.setIcon(QIcon(ICON_REFRESH))
        self.ui.pushButton_load_result.setIcon(QIcon(ICON_LOAD))
        self.ui.pushButton_cache_setting.setIcon(QIcon(ICON_CACHE))
        self.ui.pushButton_info.setIcon(QIcon(ICON_information))

        self.load_setting()

        """连接信号与槽函数"""
        # 功能
        self.ui.pushButton_start.clicked.connect(self.start_compare_thread)
        self.ui.pushButton_stop.clicked.connect(self.stop_thread)
        self.ui.pushButton_cache_setting.clicked.connect(self.cache_setting)
        self.ui.pushButton_load_result.clicked.connect(self.load_last_compare_result)
        self.ui.pushButton_refresh_result.clicked.connect(self.refresh_compare_result)
        self.ui.pushButton_info.clicked.connect(self.show_info_dialog)
        # 相似度设置
        self.ui.comboBox_hash.currentTextChanged.connect(self.change_mode_hash)
        self.ui.spinBox_threshold_hash.valueChanged.connect(self.change_threshold_hash)
        self.ui.checkBox_ssim.stateChanged.connect(self.change_mode_ssim)
        self.ui.spinBox_threshold_ssim.valueChanged.connect(self.change_threshold_ssim)
        self.ui.spinBox_extract_image_number.valueChanged.connect(self.change_extract_image_number)
        self.ui.spinBox_thread_number.valueChanged.connect(self.change_thread_number)

    @staticmethod
    def drop_folders(folders):
        """接收拖入文件夹的信号"""
        function_normal.print_function_info()
        function_config.reset_select_folders(folders)

    def update_runtime(self):
        """更新运行时间"""
        current_time = time.time()
        runtime = current_time - self.start_time_run
        minutes, seconds = divmod(runtime, 60)
        self.ui.label_schedule_time.setText(f'{int(minutes)}:{int(seconds):02d}')

    def cache_setting(self):
        """打开缓存设置"""
        function_normal.print_function_info()
        self.dialog_cache = DialogCacheSetting()
        self.dialog_cache.signal_start_thread.connect(lambda: self.set_ui_with_thread_state(state='start'))
        self.dialog_cache.signal_compare_cache_finished.connect(self.compare_thread_finished)
        self.dialog_cache.signal_schedule_step.connect(self.update_schedule_step)
        self.dialog_cache.signal_schedule_rate.connect(self.update_schedule_rate)
        self.dialog_cache.exec()

    def start_compare_thread(self):
        """原神，启动！"""
        function_normal.print_function_info()
        # 执行子线程
        self.thread_compare.start()

    def compare_thread_finished(self):
        """相似组匹配子线程结束，执行相关任务"""
        function_normal.print_function_info()
        # 设置ui
        self.set_ui_with_thread_state(state='finish')
        # 将相似组显示在ui上
        self.show_similar_comics()

    def set_ui_with_thread_state(self, state='start'):
        """在线程开始或结束时改变ui"""
        if state == 'start':
            self.treeWidget_similar_comics.clear()
            self.ui.pushButton_start.setEnabled(False)
            self.ui.pushButton_stop.setEnabled(True)
            self.ui.pushButton_cache_setting.setEnabled(False)
            self.ui.pushButton_refresh_result.setEnabled(False)
            self.ui.pushButton_load_result.setEnabled(False)

            self.ui.groupBox_similar.setEnabled(False)
            self.ui.groupBox_folderlist.setEnabled(False)

            self.ui.label_schedule_time.setText('0:00')

            # 启动计时器
            self.start_time_run = time.time()
            self.timer_runtime.start()
        elif state == 'finish':
            self.ui.pushButton_start.setEnabled(True)
            self.ui.pushButton_stop.setEnabled(False)
            self.ui.pushButton_cache_setting.setEnabled(True)
            self.ui.pushButton_refresh_result.setEnabled(True)
            self.ui.pushButton_load_result.setEnabled(True)

            self.ui.groupBox_similar.setEnabled(True)
            self.ui.groupBox_folderlist.setEnabled(True)

            self.ui.label_schedule_step.setText('完成')
            self.ui.label_schedule_rate.setText('-/-')

            # 暂停计时器
            self.timer_runtime.stop()
        elif state == 'stop':
            self.ui.pushButton_start.setEnabled(True)
            self.ui.pushButton_stop.setEnabled(False)
            self.ui.pushButton_cache_setting.setEnabled(True)
            self.ui.pushButton_refresh_result.setEnabled(False)
            self.ui.pushButton_load_result.setEnabled(False)

            self.ui.groupBox_similar.setEnabled(True)
            self.ui.groupBox_folderlist.setEnabled(True)

            self.ui.label_schedule_step.setText('终止')
            self.ui.label_schedule_rate.setText('-/-')

    def load_last_compare_result(self):
        """加载上一次的相似组匹配结果"""
        function_normal.print_function_info()
        # 将相似组显示在ui上
        self.show_similar_comics()

    def refresh_compare_result(self):
        """刷新结果，剔除失效的项"""
        function_normal.print_function_info()
        similar_groups = function_cache_similargroup.read_similar_groups_pickle()
        comics_data = function_cache_comicdata.read_comics_data_pickle()

        checked_similar_groups = []  # 检查后的相似组列表
        for group in similar_groups:
            checked_group = set()  # 检查后的单个相似组
            for comic_path in group:
                if os.path.exists(comic_path):  # 是否存在
                    comic_class = comics_data[comic_path]
                    comic_filesize = comic_class.filesize
                    if function_normal.get_size(comic_path) == comic_filesize:  # 大小是否变化
                        checked_group.add(comic_path)
            if len(checked_group) >= 2:  # 2项以上才添加
                checked_similar_groups.append(checked_group)

        function_cache_similargroup.save_similar_groups_pickle(checked_similar_groups)
        self.show_similar_comics()

    def show_similar_comics(self):
        """将相似漫画显示在ui中"""
        function_normal.print_function_info()
        self.treeWidget_similar_comics.show_comics()

    def stop_thread(self):
        """停止子线程"""
        function_normal.print_function_info()
        # 停止线程任务
        self.thread_compare.code_stop = True
        # 暂停计时器
        self.timer_runtime.stop()
        # 设置ui
        self.set_ui_with_thread_state(state='stop')

    def update_schedule_step(self, text):
        """刷新运行步骤"""
        self.ui.label_schedule_step.setText(text)

    def update_schedule_rate(self, text):
        """刷新运行进度"""
        self.ui.label_schedule_rate.setText(text)

    def load_setting(self):
        """加载设置"""
        function_normal.print_function_info()
        # hash设置
        self.ui.comboBox_hash.setCurrentText(function_config.get_mode_hash())
        self.ui.spinBox_threshold_hash.setValue(function_config.get_threshold_hash_percent())
        # ssim设置
        self.ui.checkBox_ssim.setChecked(function_config.get_mode_ssim())
        self.ui.spinBox_threshold_ssim.setValue(function_config.get_threshold_ssim_percent())
        # 提取图片数
        self.ui.spinBox_extract_image_number.setValue(function_config.get_extract_image_number())
        # 线程数
        self.ui.spinBox_thread_number.setValue(function_config.get_thread_number())
        # 需要检查的文件夹
        self.listWidget_folderlist.add_item(function_config.get_select_folders())

    @staticmethod
    def show_info_dialog():
        """显示说明dialog"""
        dialog = DialogInfo()
        dialog.exec()

    def change_mode_hash(self):
        mode_hash = self.ui.comboBox_hash.currentText()
        function_config.reset_mode_hash(mode_hash)

    def change_threshold_hash(self):
        threshold_hash = self.ui.spinBox_threshold_hash.value()
        function_config.reset_threshold_hash(threshold_hash)

    def change_mode_ssim(self):
        mode_ssim = self.ui.checkBox_ssim.isChecked()
        function_config.reset_mode_ssim(mode_ssim)

    def change_threshold_ssim(self):
        threshold_ssim = self.ui.spinBox_threshold_ssim.value()
        function_config.reset_threshold_ssim(threshold_ssim)

    def change_extract_image_number(self):
        extract_image_number = self.ui.spinBox_extract_image_number.value()
        function_config.reset_extract_image_number(extract_image_number)

    def change_thread_number(self):
        thread_number = self.ui.spinBox_thread_number.value()
        function_config.reset_thread_number(thread_number)


def main():
    function_config.check_config_exist()

    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    # 设置白色背景色
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)
    app.setWindowIcon(QIcon('icon/icon.ico'))
    show_ui = ComicDup()
    show_ui.show()
    app.exec()


if __name__ == '__main__':
    main()
