# 相似结果筛选器模块
from .area_similar_result_filter_model import AreaSimilarResultFilterModel
from .area_similar_result_filter_presenter import AreaSimilarResultFilterPresenter
from .area_similar_result_filter_viewer import AreaSimilarResultFilterViewer


def get_presenter() -> AreaSimilarResultFilterPresenter:
    """获取模块的Presenter"""
    viewer = AreaSimilarResultFilterViewer()
    model = AreaSimilarResultFilterModel()
    presenter = AreaSimilarResultFilterPresenter(viewer, model)
    return presenter
