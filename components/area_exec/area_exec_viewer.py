from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.area_exec.res.ui_area_exec import Ui_Form


class AreaExecViewer(QWidget):
    """执行模块的界面组件"""
    Start = Signal(name="开始查重")
    Stop = Signal(name="停止查重")
    LoadLastResult = Signal(name="加载上次结果")
    OpenAbout = Signal(name="打开程序说明")

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 设置图标
        self._set_icon()

        # 绑定信号
        self.ui.pushButton_start.clicked.connect(self.Start.emit)
        self.ui.pushButton_stop.clicked.connect(self.Stop.emit)
        self.ui.pushButton_load_last_result.clicked.connect(self.LoadLastResult.emit)
        self.ui.pushButton_info.clicked.connect(self.OpenAbout.emit)

    def _set_icon(self):
        """设置图标"""
        # self.ui.pushButton_start.setIcon()
        # self.ui.pushButton_stop.setIcon()
        # self.ui.pushButton_load_last_result.setIcon()
        # self.ui.pushButton_info.setIcon()


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = AreaExecViewer()
    program_ui.show()
    app_.exec()
