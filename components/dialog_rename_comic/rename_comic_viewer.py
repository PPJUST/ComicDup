import os.path

from DoujinTools import DoujinshiName
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QDialog

from components.dialog_rename_comic.res.ui_rename_comic import Ui_Dialog


class RenameComicViewer(QDialog):
    Rename = Signal(str, name='重命名的文件名（不含文件扩展名')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.comic_path: str = None  # 对应的漫画路径
        self.doujin_class: DoujinshiName = None  # 对应的漫画标题类
        self._field_pattern = []  # 手工选择的字段模板

        self._add_patterns()
        self._model_pattern_state()
        self._model_field_state()
        self.ui.pushButton_rename.setEnabled(False)

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
        self.ui.lineEdit_new_filename.textChanged.connect(self._enable_rename_button)
        self.ui.comboBox_rename_pattern.currentTextChanged.connect(self._set_mode_pattern)
        self.ui.toolButton_add_circle.clicked.connect(self._set_field_pattern_circle)
        self.ui.toolButton_add_artist.clicked.connect(self._set_field_pattern_artist)
        self.ui.toolButton_add_title.clicked.connect(self._set_field_pattern_title)
        self.ui.toolButton_add_convention.clicked.connect(self._set_field_pattern_convention)
        self.ui.toolButton_add_parody.clicked.connect(self._set_field_pattern_parody)
        self.ui.toolButton_add_language.clicked.connect(self._set_field_pattern_language)
        self.ui.toolButton_add_translator.clicked.connect(self._set_field_pattern_translator)
        self.ui.toolButton_add_special_indicator.clicked.connect(self._set_field_pattern_special_indicator)

        self.ui.pushButton_rename.clicked.connect(
            lambda: self.Rename.emit(self.ui.lineEdit_new_filename.text().strip()))
        self.ui.pushButton_quit.clicked.connect(self.close)

    def set_comic_path(self, comic_path: str):
        """设置对应的漫画路径"""
        self.comic_path = comic_path
        self._update_field()

    def _update_field(self):
        """更新字段文本"""
        if os.path.isfile(self.comic_path):
            filetitle = os.path.splitext(os.path.basename(self.comic_path))[0]
        elif os.path.isdir(self.comic_path):
            filetitle = os.path.basename(self.comic_path)
        else:
            return

        self.ui.lineEdit_original_filename.setText(filetitle)

        self.doujin_class = DoujinshiName(filetitle)
        circle = self.doujin_class.circle_names.get_processed_value()
        self.ui.lineEdit_circle.setText(" | ".join(circle))
        artist = self.doujin_class.artist_names.get_processed_value()
        self.ui.lineEdit_artist.setText(" | ".join(artist))
        title = self.doujin_class.title.get_processed_value()
        self.ui.lineEdit_title.setText(" | ".join(title))
        convention = self.doujin_class.convention_name.get_processed_value()
        self.ui.lineEdit_convention.setText(" | ".join(convention))
        parody = self.doujin_class.parody_names.get_processed_value()
        self.ui.lineEdit_parody.setText(" | ".join(parody))
        language = self.doujin_class.language.get_processed_value()
        self.ui.lineEdit_language.setText(" | ".join(language))
        translator = self.doujin_class.translators.get_processed_value()
        self.ui.lineEdit_translator.setText(" | ".join(translator))
        special_indicator = self.doujin_class.special_indicators.get_processed_value()
        self.ui.lineEdit_special_indicator.setText(" | ".join(special_indicator))

    def _add_patterns(self):
        pattern_1 = r"(即卖会名称) [社团名称 (作者名)] 标题 (原作名) [语言] [译者] [特别标示]"
        pattern_2 = r"[社团名称 (作者名)] 标题 (原作名) (即卖会名称) [语言] [译者] [特别标示]"
        pattern_3 = r"[社团名称 (作者名)] 标题 (即卖会名称) [语言] [译者] [特别标示]"
        pattern_4 = r"[社团名称 (作者名)] 标题 [语言] [译者] [特别标示]"
        pattern_5 = r"[社团名称 (作者名)] 标题 [特别标示]"
        pattern_6 = r"[社团名称 (作者名)] 标题"

        self.ui.comboBox_rename_pattern.addItems([pattern_1, pattern_2, pattern_3, pattern_4, pattern_5, pattern_6])

    def _enable_rename_button(self):
        old = self.ui.lineEdit_original_filename.text().strip().lower()
        new = self.ui.lineEdit_new_filename.text().strip().lower()
        if new and old != new:
            self.ui.pushButton_rename.setEnabled(True)
        else:
            self.ui.pushButton_rename.setEnabled(False)

    def _set_mode_pattern(self):
        """设置互斥模式选择-模板模式"""
        if self.ui.checkBox_rename_pattern.isChecked():
            self.ui.checkBox_choose_field.setChecked(False)

            pattern = self.ui.comboBox_rename_pattern.currentText()
            new_name = self.doujin_class.get_normalized_name(pattern)
            self.ui.lineEdit_new_filename.setText(new_name)

    def _set_mode_field(self):
        """设置互斥模式选择-字段模式"""
        if self.ui.checkBox_choose_field.isChecked():
            self.ui.checkBox_rename_pattern.setChecked(False)

            self.ui.lineEdit_new_filename.setText('')

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

    def _set_field_pattern(self, model: str, field: str):
        if model == 'add':
            self._field_pattern.append(field)
        elif model == 'del':
            self._field_pattern.remove(field)

        # 转换为可视化文本
        pattern = " ".join(self._field_pattern)
        pattern = pattern.replace('即卖会名称', '(即卖会名称)')
        pattern = pattern.replace('原作名', '(原作名)')
        pattern = pattern.replace('语言', '[语言]')
        pattern = pattern.replace('译者', '[译者]')
        pattern = pattern.replace('特别标示', '[特别标示]')
        if '社团名称 作者名' in pattern:
            pattern = pattern.replace('社团名称 作者名', '[社团名称 (作者名)]')
        else:
            pattern = pattern.replace('社团名称', '[社团名称]')
            pattern = pattern.replace('作者名', '[作者名]')

        new_name = self.doujin_class.get_normalized_name(pattern)
        self.ui.lineEdit_new_filename.setText(new_name)
        self.ui.label_field_pattern.setText(pattern)

    def _set_field_pattern_circle(self):
        if self.ui.toolButton_add_circle.text() == '＋':
            self.ui.toolButton_add_circle.setText('－')
            self._set_field_pattern(model='add', field='社团名称')
        else:
            self.ui.toolButton_add_circle.setText('＋')
            self._set_field_pattern(model='del', field='社团名称')

    def _set_field_pattern_artist(self):
        if self.ui.toolButton_add_artist.text() == '＋':
            self.ui.toolButton_add_artist.setText('－')
            self._set_field_pattern(model='add', field='作者名')
        else:
            self.ui.toolButton_add_artist.setText('＋')
            self._set_field_pattern(model='del', field='作者名')

    def _set_field_pattern_title(self):
        if self.ui.toolButton_add_title.text() == '＋':
            self.ui.toolButton_add_title.setText('－')
            self._set_field_pattern(model='add', field='标题')
        else:
            self.ui.toolButton_add_title.setText('＋')
            self._set_field_pattern(model='del', field='标题')

    def _set_field_pattern_convention(self):
        if self.ui.toolButton_add_convention.text() == '＋':
            self.ui.toolButton_add_convention.setText('－')
            self._set_field_pattern(model='add', field='即卖会名称')
        else:
            self.ui.toolButton_add_convention.setText('＋')
            self._set_field_pattern(model='del', field='即卖会名称')

    def _set_field_pattern_parody(self):
        if self.ui.toolButton_add_parody.text() == '＋':
            self.ui.toolButton_add_parody.setText('－')
            self._set_field_pattern(model='add', field='原作名')
        else:
            self.ui.toolButton_add_parody.setText('＋')
            self._set_field_pattern(model='del', field='原作名')

    def _set_field_pattern_language(self):
        if self.ui.toolButton_add_language.text() == '＋':
            self.ui.toolButton_add_language.setText('－')
            self._set_field_pattern(model='add', field='语言')
        else:
            self.ui.toolButton_add_language.setText('＋')
            self._set_field_pattern(model='del', field='语言')

    def _set_field_pattern_translator(self):
        if self.ui.toolButton_add_translator.text() == '＋':
            self.ui.toolButton_add_translator.setText('－')
            self._set_field_pattern(model='add', field='译者')
        else:
            self.ui.toolButton_add_translator.setText('＋')
            self._set_field_pattern(model='del', field='译者')

    def _set_field_pattern_special_indicator(self):
        if self.ui.toolButton_add_special_indicator.text() == '＋':
            self.ui.toolButton_add_special_indicator.setText('－')
            self._set_field_pattern(model='add', field='特别标示')
        else:
            self.ui.toolButton_add_special_indicator.setText('＋')
            self._set_field_pattern(model='del', field='特别标示')


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = RenameComicViewer()
    program_ui.show()
    app_.exec()
