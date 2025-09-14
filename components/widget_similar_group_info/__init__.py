# 单个相似组信息模块

from .similar_group_info_model import SimilarGroupInfoModel
from .similar_group_info_presenter import SimilarGroupInfoPresenter
from .similar_group_info_viewer import SimilarGroupInfoViewer


def get_presenter() -> SimilarGroupInfoPresenter:
    """获取模块的Presenter"""
    viewer = SimilarGroupInfoViewer()
    model = SimilarGroupInfoModel()
    presenter = SimilarGroupInfoPresenter(viewer, model)
    return presenter
