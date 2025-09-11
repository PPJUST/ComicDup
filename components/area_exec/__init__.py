# 执行模块
from .area_exec_presenter import AreaExecPresenter
from .area_exec_viewer import AreaExecViewer


def get_presenter() -> AreaExecPresenter:
    """获取模块的Presenter"""
    viewer = AreaExecViewer()
    model = None
    presenter = AreaExecPresenter(viewer, model)
    return presenter
