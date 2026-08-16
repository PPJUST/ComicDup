from .full_match_comics_model import FullMatchComicsModel
from .full_match_comics_presenter import FullMatchComicsPresenter
from .full_match_comics_viewer import FullMatchComicsViewer


def get_presenter() -> FullMatchComicsPresenter:
    """获取模块的Presenter"""
    viewer = FullMatchComicsViewer()
    model = FullMatchComicsModel()
    presenter = FullMatchComicsPresenter(viewer, model)
    return presenter
