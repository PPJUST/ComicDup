from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.area_search_list.res.ui_area_search_list import Ui_Form


class AreaSearchListViewer(QWidget):
    """检索路径模块的界面组件"""


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app_ = QApplication()
    program_ui = AreaSearchListViewer()
    program_ui.show()
    app_.exec()
