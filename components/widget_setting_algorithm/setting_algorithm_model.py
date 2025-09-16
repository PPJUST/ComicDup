from common.class_config import TYPES_HASH_ALGORITHM, TYPES_ENHANCE_ALGORITHM
from common.function_config import CONFIG_FILE, check_config_exists, SettingBasicAlgorithm, SettingEnhanceAlgorithm, \
    SettingSimilarThreshold, SettingHashLength, SettingIsEnhanceAlgorithm


class SettingAlgorithmModel:
    """设置模块（相似算法设置项）的模型组件"""

    def __init__(self):
        # 检查配置文件是否存在
        check_config_exists()

        # 实例设置项子类
        self.setting_asic_algorithm = SettingBasicAlgorithm(CONFIG_FILE)
        self.setting_is_enhance_algorithm = SettingIsEnhanceAlgorithm(CONFIG_FILE)
        self.setting_enhance_algorithm = SettingEnhanceAlgorithm(CONFIG_FILE)
        self.setting_similar_threshold = SettingSimilarThreshold(CONFIG_FILE)
        self.setting_hash_length = SettingHashLength(CONFIG_FILE)

    def get_basic_algorithm(self) -> TYPES_HASH_ALGORITHM:
        return self.setting_asic_algorithm.read()

    def get_basic_algorithm_text(self) -> str:
        algorithms = self.get_basic_algorithm()
        print(algorithms)
        return algorithms.text

    def set_basic_algorithm(self, algorithm: TYPES_HASH_ALGORITHM):
        self.setting_asic_algorithm.set(algorithm)

    def get_is_enhance_algorithm(self) -> bool:
        return self.setting_is_enhance_algorithm.read()

    def set_is_enhance_algorithm(self, is_enable: bool):
        self.setting_is_enhance_algorithm.set(is_enable)

    def get_enhance_algorithm(self) -> TYPES_ENHANCE_ALGORITHM:
        return self.setting_enhance_algorithm.read()

    def get_enhance_algorithm_text(self) -> str:
        algorithms = self.get_enhance_algorithm()
        return algorithms.text

    def set_enhance_algorithm(self, algorithm: TYPES_ENHANCE_ALGORITHM):
        self.setting_enhance_algorithm.set(algorithm)

    def get_similar_threshold(self) -> int:
        return self.setting_similar_threshold.read()

    def set_similar_threshold(self, threshold: int):
        self.setting_similar_threshold.set(threshold)

    def get_hash_length(self) -> int:
        return self.setting_hash_length.read()

    def set_hash_length(self, length: int):
        self.setting_hash_length.set(length)
