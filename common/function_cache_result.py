import os
import pickle
from typing import List

import lzytools.common

from common.class_comic import ComicInfoBase

CACHE_MATCH_RESULT_FOLDER = 'cache/'
CACHE_MATCH_RESULT_FILE_EXTENSION = '.pkl'


def check_cache_exist(cache_dirpath: str = CACHE_MATCH_RESULT_FOLDER):
    """检查缓存文件夹是否存在"""
    if not os.path.exists(cache_dirpath):
        os.makedirs(cache_dirpath)


def save_match_result(data: List[List[ComicInfoBase]]):
    """保存匹配结果"""
    check_cache_exist(CACHE_MATCH_RESULT_FOLDER)
    # 提取时间戳
    time_str = lzytools.common.get_current_time(_format='match result %Y%m%d %H_%M_%S')
    # 组合文件名
    filename = f'{time_str}{CACHE_MATCH_RESULT_FILE_EXTENSION}'
    # 组合缓存路径
    cache_filepath = os.path.normpath(os.path.join(CACHE_MATCH_RESULT_FOLDER, filename))
    # 存储匹配结果
    with open(cache_filepath, 'wb') as file:
        pickle.dump(data, file)


def read_match_result(filename) -> List[List[ComicInfoBase]]:
    """读取匹配结果"""
    # 组合缓存路径
    cache_filepath = os.path.normpath(os.path.join(CACHE_MATCH_RESULT_FOLDER, filename))
    # 读取匹配结果
    with open(cache_filepath, 'rb') as file:
        data = pickle.load(file)
        return data
