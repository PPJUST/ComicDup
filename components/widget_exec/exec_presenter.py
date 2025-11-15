from PySide6.QtCore import QObject, Signal

from components.widget_exec import ExecModel
from components.widget_exec.exec_viewer import ExecViewer


class ExecPresenter(QObject):
    """执行模块的桥梁组件"""
    Start = Signal(name="开始查重")
    Stop = Signal(name="停止查重")
    LoadLastResult = Signal(name="加载上次结果")
    OpenAbout = Signal(name="打开程序说明")

    def __init__(self, viewer: ExecViewer, model: ExecModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 绑定信号
        self.viewer.Start.connect(self.Start.emit)
        self.viewer.Stop.connect(self.Stop.emit)
        self.viewer.LoadLastResult.connect(self.LoadLastResult.emit)
        self.viewer.OpenAbout.connect(self.OpenAbout.emit)

    def set_button_state_start(self):
        """设置按钮状态-启动匹配状态"""
        self.viewer.set_button_state_start()

    def set_button_state_end(self):
        """设置按钮状态-结束匹配状态"""
        self.viewer.set_button_state_end()
