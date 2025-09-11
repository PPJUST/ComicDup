from PySide6.QtCore import QObject


from components.widget_search_list.search_list_model import SearchListModel
from components.widget_search_list.search_list_viewer import SearchListViewer


class SearchListPresenter(QObject):
    """检索路径模块的桥梁组件"""

    def __init__(self, viewer: SearchListViewer, model=SearchListModel):
        super().__init__()
        self.viewer = viewer
        self.model = model
