# 设置模块（漫画设置项）

from .setting_comic_model import SettingComicModel
from .setting_comic_presenter import SettingComicPresenter
from .setting_comic_viewer import SettingComicViewer


def get_presenter() -> SettingComicPresenter:
    """获取模块的Presenter"""
    viewer = SettingComicViewer()
    model = SettingComicModel()
    presenter = SettingComicPresenter(viewer, model)
    return presenter
