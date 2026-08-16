from typing import List

from PySide6.QtCore import QObject

from common import function_match_pages
from common.class_comic import ComicInfoBase
from components.dialog_full_match_comics.full_match_comics_model import FullMatchComicsModel
from components.dialog_full_match_comics.full_match_comics_viewer import FullMatchComicsViewer


class FullMatchComicsPresenter(QObject):

    def __init__(self, viewer: FullMatchComicsViewer, model: FullMatchComicsModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_info_group = []

        self.viewer.FullMatch.connect(self.full_match)

    def full_match(self):
        """执行全量对比"""
        comic_1_index = self.viewer.get_comic_index_1()
        comic_2_index = self.viewer.get_comic_index_2()

        print(comic_1_index, comic_2_index)

        if comic_1_index == comic_2_index:
            self.viewer.show_simple_result('错误，编号相同，请重新选择')
            return
        if comic_1_index > len(self.comic_info_group):
            self.viewer.show_simple_result('错误，主漫画编号超出范围，请重新选择')
            return
        if comic_2_index > len(self.comic_info_group):
            self.viewer.show_simple_result('错误，次漫画编号超出范围，请重新选择')
            return

        comic_1_info = self.comic_info_group[comic_1_index - 1]
        comic_2_info = self.comic_info_group[comic_2_index - 1]

        two_comic_page_match_group = function_match_pages.match_pages(comic_1_info, comic_2_info)
        print('两本漫画全量匹配页码对应表', two_comic_page_match_group)
        result_code = function_match_pages.check_match_result(comic_1_info, comic_2_info,
                                                              two_comic_page_match_group)
        self.viewer.show_simple_result(result_code.text)

    def set_comic_info_group(self, comic_info_group: List[ComicInfoBase]):
        """设置漫画信息组"""
        self.comic_info_group = comic_info_group

        # 添加选项到下拉框
        items = []
        self.viewer.clear_combobox_items()
        for index, comic_info in enumerate(comic_info_group, start=1):
            info = f'{index} - {comic_info.filename}'
            items.append(info)
        self.viewer.add_combobox_items(items)

    def exec(self):
        self.viewer.exec()

    def get_viewer(self):
        """获取视图组件"""
        return self.viewer
