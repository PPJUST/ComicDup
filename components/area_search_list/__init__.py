# 检索路径模块
from .area_search_list_model import AreaSearchListModel
from .area_search_list_presenter import AreaSearchListPresenter
from .area_search_list_viewer import AreaSearchListViewer


def get_presenter() -> AreaSearchListPresenter:
    """获取模块的Presenter"""
    viewer = AreaSearchListViewer()
    model = AreaSearchListModel()
    presenter = AreaSearchListPresenter(viewer, model)
    return presenter
