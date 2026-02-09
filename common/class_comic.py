# 漫画相关的自定义类
import os
from abc import ABC, abstractmethod
from typing import Union, Dict

import lzytools
import lzytools_archive
import natsort

from common import function_file, function_archive, function_cache_preview, function_image
from common.class_config import FileType, SimilarAlgorithm

_BASE_COLOR = ['black', 'maroon', 'red', 'purple', 'fuchsia',
               'green', 'lime', 'olive', 'yellow', 'navy',
               'blue', 'teal', 'aqua']


class ComicInfoBase(ABC):
    """漫画信息基类"""

    def __init__(self, comic_path: str, db_model: bool = False):
        """
        :param comic_path: 漫画路径
        :param db_model: 数据库模式，不主动提取信息，而从数据库中加载"""

        # 基础文件信息
        # 文件路径
        self.filepath: str = os.path.normpath(comic_path)
        # 文件类型
        self.filetype: Union[FileType.Folder, FileType.Archive] = None
        # 文件名（含扩展名）
        self.filename: str = os.path.basename(self.filepath)
        # 文件标题（不含扩展名）
        self.filetitle: str = None
        # 文件父级路径
        self.parent_dirpath: str = os.path.dirname(self.filepath)
        # 文件大小（字节）
        self.filesize_bytes: int = None
        # 文件修改时间（自纪元以来的秒数）
        self.modified_time: float = None

        # 漫画信息
        # 内部图片页路径
        self.page_paths: tuple = None
        # 页数
        self.page_count: int = None
        # 预览小图本地路径
        self.preview_path: str = None

        # 文件指纹（格式为文件大小bytes+内部文件路径，以|间隔）
        self.fingerprint: str = None

        # 数据库中对应的图片hash值，用于计算整体相似度
        self.image_hashs: set = set()

        # 非数据库模式时，自动提取信息
        if not db_model:
            self._analyse_info()
            # 计算文件指纹
            self._calc_fingerprint()

    def set_image_hashs(self, hashs: set):
        """设置对应的图片hash值"""
        self.image_hashs = hashs

    def add_image_hash(self, _hash: str):
        """添加对应的图片hash值"""
        self.image_hashs.add(_hash)

    def get_image_hashs(self):
        """获取对应的图片hash值"""
        return self.image_hashs

    def get_page_paths(self):
        """获取漫画页路径列表"""
        return self.page_paths

    def get_real_filesize(self):
        """获取真实文件大小（字节）"""
        if isinstance(self, FolderComicInfo):  # 如果是文件夹类漫画，则返回文件大小
            return self.filesize_bytes
        elif isinstance(self, ArchiveComicInfo):  # 如果是压缩文件类漫画，则返回解压后的文件大小
            return self.get_extracted_filesize_bytes()
        else:
            return 0

    @abstractmethod
    def get_extracted_filesize_bytes(self):
        """获取解压后的文件大小（字节）"""

    @abstractmethod
    def save_preview_image(self):
        """保存预览小图到缓存目录（手动调用，防止自动分析漫画信息时重复创建预览图）"""

    def fix_preview_path(self):
        """修复预览图（会更新预览图变量）"""
        # 获取无效的预览图路径
        useless_preview_path = self.preview_path
        print('修复无效预览图', '预览图原路径', useless_preview_path)
        # 生成新的预览图
        self.save_preview_image()
        # 将新生成的预览图改名为原预览图文件名
        dirpath = os.path.dirname(useless_preview_path)
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)  # 原预览图文件夹不存在时，需要创建，否则改名时会报错
        os.rename(self.preview_path, useless_preview_path)
        # 重新赋值
        self.preview_path = useless_preview_path

    def calc_point(self) -> float:
        """计算漫画评分（10分制）"""
        return calc_comic_point(self)

    @abstractmethod
    def calc_hashs(self):
        """计算漫画内所有图片的hash值"""

    """数据库模式使用的手动更新信息的方法"""

    def update_filesize(self, filesize_bytes: int):
        """更新文件大小（字节）"""
        self.filesize_bytes = filesize_bytes

    def update_filetitle(self, filetitle: str):
        """更新文件标题"""
        self.filetitle = filetitle

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

    """自动分析信息的方法"""

    @abstractmethod
    def _analyse_info(self):
        """分析漫画信息"""
        # 文件大小
        self.filesize_bytes = lzytools.file.get_size(self.filepath)
        # 文件修改时间
        self.modified_time = os.path.getmtime(self.filepath)
        # 文件标题
        self._update_filetitle()

    @abstractmethod
    def _calc_fingerprint(self):
        """计算文件指纹
        文件指纹的格式为：文件大小bytes+内部文件路径，以|间隔"""

    @abstractmethod
    def _update_filetitle(self):
        """更新文件标题"""


class FolderComicInfo(ComicInfoBase):
    """文件夹类漫画信息类"""

    def __init__(self, comic_path: str, db_model: bool = False):
        super().__init__(comic_path, db_model)
        self.filetype = FileType.Folder()

    def save_preview_image(self):
        super().save_preview_image()
        first_image = self.page_paths[0]
        self.preview_path = function_cache_preview.save_preview_image_to_cache(first_image)

    def get_extracted_filesize_bytes(self):
        """获取解压后的文件大小（字节）"""
        return 0

    def calc_hashs(self, hash_type=SimilarAlgorithm.pHash, hash_length: int = 12) -> Dict[str, str]:
        hash_dict = dict()
        for image in self.page_paths:
            image_path = os.path.normpath(os.path.join(self.filepath, image))
            hash_ = function_image.calc_image_hash(image_path, hash_type, hash_length)
            hash_dict[image] = hash_
        return hash_dict

    def _analyse_info(self):
        super()._analyse_info()
        self.page_paths = function_file.get_images_in_folder(self.filepath)
        self.page_count = len(self.page_paths)

    def _calc_fingerprint(self):
        super()._calc_fingerprint()
        # 文件大小
        filesize = self.filesize_bytes
        # 内部文件路径
        inside_paths_abs = natsort.os_sorted(self.page_paths)
        inside_paths_rel = [i.replace(self.filepath, '') for i in inside_paths_abs]  # 转换为相对路径
        inside_path_str = '|'.join(inside_paths_rel)
        # 整合为一个指纹
        self.fingerprint = f'{filesize}|{inside_path_str}'

    def _update_filetitle(self):
        super()._update_filetitle()
        self.filetitle = self.filename


class ArchiveComicInfo(ComicInfoBase):
    """压缩文件类漫画信息类"""

    def __init__(self, comic_path: str, db_model: bool = False):
        super().__init__(comic_path, db_model)
        self.filetype = FileType.Archive()

        # 压缩文件类漫画的额外参数 解压后的文件大小（字节）
        self.extracted_filesize_bytes: int = 0

        # 计算解压后的文件大小（字节）
        self._analyse_archive_size_extracted()

    def save_preview_image(self):
        super().save_preview_image()
        first_image = self.page_paths[0]
        self.preview_path = function_cache_preview.save_preview_image_in_archive_to_cache(archive=self.filepath,
                                                                                          image_path_inside=first_image)

    def update_extracted_filesize_bytes(self, filesize_bytes: int):
        """更新解压后的文件大小（字节）"""
        self.extracted_filesize_bytes = filesize_bytes

    def get_extracted_filesize_bytes(self):
        """获取解压后的文件大小（字节）"""
        return self.extracted_filesize_bytes

    def calc_hashs(self, hash_type=SimilarAlgorithm.pHash, hash_length: int = 12) -> Dict[str, str]:
        hash_dict = dict()
        for image in self.page_paths:
            hash_ = function_image.calc_archive_image_hash(self.filepath, image, hash_type, hash_length)
            hash_dict[image] = hash_
        return hash_dict

    def _analyse_archive_size_extracted(self):
        """分析压缩文件类漫画解压后的文件大小"""
        self.extracted_filesize_bytes = function_archive.get_archive_real_size(self.filepath)

    def _analyse_info(self):
        super()._analyse_info()
        self.page_paths = function_archive.get_images_in_archive(self.filepath)
        self.page_count = len(self.page_paths)

    def _calc_fingerprint(self):
        super()._calc_fingerprint()
        # 文件大小
        filesize = self.filesize_bytes
        # 压缩文件内部文件路径
        inside_paths = self.page_paths
        inside_path_str = '|'.join(inside_paths)
        # 整合为一个指纹
        self.fingerprint = f'{filesize}|{inside_path_str}'

    def _update_filetitle(self):
        super()._update_filetitle()
        self.filetitle = lzytools_archive.get_filetitle(self.filename)


def calc_comic_point(comic_info: ComicInfoBase) -> float:
    """对漫画进行评分（10分制）"""
    # 图片质量：10分制，占比70%，文件总大小/页数，每0.4MB/图加1分
    # 页数：10分制，占比20%，每20页加1分
    # 文件名规范：10分制，占比10%，每个符合规范的tag加1分

    # 计算图片质量分
    per_pic = 0.7  # 占比70%
    base_size = 0.4  # 每0.4mb加分
    page_count = comic_info.page_count
    total_filesize_bytes = comic_info.get_real_filesize()
    total_filesize_mb = total_filesize_bytes / 1024 / 1024
    point_pic = min(total_filesize_mb / page_count / base_size, 10)

    # 计算页数分
    per_count = 0.2  # 占比20%
    base_count = 10  # 每10页加1分
    point_count = min(page_count / base_count, 10)

    # 计算文件名规范分
    # todo 临时按文件名长度评分
    per_tag = 0.1  # 占比10%
    base_tag = 5
    filetitle = comic_info.filetitle
    point_tag = min(len(filetitle) / base_tag, 10)

    # 计算总分
    point_total = round(point_pic * per_pic + point_count * per_count + point_tag * per_tag, 2)

    return point_total
