from PySide6.QtCore import QObject

from components.widget_runtime_info.runtime_info_model import RuntimeInfoModel
from components.widget_runtime_info.runtime_info_viewer import RuntimeInfoViewer


class RuntimeInfoPresenter(QObject):
    """运行信息模块的桥梁组件"""

    def __init__(self, viewer: RuntimeInfoViewer, model=RuntimeInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

    def update_runtime_total(self, time_str: str):
        """更新任务运行总耗时"""
        self.viewer.update_runtime_total(time_str)

    def update_runtime_current(self, time_str: str):
        """更新任务运行当前步骤耗时"""
        self.viewer.update_runtime_current(time_str)

    def update_progress_total(self, step: str):
        """更新任务运行步骤总进度"""
        self.viewer.update_progress_total(step)

    def update_progress_current(self, progress: str):
        """更新任务运行当前步骤的内部进度"""
        self.viewer.update_progress_current(progress)

    """文本框方法"""
