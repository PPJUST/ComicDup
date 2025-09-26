# 相似组预览框架模块

from .similar_group_preview_model import SimilarGroupPreviewModel
from .similar_group_preview_presenter import SimilarGroupPreviewPresenter
from .similar_group_preview_viewer import SimilarGroupPreviewViewer


def get_presenter() -> SimilarGroupPreviewPresenter:
    """获取模块的Presenter"""
    viewer = SimilarGroupPreviewViewer()
    model = SimilarGroupPreviewModel()
    presenter = SimilarGroupPreviewPresenter(viewer, model)
    return presenter
