# 缓存设置的Dialog控件

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from constant import ICON_REFRESH, ICON_CHECK, ICON_RESET, ICON_CLEAR
from module import function_cache_hash
from module import function_config
from module import function_normal
from thread.thread_compare_cache_manager import ThreadCompareCacheManager
from thread.thread_update_cache import ThreadUpdateCache
from ui.listwidget_folderlist import ListWidgetFolderlist


class DialogCacheSetting(QDialog):
    """缓存设置的Dialog控件"""
    signal_start = Signal()
    signal_step = Signal(str)
    signal_rate = Signal(str)
    signal_finished_compare = Signal()
    signal_finished_update = Signal()
    signal_stopped = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('缓存设置')
        self.horizontalLayout_main = QHBoxLayout(self)

        # 左边列表
        self.verticalLayout_left = QVBoxLayout()

        self.label = QLabel()
        self.label.setText('缓存文件夹')
        self.verticalLayout_left.addWidget(self.label)

        self.ListWidgetFolderlist = ListWidgetFolderlist()
        self.ListWidgetFolderlist.signal_folderlist.connect(self._accept_folderlist)
        self.verticalLayout_left.addWidget(self.ListWidgetFolderlist)

        self.horizontalLayout_main.addLayout(self.verticalLayout_left)

        # 右边按钮
        self.verticalLayout_right = QVBoxLayout()

        self.pushButton_update = QPushButton()
        self.pushButton_update.setText('增量更新')
        self.pushButton_update.setIcon(QIcon(ICON_REFRESH))
        self.pushButton_update.clicked.connect(self._update_cache)
        self.verticalLayout_right.addWidget(self.pushButton_update)

        self.pushButton_check_similar = QPushButton()
        self.pushButton_check_similar.setText('缓存内查重')
        self.pushButton_check_similar.setIcon(QIcon(ICON_CHECK))
        self.pushButton_check_similar.clicked.connect(self._check_similar)
        self.verticalLayout_right.addWidget(self.pushButton_check_similar)

        self.pushButton_refresh = QPushButton()
        self.pushButton_refresh.setText('重置并更新')
        self.pushButton_refresh.setIcon(QIcon(ICON_RESET))
        self.pushButton_refresh.clicked.connect(self._refresh_cache)
        self.verticalLayout_right.addWidget(self.pushButton_refresh)

        self.pushButton_clear_unuseful = QPushButton()
        self.pushButton_clear_unuseful.setText('清理失效项')
        self.pushButton_clear_unuseful.setIcon(QIcon(ICON_CLEAR))
        self.pushButton_clear_unuseful.clicked.connect(self._clear_unuseful)
        self.verticalLayout_right.addWidget(self.pushButton_clear_unuseful)

        self.pushButton_delete = QPushButton()
        self.pushButton_delete.setText('删除缓存')
        self.pushButton_delete.setIcon(QIcon(ICON_CLEAR))
        self.pushButton_delete.clicked.connect(self._delete_cache)
        self.verticalLayout_right.addWidget(self.pushButton_delete)

        self.horizontalLayout_main.addLayout(self.verticalLayout_right)

        # 加载设置
        self._load_setting()

        # 实例化子线程
        self.thread_update = ThreadUpdateCache()
        self.thread_update.signal_start.connect(lambda: self.signal_start.emit())
        self.thread_update.signal_finished.connect(lambda: self.signal_finished_update.emit())
        self.thread_update.signal_stopped.connect(lambda: self.signal_stopped.emit())
        self.thread_update.signal_step.connect(self.emit_signal_step)
        self.thread_update.signal_rate.connect(self.emit_signal_rate)

        self.thread_compare_cache = ThreadCompareCacheManager()
        self.thread_compare_cache.signal_start.connect(lambda: self.signal_start.emit())
        self.thread_compare_cache.signal_finished.connect(lambda: self.signal_finished_compare.emit())
        self.thread_compare_cache.signal_stopped.connect(lambda: self.signal_stopped.emit())
        self.thread_compare_cache.signal_step.connect(self.emit_signal_step)
        self.thread_compare_cache.signal_rate.connect(self.emit_signal_rate)

    def reset_stop_code(self):
        self.thread_update.reset_stop_code()
        self.thread_compare_cache.reset_stop_code()

    @staticmethod
    def _accept_folderlist(folderlist: list):
        """接受拖入文件夹信号"""
        function_config.reset_cache_folder(folderlist)

    def _update_cache(self):
        """增量更新缓存"""
        self.thread_update.start()
        self.close()

    def _refresh_cache(self):
        """重置缓存"""
        function_normal.print_function_info()
        function_normal.clear_temp_image_folder()
        self._delete_cache()
        self._update_cache()

    @staticmethod
    def _delete_cache():
        """删除全部缓存"""
        function_normal.print_function_info()
        function_cache_hash.delete_hash_cache()

    @staticmethod
    def _clear_unuseful():
        """清理无效项"""
        function_normal.print_function_info()
        function_cache_hash.clear_unuseful_cache()

    def _load_setting(self):
        cache_folders = function_config.get_cache_folder()
        if cache_folders:
            self.ListWidgetFolderlist.add_item(cache_folders)

    def _check_similar(self):
        """对缓存内数据进行查重"""
        self.thread_compare_cache.start()
        self.close()

    def emit_signal_step(self, arg):
        self.signal_step.emit(arg)

    def emit_signal_rate(self, arg):
        self.signal_rate.emit(arg)
