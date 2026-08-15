from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QApplication, QDialog

from common.class_match_page_result import MatchResult
from components.dialog_full_match_comics.res.ui_full_match_comics import Ui_Dialog


class FullMatchComicsViewer(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)




if __name__ == "__main__":
    app_ = QApplication()
    program_ui = FullMatchComicsViewer()
    program_ui.show()
    app_.exec()
