# 主程序ui
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication

from child_thread.thread_group_match_db import ThreadGroupMatchDB
from child_thread.thread_group_normal import ThreadGroupNormal
from child_thread.thread_group_update_db import ThreadGroupUpdateDB
from class_ import class_comic_info
from constant import _ICON_APP
from module import function_config_size
from ui.dialog_information import DialogInformation
from ui.group_result.treeWidget_group import TreeWidgetGroup
from ui.src.ui_main import Ui_MainWindow
from ui.widget_execute import WidgetExecute
from ui.widget_filter_result import WidgetFilterResult
from ui.widget_option import WidgetOption
from ui.widget_schedule import WidgetSchedule
from ui.widget_search_list import WidgetSearchList


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(_ICON_APP))

        # 添加左半边区域自定义控件
        # 执行控件
        self.widget_execute = WidgetExecute()
        self.ui.verticalLayout_functional_area.addWidget(self.widget_execute)
        self.widget_execute.signal_start.connect(self.start)
        self.widget_execute.signal_stop.connect(self.stop)
        self.widget_execute.signal_reload.connect(self.reload_last_result)
        self.widget_execute.signal_information.connect(self.open_information)
        # 搜索文件夹列表控件
        self.widget_search_list = WidgetSearchList()
        self.ui.verticalLayout_functional_area.addWidget(self.widget_search_list)
        # 结果筛选器
        self.widget_filter_result = WidgetFilterResult()
        self.ui.verticalLayout_functional_area.addWidget(self.widget_filter_result)
        self.widget_filter_result.signal_refresh.connect(self.refresh_result)
        self.widget_filter_result.signal_filter_same.connect(self.result_filter_same)
        self.widget_filter_result.signal_filter_pages_diff.connect(self.result_filter_pages_diff)
        self.widget_filter_result.signal_filter_clear.connect(self.result_filter_clear)
        # 算法选项控件
        self.widget_option = WidgetOption()
        self.ui.verticalLayout_functional_area.addWidget(self.widget_option)
        self.widget_option.signal_match_cache.connect(self.match_cache)
        self.widget_option.signal_update_cache.connect(self.update_cache)
        # 进度控件
        self.widget_schedule = WidgetSchedule()
        self.ui.verticalLayout_functional_area.addWidget(self.widget_schedule)

        # 添加右半边区域自定义控件
        self.treeWidget_show_group = TreeWidgetGroup()
        self.ui.verticalLayout_result_area.addWidget(self.treeWidget_show_group)

        # 添加线程组
        # 一般流程线程组
        self.thread_group_normal = ThreadGroupNormal()
        self.thread_group_normal.signal_step.connect(self.update_schedule_total)
        self.thread_group_normal.signal_rate.connect(self.update_schedule_step)
        self.thread_group_normal.signal_finished.connect(self.show_result)
        # 数据库内部匹配线程组
        self.thread_group_match_db = ThreadGroupMatchDB()
        self.thread_group_match_db.signal_step.connect(self.update_schedule_total)
        self.thread_group_match_db.signal_rate.connect(self.update_schedule_step)
        self.thread_group_match_db.signal_finished.connect(self.show_result)
        # 更新数据库线程组
        self.thread_group_update_db = ThreadGroupUpdateDB()
        self.thread_group_update_db.signal_step.connect(self.update_schedule_total)
        self.thread_group_update_db.signal_rate.connect(self.update_schedule_step)
        self.thread_group_update_db.signal_finished.connect(self.finished)

        # 延迟响应控件大小事件的定时器
        self.timer_resize = QTimer(self)
        self.timer_resize.setInterval(500)  # 延迟0.5秒
        self.timer_resize.setSingleShot(True)  # 设置为单次定时器
        self.timer_resize.timeout.connect(self.update_config_size)

    def start(self):
        """开始匹配"""
        # 开始计时
        self.widget_schedule.set_start_time()
        # 禁用部分功能
        self.set_widget_enable(False)
        # 获取搜索列表中的所有路径
        paths = self.widget_search_list.get_paths_showed()
        # 启动线程组
        self.thread_group_normal.start(paths)

    def stop(self):
        """终止匹配"""
        # 结束计时
        self.widget_schedule.stopped()
        # 启用部分功能
        self.set_widget_enable(True)
        # 设置子线程的停止参数
        self.thread_group_normal.stop()
        self.thread_group_match_db.stop()
        self.thread_group_update_db.stop()

    def finished(self):
        """完成匹配"""
        # 结束计时
        self.widget_schedule.finished()
        # 启用部分功能
        self.set_widget_enable(True)

    def match_cache(self):
        """缓存内部匹配"""
        # 开始计时
        self.widget_schedule.set_start_time()
        # 禁用部分功能
        self.set_widget_enable(False)
        # 获取缓存的漫画数据
        comic_info_dict = class_comic_info.read_db()
        comics = list(comic_info_dict.keys())
        # 启动线程组
        self.thread_group_match_db.start(comics)

    def update_cache(self):
        """更新缓存数据"""
        # 开始计时
        self.widget_schedule.set_start_time()
        # 禁用部分功能
        self.set_widget_enable(False)
        # 获取缓存的漫画数据
        comic_info_dict = class_comic_info.read_db()
        comics = list(comic_info_dict.keys())
        # 启动线程组
        self.thread_group_update_db.start(comics)

    def refresh_result(self):
        """刷新匹配结果"""
        self.treeWidget_show_group.check_validity()

    def result_filter_same(self):
        """筛选器 - 仅显示页数、大小相同项"""
        self.treeWidget_show_group.filter_same()

    def result_filter_pages_diff(self):
        """筛选器 - 剔除页数差异过大项"""
        self.treeWidget_show_group.filter_pages_diff()

    def result_filter_clear(self):
        """清除筛选器"""
        self.treeWidget_show_group.refresh_widget()

    def reload_last_result(self):
        """加载上一次的匹配结果"""
        self.show_result()

    def show_result(self):
        """显示匹配结果"""
        self.finished()
        self.treeWidget_show_group.show_group()

    def open_information(self):
        """打开说明文档"""
        dialog_ = DialogInformation(self)
        dialog_.exec()

    def set_widget_enable(self, is_enable: bool):
        """启用或禁用部分控件的功能"""
        self.widget_execute.set_enable(is_enable)
        self.widget_search_list.set_enable(is_enable)
        self.widget_filter_result.set_enable(is_enable)
        self.widget_option.set_enable(is_enable)
        self.treeWidget_show_group.setEnabled(is_enable)

    def update_schedule_total(self, text: str):
        """更新总进度"""
        self.widget_schedule.update_schedule_total(text)

    def update_schedule_step(self, text: str):
        """更新步骤进度"""
        self.widget_schedule.update_schedule_step(text)

    def update_config_size(self):
        """更新配置文件-主页面大小"""
        function_config_size.main_width.update(self.width())
        function_config_size.main_height.update(self.height())

    def resizeEvent(self, event):
        # 每次大小改变时重启计时器
        self.timer_resize.start()
        super().resizeEvent(event)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = MainWindow()
    show_ui.show()
    app.exec()
