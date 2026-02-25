# 相似页匹配

from typing import Dict, List

import lzytools_image

from common.class_comic import ComicInfoBase
from common.class_match_page_result import MatchResult


def match_pages(comic_info_1: ComicInfoBase, comic_info_2: ComicInfoBase) -> Dict[int, int]:
    """匹配两本漫画相似的页面
    :return: key为comic_1的页码，value为匹配到的最相似的comic_2的页码"""
    # 计算所有页面的hash值（pHash，144位）
    images_hash_1 = comic_info_1.calc_all_pages_hash()
    images_hash_2 = comic_info_2.calc_all_pages_hash()

    # 由comic_1匹配comic_2，匹配最相似的页码
    page_match_group: Dict[int, int] = dict()  # key为comic_1的页码，value为匹配到的最相似的comic_2的页码
    for index_1, (page_1, hash_1) in enumerate(images_hash_1.items()):
        similar_pages: List[int, int] = []
        for index_2, (page_2, hash_2) in enumerate(images_hash_2.items()):
            hamming_distance = lzytools_image.calc_hash_hamming_distance(hash_1, hash_2)
            if hamming_distance <= 15:  # hash长度为144，相似度阈值为10%
                similar_pages.append((index_2, hamming_distance))
        if similar_pages:
            sorted(similar_pages, key=lambda x: x[1])  # 按汉明距离排序
            similarest_page = similar_pages[0][0]
            page_match_group[index_1] = similarest_page

    return page_match_group


def check_match_result(comic_info_1: ComicInfoBase, comic_info_2: ComicInfoBase, similar_pages: Dict[int, int]):
    """检查相似页匹配结果
    :param similar_pages: key为comic_1的页码，value为匹配到的最相似的comic_2的页码"""
    page_count_1 = comic_info_1.page_count  # 漫画1的页数
    page_count_2 = comic_info_2.page_count  # 漫画2的页数

    is_all_right_match = False  # 全部正确匹配
    is_same_count_but_wrong_page_number = False  # 全部匹配，但是有页面顺序错误
    is_same_count_but_wrong_page = False  # 页数一致，有部分页面错误
    is_comic_1_loss_page = False  # 漫画1有缺页，即漫画2有多余页
    is_comic_2_loss_page = False  # 漫画2有缺页，即漫画1有多余页

    match_pages_1 = list(similar_pages.keys())
    match_pages_2 = list(similar_pages.values())

    _wrong_pages_comic_1 = []
    _wrong_pages_comic_2 = []

    if page_count_1 == page_count_2:
        # 是否符合全部正确匹配或页面顺序错误
        if match_pages_1 == sorted(match_pages_2) and len(set(match_pages_1)) == page_count_1:
            is_all_right_match = True  # 假设为全部正确匹配
            is_same_count_but_wrong_page_number = False
            for index_1, index_2 in similar_pages.items():
                if index_1 != index_2:
                    is_all_right_match = False
                    is_same_count_but_wrong_page_number = True
                    _wrong_pages_comic_1.append(index_1)
                    _wrong_pages_comic_2.append(index_1)

        # 是否符合部分页面错误
        if match_pages_1 == sorted(match_pages_2) and len(set(match_pages_1)) != page_count_1:
            is_same_count_but_wrong_page = True
            for index_1 in range(page_count_1):
                if index_1 not in similar_pages.keys():
                    _wrong_pages_comic_1.append(index_1)
                    _wrong_pages_comic_2.append(index_1)

    elif page_count_1 > page_count_2:
        # 是否符合漫画2有缺页
        if len(match_pages_1) == len(set(match_pages_2)) and match_pages_1 == sorted(
                match_pages_1) and match_pages_2 == sorted(match_pages_2):
            if len(set(match_pages_2)) == page_count_2:
                is_comic_1_loss_page = True
                for index_1 in range(page_count_1):
                    if index_1 not in match_pages_1:
                        _wrong_pages_comic_1.append(index_1)

    elif page_count_1 < page_count_2:
        # 是否符合漫画1有缺页
        if len(match_pages_1) == len(set(match_pages_2)) and match_pages_1 == sorted(
                match_pages_1) and match_pages_2 == sorted(match_pages_2):
            if len(set(match_pages_1)) == page_count_1:
                is_comic_2_loss_page = True
                for index_2 in range(page_count_2):
                    if index_2 not in match_pages_2:
                        _wrong_pages_comic_2.append(index_2)

    # 统计结果
    if is_all_right_match:
        match_result = MatchResult.OneToOne()
    elif is_same_count_but_wrong_page_number:
        match_result = MatchResult.SameCountButWrongPageNumber()
        match_result.wrong_pages_comic_1 = _wrong_pages_comic_1
        match_result.wrong_pages_comic_2 = _wrong_pages_comic_2
    elif is_same_count_but_wrong_page:
        match_result = MatchResult.SameCountButWrongPage()
        match_result.wrong_pages_comic_1 = _wrong_pages_comic_1
        match_result.wrong_pages_comic_2 = _wrong_pages_comic_2
    elif is_comic_1_loss_page:
        match_result = MatchResult.LossPageComic1()
        match_result.wrong_pages_comic_1 = _wrong_pages_comic_1
        match_result.wrong_pages_comic_2 = _wrong_pages_comic_2
    elif is_comic_2_loss_page:
        match_result = MatchResult.LossPageComic2()
        match_result.wrong_pages_comic_1 = _wrong_pages_comic_1
        match_result.wrong_pages_comic_2 = _wrong_pages_comic_2
    else:
        match_result = MatchResult.Unknown()
        _wrong_pages_comic_1.extend([i for i in range(page_count_1)])
        _wrong_pages_comic_2.extend([i for i in range(page_count_2)])
        for index_1, index_2 in similar_pages.items():
            if index_1 == index_2:
                _wrong_pages_comic_1.remove(index_1)
                _wrong_pages_comic_2.remove(index_2)
        match_result.wrong_pages_comic_1 = _wrong_pages_comic_1
        match_result.wrong_pages_comic_2 = _wrong_pages_comic_2

    return match_result
