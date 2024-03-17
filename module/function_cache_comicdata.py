# 漫画数据dict缓存的方法
"""
字典格式说明：
key为漫画路径str，value为自定义的漫画class类
"""
import os
import pickle

from constant import COMICS_DATA_PICKLE, CURRENT_COMICS_DATA_PICKLE
from module import function_normal


def read_comics_data_pickle():
    """读取漫画数据"""
    function_normal.print_function_info()
    if os.path.exists(COMICS_DATA_PICKLE):
        with open(COMICS_DATA_PICKLE, 'rb') as sp:
            comics_data = pickle.load(sp)
    else:
        comics_data = {}

    return comics_data


def read_current_comics_data_pickle():
    """读取当前任务的漫画数据"""
    function_normal.print_function_info()
    if os.path.exists(CURRENT_COMICS_DATA_PICKLE):
        with open(CURRENT_COMICS_DATA_PICKLE, 'rb') as sp:
            comics_data = pickle.load(sp)
    else:
        comics_data = {}

    return comics_data


def save_comics_data_pickle(comics_data: dict):
    """将漫画数据保存到本地"""
    function_normal.print_function_info()

    with open(CURRENT_COMICS_DATA_PICKLE, 'wb') as sp:
        pickle.dump(comics_data, sp)


def update_comics_data_pickle(comics_data: dict):
    """将漫画数据保存到本地（增量更新）"""
    function_normal.print_function_info()
    old_comics_data = read_comics_data_pickle()
    old_comics_data.update(comics_data)

    with open(COMICS_DATA_PICKLE, 'wb') as sp:
        pickle.dump(old_comics_data, sp)


def get_extract_images_from_archive(archive: str):
    """提取指定压缩包已解压的图片路径"""
    function_normal.print_function_info()
    comics_data = read_comics_data_pickle()
    if archive in comics_data:
        comic_class = comics_data[archive]
        extract_images = comic_class.calc_hash_images
        exist_images = [i for i in extract_images if os.path.exists(i)]
        exist_images = sorted(exist_images)
        return exist_images
    else:
        return []
