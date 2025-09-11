# 设置模块（相似算法设置项）
from .area_setting_algorithm_model import AreaSettingAlgorithmModel
from .area_setting_algorithm_presenter import AreaSettingAlgorithmPresenter
from .area_setting_algorithm_viewer import AreaSettingAlgorithmViewer


def get_presenter() -> AreaSettingAlgorithmPresenter:
    """获取模块的Presenter"""
    viewer = AreaSettingAlgorithmViewer()
    model = AreaSettingAlgorithmModel()
    presenter = AreaSettingAlgorithmPresenter(viewer, model)
    return presenter
