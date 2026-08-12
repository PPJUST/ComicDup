from PySide6.QtCore import QObject

from components.dialog_rename_comic.rename_comic_model import RenameComicModel
from components.dialog_rename_comic.rename_comic_viewer import RenameComicViewer


class RenameComicPresenter(QObject):

    def __init__(self, viewer: RenameComicViewer, model: RenameComicModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

    def get_viewer(self):
        """获取视图组件"""
        return self.viewer
