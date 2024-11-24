# 子线程模板
from PySide6.QtCore import QThread, Signal


class ThreadPattern(QThread):
    """子线程模板"""
    signal_start = Signal(name='开始')
    signal_step = Signal(str, name='当前步骤的名称')
    signal_rate = Signal(str, name='内部进度')
    signal_finished = Signal(object, name='结束，传递参数')
    signal_stopped = Signal(name='终止')

    def __init__(self, parent=None):
        super().__init__(parent)
        self._stop_code = False  # 终止判断
        self._step = ''  # 当前步骤的名称

    def set_stop(self):
        self._stop_code = True

    def run(self):
        self.signal_start.emit()
        self.signal_step.emit(self._step)
        self._stop_code = False

    def finished(self, arg=''):
        if self._stop_code and arg != 'stopped but finished':
            self.signal_stopped.emit()
        elif arg == 'stopped but finished':
            self.signal_finished.emit(arg)
        else:
            self.signal_finished.emit(arg)
