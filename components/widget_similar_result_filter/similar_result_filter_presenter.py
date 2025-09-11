from PySide6.QtCore import QObject



from components.widget_similar_result_filter.similar_result_filter_model import SimilarResultFilterModel
from components.widget_similar_result_filter.similar_result_filter_viewer import SimilarResultFilterViewer


class SimilarResultFilterPresenter(QObject):
    """相似结果筛选器模块的桥梁组件"""

    def __init__(self, viewer: SimilarResultFilterViewer, model=SimilarResultFilterModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
