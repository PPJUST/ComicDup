from typing import List

from common.class_comic import ComicInfo
from components.widget_assembler_similar_result_preview import widget_similar_result_preview, widget_similar_group_info


class AssemblerSimilarResultPreview:
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
        self.presenter.show_group(1)

    def add_similar_group(self, comic_info_list: List[ComicInfo]):
        """添加相似信息组
        :param comic_info_list: 相似组内的所有漫画的漫画信息类"""
        # 实例化一个相似组信息控件
        similar_group_info_presenter = widget_similar_group_info.get_presenter()
        # 向控件中添加漫画信息（路径交由控件内部处理，不需要实例化漫画信息控件）
        similar_group_info_presenter.add_comics(comic_info_list)
        # 设置控件的编号
        current_count = self.presenter.get_group_count()
        similar_group_info_presenter.set_group_index(current_count+1)
        #  将相似组信息控件添加到主控件中
        self.presenter.add_group(similar_group_info_presenter)

    def clear(self):
        """清空结果"""
        self.presenter.clear()
