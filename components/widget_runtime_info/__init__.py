# 运行信息模块
from .runtime_info_model import RuntimeInfoModel
from .runtime_info_presenter import RuntimeInfoPresenter
from .runtime_info_viewer import RuntimeInfoViewer


def get_presenter() -> RuntimeInfoPresenter:
    """获取模块的Presenter"""
    viewer = RuntimeInfoViewer()
    model = RuntimeInfoModel()
    presenter = RuntimeInfoPresenter(viewer, model)
    return presenter
