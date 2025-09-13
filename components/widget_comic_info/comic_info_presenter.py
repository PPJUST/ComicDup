from PySide6.QtCore import QObject

from components.widget_comic_info.comic_info_model import ComicInfoModel
from components.widget_comic_info.comic_info_viewer import ComicInfoViewer


class ComicInfoPresenter(QObject):
    """单个漫画信息模块的桥梁组件"""

    def __init__(self, viewer: ComicInfoViewer, model=ComicInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_showed = None  # 显示的漫画的路径

        # 绑定信号

    def set_comic(self, comic_path:str):
        """设置需要显示的漫画"""
        self.comic_showed = comic_path
        self.model.anylse_comic(comic_path)




