from PySide6.QtCore import QObject

from components.widget_search_list.search_list_model import SearchListModel
from components.widget_search_list.search_list_viewer import SearchListViewer


class SearchListPresenter(QObject):
    """搜索列表模块的桥梁组件"""

    def __init__(self, viewer: SearchListViewer, model=SearchListModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 绑定信号
        self.viewer.DropFiles.connect(self.drop_files)

    def drop_files(self, files: list):
        """拖入文件"""
        print(files)
        if isinstance(files, str):
            files = [files]

        for file in files:
            self.viewer.add_row(file)
