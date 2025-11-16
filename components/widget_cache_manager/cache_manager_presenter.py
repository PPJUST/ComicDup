from PySide6.QtCore import QObject, Signal

from common.class_count_info import CountInfo
from components.widget_cache_manager.cache_manager_model import CacheManagerModel
from components.widget_cache_manager.cache_manager_viewer import CacheManagerViewer


# fixme 清除无效数据/刷新缓存数据单独拆分为子线程，并显示运行信息
# fixme 缓存模块功能调用时未切换到信息页面

class CacheManagerPresenter(QObject):
    """缓存管理器模块的桥梁组件"""
    CacheRefresh = Signal(name="刷新缓存")
    CacheDeleteUseless = Signal(name="删除无用缓存")
    CacheMatch = Signal(name="缓存内部匹配")
    CacheClear = Signal(name="清空缓存")

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

    def set_options_state(self, is_enable: bool):
        """设置选项启用/禁用"""
        self.viewer.set_options_state(is_enable)

    def _bind_signal(self):
        """绑定信号"""
        self.viewer.RefreshCache.connect(self.CacheRefresh.emit)
        self.viewer.MatchCache.connect(self.CacheMatch.emit)
        self.viewer.DeleteUselessCache.connect(self.CacheDeleteUseless.emit)
        self.viewer.ClearCache.connect(self.CacheClear.emit)
