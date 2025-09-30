# 漫画相关的自定义类
import math
import os

import lzytools.archive
import lzytools.file
import lzytools.image
import natsort
from PIL import Image

from common import function_file, function_archive, function_cache
from common.class_config import TYPES_HASH_ALGORITHM, SimilarAlgorithm


class FileType:
    """文件类型"""

    class File:
        """文件"""
        text = '文件'

    class Folder:
        """文件夹"""
        text = '文件夹'

    class Archive:
        """压缩文件"""
        text = '压缩文件'

    class Unknown:
        """未知类型"""
        text = '未知类型'

    class Error:
        """错误"""
        text = '错误'


FileTypes = (FileType.File, FileType.Folder, FileType.Archive, FileType.Unknown)


class ComicInfo:
    """漫画信息类"""

    def __init__(self, comic_path: str, db_model: bool = False):
        # 文件信息
        # 路径
        self.filepath: str = os.path.normpath(comic_path)
        # 文件名（含扩展名）
        self.filename: str = os.path.basename(self.filepath)
        # 文件标题（不含扩展名）
        self.filetitle: str = os.path.splitext(self.filename)[0]
        # 文件父级路径
        self.parent_dirpath: str = os.path.dirname(self.filepath)
        # 文件大小（字节）
        self.filesize_bytes: int = None
        # 文件真实大小（文件类型为解压文件时使用，为解压后的文件大小）（字节）
        self.filesize_bytes_extracted: int = self.filesize_bytes
        # 文件类型
        self.filetype: FileTypes = None
        # 文件修改时间（自纪元以来的秒数）
        self.modified_time: float = None

        # 漫画信息
        # 内部文件路径
        self.page_paths: tuple = None
        # 页数
        self.page_count: int = None
        # 预览小图本地路径
        self.preview_path: str = None

        # 文件指纹
        # 文件指纹 hash值（xxhash，如果是压缩文件类，则为压缩文件的hash，如果是文件夹类，则为其内部所有文件的hash算法整合）
        self.fingerprint_xxhash: str = None
        # 文件指纹 文件大小
        self.fingerprint_filesize: int = None
        # 文件指纹 内部文件路径（升序排序，|间隔）
        self.fingerprint_inside_paths: str = None

        # 提取需要的信息（数据库模式时，直接由数据库类赋值）
        if not db_model:
            # 文件大小
            self.filesize_bytes = lzytools.file.get_size(self.filepath)
            self.filesize_bytes_extracted = self.filesize_bytes
            # 文件类型
            if os.path.isfile(self.filepath):
                if function_archive.is_archive_by_filename(self.filepath):
                    self.filetype = FileType.Archive()
                else:
                    self.filetype = FileType.File()
            elif os.path.isdir(self.filepath):
                self.filetype = FileType.Folder()
            else:
                self.filetype = FileType.Unknown()
            # 文件修改时间
            self.modified_time = os.path.getmtime(self.filepath)
            # 页数和预览图
            if isinstance(self.filetype, FileType.Folder):
                self._analyse_folder_pages()
            elif isinstance(self.filetype, FileType.Archive):
                self._analyse_archive_pages()
                self._analyse_archive_size_extracted()

        # 计算文件指纹
        self._calc_fingerprint()

    def get_page_paths(self):
        """获取漫画页路径列表"""
        return self.page_paths

    def update_filesize(self, filesize_bytes: int):
        """更新文件大小（字节）"""
        self.filesize_bytes = filesize_bytes

    def update_filesize_extracted(self, filesize_bytes: int):
        """更新文件真实大小（字节，文件类型为解压文件时使用，为解压后的文件大小）"""
        self.filesize_bytes_extracted = filesize_bytes

    def update_filetype(self, filetype: FileTypes):
        """更新文件类型"""
        self.filetype = filetype

    def update_modified_time(self, modified_time: float):
        """更新文件修改时间"""
        self.modified_time = modified_time

    def update_page_paths(self, page_paths: tuple):
        """更新漫画页路径列表"""
        self.page_paths = page_paths
        self.page_count = len(self.page_paths)

    def update_preview_path(self, preview_path: str):
        """更新漫画预览小图路径"""
        self.preview_path = preview_path

    def update_fingerprint_xxhash(self, xxhash: str):
        """更新文件指纹 xxhash"""
        self.fingerprint_xxhash = xxhash

    def update_fingerprint_filesize(self, filesize: int):
        """更新文件指纹 文件大小"""
        self.fingerprint_filesize = filesize

    def update_fingerprint_inside_paths(self, inside_paths: str):
        """更新文件指纹 内部文件路径"""
        self.fingerprint_inside_paths = inside_paths

    def _calc_fingerprint(self):
        """计算文件指纹"""
        if isinstance(self.filetype, FileType.Folder) or self.filetype == FileType.Folder:
            """2025.09.30 文件指纹计算hash过于影响速度，弃用
            # xxhash，文件夹类为内部所有文件的hash算法整合
            inside_paths = natsort.os_sorted(self.page_paths)
            self.fingerprint_xxhash = lzytools.file.calc_xxhash_from_files(inside_paths)
            """
            # 文件大小
            self.fingerprint_filesize = self.filesize_bytes
            # 内部文件路径
            inside_paths = natsort.os_sorted(self.page_paths)
            inside_paths = [i.replace(self.filepath, '') for i in inside_paths]  # 转换为相对路径
            self.fingerprint_inside_paths = '|'.join(inside_paths)
        elif isinstance(self.filetype, FileType.Archive) or self.filetype == FileType.Archive:
            """2025.09.30 文件指纹计算hash过于影响速度，弃用
            # xxhash，压缩文件类为压缩文件的hash
            self.fingerprint_xxhash = lzytools.file.calc_xxhash_from_file(self.filepath)
            """
            # 文件大小
            self.fingerprint_filesize = self.filesize_bytes
            # 压缩文件内部文件路径
            inside_paths = self.page_paths
            self.fingerprint_inside_paths = '|'.join(inside_paths)

    def _analyse_folder_pages(self):
        """分析文件夹类漫画页"""
        self.page_paths = function_file.get_images_in_folder(self.filepath)
        self.page_count = len(self.page_paths)
        self.preview_path = function_cache.save_preview_image_to_cache(self.page_paths[0])  # 保存预览小图

    def _analyse_archive_pages(self):
        """分析压缩文件类漫画页"""
        self.page_paths = function_archive.get_images_in_archive(self.filepath)
        self.page_count = len(self.page_paths)
        # 保存预览小图
        self.preview_path = function_cache.save_preview_image_in_archive_to_cache(archive=self.filepath,
                                                                                  image_path_inside=self.page_paths[0])

    def _analyse_archive_size_extracted(self):
        """分析压缩文件类漫画大小（解压后的）"""
        self.filesize_bytes_extracted = function_archive.get_archive_real_size(self.filepath)


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
        self.calc_filesize()

    def is_useful(self):
        """检查图片是否有效"""
        # 所属漫画为文件夹类时
        if isinstance(self.comic_filetype_belong, FileType.Folder):
            if os.path.exists(self.image_path):
                filesize_latest = lzytools.file.get_size(self.image_path)
                return filesize_latest == self.filesize
        elif isinstance(self.comic_filetype_belong, FileType.Archive):
            if os.path.exists(self.comic_path_belong):
                filesize_latest = function_archive.get_filesize_inside(self.comic_path_belong, self.image_path)
                return filesize_latest == self.filesize

        return None

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
