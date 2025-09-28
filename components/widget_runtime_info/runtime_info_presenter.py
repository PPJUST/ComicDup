from PySide6.QtCore import QObject

from common.class_runtime import TYPE_RUNTIME_INFO
from components.widget_runtime_info.runtime_info_model import RuntimeInfoModel
from components.widget_runtime_info.runtime_info_viewer import RuntimeInfoViewer


class RuntimeInfoPresenter(QObject):
    """运行信息模块的桥梁组件"""

    def __init__(self, viewer: RuntimeInfoViewer, model: RuntimeInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

    def update_runtime_total(self, time_str: str):
        """更新任务运行总耗时"""
        self.viewer.update_runtime_total(time_str)

    def update_runtime_current(self, time_str: str):
        """更新任务运行当前步骤耗时"""
        self.viewer.update_runtime_current(time_str)

    def update_step_index(self, index: int):
        """更新当前步骤索引"""
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
        text_type = info_type.text
        textline = f'{text_type}{text_info}'
        self.viewer.append_textline(textline)
