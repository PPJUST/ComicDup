# 相似组list缓存的方法
"""
列表格式说明：
内部元素为集合，集合内元素为相似的漫画路径str
"""
import os
import pickle

from constant import SIMILAR_GROUPS_PICKLE
from module import function_normal


def read_similar_groups_pickle():
    """读取保存的相似组列表"""
    function_normal.print_function_info()
    if os.path.exists(SIMILAR_GROUPS_PICKLE):
        with open(SIMILAR_GROUPS_PICKLE, 'rb') as sp:
            similar_groups = pickle.load(sp)
    else:
        similar_groups = []

    return similar_groups


def save_similar_groups_pickle(similar_groups):
    """将相似组列表直接保存到本地"""
    with open(SIMILAR_GROUPS_PICKLE, 'wb') as sp:
        pickle.dump(similar_groups, sp)
