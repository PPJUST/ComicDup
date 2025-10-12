from typing import List

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

        if sort_key == OrderKey.Filesize:
            group.sort(key=lambda x: x.filesize_bytes, reverse=is_reverse)
        elif sort_key == OrderKey.FileTime:
            group.sort(key=lambda x: x.modified_time, reverse=is_reverse)
        elif sort_key == OrderKey.Pages:
            group.sort(key=lambda x: x.page_count, reverse=is_reverse)
        elif sort_key == OrderKey.ImagePixel:  # 备忘录
            pass
            # group.sort(key=lambda x: x., reverse=is_reverse)
        elif sort_key == OrderKey.Filename:  # 备忘录
            pass
            # group.sort(key=lambda x: x., reverse=is_reverse)
        elif sort_key == OrderKey.FileTag:  # 备忘录
            pass
            # group.sort(key=lambda x: x., reverse=is_reverse)
        elif sort_key == OrderKey.ParentDirpath:
            group.sort(key=lambda x: x.parent_dirpath, reverse=is_reverse)
        else:
            raise Exception('排序键错误')

        return group
