# 单本漫画相关数据的类
import os

import natsort

from module import function_cache_comicdata
from module import function_comic
from module import function_normal


class ComicData:
    """单本漫画相关数据的类"""

    def __init__(self):
        # 漫画数据
        self.path = ''  # 原始路径
        self.filetype = ''  # 文件类型，folder或archive
        self.preview_file = ''  # 预览图路径
        self.images = []  # 图片路径列表
        self.image_count = 0  # 图片数量
        self.filesize = 0  # 文件大小，单位字节
        # 其他数据
        self.calc_hash_images = []  # 计算图片哈希的图片路径列表

    def set_path(self, path):
        """设置漫画路径，并提取相关信息"""
        self.path = path
        self.filesize = function_normal.get_size(path)
        if os.path.isdir(path):
            self.filetype = 'folder'
            for i in os.listdir(path):
                filepath = os.path.normpath(os.path.join(path, i))
                filetype = function_normal.check_filetype(filepath)
                if filetype == 'image':
                    self.images.append(filepath)
            self.images = natsort.natsorted(self.images)
            self.image_count = len(self.images)
            self.preview_file = self.images[0]
        else:
            self.filetype = 'archive'
            self.image_count = function_comic.count_archive_image(path)

    def set_calc_number(self, calc_number: int):
        """设置需要计算的图片数量，并提取响应的图片路径"""
        calc_number = min(calc_number, self.image_count)
        if calc_number != 0:
            if self.filetype == 'folder':
                self.calc_hash_images = self.images[0:calc_number]

            # 如果是压缩包类型，则需要先提取本地已解压的记录（若存在），否则进行解压
            elif self.filetype == 'archive':
                extract_images_cache = function_cache_comicdata.get_extract_images_from_archive(self.path)
                if len(extract_images_cache) < calc_number:
                    self.calc_hash_images = function_comic.extract_archive_image(self.path, calc_number)
                else:
                    self.calc_hash_images = extract_images_cache
                self.preview_file = self.calc_hash_images[0]
