# 漫画预览模块

from .comic_preview_model import ComicPreviewModel
from .comic_preview_presenter import ComicPreviewPresenter
from .comic_preview_viewer import ComicPreviewViewer


def get_presenter() -> ComicPreviewPresenter:
    """获取模块的Presenter"""
    viewer = ComicPreviewViewer()
    model = ComicPreviewModel()
    presenter = ComicPreviewPresenter(viewer, model)
    return presenter
