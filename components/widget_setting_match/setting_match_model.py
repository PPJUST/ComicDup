from common.function_config import *


class SettingMatchModel:
    """设置模块（匹配设置项）的模型组件"""

    def __init__(self):
        # 检查配置文件是否存在
        check_config_exists()

        # 实例设置项子类
        self.setting_extract_pages = SettingExtractPages(CONFIG_FILE)
        self.setting_is_match_cache = SettingIsMatchCache(CONFIG_FILE)
        self.setting_is_match_same_parent_folder = SettingIsMatchSameParentFolder(CONFIG_FILE)
        self.setting_match_parent_folder_level = SettingMatchParentFolderLevel(CONFIG_FILE)
        self.setting_is_match_similar_filename = SettingIsMatchSimilarFilename(CONFIG_FILE)
        self.setting_thread_count = SettingThreadCount(CONFIG_FILE)

    def get_extract_pages(self) -> int:
        return self.setting_extract_pages.read()

    def set_extract_pages(self, count: int):
        self.setting_extract_pages.set(count)

    def get_is_match_cache(self) -> bool:
        return self.setting_is_match_cache.read()

    def set_is_match_cache(self, is_enable: bool):
        self.setting_is_match_cache.set(is_enable)

    def get_is_match_same_parent_folder(self) -> bool:
        return self.setting_is_match_same_parent_folder.read()

    def set_is_match_same_parent_folder(self, is_enable: bool):
        self.setting_is_match_same_parent_folder.set(is_enable)

    def get_match_parent_folder_level(self) -> int:
        return self.setting_match_parent_folder_level.read()

    def set_match_parent_folder_level(self, count: int):
        self.setting_match_parent_folder_level.set(count)

    def get_is_match_similar_filename(self) -> bool:
        return self.setting_is_match_similar_filename.read()

    def set_is_match_similar_filename(self, is_enable: bool):
        self.setting_is_match_similar_filename.set(is_enable)

    def get_thread_count(self) -> int:
        return self.setting_thread_count.read()

    def set_thread_count(self, count: int):
        self.setting_thread_count.set(count)
