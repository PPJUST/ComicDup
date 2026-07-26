# 单个漫画信息模块

from .comic_info_line_model import ComicInfoLineModel
from .comic_info_line_presenter import ComicInfoLinePresenter
from .comic_info_line_viewer import ComicInfoLineViewer


def get_presenter() -> ComicInfoLinePresenter:
    """获取模块的Presenter"""
    viewer = ComicInfoLineViewer()
    model = ComicInfoLineModel()
    presenter = ComicInfoLinePresenter(viewer, model)
    return presenter
