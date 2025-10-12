# 缓存方法
"""
预览图缓存存储方法：
存储在缓存文件夹下的preview文件夹中的子文件夹中，
每个子文件夹设置最多缓存图片数量，
超过上限后存储到下一个子文件夹中，以此类推
"""
import os

import lzytools.common
import lzytools.file

from common import function_file, function_archive

CACHE_PREVIEW_DIRPATH = 'cache/preview'
CACHE_PREVIEW_MAX_COUNT = 100  # 单个文件夹内最多缓存的预览图数量


def check_cache_exist(cache_dirpath):
    """检查缓存文件夹是否存在"""
    if not os.path.exists(cache_dirpath):
        os.makedirs(cache_dirpath)


def save_preview_image_to_cache(origin_image_path: str, cache_dirpath: str = CACHE_PREVIEW_DIRPATH,
                                height_zoom_out: int = 128):
    """保存指定图片的预览小图
    :param origin_image_path: 原图
    :param cache_dirpath: 缓存文件夹路径
    :param height_zoom_out: 缩放的图片高度"""
    # 检查缓存文件夹是否存在
    check_cache_exist(cache_dirpath)
    # 生成随机文件名
    filetitle_random = lzytools.common.create_random_string(16, uppercase=False)
    filename = f'{filetitle_random}.jpg'
    # 选择缓存的文件夹，选择未超过存储上限的文件夹
    dir_choose = ''
    cache_child_dirs = [os.path.normpath(os.path.join(cache_dirpath, i)) for i in os.listdir(cache_dirpath)]
    if cache_child_dirs:
        for _dir in cache_child_dirs:
            if len(os.listdir(_dir)) < CACHE_PREVIEW_MAX_COUNT:
                dir_choose = _dir
                break
    if not dir_choose:  # 如果文件夹不存在，则新建
        dirtitle_choose = lzytools.common.create_random_string(16, uppercase=False)
        dir_choose = os.path.normpath(os.path.join(cache_dirpath, dirtitle_choose))
        os.mkdir(dir_choose)
    # 生成最终路径并保存
    preview_image_path = os.path.normpath(os.path.join(dir_choose, filename))
    save_path = function_file.save_preview_image(origin_image_path, preview_image_path, height_zoom_out)
    return save_path


def save_preview_image_in_archive_to_cache(archive: str, image_path_inside: str,
                                           cache_dirpath: str = CACHE_PREVIEW_DIRPATH,
                                           height_zoom_out: int = 128) -> str:
    """保存解压文件中指定图片的预览小图
    :param archive: 压缩文件路径
    :param image_path_inside: 需要保存的压缩包内图片的内部路径
    :param cache_dirpath: 缓存文件夹路径
    :param height_zoom_out: 缩放的图片高度"""
    # 检查缓存文件夹是否存在
    check_cache_exist(cache_dirpath)
    # 生成随机文件名
    filetitle_random = lzytools.common.create_random_string(16, uppercase=False)
    filename = f'{filetitle_random}.jpg'
    # 选择缓存的文件夹，选择未超过存储上限的文件夹
    dir_choose = ''
    cache_child_dirs = [os.path.normpath(os.path.join(cache_dirpath, i)) for i in os.listdir(cache_dirpath)]
    for _dir in cache_child_dirs:
        if len(os.listdir(_dir)) < CACHE_PREVIEW_MAX_COUNT:
            dir_choose = _dir
            break
    if not dir_choose:  # 如果文件夹不存在，则新建
        dirtitle_choose = lzytools.common.create_random_string(16, uppercase=False)
        dir_choose = os.path.normpath(os.path.join(cache_dirpath, dirtitle_choose))
        os.mkdir(dir_choose)
    # 生成最终路径并保存
    preview_image_path = os.path.normpath(os.path.join(dir_choose, filename))
    save_path = function_archive.save_preview_image(archive, image_path_inside, preview_image_path, height_zoom_out)
    return save_path


def get_preview_image_count(cache_dirpath: str = CACHE_PREVIEW_DIRPATH) -> int:
    """统计缓存的预览图数量"""
    count = 0
    cache_child_dirs = [os.path.normpath(os.path.join(cache_dirpath, i)) for i in os.listdir(cache_dirpath)]
    for _dir in cache_child_dirs:
        count += len(os.listdir(_dir))
    return count


def get_preview_size(cache_dirpath: str = CACHE_PREVIEW_DIRPATH) -> int:
    """统计缓存预览图文件夹的文件大小"""
    filesize = lzytools.file.get_size(cache_dirpath)
    return filesize
