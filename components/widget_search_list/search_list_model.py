from common.function_config import CONFIG_FILE, SettingSearchList


class SearchListModel:
    """搜索列表模块的模型组件"""

    def __init__(self, ):
        super().__init__()

    def write_paths_to_config(self, paths: list):
        config = SettingSearchList(CONFIG_FILE)
        config.set(paths)

    def read_paths_from_config(self) -> list:
        config = SettingSearchList(CONFIG_FILE)
        return config.read()
