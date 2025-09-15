from typing import List

from components.widget_assembler_similar_result_preview import widget_similar_result_preview, widget_similar_group_info


class AssemblerSimilarResultPreview:
    def __init__(self):
        self.presenter = widget_similar_result_preview.get_presenter()

    def get_presenter(self):
        """获取presenter"""
        return self.presenter

    def add_similar_group(self, comics_path: List[str]):
        """添加相似信息组
        :param comics_path: 相似组内的所有漫画的路径"""
        # 实例化一个相似组信息控件
        similar_group_info_presenter = widget_similar_group_info.get_presenter()
        # 向控件中添加漫画信息（路径交由控件内部处理，不需要实例化漫画信息控件）
        similar_group_info_presenter.add_comics(comics_path)
        #  将相似组信息控件添加到主控件中
        self.presenter.add_group(similar_group_info_presenter)
