# 设置模块（匹配设置项）

from .setting_match_model import SettingMatchModel
from .setting_match_presenter import SettingMatchPresenter
from .setting_match_viewer import SettingMatchViewer


def get_presenter() -> SettingMatchPresenter:
    """获取模块的Presenter"""
    viewer = SettingMatchViewer()
    model = SettingMatchModel()
    presenter = SettingMatchPresenter(viewer, model)
    return presenter
