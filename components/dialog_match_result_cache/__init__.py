# 匹配结果缓存模块
from .match_result_cache_model import MatchResultCacheModel
from .match_result_cache_presenter import MatchResultCachePresenter
from .match_result_cache_viewer import MatchResultCacheViewer


def get_presenter() -> MatchResultCachePresenter:
    """获取模块的Presenter"""
    viewer = MatchResultCacheViewer()
    model = MatchResultCacheModel()
    presenter = MatchResultCachePresenter(viewer, model)
    return presenter
