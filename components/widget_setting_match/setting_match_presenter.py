from PySide6.QtCore import QObject

from components.widget_setting_match.setting_match_model import SettingMatchModel
from components.widget_setting_match.setting_match_viewer import SettingMatchViewer


class SettingMatchPresenter(QObject):
    """设置模块（匹配设置项）的桥梁组件"""

    def __init__(self, viewer: SettingMatchViewer, model=SettingMatchModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
