from PySide6.QtCore import QObject

from components.dialog_choose_full_match_comic.choose_full_match_comic_model import ChooseFullMatchComicModel
from components.dialog_choose_full_match_comic.choose_full_match_comic_viewer import ChooseFullMatchComicViewer


class DialogChooseFullMatchComicPresenter(QObject):

    def __init__(self, viewer: ChooseFullMatchComicViewer, model: ChooseFullMatchComicModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

    def get_viewer(self):
        """获取视图组件"""
        return self.viewer
