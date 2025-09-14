from PySide6.QtCore import QObject

from components.widget_similar_group_info.similar_group_info_model import SimilarGroupInfoModel
from components.widget_similar_group_info.similar_group_info_viewer import SimilarGroupInfoViewer


class SimilarGroupInfoPresenter(QObject):
    """单个相似组信息模块的桥梁组件"""

    def __init__(self, viewer: SimilarGroupInfoViewer, model: SimilarGroupInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

    def set_group_index(self, index: int):
        """设置当前组的编号"""
        self.viewer.set_group_index(index)

    def set_item_count(self, count: int):
        """设置当前组内部项目的总数"""
        self.viewer.set_item_count(count)

    def set_group_sign(self, sign: str):
        """设置当前组的标记"""
        self.viewer.set_group_sign(sign)

    def add_comic(self, comic_path: str):
        """添加漫画项目
        :param comic_path:漫画路径"""
        self.viewer.add_comic(comic_path)