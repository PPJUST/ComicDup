from PySide6.QtWidgets import QApplication, QDialog

from components.dialog_choose_number.res.ui_choose_number import Ui_Dialog


class ChooseNumberViewer(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def set_info(self, info: str):
        """设置文本信息"""
        self.ui.label_choose_text.setText(info)

    def set_number(self, number: int):
        """设置初始值"""
        self.ui.spinBox_number.setValue(number)

    def set_min(self, min_number: int):
        """设置最小值"""
        self.ui.spinBox_number.setMinimum(min_number)

    def set_max(self, max_number: int):
        """设置最大值"""
        self.ui.spinBox_number.setMaximum(max_number)

    def accept(self, /):
        super().accept()
        self.done(self.ui.spinBox_number.value())


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = ChooseNumberViewer()
    program_ui.show()
    app_.exec()
