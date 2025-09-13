from PySide6.QtCore import QObject

from components.widget_runtime_info.runtime_info_model import RuntimeInfoModel
from components.widget_runtime_info.runtime_info_viewer import RuntimeInfoViewer


class RuntimeInfoPresenter(QObject):
    """运行信息模块的桥梁组件"""

    def __init__(self, viewer: RuntimeInfoViewer, model=RuntimeInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
