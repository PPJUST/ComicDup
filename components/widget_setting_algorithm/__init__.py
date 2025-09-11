# 设置模块（相似算法设置项）

from .setting_algorithm_model import SettingAlgorithmModel
from .setting_algorithm_presenter import SettingAlgorithmPresenter
from .setting_algorithm_viewer import SettingAlgorithmViewer


def get_presenter() -> SettingAlgorithmPresenter:
    """获取模块的Presenter"""
    viewer = SettingAlgorithmViewer()
    model = SettingAlgorithmModel()
    presenter = SettingAlgorithmPresenter(viewer, model)
    return presenter
