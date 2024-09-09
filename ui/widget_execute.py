# 执行控件，包含开始、停止、重新加载等功能

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import _ICON_START, _ICON_STOP, _ICON_RELOAD, _ICON_INFORMATION
from ui.src.ui_widget_execute import Ui_Form


class WidgetExecute(QWidget):
    signal_start = Signal(name='开始')
    signal_stop = Signal(name='停止')
    signal_reload = Signal(name='加载上一次的匹配结果')
    signal_information = Signal(name='打开说明文档')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化
        self._set_icon()
        self.ui.pushButton_stop.setEnabled(False)

        # 绑定槽函数
        self.ui.pushButton_start.clicked.connect(self.signal_start.emit)
        self.ui.pushButton_stop.clicked.connect(self.signal_stop.emit)
        self.ui.pushButton_load_last_result.clicked.connect(self.signal_reload.emit)
        self.ui.pushButton_information.clicked.connect(self.signal_information.emit)

    def set_enable(self, is_enable: bool):
        """是否启用，True时为启动start禁用stop按钮，False为禁用start启动stop按钮"""
        if is_enable:
            self.ui.pushButton_start.setEnabled(True)
            self.ui.pushButton_stop.setEnabled(False)
            self.ui.pushButton_load_last_result.setEnabled(True)
        else:
            self.ui.pushButton_start.setEnabled(False)
            self.ui.pushButton_stop.setEnabled(True)
            self.ui.pushButton_load_last_result.setEnabled(False)

    def _set_icon(self):
        """设置图标"""
        self.ui.pushButton_start.setIcon(QIcon(_ICON_START))
        self.ui.pushButton_stop.setIcon(QIcon(_ICON_STOP))
        self.ui.pushButton_load_last_result.setIcon(QIcon(_ICON_RELOAD))
        self.ui.pushButton_information.setIcon(QIcon(_ICON_INFORMATION))


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = WidgetExecute()
    show_ui.show()
    app.exec()
