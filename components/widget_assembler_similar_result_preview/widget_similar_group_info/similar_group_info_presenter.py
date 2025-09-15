from typing import List

from PySide6.QtCore import QObject

from components.widget_assembler_similar_result_preview import widget_comic_info
from components.widget_assembler_similar_result_preview.widget_comic_info import ComicInfoPresenter
from components.widget_assembler_similar_result_preview.widget_similar_group_info.similar_group_info_model import SimilarGroupInfoModel
from components.widget_assembler_similar_result_preview.widget_similar_group_info.similar_group_info_viewer import SimilarGroupInfoViewer


class SimilarGroupInfoPresenter(QObject):
    """单个相似组信息模块的桥梁组件"""

    def __init__(self, viewer: SimilarGroupInfoViewer, model: SimilarGroupInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comics_path: List[str] = []  # 内部漫画项的路径
        self.comics_presenter: List[ComicInfoPresenter] = []  # 内部漫画项的桥梁组件

    def set_group_index(self, index: int):
        """设置当前组的编号"""
        self.viewer.set_group_index(index)

    def set_item_count(self):
        """设置当前组内部项目的总数"""
        self.viewer.set_item_count(len(self.comics_path))

    def set_group_sign(self, sign: str):
        """设置当前组的标记"""
        self.viewer.set_group_sign(sign)

    def add_comics(self, comics_path: List[str]):
        """批量添加内部漫画信息项"""
        for comic_path in comics_path:
            self.add_comic(comic_path)

    def add_comic(self, comic_path: str):
        """添加内部漫画信息项
        :param comic_path:漫画路径"""
        self.comics_path.append(comic_path)

        comic_info_presenter = widget_comic_info.get_presenter()
        comic_info_presenter.set_comic(comic_path)
        self.comics_presenter.append(comic_info_presenter)

        widget = comic_info_presenter.get_viewer()
        self.viewer.add_widget(widget)
