from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.area_setting_match.res.ui_area_setting_match import Ui_Form


class AreaSettingMatchViewer(QWidget):
    """设置模块（匹配设置项）的界面组件"""


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app_ = QApplication()
    program_ui = AreaSettingMatchViewer()
    program_ui.show()
    app_.exec()
