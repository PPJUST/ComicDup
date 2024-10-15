# 保存相似匹配结果

import os
import pickle

import natsort

from class_ import class_comic_info
from constant import _MATCH_RESULT
from module import function_normal


def save_result(similar_comic_group: list):
    """保存匹配结果到本地
    :param similar_comic_group:list，相似漫画组，内部元素为集合，集合内部元素为漫画路径"""
    function_normal.print_function_info()
    similar_sorted = []
    # 排序内部组的内部元素
    for comics in similar_comic_group:
        comics: set  # 集合内部元素为漫画路径
        comics_sorted = natsort.natsorted(set(comics))
        similar_sorted.append(comics_sorted)
    # 排序内部组
    similar_sorted = natsort.natsorted(similar_sorted)  # # 相似漫画组，内部元素为列表，列表内部元素为漫画路径

    with open(_MATCH_RESULT, 'wb') as sp:
        pickle.dump(similar_sorted, sp)


def read_result():
    """读取本地的匹配结果（经过校验后的）
    :return: list，相似漫画组，内部元素为列表，列表内部元素为漫画路径"""
    function_normal.print_function_info()
    if os.path.exists(_MATCH_RESULT):
        with open(_MATCH_RESULT, 'rb') as sp:
            similar_comic_group: list = pickle.load(sp)  # 相似漫画组，内部元素为列表，列表内部元素为漫画路径
    else:
        similar_comic_group = []

    # 校验
    comic_info_dict = class_comic_info.read_db()
    for comics in similar_comic_group:
        comics: list
        for comic in comics.copy():
            if comic not in comic_info_dict or not os.path.exists(comic):
                comics.remove(comic)

    # 如果内部元素计数<2，则删除该项
    similar_comic_group = [i for i in similar_comic_group if len(i) >= 2]

    return similar_comic_group


def delete_item(comic_path: str):
    """删除指定漫画项"""
    function_normal.print_function_info()
    similar_comic_group = read_result()  # 相似漫画组，内部元素为列表，列表内部元素为漫画路径
    for comics in similar_comic_group:
        comics: list
        if comic_path in comics:
            comics.remove(comic_path)
            break

    # 如果内部元素计数<2，则删除该项
    similar_comic_group = [i for i in similar_comic_group if len(i) >= 2]

    with open(_MATCH_RESULT, 'wb') as sp:
        pickle.dump(similar_comic_group, sp)
