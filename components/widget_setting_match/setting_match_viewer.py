from PySide6.QtWidgets import QWidget, QApplication

from components.widget_setting_match.res.ui_setting_match import Ui_Form


class SettingMatchViewer(QWidget):
    """设置模块（匹配设置项）的界面组件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SettingMatchViewer()
    program_ui.show()
    app_.exec()
