from PySide6.QtCore import QObject

from common.class_config import TYPES_HASH_ALGORITHM, TYPES_ENHANCE_ALGORITHM
from components.widget_setting_algorithm.setting_algorithm_model import SettingAlgorithmModel
from components.widget_setting_algorithm.setting_algorithm_viewer import SettingAlgorithmViewer


class SettingAlgorithmPresenter(QObject):
    """设置模块（相似算法设置项）的桥梁组件"""

    def __init__(self, viewer: SettingAlgorithmViewer, model: SettingAlgorithmModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 加载初始设置
        self._load_setting()

        # 绑定信号
        self._bind_signal()

    def get_base_algorithm(self) -> TYPES_HASH_ALGORITHM:
        """获取基础hash算法"""
        return self.model.get_basic_algorithm()

    def get_is_enhance_algorithm(self) -> bool:
        return self.model.get_is_enhance_algorithm()

    def get_enhance_algorithm(self) -> TYPES_ENHANCE_ALGORITHM:
        return self.model.get_enhance_algorithm()

    def get_similar_threshold(self) -> int:
        return self.model.get_similar_threshold()

    def get_hamming_distance(self) -> int:
        return self.model.get_hamming_distance()

    def get_hash_length(self) -> int:
        return self.model.get_hash_length()

    def _load_setting(self):
        """加载初始设置"""
        basic_algorithm = self.model.get_basic_algorithm_text()
        self.viewer.set_basic_algorithm(basic_algorithm)

        is_enhance_algorithm = self.model.get_is_enhance_algorithm()
        self.viewer.set_is_enhance_algorithm(is_enhance_algorithm)

        enhance_algorithm = self.model.get_enhance_algorithm_text()
        self.viewer.set_enhance_algorithm(enhance_algorithm)

        similar_threshold = self.model.get_similar_threshold()
        self.viewer.set_similar_threshold(similar_threshold)

        hash_length = self.model.get_hash_length()
        self.viewer.set_hash_length(hash_length)

    def _bind_signal(self):
        """绑定信号"""
        self.viewer.ChangeBasicAlgorithm.connect(self.model.set_basic_algorithm)
        self.viewer.ChangeIsEnhanceAlgorithm.connect(self.model.set_is_enhance_algorithm)
        self.viewer.ChangeEnhanceAlgorithm.connect(self.model.set_enhance_algorithm)
        self.viewer.ChangeSimilarThreshold.connect(self.model.set_similar_threshold)
        self.viewer.ChangeHashLength.connect(self.model.set_hash_length)
