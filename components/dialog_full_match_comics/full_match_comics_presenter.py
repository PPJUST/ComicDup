from PySide6.QtCore import QObject

from components.dialog_full_match_comics.full_match_comics_model import FullMatchComicsModel
from components.dialog_full_match_comics.full_match_comics_viewer import FullMatchComicsViewer


class FullMatchComicsPresenter(QObject):

    def __init__(self, viewer: FullMatchComicsViewer, model: FullMatchComicsModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

    def get_viewer(self):
        """获取视图组件"""
        return self.viewer
