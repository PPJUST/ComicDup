# 子线程-对比漫画信息
import itertools
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict
from typing import List

import lzytools
import lzytools_image

from common.class_comic import ComicInfoBase
from common.class_config import TYPES_HASH_ALGORITHM, TYPES_ENHANCE_ALGORITHM, FileType
from common.class_runtime import TypeRuntimeInfo
from thread.thread_pattern import ThreadPattern


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

    def get_hashs_neeced(self, comic_info: ComicInfoBase):
        """获取一个漫画信息类需要匹配的hash值（按0个数排序）"""
        hashs = []  # 提取的hash值

        # 提取每本漫画指定数量的图片
        images = comic_info.get_page_paths()[0:self.extract_pages_count]
        for image in images:
            # 提取hash值
            if isinstance(comic_info.filetype, FileType.Folder):
                hash_ = self.get_hash(image, self.hash_type, self.hash_length)
            elif isinstance(comic_info.filetype, FileType.Archive):
                path_db_key = os.path.normpath(os.path.join(comic_info.filepath, image))
                hash_ = self.get_hash(path_db_key, self.hash_type, self.hash_length)
            else:
                hash_ = None

            # 检查hash值，跳过纯色图片
            zero_count_hash = hash_.count('0')
            length_hash = len(hash_)
            if zero_count_hash / length_hash >= 0.9 or zero_count_hash / length_hash <= 0.1:
                continue

            if hash_:
                hashs.append(hash_)

        # 按0的个数排序
        hashs.sort(key=lambda x: x.count('0'))

        return hashs

    def preprocess_comic_info(self):
        """预处理漫画信息类"""
        # 写入需要匹配的hash到漫画信息类中
        for comic_info in self.comic_info_list:
            hashs = self.get_hashs_neeced(comic_info)
            comic_info.set_image_hashs(hashs)
        for comic_info in self.cache_comic_info_list:
            hashs = self.get_hashs_neeced(comic_info)
            comic_info.set_image_hashs(hashs)

        # 按0的个数排序漫画信息类
        self.comic_info_list.sort(key=lambda x: x.image_hashs[0].count('0'))
        self.cache_comic_info_list.sort(key=lambda x: x.image_hashs[0].count('0'))

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始对比漫画相似度')
        print(f'启动线程池 对比漫画相似度，线程数量：{self.max_workers}')

        total_comic = len(self.comic_info_list)
        print('漫画总数', total_comic)
        if total_comic == 0:
            self._finish_compare()
            return

        # note 直接生成的漫画信息类和从数据库中读取的漫画信息类不是同一个对象，所以在勾选匹配缓存选项的情况下，
        # note 会导致漫画信息类与其自身进行匹配并判断为相似，最终导致相似结果中出现相同文件路径的两个不同项目，
        # note 需要在后续判断时做一次筛选来处理这问题

        # 预处理漫画信息类
        self.preprocess_comic_info()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '预处理漫画信息类')

        similar_groups: List[List[ComicInfoBase]] = []  # 匹配到的两两组合的相似漫画组列表
        # 使用线程池进行并发处理，遍历迭代器，搜索相似项
        completed_count = 0
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有任务
            futures = {executor.submit(self._compare, comic): comic for comic in self.comic_info_list}

            # 处理完成的任务
            for future in as_completed(futures):
                if self._is_stop:
                    executor.shutdown(wait=False, cancel_futures=True)
                    break

                comic = futures[future]
                try:
                    similar_group = future.result()
                    if similar_group:
                        similar_groups.append(similar_group)
                    completed_count += 1
                    self.SignalRate.emit(f'{completed_count}/{total_comic}')
                except Exception as e:
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, f'对比{comic.filepath}失败：{str(e)}')

        # 处理匹配结果，合并相似组
        # 先统一转换为文件路径
        similar_groups_filepath = []
        for similar_group in similar_groups:
            similar_groups_filepath.append([item.filepath for item in similar_group])
        # 合并有交集的项目
        similar_groups_filepath_merged = lzytools.common.merge_intersection_item(similar_groups_filepath)
        # 转换文件路径为漫画信息类
        similar_groups_merged = []
        for similar_group_filepath in similar_groups_filepath_merged:
            similar_group = []
            for filepath in set(similar_group_filepath):
                comic_info_convert = None
                for comic_info in (self.comic_info_list + self.similar_comic_info_groups):
                    if filepath == comic_info.filepath:
                        comic_info_convert = comic_info
                        break
                similar_group.append(comic_info_convert)
            similar_groups_merged.append(similar_group)

        self.similar_comic_info_groups = similar_groups_merged
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
        self.finished()

    def _compare(self, comic_info: ComicInfoBase):
        """对比漫画相似度"""
        # 检查漫画路径
        comic_path = comic_info.filepath
        if not comic_path and not os.path.exists(comic_path):
            return []

        # 提取需要匹配的漫画信息列表
        # 如果选择了匹配缓存，则对应的漫画信息列表为缓存数据库，缓存中本身存在本次需匹配的数据库）
        if self.is_match_cache:
            match_comic_info_list = self.cache_comic_info_list  # note 不要修改列表
        else:
            match_comic_info_list = self.comic_info_list  # note 不要修改列表

        # 遍历对比列表，匹配相似组
        similar_group = []
        hashs_base = comic_info.image_hashs  # 漫画的hash值列表
        min_zero_count_base = hashs_base[0].count('0')  # 漫画的hash值列表中0的个数最小的值
        max_zero_count_base = hashs_base[-1].count('0')  # 漫画的hash值列表中0的个数最大的值
        # 在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，则两个hash值的汉明距离不可能低于阈值
        threshold_zero_count = (min_zero_count_base - self.hamming_distance * 0.5,
                                max_zero_count_base + self.hamming_distance * 0.5)
        for compare_comic_info in match_comic_info_list:
            filepath_compare = compare_comic_info.filepath
            # 相同路径校验
            if filepath_compare == comic_path:
                continue

            # 如果选择了仅匹配相同层级父目录选项，则进行父目录判断
            if self.is_match_same_parent_dir:
                parent_dirpath_base = lzytools.file.get_parent_dirpath(comic_path, self.parent_dir_level)
                parent_dirpath_compare = lzytools.file.get_parent_dirpath(filepath_compare, self.parent_dir_level)
                if parent_dirpath_base == parent_dirpath_compare:
                    pass
                elif lzytools.file.is_subpath(parent_dirpath_base, parent_dirpath_compare):
                    pass
                elif lzytools.file.is_subpath(parent_dirpath_compare, parent_dirpath_base):
                    pass
                else:
                    continue

            # hash校验
            hashs_compare = compare_comic_info.image_hashs
            min_zero_count_compare = hashs_compare[0].count('0')
            max_zero_count_compare = hashs_compare[-1].count('0')
            if min_zero_count_compare < threshold_zero_count[0] or max_zero_count_compare > threshold_zero_count[1]:
                continue
            # 计算hash组之间的最小汉明距离
            for hash_1, hash_2 in itertools.product(hashs_base, hashs_compare):
                hamming_distance = lzytools_image.calc_hash_hamming_distance(hash_1, hash_2)
                if hamming_distance <= self.hamming_distance:
                    similar_group.append(compare_comic_info)
                    break

        # 处理结果
        if similar_group:
            similar_group.append(comic_info)
        return similar_group
