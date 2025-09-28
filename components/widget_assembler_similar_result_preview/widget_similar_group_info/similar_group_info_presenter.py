from typing import List

from PySide6.QtCore import QObject

from common.class_comic import ComicInfo
from components import widget_assembler_comics_preview
from components.widget_assembler_similar_result_preview import widget_comic_info
from components.widget_assembler_similar_result_preview.widget_comic_info import ComicInfoPresenter
from components.widget_assembler_similar_result_preview.widget_similar_group_info.similar_group_info_model import \
    SimilarGroupInfoModel
from components.widget_assembler_similar_result_preview.widget_similar_group_info.similar_group_info_viewer import \
    SimilarGroupInfoViewer


class SimilarGroupInfoPresenter(QObject):
    """单个相似组信息模块的桥梁组件"""

    def __init__(self, viewer: SimilarGroupInfoViewer, model: SimilarGroupInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_info_list: List[ComicInfo] = []  # 内部漫画项的漫画信息类列表
        self.comics_presenter: List[ComicInfoPresenter] = []  # 内部漫画项的桥梁组件


        # 绑定信号
        self.viewer.Preview.connect(self.preview_comics)

    def set_group_index(self, index: int):
        """设置当前组的编号"""
        self.viewer.set_group_index(index)

    def set_item_count(self):
        """设置当前组内部项目的总数"""
        self.viewer.set_item_count(len(self.comic_info_list))

    def set_group_sign(self, sign: str):
        """设置当前组的标记"""
        self.viewer.set_group_sign(sign)

    def add_comics(self, comic_info_list: List[ComicInfo]):
        """批量添加内部漫画信息项"""
        for comic_info in comic_info_list:
            self.add_comic(comic_info)

    def add_comic(self, comic_info: ComicInfo):
        """添加内部漫画信息项"""
        self.comic_info_list.append(comic_info)

        comic_info_presenter = widget_comic_info.get_presenter()
        comic_info_presenter.set_comic_info(comic_info)
        self.comics_presenter.append(comic_info_presenter)

        widget = comic_info_presenter.get_viewer()
        self.viewer.add_widget(widget)

    def preview_comics(self):
        """预览当前组内的所有漫画"""
        self.dialog_comics_preview = widget_assembler_comics_preview.get_assembler()

        for comic_info in self.comic_info_list:
            self.dialog_comics_preview.add_comic(comic_info)

        self.dialog_comics_preview.exec()
        self.dialog_comics_preview.deleteLater()
