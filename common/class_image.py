import math
import os

import lzytools.file
import lzytools.image
from PIL import Image

from common import function_archive
from common.class_comic import ComicInfo
from common.class_config import TYPES_HASH_ALGORITHM, SimilarAlgorithm, FileType, FileTypes


class ImageInfo:
    """图片信息类"""

    def __init__(self, image_path: str):
        # 图片路径
        self.image_path: str = os.path.normpath(image_path)
        # 图片大小（字节bytes）
        self.filesize: int = 0
        # 图片hash值
        # aHash
        self.aHash_64: str = ''
        self.aHash_144: str = ''
        self.aHash_256: str = ''
        # pHash
        self.pHash_64: str = ''
        self.pHash_144: str = ''
        self.pHash_256: str = ''
        # dHash
        self.dHash_64: str = ''
        self.dHash_144: str = ''
        self.dHash_256: str = ''

        # 图片所属漫画的路径
        self.comic_path_belong: str = ''
        # 图片所属漫画的文件类型
        self.comic_filetype_belong: FileTypes = None
        # 图片所属漫画的文件指纹
        self.comic_fingerprint_belong: str = ''

    def calc_filesize(self):
        """计算图片文件大小"""
        if isinstance(self.comic_filetype_belong, FileType.Folder):
            self.filesize = lzytools.file.get_size(self.image_path)
        elif isinstance(self.comic_filetype_belong, FileType.Archive):
            self.filesize = function_archive.get_filesize_inside(self.comic_path_belong, self.image_path)

    def calc_hash(self, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        """计算图片hash值"""
        hash_type_str = hash_type.text
        hash_size = int(math.sqrt(hash_length))
        # 创建ImageFile对象
        image_pil = Image.open(self.image_path)
        hash_dict = lzytools.image.calc_hash(image_pil, hash_type_str, hash_size)
        if hash_dict['ahash']:
            if len(hash_dict['ahash']) == 64:
                self.aHash_64 = hash_dict['ahash']
            elif len(hash_dict['ahash']) == 144:
                self.aHash_144 = hash_dict['ahash']
            elif len(hash_dict['ahash']) == 256:
                self.aHash_256 = hash_dict['ahash']
        elif hash_dict['phash']:
            if len(hash_dict['phash']) == 64:
                self.pHash_64 = hash_dict['phash']
            elif len(hash_dict['phash']) == 144:
                self.pHash_144 = hash_dict['phash']
            elif len(hash_dict['phash']) == 256:
                self.pHash_256 = hash_dict['phash']
        elif hash_dict['dhash']:
            if len(hash_dict['dhash']) == 64:
                self.dHash_64 = hash_dict['dhash']
            elif len(hash_dict['dhash']) == 144:
                self.dHash_144 = hash_dict['dhash']
            elif len(hash_dict['dhash']) == 256:
                self.dHash_256 = hash_dict['dhash']

    def update_info_by_comic_info(self, comic_info: ComicInfo):
        """根据漫画信息类更新信息"""
        self.comic_path_belong = comic_info.filepath
        self.comic_filetype_belong = comic_info.filetype
        self.comic_fingerprint_belong = comic_info.fingerprint
        self.calc_filesize()

    def is_useful(self):
        """检查图片是否有效"""
        if isinstance(self.comic_filetype_belong, FileType.Folder):
            if os.path.exists(self.image_path):
                filesize_latest = lzytools.file.get_size(self.image_path)
                return filesize_latest == self.filesize
        elif isinstance(self.comic_filetype_belong, FileType.Archive):
            if os.path.exists(self.comic_path_belong):
                filesize_latest = function_archive.get_filesize_inside(self.comic_path_belong, self.image_path)
                return filesize_latest == self.filesize

        return False

    def update_hash(self, hash_: str, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        """更新hash值"""
        if isinstance(hash_type, SimilarAlgorithm.aHash):
            if hash_length == 64:
                self.aHash_64 = hash_
            elif hash_length == 144:
                self.aHash_144 = hash_
            elif hash_length == 256:
                self.aHash_256 = hash_
        elif isinstance(hash_type, SimilarAlgorithm.pHash):
            if hash_length == 64:
                self.pHash_64 = hash_
            elif hash_length == 144:
                self.pHash_144 = hash_
            elif hash_length == 256:
                self.pHash_256 = hash_
        elif isinstance(hash_type, SimilarAlgorithm.dHash):
            if hash_length == 64:
                self.dHash_64 = hash_
            elif hash_length == 144:
                self.dHash_144 = hash_
            elif hash_length == 256:
                self.dHash_256 = hash_

    def get_hash(self, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        """获取指定的hash值"""
        if isinstance(hash_type, SimilarAlgorithm.aHash) or hash_type == SimilarAlgorithm.aHash:
            if hash_length == 64:
                return self.aHash_64
            elif hash_length == 144:
                return self.aHash_144
            elif hash_length == 256:
                return self.aHash_256
        elif isinstance(hash_type, SimilarAlgorithm.pHash) or hash_type == SimilarAlgorithm.pHash:
            if hash_length == 64:
                return self.pHash_64
            elif hash_length == 144:
                return self.pHash_144
            elif hash_length == 256:
                return self.pHash_256
        elif isinstance(hash_type, SimilarAlgorithm.dHash) or hash_type == SimilarAlgorithm.dHash:
            if hash_length == 64:
                return self.dHash_64
            elif hash_length == 144:
                return self.dHash_144
            elif hash_length == 256:
                return self.dHash_256

        return ''

    """手动更新参数的方法"""

    def update_filesize(self, filesize: int):
        """更新图片大小"""
        self.filesize = filesize

    def update_comic_path_belong(self, comic_path: str):
        """更新图片所属漫画的路径"""
        self.comic_path_belong = comic_path

    def update_comic_filetype_belong(self, comic_filetype: FileTypes):
        """更新图片所属漫画的文件类型"""
        self.comic_filetype_belong = comic_filetype

    def update_comic_fingerprint_belong(self, comic_fingerprint: str):
        """更新图片所属漫画的指纹"""
        self.comic_fingerprint_belong = comic_fingerprint
