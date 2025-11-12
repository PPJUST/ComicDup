from PySide6.QtWidgets import QApplication, QDialog

from components.dialog_choose_number.res.ui_choose_number import Ui_Dialog


class ChooseNumberViewer(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = ChooseNumberViewer()
    program_ui.show()
    app_.exec()
