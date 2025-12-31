from PySide6.QtWidgets import QWidget, QApplication

from components.widget_runtime_info.res.ui_runtime_info import Ui_Form

MAX_LINES = 500


class RuntimeInfoViewer(QWidget):
    """运行信息模块的界面组件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.lines_count = 0  # 行数

    def update_runtime_total(self, time_str: str):
        """更新任务运行总耗时"""
        self.ui.label_runtime_total.setText(time_str)

    def update_runtime_current(self, time_str: str):
        """更新任务运行当前步骤耗时"""
        self.ui.label_runtime_current.setText(time_str)

    def update_step_index(self, index: int):
        """更新当前步骤索引"""
        self.ui.label_step_index.setText(str(index))

    def update_step_count(self, count: int):
        """更新步骤总数"""
        self.ui.label_step_count.setText(str(count))

    def update_step_title(self, title: str):
        """更新当前步骤标题"""
        self.ui.label_step_title.setText(title)

    def update_progress_current(self, progress: str):
        """更新任务运行当前步骤的内部进度"""
        self.ui.label_progress_current.setText(progress)

    def clear_step_info(self):
        """清空步骤信息"""
        self.update_runtime_total('0:00:00')
        self.update_runtime_current('0:00:00')
        self.update_step_index('-')
        self.update_step_count('-')
        self.update_step_title('')
        self.update_progress_current('-/-')

    """文本框方法"""

    def append_textline(self, text_info: str):
        """向文本框中添加文本行"""
        self.lines_count += 1
        # 检查文本量，超过上限后清空
        if self.lines_count >= MAX_LINES:
            self.ui.textBrowser_runtime_info.clear()
            self.lines_count = 1

        self.ui.textBrowser_runtime_info.append(text_info)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = RuntimeInfoViewer()
    program_ui.show()
    app_.exec()
