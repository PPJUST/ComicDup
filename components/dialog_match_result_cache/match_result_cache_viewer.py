from typing import Union

import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QDialog

from common.class_cache import CacheMatchResult
from components.dialog_match_result_cache.res.icon_base64 import ICON_DELETE, ICON_RESTORE
from components.dialog_match_result_cache.res.ui_match_result_cache import Ui_Dialog


class MatchResultCacheViewer(QDialog):
    """匹配结果缓存模块的界面组件"""
    Restore = Signal(str, name='还原缓存文件')
    Delete = Signal(str, name='删除缓存文件')
    ShowInfo = Signal(name='显示信息')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 初始化按钮ui
        self._init_button()

        # 设置图标
        self._set_icon()

        # 绑定信号
        self._bind_signal()

    def set_line(self, index: int, match_result_file_info: Union[CacheMatchResult, None], button_state: bool = True):
        """设置行信息"""
        if match_result_file_info:
            filename = match_result_file_info.filename
            file_date = match_result_file_info.date
            group_count = match_result_file_info.group_count
            size_count = match_result_file_info.size_count
        else:
            filename = ''
            file_date = ''
            group_count = ''
            size_count = ''

        if index == 1:
            self.ui.label_filename_1.setText(str(filename))
            self.ui.label_date_1.setText(str(file_date))
            self.ui.label_group_count_1.setText(str(group_count))
            self.ui.label_size_count_1.setText(str(size_count))
            self.ui.pushButton_restore_1.setEnabled(button_state)
            self.ui.toolButton_delete_1.setEnabled(button_state)
        elif index == 2:
            self.ui.label_filename_2.setText(str(filename))
            self.ui.label_date_2.setText(str(file_date))
            self.ui.label_group_count_2.setText(str(group_count))
            self.ui.label_size_count_2.setText(str(size_count))
            self.ui.pushButton_restore_2.setEnabled(button_state)
            self.ui.toolButton_delete_2.setEnabled(button_state)
        elif index == 3:
            self.ui.label_filename_3.setText(str(filename))
            self.ui.label_date_3.setText(str(file_date))
            self.ui.label_group_count_3.setText(str(group_count))
            self.ui.label_size_count_3.setText(str(size_count))
            self.ui.pushButton_restore_3.setEnabled(button_state)
            self.ui.toolButton_delete_3.setEnabled(button_state)
        elif index == 4:
            self.ui.label_filename_4.setText(str(filename))
            self.ui.label_date_4.setText(str(file_date))
            self.ui.label_group_count_4.setText(str(group_count))
            self.ui.label_size_count_4.setText(str(size_count))
            self.ui.pushButton_restore_4.setEnabled(button_state)
            self.ui.toolButton_delete_4.setEnabled(button_state)
        elif index == 5:
            self.ui.label_filename_5.setText(str(filename))
            self.ui.label_date_5.setText(str(file_date))
            self.ui.label_group_count_5.setText(str(group_count))
            self.ui.label_size_count_5.setText(str(size_count))
            self.ui.pushButton_restore_5.setEnabled(button_state)
            self.ui.toolButton_delete_5.setEnabled(button_state)

    def _init_line(self, index: int):
        """初始化行信息"""
        self.set_line(index, '', '', '', '', False)

    def _init_button(self):
        """初始化按钮"""
        self.ui.pushButton_restore_1.setEnabled(False)
        self.ui.pushButton_restore_2.setEnabled(False)
        self.ui.pushButton_restore_3.setEnabled(False)
        self.ui.pushButton_restore_4.setEnabled(False)
        self.ui.pushButton_restore_5.setEnabled(False)
        self.ui.toolButton_delete_1.setEnabled(False)
        self.ui.toolButton_delete_2.setEnabled(False)
        self.ui.toolButton_delete_3.setEnabled(False)
        self.ui.toolButton_delete_4.setEnabled(False)
        self.ui.toolButton_delete_5.setEnabled(False)

    def _set_icon(self):
        """设置图标"""
        self.ui.pushButton_restore_1.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_RESTORE))
        self.ui.pushButton_restore_2.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_RESTORE))
        self.ui.pushButton_restore_3.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_RESTORE))
        self.ui.pushButton_restore_4.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_RESTORE))
        self.ui.pushButton_restore_5.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_RESTORE))
        self.ui.toolButton_delete_1.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_DELETE))
        self.ui.toolButton_delete_2.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_DELETE))
        self.ui.toolButton_delete_3.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_DELETE))
        self.ui.toolButton_delete_4.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_DELETE))
        self.ui.toolButton_delete_5.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_DELETE))

    def _bind_signal(self):
        """绑定信号"""
        self.ui.pushButton_restore_1.clicked.connect(lambda: self.Restore.emit(self.ui.label_filename_1.text()))
        self.ui.pushButton_restore_2.clicked.connect(lambda: self.Restore.emit(self.ui.label_filename_2.text()))
        self.ui.pushButton_restore_3.clicked.connect(lambda: self.Restore.emit(self.ui.label_filename_3.text()))
        self.ui.pushButton_restore_4.clicked.connect(lambda: self.Restore.emit(self.ui.label_filename_4.text()))
        self.ui.pushButton_restore_5.clicked.connect(lambda: self.Restore.emit(self.ui.label_filename_5.text()))
        self.ui.toolButton_delete_1.clicked.connect(lambda: self.Delete.emit(self.ui.label_filename_1.text()))
        self.ui.toolButton_delete_2.clicked.connect(lambda: self.Delete.emit(self.ui.label_filename_2.text()))
        self.ui.toolButton_delete_3.clicked.connect(lambda: self.Delete.emit(self.ui.label_filename_3.text()))
        self.ui.toolButton_delete_4.clicked.connect(lambda: self.Delete.emit(self.ui.label_filename_4.text()))
        self.ui.toolButton_delete_5.clicked.connect(lambda: self.Delete.emit(self.ui.label_filename_5.text()))

    def exec(self):
        self.ShowInfo.emit()
        super().exec()


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = MatchResultCacheViewer()
    program_ui.show()
    app_.exec()
