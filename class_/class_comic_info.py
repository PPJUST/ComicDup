# 漫画信息类及其数据库的相关方法
"""
漫画信息的pickle数据库：存储漫画的基本信息（路径、文件类型、文件大小、内部图片路径list、内部图片数、预览图路径）
读取的数据统一用comic_info_dict变量
"""
import os
import pickle

import module.function_archive
from constant import _COMICS_INFO_DB, _PREVIEW_DIRPATH
from module import function_normal, function_archive


class ComicInfo:
    """漫画信息类"""

    def __init__(self, path):
        self.path = ''  # 路径
        self.filetype = ''  # 文件类型，folder或archive
        self.images = []  # 内部图片路径列表
        self.image_count = 0  # 图片数量
        self.preview_path = ''  # 预览图路径（压缩包需要解压首张图片）
        self.filesize = 0  # 文件大小（字节）
        self.real_filesize = 0  # 真实文件大小（字节）（压缩包解压后的大小）

        self.get_information(path)

    def get_information(self, comic_path: str):
        """设置漫画的路径，并提取信息"""
        # 路径
        self.path = comic_path
        # 文件大小
        self.filesize = function_normal.get_size(comic_path)
        # 文件类型
        if os.path.isdir(comic_path):
            self.filetype = 'folder'
        else:
            self.filetype = 'archive'
        # 内部图片路径列表
        if self.filetype == 'folder':
            self.images = function_normal.get_images_from_folder(self.path)
            self.image_count = len(self.images)
            # 缩放文件夹内的第一张图片作为预览图
            self.preview_path = function_normal.save_image_as_preview(self.images[0])
        else:
            self.images = module.function_archive.get_images_from_archive(self.path)
            self.image_count = len(self.images)
            # 解压压缩包内的第一张图片作为预览图
            self.preview_path = function_archive.save_image_as_preview(self.path, self.images[0])
        # 真实文件大小
        if self.filetype == 'folder':
            self.real_filesize = self.filesize
        else:
            self.real_filesize = function_archive.get_archive_real_size(self.path)

    def is_exist(self):
        """检验漫画是否有效"""
        if os.path.exists(self.path):
            local_filesize = function_normal.get_size(self.path)
            return local_filesize == self.filesize
        else:
            return False

    def fix_preview(self):
        """修复本地不存在的预览图，重新创建预览缩略图"""
        if not os.path.exists(self.preview_path):
            if self.filetype == 'folder':
                preview_fix = function_normal.save_image_as_preview(self.images[0])
            else:
                preview_fix = function_archive.save_image_as_preview(self.path, self.images[0])
            os.rename(preview_fix, self.preview_path)


def read_db() -> dict:
    """读取所有漫画信息
    :return: dict，key为漫画路径，value为comic_info类"""
    if os.path.exists(_COMICS_INFO_DB):
        with open(_COMICS_INFO_DB, 'rb') as sp:
            comic_info_dict = pickle.load(sp)
    else:
        comic_info_dict = {}

    return comic_info_dict


def get_comic_info(comic_path: str) -> ComicInfo:
    """读取单本漫画对应的comic_info类"""
    datas = read_db()
    _comic_info = datas[comic_path]
    return _comic_info


def update_db(comic_info_dict: dict, incremental_update=True):
    """将漫画信息保存到本地（增量更新）
    :param comic_info_dict: dict，key为漫画路径，value为comic_info类
    :param incremental_update: bool，是否增量更新，否则全量更新"""
    if incremental_update:
        final_dict = read_db()
        final_dict.update(comic_info_dict)
    else:
        final_dict = comic_info_dict

    with open(_COMICS_INFO_DB, 'wb') as sp:
        pickle.dump(final_dict, sp)


def clear_db():
    """清空数据库"""
    with open(_COMICS_INFO_DB, 'wb') as sp:
        pickle.dump({}, sp)


def delete_useless_item():
    """删除数据库中无效的数据"""
    comic_info_dict = read_db()
    for comic_path, comic_info in comic_info_dict.copy().items():
        comic_info: ComicInfo
        filesize = comic_info.filesize
        if os.path.exists(comic_path) and function_normal.get_size(comic_path) == filesize:
            continue
        comic_info_dict.pop(comic_path)

    clear_db()
    update_db(comic_info_dict, False)


def delete_useless_preview():
    """删除无效的预览图"""
    previews = []  # 仅包含文件名
    # 提取数据库中的数据
    comic_info_dict = read_db()
    for comic_path, comic_info in comic_info_dict.copy().items():
        comic_info: ComicInfo
        preview = comic_info.preview_path
        filename = os.path.basename(preview)
        previews.append(filename)
    # 提取本地目录
    local_filenames = os.listdir(_PREVIEW_DIRPATH)
    # 删除本地多余的预览图
    for filename in local_filenames:
        if filename not in previews:
            full_path = os.path.join(_PREVIEW_DIRPATH, filename)
            os.remove(full_path)
