# 一般的通用方法
import inspect
import os
import random
import shutil
import string
import time

import natsort
import send2trash

from module import function_archive


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


def _get_folder_size(dirpath: str) -> int:
    """获取指定文件夹的总大小/byte"""
    folder_size = 0
    for dirpath_, dirnames, filenames in os.walk(dirpath):
        for item in filenames:
            filepath = os.path.join(dirpath_, item)
            folder_size += os.path.getsize(filepath)

    return folder_size


def get_size(path: str) -> int:
    """获取文件/文件夹的总大小/byte"""
    if os.path.isdir(path):
        return _get_folder_size(path)
    elif os.path.isfile(path):
        return os.path.getsize(path)
    else:
        return 0


def guess_filetype(filepath: str):
    """判断文件类型类型"""
    # 为了速度，直接使用后缀名判断
    image_suffix = ['.jpg', '.png', '.webp', '.jpeg']
    archive_suffix = ['.zip', '.rar']

    suffix = os.path.splitext(filepath)[1].lower()
    if suffix in image_suffix:
        return 'image'
    elif suffix in archive_suffix:
        return 'archive'


def filter_child_folder(folder_list: list) -> list:
    """过滤文件夹列表中的所有子文件夹，返回剔除子文件夹后的list"""
    child_folder = set()
    for folder in folder_list:
        # 相互比对，检查是否为当前文件夹的下级
        for other_folder in folder_list:
            # 统一路径分隔符（os.path.normpath无法实现）
            other_folder_replace = os.path.normpath(other_folder).replace('/', '\\')
            folder_replace = os.path.normpath(folder).replace('/', '\\')
            compare_path = os.path.normpath(folder + os.sep).replace('/', '\\')
            if other_folder_replace.startswith(str(compare_path)) and other_folder_replace != folder_replace:
                child_folder.add(other_folder)

    for i in child_folder:
        if i in folder_list:
            folder_list.remove(i)

    return folder_list


def get_images_in_folder(dirpath: str) -> list:
    """获取文件夹内所有图片的路径list（仅检查内部一级）"""
    listdir = [os.path.normpath(os.path.join(dirpath, i)) for i in os.listdir(dirpath)]
    images = [i for i in listdir if guess_filetype(i) == 'image']
    return images


def create_random_string(length: int = 16) -> str:
    """生成一个指定长度的随机字符串（小写英文+数字）"""
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choices(characters, k=length))

    return random_string


def get_images_from_folder(dirpath: str) -> list:
    """提取文件夹内的所有图片路径"""
    images = get_images_in_folder(dirpath)
    images = natsort.natsorted(images)
    return images


def get_images_from_archive(archive: str) -> list:
    """提取压缩包内的所有图片路径"""
    images = function_archive.get_images(archive)
    images = natsort.natsorted(images)
    return images


def merge_intersecting_sets(sets_list: list) -> list:
    """合并list中的有交集的集合 [(1,2),(2,3)]->[(1,2,3)]"""
    list_merged = []

    for i in range(len(sets_list)):
        set_merged = False

        for j in range(len(list_merged)):
            if set(sets_list[i]) & set(list_merged[j]):
                list_merged[j] = set(set(sets_list[i]) | set(list_merged[j]))
                set_merged = True
                break

        if not set_merged:
            list_merged.append(sets_list[i])

    return list_merged


def convert_time(runtime: float):
    """将一个时间差转换为时分秒的str"""
    hours = int(runtime // 3600)
    minutes = int((runtime % 3600) // 60)
    seconds = int(runtime % 60)
    time_str = f'{hours}:{minutes:02d}:{seconds:02d}'

    return time_str


def delete(path: str, send_to_trash: bool = False):
    """删除路径对应的文件/文件夹"""
    if os.path.exists(path):
        if send_to_trash:
            send2trash.send2trash(path)
        else:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
