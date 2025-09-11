from PySide6.QtCore import QObject

from components.area_search_list.area_search_list_model import AreaSearchListModel
from components.area_search_list.area_search_list_viewer import AreaSearchListViewer


class AreaSearchListPresenter(QObject):
    """检索路径模块的桥梁组件"""

    def __init__(self, viewer: AreaSearchListViewer, model=AreaSearchListModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
