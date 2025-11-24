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

    class _ImagePixel:
        """图片像素"""
        text = '图片像素'
        # 不使用

    class Filename:
        """文件名"""
        text = '文件名'

    class ParentDirpath:
        """父目录"""
        text = '父目录'

    class ComicPoint:
        """漫画质量评分"""
        text = '漫画质量评分'


class OrderDirection:
    """排序方向"""

    class Descending:
        """倒序"""
        text = '倒序'

    class Ascending:
        """正序"""
        text = '正序'


ORDER_KEYS = [OrderKey.ComicPoint, OrderKey.Filesize, OrderKey.Pages, OrderKey.Filename, OrderKey.FileTime,
              OrderKey.ParentDirpath]
ORDER_KEYS_TEXT = [key.text for key in ORDER_KEYS]

ORDER_DIRECTIONS = [OrderDirection.Descending, OrderDirection.Ascending]
ORDER_DIRECTIONS_TEXT = [direction.text for direction in ORDER_DIRECTIONS]
