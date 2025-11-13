# 排序相关的类

class OrderKey:
    """排序的键"""

    class Filesize:
        """文件大小"""
        text = '文件大小'

    class FileTime:
        """文件时间"""
        text = '文件时间'

    class Pages:
        """页数"""
        text = '页数'

    class ImagePixel:
        """图片像素"""
        text = '图片像素'

    class Filename:
        """文件名"""
        text = '文件名'

    class FileTag:
        """文件名标识"""
        text = '文件名标识'

    class ParentDirpath:
        """父目录"""
        text = '父目录'


class OrderDirection:
    """排序方向"""

    class Descending:
        """倒序"""
        text = '倒序'

    class Ascending:
        """正序"""
        text = '正序'


ORDER_KEYS = [OrderKey.Filesize, OrderKey.FileTime, OrderKey.Pages, OrderKey.ParentDirpath]  # todo 禁用未完成的key
ORDER_KEYS_TEXT = [key.text for key in ORDER_KEYS]

ORDER_DIRECTIONS = [OrderDirection.Descending, OrderDirection.Ascending]
ORDER_DIRECTIONS_TEXT = [direction.text for direction in ORDER_DIRECTIONS]
