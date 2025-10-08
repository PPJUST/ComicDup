import os

import natsort

import common.function_cache_result
from common.class_cache import CacheMatchResult
from common.function_cache_result import CACHE_MATCH_RESULT_FOLDER, CACHE_MATCH_RESULT_FILE_EXTENSION

MAX_COUNT = 5  # 最大保存n个缓存文件


class MatchResultCacheModel:
    """匹配结果缓存模块的模型组件"""

    def __init__(self, ):
        super().__init__()

    def get_cache_filenames(self):
        """获取缓存文件名列表"""
        cache_filenames = [i for i in os.listdir(CACHE_MATCH_RESULT_FOLDER) if
                           i.endswith(CACHE_MATCH_RESULT_FILE_EXTENSION)]
        return cache_filenames

    def get_cache_file_infos(self):
        """获取缓存文件信息"""
        cache_filenames = self.get_cache_filenames()
        cache_filepaths = [os.path.join(CACHE_MATCH_RESULT_FOLDER, i) for i in cache_filenames]
        cache_infos = [CacheMatchResult(i) for i in cache_filepaths]
        return cache_infos

    def save_match_result(self, data):
        """保存匹配结果"""
        # 检查文件数量，超过上限则删除最旧的
        cache_filenames = self.get_cache_filenames()
        if len(cache_filenames) >= MAX_COUNT:
            oldest_filename = natsort.os_sorted(cache_filenames)[0]
            self.delete(oldest_filename)

        common.function_cache_result.save_match_result(data)

    def read_match_result(self, filename):
        """读取匹配结果"""
        return common.function_cache_result.read_match_result(filename)

    def delete(self, filename):
        """删除缓存文件"""
        # 组合缓存路径
        cache_filepath = os.path.normpath(os.path.join(CACHE_MATCH_RESULT_FOLDER, filename))
        # 删除
        os.remove(cache_filepath)
