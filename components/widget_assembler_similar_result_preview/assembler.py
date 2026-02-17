from typing import List

from PySide6.QtCore import Signal, QObject

from common.class_comic import ComicInfoBase
from common.class_order import ORDER_KEYS, ORDER_DIRECTIONS
from components.widget_assembler_similar_result_preview import widget_similar_result_preview


class AssemblerSimilarResultPreview(QObject):
    """相似匹配结果预览器组装器"""
    UpdateComicInfo = Signal(ComicInfoBase, name='更新数据库中的漫画信息')

    def __init__(self):
        super().__init__()
        self.presenter = widget_similar_result_preview.get_presenter()

        self.similar_groups: List[List[ComicInfoBase]] = []  # 原始相似组列表

        self.presenter.UpdateComicInfo.connect(self.UpdateComicInfo.emit)

    def get_presenter(self):
        """获取presenter"""
        return self.presenter

    def get_viewer(self):
        """获取viewer"""
        return self.presenter.get_viewer()

    def show_similar_result(self):
        """显示相似结果"""
        self.presenter.reload()

    def sort_groups_item(self, sort_key: ORDER_KEYS, sort_direction: ORDER_DIRECTIONS):
        """排序相似组内元素"""
        self.presenter.sort_groups_item(sort_key, sort_direction)

    def reload(self):
        """重新加载"""
        self.presenter.set_groups(self.similar_groups)
        self.presenter.reload()

    def show_filter_result(self, similar_groups_filter: List[List[ComicInfoBase]]):
        """显示筛选后的相似匹配结果"""
        self.presenter.set_groups(similar_groups_filter)
        self.presenter.reload()

    def hide_complete_group(self):
        """隐藏已经完成处理的相似组"""
        self.presenter.hide_complete_group()

    def show_same_item_in_group(self):
        """仅在相似组中显示存在相同项的漫画项（根据文件指纹判断）"""
        # 筛选相似组，仅提取同组中存在相同项的漫画项
        similar_groups_filter = []
        for group in self.similar_groups:
            group_filter = []
            fingerprints = [i.fingerprint for i in group]
            for info_class in group:
                fingerprint = info_class.fingerprint
                if fingerprints.count(fingerprint) >= 2:
                    group_filter.append(info_class)
            if len(group_filter) >= 2:
                similar_groups_filter.append(group_filter)

        self.show_filter_result(similar_groups_filter)

    def show_same_filesize_item_in_group(self):
        """仅在相似组中显示存在相同项的漫画项（根据文件大小判断）"""
        # 筛选相似组，仅提取同组中存在相同项的漫画项
        similar_groups_filter = []
        for group in self.similar_groups:
            group_filter = []
            filesizes = [i.get_real_filesize() for i in group]
            for info_class in group:
                filesize = info_class.get_real_filesize()
                if filesize and filesizes.count(filesize) >= 2:
                    group_filter.append(info_class)
            if len(group_filter) >= 2:
                similar_groups_filter.append(group_filter)

        self.show_filter_result(similar_groups_filter)

    def show_similar_pages_item_in_group(self, pages_threshold: int = 30):
        """仅在相似组中显示页数相近的漫画项"""
        similar_groups_filter = []
        for group in self.similar_groups:
            group_filter = []
            # 先按页数排序
            group = sorted(group, key=lambda x: x.page_count)
            # 遍历相似组元素
            for index in range(len(group)):
                # 如果当前项的页码与左右元素页数差异小于n，则加入列表
                pages_current = group[index].page_count
                if index - 1 >= 0:
                    pages_previous = group[index - 1].page_count
                    diff_left = abs(pages_current - pages_previous)
                    if diff_left <= pages_threshold:
                        group_filter.append(group[index])
                        continue
                if index + 1 < len(group):
                    pages_next = group[index + 1].page_count
                    diff_right = abs(pages_current - pages_next)
                    if diff_right <= pages_threshold:
                        group_filter.append(group[index])
                        continue
            if len(group_filter) >= 2:
                similar_groups_filter.append(group_filter)

        self.show_filter_result(similar_groups_filter)

    def set_groups(self, comic_info_lists: List[List[ComicInfoBase]]):
        """设置相似组列表"""
        self.similar_groups = comic_info_lists
        self.presenter.set_groups(comic_info_lists)

    def set_is_reconfirm_before_delete(self, is_reconfirm: bool):
        """设置是否删除前再次确认"""
        self.presenter.set_is_reconfirm_before_delete(is_reconfirm)

    def clear(self):
        """清空结果"""
        self.presenter.clear()
