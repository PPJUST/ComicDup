from PySide6.QtCore import QObject

from components.dialog_choose_number.choose_number_model import ChooseNumberModel
from components.dialog_choose_number.choose_number_viewer import ChooseNumberViewer


class ChooseNumberPresenter(QObject):

    def __init__(self, viewer: ChooseNumberViewer, model: ChooseNumberModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

    def get_viewer(self):
        """获取视图组件"""
        return self.viewer
