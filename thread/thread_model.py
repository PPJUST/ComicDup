# 子线程标准模板
from PySide6.QtCore import QThread, Signal


class ThreadModel(QThread):
    """子线程标准模板"""
    signal_start = Signal()
    signal_step = Signal(str)
    signal_rate = Signal(str)
    signal_finished = Signal()
    signal_stopped = Signal()

    def __init__(self):
        super().__init__()
        self.code_stop = False
        self.step = ''

    def reset_stop_code(self):
        self.code_stop = True

    def run(self):
        self.signal_start.emit()
        self.signal_step.emit(self.step)
        self.code_stop = False

    def emit_signal_start(self):
        self.signal_start.emit()

    def emit_signal_step(self, x):
        self.signal_step.emit(x)

    def emit_signal_rate(self, x):
        self.signal_rate.emit(x)

    def emit_signal_finished(self):
        self.signal_finished.emit()

    def emit_signal_stopped(self):
        self.signal_stopped.emit()
