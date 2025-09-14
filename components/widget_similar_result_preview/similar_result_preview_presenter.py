from PySide6.QtCore import QObject

from components.widget_similar_result_preview.similar_result_preview_model import SimilarResultPreviewModel
from components.widget_similar_result_preview.similar_result_preview_viewer import SimilarResultPreviewViewer


class SimilarResultPreviewPresenter(QObject):
    """相似匹配结果模块的桥梁组件"""

    def __init__(self, viewer: SimilarResultPreviewViewer, model: SimilarResultPreviewModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 绑定信号
        self.viewer.NextPage.connect(self.next_page)
        self.viewer.PreviousPage.connect(self.previous_page)
        self.viewer.ChangeShowGroupCount.connect(self.change_show_group_count)

    def previous_page(self):
        """上一页"""

    def next_page(self):
        """下一页"""

    def change_show_group_count(self, show_count: int):
        """修改一页显示的组数"""
