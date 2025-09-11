from PySide6.QtCore import QObject


from components.area_similar_result_filter.area_similar_result_filter_model import AreaSimilarResultFilterModel
from components.area_similar_result_filter.area_similar_result_filter_viewer import AreaSimilarResultFilterViewer


class AreaSimilarResultFilterPresenter(QObject):
    """相似结果筛选器模块的桥梁组件"""

    def __init__(self, viewer: AreaSimilarResultFilterViewer, model=AreaSimilarResultFilterModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
