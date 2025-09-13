from PySide6.QtWidgets import QWidget, QApplication

from components.widget_runtime_info.res.ui_runtime_info import Ui_Form


class RuntimeInfoViewer(QWidget):
    """运行信息模块的界面组件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def update_runtime_total(self, time_str: str):
        """更新任务运行总耗时"""
        self.ui.label_runtime_total.setText(time_str)

    def update_runtime_current(self, time_str: str):
        """更新任务运行当前步骤耗时"""
        self.ui.label_runtime_current.setText(time_str)

    def update_progress_total(self, step: str):
        """更新任务运行步骤总进度"""
        self.ui.label_progress_total.setText(step)

    def update_progress_current(self, progress: str):
        """更新任务运行当前步骤的内部进度"""
        self.ui.label_progress_current.setText(progress)

    """文本框方法"""


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = RuntimeInfoViewer()
    program_ui.show()
    app_.exec()
