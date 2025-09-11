from PySide6.QtCore import QObject

from components.area_setting_match.area_setting_match_model import AreaSettingMatchModel
from components.area_setting_match.area_setting_match_viewer import AreaSettingMatchViewer


class AreaSettingMatchPresenter(QObject):
    """设置模块（匹配设置项）的桥梁组件"""

    def __init__(self, viewer: AreaSettingMatchViewer, model=AreaSettingMatchModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
