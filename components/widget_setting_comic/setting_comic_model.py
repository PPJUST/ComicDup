from common.function_config import check_config_exists, CONFIG_FILE, SettingComicPagesLowerLimit, \
    SettingIsAnalyzeArchive, SettingIsAllowOtherFiletypesInComic


class SettingComicModel:
    """设置模块（漫画设置项）的模型组件"""

    def __init__(self):
        super().__init__()
        # 检查配置文件是否存在
        check_config_exists()

        # 实例设置项子类
        self.setting_pages_lower_limit = SettingComicPagesLowerLimit(CONFIG_FILE)
        self.setting_is_analyze_archive = SettingIsAnalyzeArchive(CONFIG_FILE)
        self.setting_is_allow_other_filetypes = SettingIsAllowOtherFiletypesInComic(CONFIG_FILE)

    def get_pages_lower_limit(self) -> int:
        return self.setting_pages_lower_limit.read()

    def set_pages_lower_limit(self, limit: int):
        self.setting_pages_lower_limit.set(limit)

    def get_is_analyze_archive(self) -> bool:
        return self.setting_is_analyze_archive.read()

    def set_is_analyze_archive(self, is_enable: bool):
        self.setting_is_analyze_archive.set(is_enable)

    def get_is_allow_other_filetypes(self) -> bool:
        return self.setting_is_allow_other_filetypes.read()

    def set_is_allow_other_filetypes(self, is_enable: bool):
        self.setting_is_allow_other_filetypes.set(is_enable)
