from PySide6.QtWidgets import QApplication, QDialog

from components.dialog_rename_comic.res.ui_rename_comic import Ui_Dialog


class RenameComicViewer(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 设置文本框只读
        self.ui.lineEdit_original_filename.setReadOnly(True)
        self.ui.lineEdit_circle.setReadOnly(True)
        self.ui.lineEdit_artist.setReadOnly(True)
        self.ui.lineEdit_title.setReadOnly(True)
        self.ui.lineEdit_convention.setReadOnly(True)
        self.ui.lineEdit_parody.setReadOnly(True)
        self.ui.lineEdit_language.setReadOnly(True)
        self.ui.lineEdit_translator.setReadOnly(True)
        self.ui.lineEdit_special_indicator.setReadOnly(True)

    def _add_patterns(self):
        pattern_1 = r""

if __name__ == "__main__":
    app_ = QApplication()
    program_ui = RenameComicViewer()
    program_ui.show()
    app_.exec()
