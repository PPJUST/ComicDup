# 进度

import time

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import *

from module import function_normal
from ui.src.ui_widget_schedule import Ui_Form


class WidgetSchedule(QWidget):
    """进度"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化
        self._reset_text()
        self._start_time_total = None  # 开始时间点
        self._start_time_step = None  # 分步步骤开始时间点

        # 设置计时器
        self._timer_runtime = QTimer()
        self._timer_runtime.setInterval(500)  # 刷新时间0.5秒
        self._timer_runtime.timeout.connect(self._update_runtime)

    def set_start_time(self):
        """开始"""
        self._reset_text()
        self._start_time_total = time.time()
        self._start_time_step = self._start_time_total

        self._timer_runtime.start()

    def finished(self):
        """结束"""
        self._timer_runtime.stop()
        self.update_schedule_total('已完成')

    def stopped(self):
        """终止"""
        self._timer_runtime.stop()
        self.update_schedule_total(f'{self.ui.label_schedule_total.text()} - 已终止')

    def update_schedule_total(self, text: str):
        """更新进度"""
        self.ui.label_schedule_total.setText(text)

        self._start_time_step = time.time()

    def update_schedule_step(self, text: str):
        """更新进度"""
        self.ui.label_schedule_step.setText(text)

    def _reset_text(self):
        """重设所有文本"""
        self.ui.label_schedule_total.setText('-/-')
        self.ui.label_runtime_total.setText('0:00:00')
        self.ui.label_schedule_step.setText('-/-')
        self.ui.label_runtime_step.setText('0:00:00')

    def _update_runtime(self):
        """更新运行时间"""
        # 总时间
        now_time = time.time()
        runtime_total = now_time - self._start_time_total
        time_str = function_normal.convert_time(runtime_total)
        self._update_runtime_total(time_str)

        # 单步时间
        runtime_step = now_time - self._start_time_step
        time_str = function_normal.convert_time(runtime_step)
        self._update_runtime_step(time_str)

    def _update_runtime_total(self, text):
        """更新运行时间"""
        self.ui.label_runtime_total.setText(text)

    def _update_runtime_step(self, text):
        """更新运行时间"""
        self.ui.label_runtime_step.setText(text)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = WidgetSchedule()
    show_ui.show()
    app.exec()
