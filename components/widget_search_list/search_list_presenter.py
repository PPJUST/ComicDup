import natsort
from PySide6.QtCore import QObject

from components.widget_search_list.search_list_model import SearchListModel
from components.widget_search_list.search_list_viewer import SearchListViewer


class SearchListPresenter(QObject):
    """搜索列表模块的桥梁组件"""

    def __init__(self, viewer: SearchListViewer, model: SearchListModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 初始化
        self._load_setting()

        # 绑定信号
        self.viewer.DropFiles.connect(self.drop_files)

    def get_paths(self):
        """获取所有文件路径"""
        paths = self.viewer.get_paths()
        # 去重
        paths = list(set(paths))
        # 排序
        paths = natsort.os_sorted(paths)

        return paths

    def drop_files(self, files: list):
        """拖入文件"""
        if isinstance(files, str):
            files = [files]

        for file in files:
            self.viewer.add_row(file)

        # 写入配置文件
        self.model.write_paths_to_config(self.get_paths())

    def _load_setting(self):
        """加载配置文件"""
        paths = self.model.read_paths_from_config()
        if paths:
            for path in paths:
                self.viewer.add_row(path)
