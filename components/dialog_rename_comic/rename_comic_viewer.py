from PySide6.QtWidgets import QApplication, QDialog

from components.dialog_rename_comic.res.ui_rename_comic import Ui_Dialog


class RenameComicViewer(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self._add_patterns()
        self._model_pattern_state()
        self._model_field_state()

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

        # 绑定信号
        self.ui.checkBox_rename_pattern.clicked.connect(self._set_mode_pattern)
        self.ui.checkBox_rename_pattern.stateChanged.connect(self._model_pattern_state)
        self.ui.checkBox_choose_field.clicked.connect(self._set_mode_field)
        self.ui.checkBox_choose_field.stateChanged.connect(self._model_field_state)

    def _add_patterns(self):
        pattern_1 = r"(即卖会名称) [社团名称 (作者名)] 标题 (原作名) [语言] [译者] [特殊标识]"
        pattern_2 = r"[社团名称 (作者名)] 标题 (原作名) (即卖会名称) [语言] [译者] [特殊标识]"
        pattern_3 = r"[社团名称 (作者名)] 标题 (即卖会名称) [语言] [译者] [特殊标识]"
        pattern_4 = r"[社团名称 (作者名)] 标题 [语言] [译者] [特殊标识]"
        pattern_5 = r"[社团名称 (作者名)] 标题 [特殊标识]"
        pattern_6 = r"[社团名称 (作者名)] 标题"

        self.ui.comboBox_rename_pattern.addItems([pattern_1, pattern_2, pattern_3, pattern_4, pattern_5, pattern_6])

    def _set_mode_pattern(self):
        """设置互斥模式选择-模板模式"""
        if self.ui.checkBox_rename_pattern.isChecked():
            self.ui.checkBox_choose_field.setChecked(False)

    def _set_mode_field(self):
        """设置互斥模式选择-字段模式"""
        if self.ui.checkBox_choose_field.isChecked():
            self.ui.checkBox_rename_pattern.setChecked(False)

    def _model_pattern_state(self):
        """模板模式UI状态设置"""
        if self.ui.checkBox_rename_pattern.isChecked():
            self.ui.comboBox_rename_pattern.setEnabled(True)
        else:
            self.ui.comboBox_rename_pattern.setEnabled(False)

    def _model_field_state(self):
        """字段模式UI状态设置"""
        if self.ui.checkBox_choose_field.isChecked():
            self.ui.toolButton_add_circle.setEnabled(True)
            self.ui.toolButton_add_artist.setEnabled(True)
            self.ui.toolButton_add_title.setEnabled(True)
            self.ui.toolButton_add_convention.setEnabled(True)
            self.ui.toolButton_add_parody.setEnabled(True)
            self.ui.toolButton_add_language.setEnabled(True)
            self.ui.toolButton_add_translator.setEnabled(True)
            self.ui.toolButton_add_special_indicator.setEnabled(True)

            self.ui.lineEdit_circle.setEnabled(True)
            self.ui.lineEdit_artist.setEnabled(True)
            self.ui.lineEdit_title.setEnabled(True)
            self.ui.lineEdit_convention.setEnabled(True)
            self.ui.lineEdit_parody.setEnabled(True)
            self.ui.lineEdit_language.setEnabled(True)
            self.ui.lineEdit_translator.setEnabled(True)
            self.ui.lineEdit_special_indicator.setEnabled(True)
        else:
            self.ui.toolButton_add_circle.setEnabled(False)
            self.ui.toolButton_add_artist.setEnabled(False)
            self.ui.toolButton_add_title.setEnabled(False)
            self.ui.toolButton_add_convention.setEnabled(False)
            self.ui.toolButton_add_parody.setEnabled(False)
            self.ui.toolButton_add_language.setEnabled(False)
            self.ui.toolButton_add_translator.setEnabled(False)
            self.ui.toolButton_add_special_indicator.setEnabled(False)

            self.ui.lineEdit_circle.setEnabled(False)
            self.ui.lineEdit_artist.setEnabled(False)
            self.ui.lineEdit_title.setEnabled(False)
            self.ui.lineEdit_convention.setEnabled(False)
            self.ui.lineEdit_parody.setEnabled(False)
            self.ui.lineEdit_language.setEnabled(False)
            self.ui.lineEdit_translator.setEnabled(False)
            self.ui.lineEdit_special_indicator.setEnabled(False)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = RenameComicViewer()
    program_ui.show()
    app_.exec()
