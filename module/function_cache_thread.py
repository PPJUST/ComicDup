# 子线程运行时的数据缓存
import os
import pickle

from constant import COMIC_FOLDERS, ARCHIVES, IMAGE_DATA_DICT
from module import function_normal


def read_comic_folders():
    """读取漫画文件夹set"""
    function_normal.print_function_info()
    if os.path.exists(COMIC_FOLDERS):
        with open(COMIC_FOLDERS, 'rb') as sp:
            data = pickle.load(sp)
    else:
        data = set()

    return data


def save_comic_folders(comic_folders: set):
    """将漫画文件夹set直接保存到本地"""
    with open(COMIC_FOLDERS, 'wb') as sp:
        pickle.dump(comic_folders, sp)


def read_archives():
    """读取压缩包set"""
    function_normal.print_function_info()
    if os.path.exists(ARCHIVES):
        with open(ARCHIVES, 'rb') as sp:
            data = pickle.load(sp)
    else:
        data = set()

    return data


def save_archives(archives: set):
    """将压缩包set直接保存到本地"""
    with open(ARCHIVES, 'wb') as sp:
        pickle.dump(archives, sp)

def read_current_image_data_dict():
    """读取当前任务的图片数据字典"""
    function_normal.print_function_info()
    if os.path.exists(IMAGE_DATA_DICT):
        with open(IMAGE_DATA_DICT, 'rb') as sp:
            data = pickle.load(sp)
    else:
        data = dict()

    return data


def save_current_image_data_dict(current_image_data_dict: dict):
    """将读取当前任务的图片数据字典保存到本地"""
    with open(IMAGE_DATA_DICT, 'wb') as sp:
        pickle.dump(current_image_data_dict, sp)