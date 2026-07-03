from typing import List

import natsort

from common.class_comic import ComicInfoBase
from common.class_order import ORDER_KEYS, ORDER_DIRECTIONS, OrderKey, OrderDirection


class SimilarResultPreviewModel:
    """相似匹配结果模块的模型组件"""

    def __init__(self):
        pass

    def sort_item(self, group: List[ComicInfoBase], sort_key: ORDER_KEYS, sort_direction: ORDER_DIRECTIONS):
        """排序相似组内元素"""
        is_reverse = (isinstance(sort_direction, OrderDirection.Descending) or
                      sort_direction == OrderDirection.Descending)

        if isinstance(group, set):  # 多做一次检查，防止报错
            group = list(group)

        if sort_key == OrderKey.Filesize:
            group.sort(key=lambda x: x.filesize_bytes if x else 0, reverse=is_reverse)
        elif sort_key == OrderKey.FileTime:
            group.sort(key=lambda x: x.modified_time if x else 0, reverse=is_reverse)
        elif sort_key == OrderKey.Pages:
            group.sort(key=lambda x: x.page_count if x else 0, reverse=is_reverse)
        elif sort_key == OrderKey.Filename:
            group.sort(key=lambda x: x.filename if x else '', reverse=is_reverse)
        elif sort_key == OrderKey.ParentDirpath:
            group.sort(key=lambda x: x.parent_dirpath if x else '', reverse=is_reverse)
        elif sort_key == OrderKey.ComicPoint:
            group.sort(key=lambda x: x.calc_point() if x else 0, reverse=is_reverse)
        else:
            raise Exception('排序键错误')

        return group

    def sort_groups(self, group_list: List[List[ComicInfoBase]], sort_key: ORDER_KEYS,
                    sort_direction: ORDER_DIRECTIONS):
        """排序相似组"""
        is_reverse = (isinstance(sort_direction, OrderDirection.Descending) or
                      sort_direction == OrderDirection.Descending)

        if isinstance(group_list, set):  # 多做一次检查，防止报错
            group_list = list(group_list)

        if sort_key == OrderKey.Filesize:
            group_list.sort(key=lambda x: sum(item.filesize_bytes for item in x if x) if x else 0, reverse=is_reverse)
        elif sort_key == OrderKey.Pages:
            group_list.sort(key=lambda x: sum(item.page_count for item in x) / len(x) if x else 0, reverse=is_reverse)
        elif sort_key == OrderKey.Filename:
            group_list = natsort.os_sorted(group_list,
                                           key=lambda x: natsort.os_sorted([item.filename for item in x])[0]
                                           if x else '',
                                           reverse=is_reverse)
        elif sort_key == OrderKey.ParentDirpath:
            group_list = natsort.os_sorted(group_list,
                                           key=lambda x: natsort.os_sorted([item.parent_dirpath for item in x])[0]
                                           if x else '',
                                           reverse=is_reverse)
        else:
            raise Exception('排序键错误')

        return group_list
