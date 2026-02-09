# 子线程-对比漫画信息
import itertools
import os
from typing import List, Dict

import lzytools
import lzytools_image

from common.class_comic import ComicInfoBase
from common.class_config import TYPES_HASH_ALGORITHM, TYPES_ENHANCE_ALGORITHM
from common.class_runtime import TypeRuntimeInfo
from thread.thread_pattern import ThreadPattern


# todo 多线程

class ThreadCompareComic(ThreadPattern):
    """子线程-对比漫画信息"""

    def __init__(self):
        super().__init__()
        self.step_index = 4
        self.step_info = '对比漫画相似度'

        # 需要匹配的漫画信息类列表
        self.comic_info_list: List[ComicInfoBase] = []
        # 匹配到的相似漫画组列表
        self.similar_comic_info_groups: List[List[ComicInfoBase]] = []

        # 用于hash匹配的字典，键为虚拟图片路径，值为3种图片hash*3种长度的字典
        self.cache_image_hash_dict: Dict[str, Dict[str, str]] = dict()
        # 是否匹配缓存数据
        self.is_match_cache = False
        # 缓存中的漫画信息类列表（如果需要匹配缓存数据）
        self.cache_comic_info_list: List[ComicInfoBase] = []
        # 提取的图片数量
        self.extract_pages_count = 0
        # 匹配的hash值类型
        self.hash_type: TYPES_HASH_ALGORITHM = None
        # 匹配的hash值长度
        self.hash_length: int = 64
        # 判断hash值相似时的汉明距离阈值
        self.hamming_distance: int = 10
        # 是否仅匹配相同父目录
        self.is_match_same_parent_dir: bool = False
        # 匹配的父目录层级
        self.parent_dir_level: int = 0
        # 是否使用增强算法再次校验
        self.is_use_enhance_algorithm: bool = False
        # 增强算法类型
        self.enhance_algorithm_type: TYPES_ENHANCE_ALGORITHM = None

    def initialize(self):
        """初始化"""
        super().initialize()
        self.comic_info_list = []
        self.similar_comic_info_groups = []
        self.cache_image_hash_dict = dict()
        self.is_match_cache = False
        self.cache_comic_info_list = []
        self.extract_pages_count = 0
        self.hash_type = None
        self.hash_length = 64
        self.hamming_distance = 10
        self.is_match_same_parent_dir = False
        self.parent_dir_level = 0
        self.is_use_enhance_algorithm = False
        self.enhance_algorithm_type = None

    def get_similar_groups(self):
        """获取匹配到的相似漫画组列表"""
        return self.similar_comic_info_groups

    def set_comic_info_list(self, comic_info_list: List[ComicInfoBase]):
        """设置需要匹配的漫画信息类列表"""
        self.comic_info_list = comic_info_list

    def set_is_match_cache(self, is_enable: bool):
        """设置是否匹配缓存数据"""
        self.is_match_cache = is_enable

    def set_cache_comic_info_list(self, cache_comic_info_list: List[ComicInfoBase]):
        """设置缓存中的漫画信息类列表"""
        self.cache_comic_info_list = cache_comic_info_list

    def set_extract_pages(self, extract_pages_count: int):
        """设置提取的图片数量"""
        self.extract_pages_count = extract_pages_count

    def set_hash_type(self, hash_type: TYPES_HASH_ALGORITHM):
        """设置匹配的hash值类型"""
        self.hash_type = hash_type

    def set_hash_length(self, hash_length: int):
        """设置匹配的hash值长度"""
        self.hash_length = hash_length

    def set_hamming_distance(self, hamming_distance: int):
        """设置判断hash值相似时的汉明距离阈值"""
        self.hamming_distance = hamming_distance

    def set_image_hash_dict(self, image_hash_dict: Dict[str, Dict[str, str]]):
        """设置用于hash匹配的字典，键为虚拟图片路径，值为3种图片hash*3种长度的字典"""
        self.cache_image_hash_dict = image_hash_dict

    def set_is_match_same_parent_dir(self, is_enable: bool):
        """设置是否仅匹配相同父目录"""
        self.is_match_same_parent_dir = is_enable

    def set_parent_dir_level(self, parent_dir_level: int):
        """设置匹配的父目录层级"""
        self.parent_dir_level = parent_dir_level

    def set_is_enhance_algorithm(self, is_enable: bool):
        """设置是否使用增强算法再次校验"""
        self.is_use_enhance_algorithm = is_enable

    def set_enhance_algorithm(self, enhance_algorithm_type: TYPES_ENHANCE_ALGORITHM):
        """设置增强算法类型"""
        self.enhance_algorithm_type = enhance_algorithm_type

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始对比漫画相似度')
        print(f'启动线程池 对比漫画相似度，线程数量：{self.max_workers}')

        # 生成两两组合的无序组合迭代器
        if self.is_match_cache:
            # 缓存数据中本身就存在本次匹配的数据，使用笛卡尔积算法即可实现匹配组内部匹配和匹配组与缓存数据匹配
            comb_iterator = itertools.product(self.comic_info_list, self.cache_comic_info_list)
        else:
            comb_iterator = itertools.combinations(self.comic_info_list, 2)

        similar_groups: List[List[ComicInfoBase]] = []  # 匹配到的两两组合的相似漫画组列表
        # 遍历迭代器，搜索相似项
        for comb in comb_iterator:
            comic_info_1, comic_info_2 = comb
            print(f'正在对比：{comic_info_1.filepath} 和 {comic_info_2.filepath}')

            # 检查漫画是否存在
            comic_path_1 = comic_info_1.filepath
            comic_path_2 = comic_info_2.filepath
            if not os.path.exists(comic_path_1) or not os.path.exists(comic_path_2):
                print('漫画不存在，跳过')
                continue

            # 如果选择了仅匹配相同层级父目录选项，则进行父目录判断
            if self.is_match_same_parent_dir:
                print('同目录判断')
                # 提取父目录
                parent_dirpath_1 = lzytools.file.get_parent_dirpath(comic_path_1, self.parent_dir_level)
                parent_dirpath_2 = lzytools.file.get_parent_dirpath(comic_path_2, self.parent_dir_level)
                # 层级对比
                if parent_dirpath_1 == parent_dirpath_2:  # 相同父目录，正常执行
                    pass
                elif lzytools.file.is_subpath(parent_dirpath_1, parent_dirpath_2):  # 子目录，正常执行
                    pass
                elif lzytools.file.is_subpath(parent_dirpath_2, parent_dirpath_1):  # 子目录，正常执行
                    pass
                else:  # 不同父目录，跳过
                    print('不同父目录，跳过')
                    continue

            # 提取每本漫画指定数量的图片
            comic_info_1_images = comic_info_1.get_page_paths()[0:self.extract_pages_count]
            comic_info_2_images = comic_info_2.get_page_paths()[0:self.extract_pages_count]

            # 将图片两两组合进行相似度匹配
            for image_1, image_2 in itertools.product(comic_info_1_images, comic_info_2_images):
                print(f'对比图片相似度，{image_1} 和 {image_2}')
                hash_1 = self.get_hash(image_1, self.hash_type, self.hash_length)
                hash_2 = self.get_hash(image_2, self.hash_type, self.hash_length)
                # 写入信息类中
                comic_info_1.add_image_hash(hash_1)
                comic_info_2.add_image_hash(hash_2)
                # 加快判断速度，在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，则两个hash值的汉明距离不可能低于阈值
                zero_count_diff = abs(hash_1.count('0') - hash_2.count('0'))
                if zero_count_diff > self.hamming_distance / 2:
                    continue
                # 计算汉明距离
                hamming_distance = lzytools_image.calc_hash_hamming_distance(hash_1, hash_2)
                if hamming_distance <= self.hamming_distance:
                    # 如果选择了增强算法，则使用相应的增强算法进行校验
                    if self.is_use_enhance_algorithm:
                        pass  # todo
                    similar_groups.append([comic_info_1, comic_info_2])
                    print('判断为相似')
                else:
                    print('判断为不相似')

        # 处理匹配结果，合并相似组
        print('处理匹配结果，合并相似组')
        self.similar_comic_info_groups = lzytools.common.merge_intersection_item(similar_groups)

        self._finish_compare()

    def get_hash(self, path, hash_type, hash_length):
        hash_key = f'{hash_type.text}_{hash_length}'
        _hash = self.cache_image_hash_dict.get(path, {}).get(hash_key, '')
        return _hash

    def _finish_compare(self):
        """完成对比后的处理"""
        print('结束线程池 对比漫画相似度')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '全部漫画对比完成')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'共匹配到{len(self.similar_comic_info_groups)}组相似组')
        print(self.similar_comic_info_groups)
        self.finished()
