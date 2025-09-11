from PySide6.QtCore import QObject

from components.area_runtime_info.area_runtime_info_model import AreaRuntimeInfoModel
from components.area_runtime_info.area_runtime_info_viewer import AreaRuntimeInfoViewer


class AreaRuntimeInfoPresenter(QObject):
    """运行信息模块的桥梁组件"""

    def __init__(self, viewer: AreaRuntimeInfoViewer, model=AreaRuntimeInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
