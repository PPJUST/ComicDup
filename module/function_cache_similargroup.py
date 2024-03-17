# 相似组list缓存的方法
"""
列表格式说明：
内部元素为集合，集合内元素为相似的漫画路径str
"""
import os
import pickle

from constant import SIMILAR_GROUPS_PICKLE
from module import function_normal, function_cache_comicdata


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


def read_similar_groups_pickle_filter(filter_type='same_page_size'):
    """读取过滤后的相似组列表"""
    # 暂时不做其他筛选，只有相同页数大小的筛选器
    filter_groups = filter_same_page_and_size()

    return filter_groups


def filter_same_page_and_size():
    """过滤相似组中大小、页数相同的项"""
    similar_groups = read_similar_groups_pickle()
    comics_data = function_cache_comicdata.read_comics_data_pickle()
    filter_groups = []
    for group in similar_groups:
        exist_paths = [i for i in group if os.path.exists(i)]
        if len(exist_paths) >= 2:
            filter_group = []
            # 将每一项的页数和大小组合为一串str，统计组中是否存在重复的str项，有则保存，无则剔除
            temp_str_path_dict = {}
            for comic_path in exist_paths:
                comic_data = comics_data[comic_path]
                page = comic_data.image_count
                size = comic_data.filesize
                str_page_size = f'{page} - {size}'
                if str_page_size not in temp_str_path_dict:
                    temp_str_path_dict[str_page_size] = []
                temp_str_path_dict[str_page_size].append(comic_path)
            for _, paths in temp_str_path_dict.items():
                if len(paths) >= 2:
                    filter_group += paths

            if filter_group:
                filter_groups.append(filter_group)

    return filter_groups


def filter_large_diff_page():
    """过滤相似组中页数差异较大的项"""
    pass
