# 一般方法
import inspect
import os
import random
import shutil
import string
import time

from constant import TEMP_IMAGE_FOLDER


def print_function_info(mode: str = 'current'):
    """打印当前/上一个执行的函数信息
    传参：mode 'current' 或 'last'"""
    # pass

    if mode == 'current':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back).function)
    elif mode == 'last':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back.f_back).function)


def clear_temp_image_folder():
    """清空临时图片文件夹"""
    print_function_info()
    if os.path.exists(TEMP_IMAGE_FOLDER):
        for dirpath, dirnames, filenames in os.walk(TEMP_IMAGE_FOLDER):
            for j in filenames:
                filepath_join = os.path.normpath(os.path.join(dirpath, j))
                os.remove(filepath_join)

        shutil.rmtree(TEMP_IMAGE_FOLDER)

    os.mkdir(TEMP_IMAGE_FOLDER)


def create_random_string(length: int):
    """生成一个指定长度的随机字符串（小写英文+数字）"""
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choices(characters, k=length))

    return random_string


def merge_intersecting_sets(sets_list: list) -> list:
    """合并list中的有交集的集合 [(1,2),(2,3)]->[(1,2,3)]"""
    merged_list = []

    for i in range(len(sets_list)):
        set_merged = False

        for j in range(len(merged_list)):
            if set(sets_list[i]) & set(merged_list[j]):
                merged_list[j] = set(set(sets_list[i]) | set(merged_list[j]))
                set_merged = True
                break

        if not set_merged:
            merged_list.append(sets_list[i])

    return merged_list


def _get_folder_size(folder: str) -> int:
    """获取指定文件夹的总大小/byte"""
    folder_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for item in filenames:
            filepath = os.path.join(dirpath, item)
            folder_size += os.path.getsize(filepath)

    return folder_size


def get_size(path: str):
    """获取文件/文件夹的总大小/byte"""
    if os.path.isdir(path):
        return _get_folder_size(path)
    elif os.path.isfile(path):
        return os.path.getsize(path)


def check_filetype(file: str):
    """获取一个文件的文件类型"""
    # 为了速度，直接使用后缀名判断
    image_suffix = ['.jpg', '.png', '.webp', '.jpeg']
    archive_suffix = ['.zip', '.rar']

    suffix = os.path.splitext(file)[1].lower()
    if suffix in image_suffix:
        return 'image'
    elif suffix in archive_suffix:
        return 'archive'


def reverse_path(path: str):
    """反转路径，从后到前排列目录层级"""
    path = os.path.normpath(path)
    split_path = path.split('\\')
    path_reversed = '\\'.join(split_path[::-1])
    path_reversed = os.path.normpath(path_reversed)
    return path_reversed
