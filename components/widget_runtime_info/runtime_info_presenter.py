import time

import lzytools.common
from PySide6.QtCore import QObject, QTimer

from common.class_runtime import TYPE_RUNTIME_INFO
from components.widget_runtime_info.runtime_info_model import RuntimeInfoModel
from components.widget_runtime_info.runtime_info_viewer import RuntimeInfoViewer


class RuntimeInfoPresenter(QObject):
    """运行信息模块的桥梁组件"""

    def __init__(self, viewer: RuntimeInfoViewer, model: RuntimeInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self._update_time)

        self.start_time_total: float = 0  # 任务开始运行时间（秒，浮点数）
        self.start_time_current: float = 0  # 步骤开始运行时间（秒，浮点数）

    def start_time(self):
        """开始计时"""
        self.start_time_total = time.time()
        self.start_time_current = time.time()
        self.timer.start()

    def _update_time(self):
        """更新耗时"""
        time_ = time.time()
        runtime_total = time_ - self.start_time_total
        runtime_current = time_ - self.start_time_current
        self._update_runtime_total(runtime_total)
        self._update_runtime_current(runtime_current)

    def stop_time(self):
        """结束计时"""
        self.timer.stop()

    def _update_runtime_total(self, runtime: float):
        """更新任务运行总耗时"""
        self.viewer.update_runtime_total(lzytools.common.convert_time(runtime))

    def _update_runtime_current(self, runtime: float):
        """更新任务运行当前步骤耗时"""
        self.viewer.update_runtime_current(lzytools.common.convert_time(runtime))

    def update_step_index(self, index: int):
        """更新当前步骤索引"""
        self.start_time_current = time.time()
        self.viewer.update_step_index(index)

    def update_step_count(self, count: int):
        """更新步骤总数"""
        self.viewer.update_step_count(count)

    def update_step_title(self, title: str):
        """更新当前步骤标题"""
        self.viewer.update_step_title(title)

    def update_progress_current(self, progress: str):
        """更新任务运行当前步骤的内部进度"""
        self.viewer.update_progress_current(progress)

    """文本框方法"""

    def update_textline(self, info_type: TYPE_RUNTIME_INFO, text_info: str):
        """更新文本行信息"""
        # 提取时间戳
        time_str = time.strftime("%H:%M:%S", time.localtime())
        # 转换为富文本
        content = (f"<p>"
                   f"<span style='color: black; font-size: 12px'>{time_str}</span> "  # 时间戳为黑色
                   f"<span style='color: {info_type.color}; font-size: 12px'>{text_info}</span>"  # 文本信息为设定的颜色
                   f"</p>")

        self.viewer.append_textline(content)
