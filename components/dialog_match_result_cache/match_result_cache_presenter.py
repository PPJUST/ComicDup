from PySide6.QtCore import QObject, Signal

from components.dialog_match_result_cache.match_result_cache_model import MatchResultCacheModel
from components.dialog_match_result_cache.match_result_cache_viewer import MatchResultCacheViewer


class MatchResultCachePresenter(QObject):
    """匹配结果缓存模块的桥梁组件"""
    Restore = Signal(object, name='还原缓存文件')

    def __init__(self, viewer: MatchResultCacheViewer, model: MatchResultCacheModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 绑定信号
        self.viewer.Restore.connect(self.restore)
        self.viewer.Delete.connect(self.delete)
        self.viewer.ShowInfo.connect(self.show_info)

    def save_match_result(self, data):
        """保存匹配结果"""
        self.model.save_match_result(data)

    def restore(self, filename: str):
        """还原缓存文件"""
        data = self.model.read_match_result(filename)
        self.Restore.emit(data)
        self.viewer.close()

    def delete(self, filename: str):
        """删除缓存文件"""
        self.model.delete(filename)

    def show_info(self):
        """显示缓存信息"""
        result_infos = self.model.get_cache_file_infos()
        for index, info in enumerate(result_infos, start=1):
            self.viewer.set_line(index, info)

    def get_viewer(self):
        """获取视图组件"""
        return self.viewer
