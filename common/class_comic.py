# 漫画相关的自定义类
import os

import lzytools.archive
import lzytools.file

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


class ComicInfo:
    """漫画信息类"""

    def __init__(self, comic_path: str):
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
        self.filesize_bytes: int = lzytools.file.get_size(self.filepath)
        # 文件真实大小（文件类型为解压文件时使用，为解压后的文件大小）（字节）
        self.filesize_bytes_extracted: int = self.filesize_bytes
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
        # 文件修改时间（自纪元以来的秒数）
        self.modified_time: float = os.path.getmtime(self.filepath)

        # 漫画信息
        # 内部文件路径
        self.page_paths: tuple = None
        # 页数
        self.page_count: int = None
        # 预览小图本地路径
        self.preview_path: str = None

        # 提取需要的信息
        if isinstance(self.filetype, FileType.Folder):
            self._analyse_folder_pages()
        elif isinstance(self.filetype, FileType.Archive):
            self._analyse_archive_pages()
            self._analyse_archive_size_extracted()

    def get_page_paths(self):
        """获取漫画页路径列表"""
        return self.page_paths

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
        # 备忘录
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
        self.comic_filetype_belong: FileTypes = FileType.File()

    def update_by_comic_info(self, comic_info: ComicInfo):
        """根据漫画信息类更新信息"""
        self.comic_path_belong = comic_info.filepath
        self.comic_filetype_belong = comic_info.filetype

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

    def get_hash(self, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        """获取指定的hash值"""
        if isinstance(hash_type, SimilarAlgorithm.aHash):
            if hash_length == 64:
                return self.aHash_64
            elif hash_length == 144:
                return self.aHash_144
            elif hash_length == 256:
                return self.aHash_256
        elif isinstance(hash_type, SimilarAlgorithm.pHash):
            if hash_length == 64:
                return self.pHash_64
            elif hash_length == 144:
                return self.pHash_144
            elif hash_length == 256:
                return self.pHash_256
        elif isinstance(hash_type, SimilarAlgorithm.dHash):
            if hash_length == 64:
                return self.dHash_64
            elif hash_length == 144:
                return self.dHash_144
            elif hash_length == 256:
                return self.dHash_256

        return ''


FileTypes = (FileType.File, FileType.Folder, FileType.Archive, FileType.Unknown)
