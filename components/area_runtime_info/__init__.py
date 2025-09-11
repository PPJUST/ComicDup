# 运行信息模块
from .area_runtime_info_model import AreaRuntimeInfoModel
from .area_runtime_info_presenter import AreaRuntimeInfoPresenter
from .area_runtime_info_viewer import AreaRuntimeInfoViewer


def get_presenter() -> AreaRuntimeInfoPresenter:
    """获取模块的Presenter"""
    viewer = AreaRuntimeInfoViewer()
    model = AreaRuntimeInfoModel()
    presenter = AreaRuntimeInfoPresenter(viewer, model)
    return presenter
