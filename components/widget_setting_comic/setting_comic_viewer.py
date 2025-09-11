from PySide6.QtWidgets import QWidget, QApplication

from components.widget_setting_comic.res.ui_setting_comic import Ui_Form


class SettingComicViewer(QWidget):
    """设置模块（漫画设置项）的界面组件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SettingComicViewer()
    program_ui.show()
    app_.exec()
