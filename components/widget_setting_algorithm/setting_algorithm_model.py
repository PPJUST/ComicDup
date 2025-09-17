import math

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

    def convert_percentage_to_distance(self, percentage: int, hash_length: int):
        """转换相似百分比为汉明距离"""
        # 将百分比转换为小数
        similarity = percentage / 100.0

        # 非线性转换：使用指数函数实现非线性关系
        # 当相似度接近100%时，汉明距离迅速趋近于0
        # 当相似度降低时，汉明距离增长速度加快
        max_distance = hash_length // 2  # 最大有意义的距离
        distance = max_distance * (1 - math.pow(similarity, 3))

        # 确保距离在有效范围内并转换为整数
        distance = int(round(distance))
        return max(0, min(distance, max_distance))

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

    def get_hamming_distance(self):
        """获取汉明距离（由相似度百分比换算）"""
        similar_percentage = self.get_similar_threshold()
        hash_length = self.get_hash_length()
        return self.convert_percentage_to_distance(similar_percentage, hash_length)

    def set_similar_threshold(self, threshold: int):
        self.setting_similar_threshold.set(threshold)

    def get_hash_length(self) -> int:
        return self.setting_hash_length.read()

    def set_hash_length(self, length: int):
        self.setting_hash_length.set(length)
