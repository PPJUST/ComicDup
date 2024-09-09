# 匹配结果筛选器

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import _ICON_REFRESH
from ui.src.ui_widget_filter_result import Ui_Form


class WidgetFilterResult(QWidget):
    """匹配结果筛选器"""
    signal_refresh = Signal(name='刷新匹配结果')
    signal_filter_same = Signal(name='启用筛选器 - 仅显示页数、大小相同项')
    signal_filter_pages_diff = Signal(name='启用筛选器 - 剔除页数差异过大项')
    signal_filter_clear = Signal(name='清除筛选器')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化
        self.setEnabled(False)
        self._set_icon()

        # 绑定槽函数
        self.ui.pushButton_refresh.clicked.connect(self.signal_refresh.emit)
        self.ui.checkBox_filter_same_items.stateChanged.connect(self.filter_same_clicked)
        self.ui.checkBox_filter_pages_diff_items.stateChanged.connect(self.filter_pages_diff)

    def emit_signal(self):
        if self.ui.checkBox_filter_same_items.isChecked():
            self.signal_filter_same.emit()
        elif self.ui.checkBox_filter_pages_diff_items.isChecked():
            self.signal_filter_pages_diff.emit()
        else:
            self.signal_filter_clear.emit()

    def filter_same_clicked(self, state):
        """特殊的互斥按钮组"""
        if state == 2:  # 选中状态
            self.ui.checkBox_filter_pages_diff_items.setChecked(False)
            self.emit_signal()

        if (not self.ui.checkBox_filter_same_items.isChecked()
                and not self.ui.checkBox_filter_pages_diff_items.isChecked()):
            self.emit_signal()

    def filter_pages_diff(self, state):
        """特殊的互斥按钮组"""
        if state == 2:  # 选中状态
            self.ui.checkBox_filter_same_items.setChecked(False)
            self.emit_signal()

        if (not self.ui.checkBox_filter_same_items.isChecked()
                and not self.ui.checkBox_filter_pages_diff_items.isChecked()):
            self.emit_signal()

    def _set_icon(self):
        """设置图标"""
        self.ui.pushButton_refresh.setIcon(QIcon(_ICON_REFRESH))

    def set_enable(self, is_enable: bool):
        """是否启用"""
        self.setEnabled(is_enable)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = WidgetFilterResult()
    show_ui.show()
    app.exec()
