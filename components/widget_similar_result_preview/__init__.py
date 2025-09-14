# 相似匹配结果模块

from .similar_result_preview_model import SimilarResultPreviewModel
from .similar_result_preview_presenter import SimilarResultPreviewPresenter
from .similar_result_preview_viewer import SimilarResultPreviewViewer


def get_presenter() -> SimilarResultPreviewPresenter:
    """获取模块的Presenter"""
    viewer = SimilarResultPreviewViewer()
    model = SimilarResultPreviewModel()
    presenter = SimilarResultPreviewPresenter(viewer, model)
    return presenter
