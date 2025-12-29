# 相似页匹配

"""
1.传入两个comicinfo类
2.计算comicinfo类中所有图片的hash
3.已页数多的comicinfo类为基础，逐个读取其页码图片hash，与另一个comicinfo类的所有页码进行匹配，如果识别为相似图片，则写入字典变量
4.完成全部读取后，整理字典列表，返回一个能表示两个info类页码相似对应关系的字典
"""
from typing import Dict, List

import lzytools_image

from common.class_comic import ComicInfoBase


def match_pages(comic_info_1: ComicInfoBase, comic_info_2: ComicInfoBase):
    """匹配两本漫画相似的页码"""
    # 计算ComicInfo类中所有图片的hash值
    # 计算第一个ComicInfo
    images_hash_1 = comic_info_1.calc_hashs()
    # 计算第二个ComicInfo
    images_hash_2 = comic_info_2.calc_hashs()

    # 对比两个hash字典，找出相似的页码
    similar_pages: Dict[str, List[str]] = dict()
    for page_1, hash_1 in images_hash_1.items():
        for page_2, hash_2 in images_hash_2.items():
            hamming_distance = lzytools_image.calc_hash_hamming_distance(hash_1, hash_2)
            if hamming_distance <= 12 * 12 * 0.1:  # hash长度为12*12
                if page_1 not in similar_pages:
                    similar_pages[page_1] = []
                similar_pages[page_1].append(page_2)
