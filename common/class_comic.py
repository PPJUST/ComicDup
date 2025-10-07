# 漫画相关的自定义类
import os

import lzytools.archive
import lzytools.file
import lzytools.image
import natsort

from common import function_file, function_archive, function_cache
from common.class_config import FileType, FileTypes


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

        # 文件指纹（格式为文件大小bytes+内部文件路径，以|间隔）
        self.fingerprint: str = None

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

    def save_preview_image(self):
        """保存预览小图到缓存目录（手动调用）"""
        if isinstance(self.filetype, FileType.Folder):
            self.preview_path = function_cache.save_preview_image_to_cache(self.page_paths[0])
        elif isinstance(self.filetype, FileType.Archive):
            self.preview_path = function_cache.save_preview_image_in_archive_to_cache(archive=self.filepath,
                                                                                      image_path_inside=self.page_paths[
                                                                                          0])

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

    def update_fingerprint(self, fingerprint: str):
        """更新文件指纹"""
        self.fingerprint = fingerprint

    def _calc_fingerprint(self):
        """计算文件指纹"""
        if isinstance(self.filetype, FileType.Folder) or self.filetype == FileType.Folder:
            # 文件大小
            filesize = self.filesize_bytes
            # 内部文件路径
            inside_paths_abs = natsort.os_sorted(self.page_paths)
            inside_paths_rel = [i.replace(self.filepath, '') for i in inside_paths_abs]  # 转换为相对路径
            inside_path_str = '|'.join(inside_paths_rel)
            # 整合为一个指纹
            self.fingerprint = f'{filesize}|{inside_path_str}'
        elif isinstance(self.filetype, FileType.Archive) or self.filetype == FileType.Archive:
            # 文件大小
            filesize = self.filesize_bytes
            # 压缩文件内部文件路径
            inside_paths = self.page_paths
            inside_path_str = '|'.join(inside_paths)
            # 整合为一个指纹
            self.fingerprint = f'{filesize}|{inside_path_str}'

    def _analyse_folder_pages(self):
        """分析文件夹类漫画页"""
        self.page_paths = function_file.get_images_in_folder(self.filepath)
        self.page_count = len(self.page_paths)

    def _analyse_archive_pages(self):
        """分析压缩文件类漫画页"""
        self.page_paths = function_archive.get_images_in_archive(self.filepath)
        self.page_count = len(self.page_paths)

    def _analyse_archive_size_extracted(self):
        """分析压缩文件类漫画大小（解压后的）"""
        self.filesize_bytes_extracted = function_archive.get_archive_real_size(self.filepath)


