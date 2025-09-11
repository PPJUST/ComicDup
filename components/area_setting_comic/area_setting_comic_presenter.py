from PySide6.QtCore import QObject

from components.area_setting_comic.area_setting_comic_model import AreaSettingComicModel
from components.area_setting_comic.area_setting_comic_viewer import AreaSettingComicViewer


class AreaSettingComicPresenter(QObject):
    """设置模块（漫画设置项）的桥梁组件"""

    def __init__(self, viewer: AreaSettingComicViewer, model=AreaSettingComicModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
