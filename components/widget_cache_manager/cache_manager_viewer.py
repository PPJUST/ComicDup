from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from common.class_count_info import CountInfo
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

        self.ui.pushButton_refresh.setEnabled(False)  # 备忘录
        self.ui.pushButton_cache_match.setEnabled(False)  # 备忘录
        self.ui.pushButton_delete_useless.setEnabled(False)  # 备忘录
        self.ui.pushButton_clear.setEnabled(False)  # 备忘录

    def set_comic_cache_count_info(self, count_info: CountInfo):
        """设置漫画数据库信息"""
        self.ui.label_comic_count.setText(str(count_info.get_item_count()))
        self.ui.label_comic_size.setText(str(count_info.get_size_count()))
        self.ui.label_comic_update.setText(str(count_info.get_update_time()))

    def set_image_cache_count_info(self, count_info: CountInfo):
        """设置图片数据库信息"""
        self.ui.label_image_count.setText(str(count_info.get_item_count()))
        self.ui.label_image_size.setText(str(count_info.get_size_count()))
        self.ui.label_image_update.setText(str(count_info.get_update_time()))

    def set_preview_cache_count_info(self, count_info: CountInfo):
        """设置预览图信息"""
        self.ui.label_preview_count.setText(str(count_info.get_item_count()))
        self.ui.label_preview_size.setText(str(count_info.get_size_count()))

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
