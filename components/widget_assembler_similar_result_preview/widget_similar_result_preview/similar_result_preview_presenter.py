from typing import List

from PySide6.QtCore import QObject

from common import function_file
from common.class_comic import ComicInfoBase
from components.widget_assembler_similar_result_preview import widget_similar_group_info
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

        self.comic_info_groups: List[List[ComicInfoBase]] = []  # 相似组列表
        self.comic_widgets_showed: List[SimilarGroupInfoPresenter] = []  # 显示的相似组控件
        self.current_page = 1  # 当前页数
        self.total_page = 1  # 总页数
        self.show_group_count = 5  # 一页显示的组数

        # 绑定信号
        self.viewer.NextPage.connect(self.next_page)
        self.viewer.PreviousPage.connect(self.previous_page)
        self.viewer.ChangeShowGroupCount.connect(self.change_show_group_count)

    def set_groups(self, comic_info_list_list: List[List[ComicInfoBase]]):
        """设置相似组列表"""
        self.comic_info_groups = comic_info_list_list
        self._calc_total_page()
        self._show_count_info()

    def show_page(self, show_page: int):
        """显示第n页相似组漫画
        :param show_page:显示的页数"""
        self.viewer.clear()
        index_start = (show_page - 1) * self.show_group_count
        index_end = index_start + self.show_group_count
        for index, group in enumerate(self.comic_info_groups[index_start:index_end], start=1):
            group: List[ComicInfoBase]
            # 实例化单本漫画的控件类
            similar_group_info_presenter = widget_similar_group_info.get_presenter()
            # 向控件中添加漫画信息（路径交由控件内部处理，不需要实例化漫画信息控件）
            similar_group_info_presenter.add_comics(group)
            # 设置编号
            index_page = (show_page - 1) * self.show_group_count + index
            similar_group_info_presenter.set_group_index(index_page)
            # 添加控件到变量中
            self.comic_widgets_showed.append(similar_group_info_presenter)
            # 添加控件到视图中
            viewer = similar_group_info_presenter.get_viewer()
            self.viewer.add_similar_group(viewer)

    def previous_page(self):
        """上一页"""
        if self.current_page == 1:
            pass
        else:
            self.current_page -= 1
            self.viewer.set_current_page(self.current_page)
            self.show_page(self.current_page)

    def next_page(self):
        """下一页"""
        if self.current_page == self.total_page:
            pass
        else:
            self.current_page += 1
            self.viewer.set_current_page(self.current_page)
            self.show_page(self.current_page)

    def reload(self):
        """重新加载"""
        self.current_page = 1
        self.viewer.set_current_page(self.current_page)
        self.show_page(self.current_page)

    def change_show_group_count(self, show_count: int):
        """修改一页显示的组数"""
        self.show_group_count = int(show_count)
        # 更新组数
        self._calc_total_page()
        # 重新显示第一页
        self.show_page(1)

    def set_is_reconfirm_before_delete(self, is_reconfirm: bool):
        """设置是否删除前再次确认"""
        for widget in self.comic_widgets_showed:
            widget: SimilarGroupInfoPresenter
            widget.set_is_reconfirm_before_delete(is_reconfirm)

    def get_group_count(self):
        """获取组数"""
        return len(self.comic_info_groups)

    def get_viewer(self):
        """获取模块的Viewer"""
        return self.viewer

    def _show_count_info(self):
        """显示统计信息"""
        # 相似组数
        groups_count = len(self.comic_info_groups)
        # 内部漫画项目数
        items_count = 0
        for group in self.comic_info_groups:
            items_count += len(group)
        # 文件总大小
        filesize_count_bytes = 0
        for group in self.comic_info_groups:
            for comic_info in group:
                filesize_count_bytes += comic_info.filesize_bytes
        filesize_str = function_file.format_bytes_size(filesize_count_bytes)  # 规范文件大小表示

        self.viewer.set_group_count(groups_count)
        self.viewer.set_item_count(items_count)
        self.viewer.set_filesize_count(filesize_str)

    def clear(self):
        """清空结果"""
        self.viewer.clear()
        self.comic_info_groups.clear()
        self.current_page = 1
        self.total_page = 1

    def _calc_total_page(self):
        """计算总页数（向上整除）"""
        self.total_page = (len(self.comic_info_groups) - 1 + self.show_group_count) // self.show_group_count  # 向上整除
        self.viewer.set_total_page(self.total_page)
