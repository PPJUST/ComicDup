from typing import List

from PySide6.QtCore import QObject

from components.widget_assembler_similar_result_preview.widget_similar_group_info import SimilarGroupInfoPresenter
from components.widget_assembler_similar_result_preview.widget_similar_result_preview.similar_result_preview_model import \
    SimilarResultPreviewModel
from components.widget_assembler_similar_result_preview.widget_similar_result_preview.similar_result_preview_viewer import \
    SimilarResultPreviewViewer


class SimilarResultPreviewPresenter(QObject):
    """相似匹配结果模块的桥梁组件"""

    def __init__(self, viewer: SimilarResultPreviewViewer, model: SimilarResultPreviewModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.widgets_similar_group_info: List[SimilarGroupInfoPresenter] = []  # 需要显示的相似信息组类列表
        self.current_page = 1  # 当前页数
        self.total_page = 1  # 总页数
        self.show_group_count = 5  # 一页显示的组数

        # 绑定信号
        self.viewer.NextPage.connect(self.next_page)
        self.viewer.PreviousPage.connect(self.previous_page)
        self.viewer.ChangeShowGroupCount.connect(self.change_show_group_count)

    def add_group(self, similar_group_info_presenter: SimilarGroupInfoPresenter):
        """添加相似信息组类"""
        self.widgets_similar_group_info.append(similar_group_info_presenter)
        self._calc_total_page()

    def show_group(self, show_page: int):
        """显示相似组
        :param show_page:显示的页数"""
        self.viewer.clear()
        index_start = (show_page - 1) * self.show_group_count
        index_end = index_start + self.show_group_count
        for presenter in self.widgets_similar_group_info[index_start:index_end]:
            self.viewer.add_similar_group(presenter.viewer)

    def previous_page(self):
        """上一页"""

    def next_page(self):
        """下一页"""

    def change_show_group_count(self, show_count: int):
        """修改一页显示的组数"""
        self.show_group_count = int(show_count)
        self._calc_total_page()

    def _calc_total_page(self):
        """计算总页数（向上整除）"""
        self.total_page = (len(self.widgets_similar_group_info) + self.show_group_count) // self.show_group_count  # 向上整除

    def get_viewer(self):
        """获取模块的Viewer"""
        return self.viewer