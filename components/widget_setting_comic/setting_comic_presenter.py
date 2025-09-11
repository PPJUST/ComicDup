from PySide6.QtCore import QObject

from components.widget_setting_comic.setting_comic_model import SettingComicModel
from components.widget_setting_comic.setting_comic_viewer import SettingComicViewer


class SettingComicPresenter(QObject):
    """设置模块（漫画设置项）的桥梁组件"""

    def __init__(self, viewer: SettingComicViewer, model=SettingComicModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
