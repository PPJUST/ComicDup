from PySide6.QtWidgets import QApplication, QMainWindow
from lzytools._qt_pyside6 import base64_to_pixmap

from components.window.res.icon_base64 import ICON_LOGO
from components.window.res.ui_window import Ui_MainWindow


class WindowViewer(QMainWindow):
    """主窗口的界面组件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 绑定信号
        self.ui.pushButton_back_to_search_list.clicked.connect(self.turn_page_search_list)

        # 设置图标
        self.setWindowIcon(base64_to_pixmap(ICON_LOGO))

    def turn_page_search_list(self):
        """翻页到搜索目录页"""
        self.ui.stackedWidget.setCurrentIndex(0)

    def turn_page_running_info(self):
        """翻页到运行信息页"""
        self.ui.stackedWidget.setCurrentIndex(1)

    def turn_page_match_result(self):
        """翻页到结果预览页"""
        self.ui.tabWidget.setCurrentIndex(1)

    def add_viewer_exec(self, widget):
        """添加功能区控件"""
        self.ui.groupBox_exec.layout().addWidget(widget)

    def add_viewer_setting_1(self, widget):
        """添加设置控件"""
        self.ui.verticalLayout_setting_1.addWidget(widget)

    def add_viewer_setting_2(self, widget):
        """添加设置控件"""
        self.ui.verticalLayout_setting_2.addWidget(widget)

    def add_viewer_setting_3(self, widget):
        """添加设置控件"""
        self.ui.verticalLayout_setting_3.addWidget(widget)

    def add_viewer_search_list(self, widget):
        """添加检索路径控件"""
        self.ui.groupBox_search_list.layout().addWidget(widget)

    def add_viewer_runtime_info(self, widget):
        """添加运行信息控件"""
        self.ui.groupBox_runtime_info.layout().addWidget(widget)

    def add_viewer_result_filter(self, widget):
        """添加结果过滤器控件"""
        self.ui.groupBox_result_filter.layout().addWidget(widget)

    def add_viewer_result_preview(self, widget):
        """添加相似结果预览控件"""
        self.ui.groupBox_result_preview.layout().addWidget(widget)

    def add_viewer_cache_manager(self, widget):
        """添加缓存管理器控件"""
        self.ui.groupBox_cache.layout().addWidget(widget)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = WindowViewer()
    program_ui.show()
    app_.exec()
