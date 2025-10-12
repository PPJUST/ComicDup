from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.widget_cache_manager.res.ui_cache_manager import Ui_Form


class CacheManagerViewer(QWidget):
    """缓存管理器模块的界面组件"""
    RefreshCache = Signal(name="刷新缓存")
    ClearCache = Signal(name="清空缓存")
    DeleteUselessCache = Signal(name="删除无效缓存")
    MatchCache = Signal(name="缓存内部匹配")

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 绑定信号
        self._bind_signal()

    def set_comic_cache_info_item_count(self, count: int):
        """设置漫画数据库存储项目数"""
        self.ui.label_comic_count.setText(count)

    def set_comic_cache_info_size(self, size: str):
        """设置漫画数据库文件大小"""
        self.ui.label_comic_size.setText(size)

    def set_comic_cache_info_last_update_time(self, time: str):
        """设置漫画数据库最后更新时间"""
        self.ui.label_comic_update.setText(time)

    def set_image_cache_info_item_count(self, count: int):
        """设置图片数据库存储项目数"""
        self.ui.label_image_count.setText(count)

    def set_image_cache_info_size(self, size: str):
        """设置图片数据库文件大小"""
        self.ui.label_image_size.setText(size)

    def set_image_cache_info_last_update_time(self, time: str):
        """设置图片数据库最后更新时间"""
        self.ui.label_image_update.setText(time)

    def set_preview_cache_info_item_count(self, count: int):
        """设置预览图缓存存储图片数量"""
        self.ui.label_preview_count.setText(count)

    def set_preview_cache_info_size(self, size: str):
        """设置预览图缓存存储图片总大小"""
        self.ui.label_preview_size.setText(size)

    def _bind_signal(self):
        """绑定信号"""
        self.ui.pushButton_refresh.clicked.connect(self.RefreshCache.emit)
        self.ui.pushButton_cache_match.clicked.connect(self.MatchCache.emit)
        self.ui.pushButton_delete_useless.clicked.connect(self.DeleteUselessCache.emit)
        self.ui.pushButton_clear.clicked.connect(self.ClearCache.emit)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = CacheManagerViewer()
    program_ui.show()
    app_.exec()
