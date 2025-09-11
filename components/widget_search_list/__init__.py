# 检索路径模块

from .search_list_model import SearchListModel
from .search_list_presenter import SearchListPresenter
from .search_list_viewer import SearchListViewer


def get_presenter() -> SearchListPresenter:
    """获取模块的Presenter"""
    viewer = SearchListViewer()
    model = SearchListModel()
    presenter = SearchListPresenter(viewer, model)
    return presenter
