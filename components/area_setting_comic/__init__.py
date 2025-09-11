# 设置模块（漫画设置项）
from .area_setting_comic_model import AreaSettingComicModel
from .area_setting_comic_presenter import AreaSettingComicPresenter
from .area_setting_comic_viewer import AreaSettingComicViewer


def get_presenter() -> AreaSettingComicPresenter:
    """获取模块的Presenter"""
    viewer = AreaSettingComicViewer()
    model = AreaSettingComicModel()
    presenter = AreaSettingComicPresenter(viewer, model)
    return presenter
