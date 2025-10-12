from PySide6.QtCore import QObject

from common.class_count_info import CountInfo
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

    def set_comic_cache_count_info(self, count_info: CountInfo):
        """设置漫画数据库信息"""
        self.viewer.set_comic_cache_count_info(count_info)

    def set_image_cache_count_info(self, count_info: CountInfo):
        """设置图片数据库信息"""
        self.viewer.set_image_cache_count_info(count_info)

    def set_preview_cache_count_info(self, count_info: CountInfo):
        """设置预览图信息"""
        self.viewer.set_preview_cache_count_info(count_info)

    def _bind_signal(self):
        """绑定信号"""
        # self.viewer.RefreshCache.connect()
        # self.viewer.MatchCache.connect()
        # self.viewer.DeleteUselessCache.connect()
        # self.viewer.ClearCache.connect()
