from typing import List

from common.class_comic import ComicInfoBase
from components.widget_assembler_similar_result_preview import widget_similar_result_preview


class AssemblerSimilarResultPreview:
    """相似匹配结果预览器组装器"""

    def __init__(self):
        self.presenter = widget_similar_result_preview.get_presenter()

    def get_presenter(self):
        """获取presenter"""
        return self.presenter

    def get_viewer(self):
        """获取viewer"""
        return self.presenter.get_viewer()

    def show_similar_result(self):
        """显示相似结果"""
        self.presenter.show_page(1)

    def set_groups(self, comic_info_list_list: List[List[ComicInfoBase]]):
        """设置相似组列表"""
        self.presenter.set_groups(comic_info_list_list)

    def set_is_reconfirm_before_delete(self, is_reconfirm: bool):
        """设置是否删除前再次确认"""
        self.presenter.set_is_reconfirm_before_delete(is_reconfirm)

    def clear(self):
        """清空结果"""
        self.presenter.clear()
