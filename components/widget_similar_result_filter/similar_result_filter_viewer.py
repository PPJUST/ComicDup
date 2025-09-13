from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.widget_similar_result_filter.res.ui_similar_result_filter import Ui_Form


class SimilarResultFilterViewer(QWidget):
    """相似结果筛选器模块的界面组件"""


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SimilarResultFilterViewer()
    program_ui.show()
    app_.exec()
