# 设置模块（匹配设置项）
from .area_setting_match_model import AreaSettingMatchModel
from .area_setting_match_presenter import AreaSettingMatchPresenter
from .area_setting_match_viewer import AreaSettingMatchViewer


def get_presenter() -> AreaSettingMatchPresenter:
    """获取模块的Presenter"""
    viewer = AreaSettingMatchViewer()
    model = AreaSettingMatchModel()
    presenter = AreaSettingMatchPresenter(viewer, model)
    return presenter
