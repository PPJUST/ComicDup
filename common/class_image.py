import os
from abc import ABC, abstractmethod

import lzytools.archive
import lzytools.file
import lzytools.image

from common import function_archive, function_image
from common.class_comic import ComicInfoBase
from common.class_config import TYPES_HASH_ALGORITHM, SimilarAlgorithm, FileTypes


class ImageInfoBase(ABC):
    """图片信息基类"""

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
        self.belong_comic_path: str = ''
        # 图片所属漫画的文件类型
        self.belong_comic_filetype: FileTypes = None
        # 图片所属漫画的文件指纹
        self.belong_comic_fingerprint: str = ''

        # 虚拟路径（漫画路径+图片相对路径）
        self.faker_path: str = ''

    @abstractmethod
    def calc_filesize(self):
        """计算图片文件大小"""

    @abstractmethod
    def calc_hash(self, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        """计算图片hash值"""

    def update_info_by_comic_info(self, comic_info: ComicInfoBase):
        """根据漫画信息类更新信息"""
        self.belong_comic_path = comic_info.filepath
        self.belong_comic_filetype = comic_info.filetype
        self.belong_comic_fingerprint = comic_info.fingerprint
        self.calc_filesize()
        self.calc_faker_path()

    @abstractmethod
    def calc_faker_path(self):
        """计算虚拟路径"""

    @abstractmethod
    def is_useful(self):
        """检查图片是否有效"""

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

    def update_belong_comic_path(self, comic_path: str):
        """更新图片所属漫画的路径"""
        self.belong_comic_path = comic_path

    def update_belong_comic_filetype(self, comic_filetype: FileTypes):
        """更新图片所属漫画的文件类型"""
        self.belong_comic_filetype = comic_filetype

    def update_belong_comic_fingerprint(self, comic_fingerprint: str):
        """更新图片所属漫画的指纹"""
        self.belong_comic_fingerprint = comic_fingerprint

    def update_faker_path(self, faker_path: str):
        """更新虚拟路径"""
        self.faker_path = faker_path


class ImageInfoFolder(ImageInfoBase):
    """文件夹类漫画的图片信息类"""

    def __init__(self, image_path: str):
        super().__init__(image_path)

    def calc_filesize(self):
        super().calc_filesize()
        self.filesize = lzytools.file.get_size(self.image_path)

    def calc_hash(self, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        super().calc_hash(hash_type, hash_length)
        hash_ = function_image.calc_image_hash(self.image_path, hash_type, hash_length)

        if isinstance(hash_type, SimilarAlgorithm.aHash):
            if len(hash_) == 64:
                self.aHash_64 = hash_
            elif len(hash_) == 144:
                self.aHash_144 = hash_
            elif len(hash_) == 256:
                self.aHash_256 = hash_
        elif isinstance(hash_type, SimilarAlgorithm.pHash):
            if len(hash_) == 64:
                self.pHash_64 = hash_
            elif len(hash_) == 144:
                self.pHash_144 = hash_
            elif len(hash_) == 256:
                self.pHash_256 = hash_
        elif isinstance(hash_type, SimilarAlgorithm.dHash):
            if len(hash_) == 64:
                self.dHash_64 = hash_
            elif len(hash_) == 144:
                self.dHash_144 = hash_
            elif len(hash_) == 256:
                self.dHash_256 = hash_

    def is_useful(self):
        super().is_useful()
        if os.path.exists(self.image_path):
            filesize_latest = lzytools.file.get_size(self.image_path)
            return filesize_latest == self.filesize

        return False

    def calc_faker_path(self):
        super().calc_faker_path()
        self.faker_path = self.image_path


class ImageInfoArchive(ImageInfoBase):
    """压缩文件类漫画的图片信息类"""

    def __init__(self, image_path: str):
        super().__init__(image_path)

    def calc_filesize(self):
        super().calc_filesize()

        self.filesize = function_archive.get_filesize_inside(self.belong_comic_path, self.image_path)
    def calc_hash(self, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        super().calc_hash(hash_type, hash_length)
        hash_ = function_image.calc_archive_image_hash(self.belong_comic_path, self.image_path, hash_type, hash_length)

        if isinstance(hash_type, SimilarAlgorithm.aHash):
            if len(hash_) == 64:
                self.aHash_64 = hash_
            elif len(hash_) == 144:
                self.aHash_144 = hash_
            elif len(hash_) == 256:
                self.aHash_256 = hash_
        elif isinstance(hash_type, SimilarAlgorithm.pHash):
            if len(hash_) == 64:
                self.pHash_64 = hash_
            elif len(hash_) == 144:
                self.pHash_144 = hash_
            elif len(hash_) == 256:
                self.pHash_256 = hash_
        elif isinstance(hash_type, SimilarAlgorithm.dHash):
            if len(hash_) == 64:
                self.dHash_64 = hash_
            elif len(hash_) == 144:
                self.dHash_144 = hash_
            elif len(hash_) == 256:
                self.dHash_256 = hash_

    def is_useful(self):
        super().is_useful()
        if os.path.exists(self.belong_comic_path):
            filesize_latest = function_archive.get_filesize_inside(self.belong_comic_path, self.image_path)
            return filesize_latest == self.filesize

        return False

    def calc_faker_path(self):
        super().calc_faker_path()
        self.faker_path = os.path.normpath(os.path.join(self.belong_comic_path, self.image_path))
