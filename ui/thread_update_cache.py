# 进行相似比较的子线程
import os

from PySide6.QtCore import QThread, Signal

from constant import MAX_EXTRACT_IMAGE_NUMBER
from module import function_cache_hash, function_comic
from module import function_cache_similargroup
from module import function_config
from module import function_hash
from module.class_comic_data import ComicData


class ThreadUpdateCache(QThread):
    """增量更新缓存数据的子线程"""
    signal_start_thread = Signal()
    signal_schedule_step = Signal(str)
    signal_schedule_rate = Signal(str)
    signal_finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        # 获取设置
        self.signal_start_thread.emit()
        # 读取缓存
        cache_image_data_dict = function_cache_similargroup.read_similar_groups_pickle()
        cache_folders = function_config.get_cache_folder()

        self.signal_schedule_step.emit('1/3 检查文件夹')
        # 提取符合要求的漫画文件夹和压缩包
        all_comic_folders = set()
        all_archives = set()
        for index_rate, dirpath in enumerate(cache_folders, start=1):
            self.signal_schedule_rate.emit(f'{index_rate}/{len(cache_folders)}')
            comic_folders, archives = function_comic.filter_comic_folder_and_archive(dirpath)
            all_comic_folders.update(comic_folders)
            all_archives.update(archives)

        self.signal_schedule_step.emit('2/3 提取漫画数据')
        # 遍历两个列表，并提取漫画数据
        comics_data = {}
        all_files = all_comic_folders.union(all_archives)
        for index_rate, path in enumerate(all_files, start=1):
            self.signal_schedule_rate.emit(f'{index_rate}/{len(all_files)}')
            comic_class = ComicData()
            comic_class.set_path(path)
            comic_class.set_calc_number(MAX_EXTRACT_IMAGE_NUMBER)  # 提取图片数上限为3
            comics_data[path] = comic_class

        self.signal_schedule_step.emit('3/3 计算Hash')
        # 生成图片数据字典
        image_data_dict = {}
        for index_rate, comic_class in enumerate(comics_data.values(), start=1):
            self.signal_schedule_rate.emit(f'{index_rate}/{len(comics_data)}')
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

        self.signal_finished.emit()
