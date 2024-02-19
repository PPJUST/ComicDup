# 缓存设置的Dialog控件
import os

from PySide6.QtCore import Signal
from PySide6.QtWidgets import *

from constant import MAX_EXTRACT_IMAGE_NUMBER
from module import function_cache_hash
from module import function_cache_similargroup
from module import function_comic
from module import function_config
from module import function_hash
from module import function_normal
from module.class_comic_data import ComicData
from ui.listwidget_folderlist import ListWidgetFolderlist
from ui.thread_compare_cache import ThreadCompareCache


class DialogCacheSetting(QDialog):
    """缓存设置的Dialog控件"""
    signal_start_thread = Signal()
    signal_schedule_step = Signal(str)
    signal_schedule_rate = Signal(str)
    signal_compare_cache_finished = Signal()

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
        self.pushButton_update.setText('增量更新缓存')
        self.pushButton_update.clicked.connect(self._update_cache)
        self.verticalLayout_right.addWidget(self.pushButton_update)

        self.pushButton_check_similar = QPushButton()
        self.pushButton_check_similar.setText('缓存数据查重')
        self.pushButton_check_similar.clicked.connect(self._check_similar)
        self.verticalLayout_right.addWidget(self.pushButton_check_similar)

        self.pushButton_refresh = QPushButton()
        self.pushButton_refresh.setText('重置缓存')
        self.pushButton_refresh.clicked.connect(self._refresh_cache)
        self.verticalLayout_right.addWidget(self.pushButton_refresh)

        self.pushButton_clear = QPushButton()
        self.pushButton_clear.setText('清除缓存')
        self.pushButton_clear.clicked.connect(self._clear_cache)
        self.verticalLayout_right.addWidget(self.pushButton_clear)

        self.horizontalLayout_main.addLayout(self.verticalLayout_right)

        # 加载设置
        self._load_setting()

    @staticmethod
    def _accept_folderlist(folderlist: list):
        """接受拖入文件夹信号"""
        function_config.reset_cache_folder(folderlist)

    @staticmethod
    def _update_cache():
        """增量更新缓存"""
        function_normal.print_function_info()
        # 读取缓存
        cache_image_data_dict = function_cache_similargroup.read_similar_groups_pickle()
        cache_folders = function_config.get_cache_folder()

        # 提取符合要求的漫画文件夹和压缩包
        all_comic_folders = set()
        all_archives = set()
        for dirpath in cache_folders:
            comic_folders, archives = function_comic.filter_comic_folder_and_archive(dirpath)
            all_comic_folders.update(comic_folders)
            all_archives.update(archives)

        # 遍历两个列表，并提取漫画数据
        comics_data = {}
        all_files = all_comic_folders.union(all_archives)
        for path in all_files:
            comic_class = ComicData()
            comic_class.set_path(path)
            comic_class.set_calc_number(MAX_EXTRACT_IMAGE_NUMBER)  # 提取图片数上限为3
            comics_data[path] = comic_class

        # 生成图片数据字典
        image_data_dict = {}
        for comic_class in comics_data.values():
            comic_path = comic_class.path
            calc_hash_images = comic_class.calc_hash_images
            for image in calc_hash_images:
                # 生成基本数据
                image_filesize = os.path.getsize(image)
                image_data_dict[image] = {'comic_path': comic_path, 'filesize': image_filesize}
                # 计算hash
                if (image in cache_image_data_dict
                        and image_filesize == cache_image_data_dict['filesize']
                        and cache_image_data_dict['ahash']
                        and cache_image_data_dict['phash']
                        and cache_image_data_dict['dhash']):  # 同一文件且3种hash齐全时才直接提取缓存中的数据，否则重新计算
                    image_data_dict[image]['ahash'] = cache_image_data_dict[image]['ahash']
                    image_data_dict[image]['phash'] = cache_image_data_dict[image]['phash']
                    image_data_dict[image]['dhash'] = cache_image_data_dict[image]['dhash']
                else:
                    hash_dict = function_hash.calc_image_hash(image)
                    image_data_dict[image]['ahash'] = hash_dict['ahash']
                    image_data_dict[image]['phash'] = hash_dict['phash']
                    image_data_dict[image]['dhash'] = hash_dict['dhash']

        # 更新写入hash缓存
        function_cache_hash.update_hash_cache(image_data_dict)

    def _refresh_cache(self):
        """重置缓存"""
        function_normal.print_function_info()
        function_normal.clear_temp_image_folder()
        self._clear_cache()
        self._update_cache()

    @staticmethod
    def _clear_cache():
        """清除缓存"""
        function_normal.print_function_info()
        function_cache_hash.clear_hash_cache()

    def _load_setting(self):
        cache_folders = function_config.get_cache_folder()
        if cache_folders:
            self.ListWidgetFolderlist.add_item(cache_folders)

    def _check_similar(self):
        """对缓存内数据进行查重"""
        self.thread_compare_cache = ThreadCompareCache()
        self.thread_compare_cache.signal_start_thread.connect(self.signal_start_thread.emit)
        self.thread_compare_cache.signal_finished.connect(self.signal_compare_cache_finished.emit)
        self.thread_compare_cache.signal_schedule_step.connect(self.emit_signal_schedule_step)
        self.thread_compare_cache.signal_schedule_rate.connect(self.emit_signal_schedule_rate)
        self.thread_compare_cache.start()
        self.close()

    def emit_signal_schedule_step(self, arg):
        self.signal_schedule_step.emit(arg)

    def emit_signal_schedule_rate(self, arg):
        self.signal_schedule_rate.emit(arg)
