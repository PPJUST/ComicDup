from PySide6.QtCore import QObject, Signal

from components.area_exec.area_exec_viewer import AreaExecViewer


class AreaExecPresenter(QObject):
    """执行模块的桥梁组件"""
    Start = Signal(name="开始查重")
    Stop = Signal(name="停止查重")
    LoadLastResult = Signal(name="加载上次结果")
    OpenAbout = Signal(name="打开程序说明")

    def __init__(self, viewer: AreaExecViewer, model=None):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 绑定信号
        self.viewer.Start.connect(self.Start.emit)
        self.viewer.Stop.connect(self.Stop.emit)
        self.viewer.LoadLastResult.connect(self.LoadLastResult.emit)
        self.viewer.OpenAbout.connect(self.OpenAbout.emit)
