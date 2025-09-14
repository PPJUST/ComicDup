# 单个漫画信息模块

from .comic_info_model import ComicInfoModel
from .comic_info_presenter import ComicInfoPresenter
from .comic_info_viewer import ComicInfoViewer


def get_presenter() -> ComicInfoPresenter:
    """获取模块的Presenter"""
    viewer = ComicInfoViewer()
    model = ComicInfoModel()
    presenter = ComicInfoPresenter(viewer, model)
    return presenter
