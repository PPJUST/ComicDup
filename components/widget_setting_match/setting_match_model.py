import configparser

from common.function_config import check_config_exists, CONFIG_FILE, SettingExtractPages, SettingIsMatchCache, \
    SettingIsMatchSimilarFilename, SettingThreadCount


class SettingMatchModel:
    """设置模块（匹配设置项）的模型组件"""

    def __init__(self):
        # 检查配置文件是否存在
        check_config_exists()

        # 读取配置文件实例对象
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE, encoding='utf-8')

        # 实例设置项子类
        self.setting_extract_pages = SettingExtractPages(self.config)
        self.setting_is_match_cache = SettingIsMatchCache(self.config)
        self.setting_is_match_similar_filename = SettingIsMatchSimilarFilename(self.config)
        self.setting_thread_count = SettingThreadCount(self.config)

    def get_extract_pages(self) -> int:
        return self.setting_extract_pages.read()

    def set_extract_pages(self, count: int):
        self.setting_extract_pages.set(count)

    def get_is_match_cache(self) -> bool:
        return self.setting_is_match_cache.read()

    def set_is_match_cache(self, is_enable: bool):
        self.setting_is_match_cache.set(is_enable)

    def get_is_match_similar_filename(self) -> bool:
        return self.setting_is_match_similar_filename.read()

    def set_is_match_similar_filename(self, is_enable: bool):
        self.setting_is_match_similar_filename.set(is_enable)

    def get_thread_count(self) -> int:
        return self.setting_thread_count.read()

    def set_thread_count(self, count: int):
        self.setting_thread_count.set(count)
