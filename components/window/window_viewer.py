from PySide6.QtWidgets import QApplication, QMainWindow

from components.window.res.ui_window import Ui_MainWindow


class WindowViewer(QMainWindow):
    """主窗口的界面组件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = WindowViewer()
    program_ui.show()
    app_.exec()
