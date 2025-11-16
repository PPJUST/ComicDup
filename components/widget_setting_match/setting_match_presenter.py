from PySide6.QtCore import QObject

from components.widget_setting_match.setting_match_model import SettingMatchModel
from components.widget_setting_match.setting_match_viewer import SettingMatchViewer


class SettingMatchPresenter(QObject):
    """设置模块（匹配设置项）的桥梁组件"""

    def __init__(self, viewer: SettingMatchViewer, model: SettingMatchModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 加载初始设置
        self._load_setting()

        # 绑定信号
        self._bind_signal()

    def get_extract_pages(self) -> int:
        """获取每本漫画的提取页数"""
        return self.model.get_extract_pages()

    def get_is_match_cache(self) -> bool:
        """获取是否匹配缓存"""
        return self.model.get_is_match_cache()

    def get_is_match_similar_filename(self) -> bool:
        """获取是否仅匹配相似文件名"""
        return self.model.get_is_match_similar_filename()

    def get_thread_count(self) -> int:
        """获取线程数"""
        return self.model.get_thread_count()

    def set_options_state(self, is_enable: bool):
        """设置选项启用/禁用"""
        self.viewer.set_options_state(is_enable)

    def _load_setting(self):
        """加载初始设置"""
        extract_pages = self.model.get_extract_pages()
        self.viewer.set_extract_pages(extract_pages)

        is_match_cache = self.model.get_is_match_cache()
        self.viewer.set_is_match_cache(is_match_cache)

        is_match_similar_filename = self.model.get_is_match_similar_filename()
        self.viewer.set_is_match_similar_filename(is_match_similar_filename)

        thread_count = self.model.get_thread_count()
        self.viewer.set_thread_count(thread_count)

    def _bind_signal(self):
        """绑定信号"""
        self.viewer.ChangeExtractPages.connect(self.model.set_extract_pages)
        self.viewer.ChangeIsMatchCache.connect(self.model.set_is_match_cache)
        self.viewer.ChangeIsMatchSimilarFilename.connect(self.model.set_is_match_similar_filename)
        self.viewer.ChangeThreadCount.connect(self.model.set_thread_count)
