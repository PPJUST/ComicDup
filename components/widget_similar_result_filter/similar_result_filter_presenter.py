from PySide6.QtCore import QObject, Signal

from components.widget_similar_result_filter.similar_result_filter_model import SimilarResultFilterModel
from components.widget_similar_result_filter.similar_result_filter_viewer import SimilarResultFilterViewer


class SimilarResultFilterPresenter(QObject):
    """相似结果筛选器模块的桥梁组件"""
    RefreshResult = Signal(name='重置匹配结果')
    HideCompleteGroup = Signal(name='隐藏完成处理的相似组')
    FilterSameItems = Signal(name='筛选器 仅显示页数、文件大小相同项')
    FilterSameFilesizeItems = Signal(name='筛选器 仅显示文件大小相同项')
    FilterExcludeDiffPages = Signal(int, name='筛选器 剔除页数差异过大项')
    ReconfirmDelete = Signal(bool, name='删除前再次确认')
    ChangeSortKeyInGroup = Signal(str, name='组内排序的排序键值改变')
    ChangeSortDirectionInGroup = Signal(str, name='组内排序的排序方向改变')
    ChangeSortKeyBetweenGroup = Signal(str, name='组间排序的排序键值改变')
    ChangeSortDirectionBetweenGroup = Signal(str, name='组间排序的排序方向改变')

    def __init__(self, viewer: SimilarResultFilterViewer, model: SimilarResultFilterModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 绑定信号
        self.viewer.FilterSameItems.connect(self.FilterSameItems.emit)
        self.viewer.FilterSameFilesizeItems.connect(self.FilterSameFilesizeItems.emit)
        self.viewer.FilterExcludeDiffPages.connect(lambda param: self.FilterExcludeDiffPages.emit(param))
        self.viewer.RefreshResult.connect(self.RefreshResult.emit)
        self.viewer.HideCompleteGroup.connect(self.HideCompleteGroup.emit)
        self.viewer.ReconfirmDelete.connect(self.ReconfirmDelete.emit)
        self.viewer.ChangeSortKeyInGroup.connect(self.ChangeSortKeyInGroup.emit)
        self.viewer.ChangeSortDirectionInGroup.connect(self.ChangeSortDirectionInGroup.emit)
        self.viewer.ChangeSortKeyBetweenGroup.connect(self.ChangeSortKeyBetweenGroup.emit)
        self.viewer.ChangeSortDirectionBetweenGroup.connect(self.ChangeSortDirectionBetweenGroup.emit)

    def get_order_key_in_group(self):
        """获取组内排序的排序键"""
        return self.viewer.get_order_key_in_group()

    def get_order_direction_in_group(self):
        """获取组内排序的排序方向"""
        return self.viewer.get_order_direction_in_group()

    def get_order_key_between_group(self):
        """获取组间排序的排序键"""
        return self.viewer.get_order_key_between_group()

    def get_order_direction_between_group(self):
        """获取组间排序的排序方向"""
        return self.viewer.get_order_direction_between_group()