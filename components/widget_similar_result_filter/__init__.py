# 相似结果筛选器模块

from .similar_result_filter_model import SimilarResultFilterModel
from .similar_result_filter_presenter import SimilarResultFilterPresenter
from .similar_result_filter_viewer import SimilarResultFilterViewer


def get_presenter() -> SimilarResultFilterPresenter:
    """获取模块的Presenter"""
    viewer = SimilarResultFilterViewer()
    model = SimilarResultFilterModel()
    presenter = SimilarResultFilterPresenter(viewer, model)
    return presenter
