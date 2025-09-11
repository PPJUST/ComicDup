from PySide6.QtCore import QObject

from components.area_setting_algorithm.area_setting_algorithm_model import AreaSettingAlgorithmModel
from components.area_setting_algorithm.area_setting_algorithm_viewer import AreaSettingAlgorithmViewer


class AreaSettingAlgorithmPresenter(QObject):
    """设置模块（相似算法设置项）的桥梁组件"""

    def __init__(self, viewer: AreaSettingAlgorithmViewer, model=AreaSettingAlgorithmModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
