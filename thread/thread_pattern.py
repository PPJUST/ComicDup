# 子线程模板

from PySide6.QtCore import QThread, Signal


class ThreadPattern(QThread):
    """子线程模板"""
    SignalStart = Signal(name='执行线程')
    SignalIndex = Signal(int, int, name='索引')
    SignalInfo = Signal(str, name='信息')
    SignalRate = Signal(str, name='进度')
    SignalRuntimeInfo = Signal(object, str, name='运行信息')
    SignalFinished = Signal(name='线程执行完毕')
    SignalStopped = Signal(name='线程终止执行')

    def __init__(self, parent=None):
        super().__init__(parent)
        # 步骤参数
        self.step_index = 1  # 步骤索引
        self.step_count = 6  # 总步骤数量
        self.step_info = ''  # 步骤名称

        # 基础设置参数
        self.max_workers = 2  # 线程数量
        self._is_stop = False  # 终止判断

    """参数设置方法"""

    def initialize(self):
        """初始化"""
        self._is_stop = False

    def set_max_workers(self, max_workers: int):
        """设置线程数量"""
        self.max_workers = max_workers

    """线程方法"""

    def set_stop(self):
        self._is_stop = True

    def run(self):
        self.SignalStart.emit()
        self.SignalIndex.emit(self.step_index, self.step_count)
        self.SignalInfo.emit(self.step_info)
        self._is_stop = False

    def finished(self):
        self.SignalFinished.emit()
