# 漫画相关的自定义类
import os

import lzytools.file

from common import function_file, function_archive


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
        # 备忘录 提取预览图

    def _analyse_folder_pages(self):
        """分析文件夹类漫画页"""
        self.page_paths = function_file.get_images_in_folder(self.filepath)
        self.page_count = len(self.page_paths)
        # 备忘录 提取预览图

    def _analyse_archive_pages(self):
        """分析压缩文件类漫画页"""
        self.page_paths = function_archive.get_images_in_archive(self.filepath)
        print(self.page_paths)
        self.page_count = len(self.page_paths)
        # 备忘录 提取预览图

    def _analyse_archive_size_extracted(self):
        """分析压缩文件类漫画大小（解压后的）"""
        self.filesize_bytes_extracted = function_archive.get_archive_real_size(self.filepath)
