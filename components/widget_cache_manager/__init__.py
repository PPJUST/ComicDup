# 缓存管理器模块
from .cache_manager_model import CacheManagerModel
from .cache_manager_presenter import CacheManagerPresenter
from .cache_manager_viewer import CacheManagerViewer


def get_presenter() -> CacheManagerPresenter:
    """获取模块的Presenter"""
    viewer = CacheManagerViewer()
    model = CacheManagerModel()
    presenter = CacheManagerPresenter(viewer, model)
    return presenter
