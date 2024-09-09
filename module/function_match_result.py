# 保存相似匹配结果

import os
import pickle

from constant import _MATCH_RESULT


def save_result(similar_comic_group):
    """保存匹配结果到本地
    :param similar_comic_group:list，相似漫画组，内部元素为元组，元组内部元素为漫画路径"""
    with open(_MATCH_RESULT, 'wb') as sp:
        pickle.dump(similar_comic_group, sp)


def read_result():
    """读取本地的匹配结果
    :return: list，相似漫画组，内部元素为元组，元组内部元素为漫画路径"""
    if os.path.exists(_MATCH_RESULT):
        with open(_MATCH_RESULT, 'rb') as sp:
            result = pickle.load(sp)
    else:
        result = []

    return result
