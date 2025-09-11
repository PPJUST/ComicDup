from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.area_runtime_info.res.ui_area_runtime_info import Ui_Form


class AreaRuntimeInfoViewer(QWidget):
    """运行信息模块的界面组件"""


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app_ = QApplication()
    program_ui = AreaRuntimeInfoViewer()
    program_ui.show()
    app_.exec()
