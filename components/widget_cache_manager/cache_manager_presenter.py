from PySide6.QtCore import QObject

from components.widget_cache_manager.cache_manager_model import CacheManagerModel
from components.widget_cache_manager.cache_manager_viewer import CacheManagerViewer


class CacheManagerPresenter(QObject):
    """缓存管理器模块的桥梁组件"""

    def __init__(self, viewer: CacheManagerViewer, model: CacheManagerModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 绑定信号
        self._bind_signal()

    def _bind_signal(self):
        """绑定信号"""
        # self.viewer.RefreshCache.connect()
        # self.viewer.MatchCache.connect()
        # self.viewer.DeleteUselessCache.connect()
        # self.viewer.ClearCache.connect()
