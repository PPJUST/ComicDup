# 相似页匹配

"""
1.传入两个comicinfo类
2.计算comicinfo类中所有图片的hash
3.已页数多的comicinfo类为基础，逐个读取其页码图片hash，与另一个comicinfo类的所有页码进行匹配，如果识别为相似图片，则写入字典变量
4.完成全部读取后，整理字典列表，返回一个能表示两个info类页码相似对应关系的字典
"""
from common.class_comic import ComicInfoBase


def match_pages(comic_info_1: ComicInfoBase, comic_info_2: ComicInfoBase):
    """匹配两本漫画相似的页码"""
    # 计算ComicInfo类中所有图片的hash值
    images_info_1 = dict()
    images_info_2 = dict()

