from PySide6.QtCore import QObject, Signal

from components.widget_similar_result_filter.similar_result_filter_model import SimilarResultFilterModel
from components.widget_similar_result_filter.similar_result_filter_viewer import SimilarResultFilterViewer


class SimilarResultFilterPresenter(QObject):
    """相似结果筛选器模块的桥梁组件"""
    RefreshResult = Signal(name='重置匹配结果')
    FilterSameItems = Signal(name='筛选器 仅显示页数、文件大小相同项')
    FilterExcludeDiffPages = Signal(name='筛选器 剔除页数差异过大项')

    def __init__(self, viewer: SimilarResultFilterViewer, model:SimilarResultFilterModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 绑定信号
        self.viewer.FilterSameItems.connect(self.FilterSameItems.emit)
        self.viewer.FilterExcludeDiffPages.connect(self.FilterExcludeDiffPages.emit)
        self.viewer.RefreshResult.connect(self.RefreshResult.emit)
