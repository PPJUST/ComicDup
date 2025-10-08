# 缓存文件的相关类
import os
from datetime import datetime

import common.function_cache_result
from common import function_file


class CacheMatchResult:
    """缓存匹配结果"""

    def __init__(self, filepath: str):
        # 文件路径
        self.filepath = os.path.normpath(filepath)
        # 文件名
        self.filename = os.path.basename(self.filepath)
        # 提取文件创建时间（自纪元以来的秒数）
        self.date = datetime.fromtimestamp(os.path.getctime(self.filepath)).strftime("%Y-%m-%d %H:%M:%S")
        # 提取相似组数
        similar_info_groups = common.function_cache_result.read_match_result(self.filename)
        self.group_count = len(similar_info_groups)
        # 提取相似组总大小
        size_count_bytes = 0
        for group in similar_info_groups:
            for comic_info in group:
                filesize = comic_info.filesize_bytes
                size_count_bytes += filesize
        self.size_count = function_file.format_bytes_size(size_count_bytes)
