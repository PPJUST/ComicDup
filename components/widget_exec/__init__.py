# 执行模块
from .exec_presenter import ExecPresenter
from .exec_viewer import ExecViewer


def get_presenter() -> ExecPresenter:
    """获取模块的Presenter"""
    viewer = ExecViewer()
    model = None
    presenter = ExecPresenter(viewer, model)
    return presenter
