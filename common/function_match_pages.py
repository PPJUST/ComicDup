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

    # 检查漫画1和漫画2的页码是否被全部匹配
    is_full_match_comic_1 = False  # 漫画1的页码是否被全部匹配
    if page_count_1 == len(similar_pages):
        is_full_match_comic_1 = True
    is_full_match_comic_2 = False  # 漫画2的页码是否被全部匹配
    _pages_2 = set()
    for i in similar_pages.values():
        _pages_2.add(i)
    if page_count_2 == len(_pages_2):
        is_full_match_comic_2 = True

    match_result = None
    if is_full_match_comic_1 and is_full_match_comic_2:
        # 检查两本漫画的页数
        if page_count_1 == page_count_2:
            # 最优情况，一一对应
            is_right_match = True
            for index_1, index_2 in similar_pages.items():
                if index_1 != index_2:
                    is_right_match = False
                    break
            if is_right_match:
                match_result = MatchResult.OneToOne()
                return match_result

            # 页数一致，一一对应，但是有页码错误（全部被匹配，但是有页面顺序错误）
            is_same_count_but_wrong_page_number = False
            # 页数一致，但是有不同的页（没有全部匹配）
            is_same_count_but_wrong_page = False
            _right_pages = dict()
            _right_page_comic_1 = []
            _right_page_comic_2 = []
            _wrong_pages = dict()
            _wrong_page_comic_1 = []
            _wrong_page_comic_2 = []
            # 找出匹配页和不匹配页
            for index_1, index_2 in similar_pages.items():
                if index_1 == index_2:
                    _right_pages[index_1] = index_2
                    _right_page_comic_1.append(index_1)
                    _right_page_comic_2.append(index_2)
                else:
                    _wrong_pages[index_1] = index_2
                    _wrong_page_comic_1.append(index_1)
                    _wrong_page_comic_2.append(index_2)
            # 从漫画2中的不匹配页列表中剔除已经被匹配到的页面
            _wrong_page_comic_2 = [i for i in _wrong_page_comic_2 if i not in _right_page_comic_2]
            if sorted(_right_page_comic_1) == sorted(_right_page_comic_2):
                is_same_count_but_wrong_page_number = True
            else:
                is_same_count_but_wrong_page = True

            if is_same_count_but_wrong_page_number:
                match_result = MatchResult.SameCountButWrongPageNumber()
                match_result.wrong_pages_comic_1 = _wrong_page_comic_1
                match_result.wrong_pages_comic_2 = _wrong_page_comic_2
                return match_result
            if is_same_count_but_wrong_page:
                match_result = MatchResult.SameCountButWrongPage()
                match_result.wrong_pages_comic_1 = _wrong_page_comic_1
                match_result.wrong_pages_comic_2 = _wrong_page_comic_2
                return match_result
    else:
        # 漫画1有缺页，即漫画2有多余页（漫画1全部被顺序匹配，但漫画2没有被全部顺序匹配）
        if is_full_match_comic_1 and not is_full_match_comic_2:
            is_comic_1_loss_page = True
            extra_page_comic_2 = [i for i in range(page_count_2) if i not in similar_pages.values()]
            match_result = MatchResult.LossPageComic1()
            match_result.wrong_pages_comic_2 = extra_page_comic_2
            return match_result

        # 漫画2有缺页，即漫画1有多余页（漫画2全部被顺序匹配，但漫画1没有全部被顺序匹配）
        if not is_full_match_comic_1 and is_full_match_comic_2:
            is_comic_2_loss_page = True
            extra_page_comic_1 = [i for i in range(page_count_1) if i not in similar_pages.keys()]
            match_result = MatchResult.LossPageComic2()
            match_result.wrong_pages_comic_1 = extra_page_comic_1
            return match_result
