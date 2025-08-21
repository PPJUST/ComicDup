# 子线程-对比漫画相似性
from functools import partial
from multiprocessing import Pool

from child_thread.thread_pattern import ThreadPattern
from class_ import class_image_info
from class_.class_image_info import ImageInfo
from module import function_config_similar_option, function_image_hash, function_ssim, function_normal, \
    function_match_result


class ThreadMatch(ThreadPattern):
    """对比漫画相似性"""

    def __init__(self):
        super().__init__()
        self._step = '相似匹配'
        self.image_info_dict = dict()

    def set_image_info_dict(self, image_info_dict: dict):
        self.image_info_dict = image_info_dict

    def run(self):
        super().run()
        # 获取相似度算法设置
        match_cache_enable = function_config_similar_option.cache.get()
        # 将上一步计算出来的图片信息字典进行内部对比，找出所有漫画相似组
        similar_comic_group_inside = self.match_inside(self.image_info_dict)
        # 如果选择了与缓存数据对比，则将该任务字典与数据库（剔除该任务字典项之外的数据库项，防止重复匹配）对比，找出所有漫画相似组
        if match_cache_enable:
            similar_comic_group_cache = self.match_cache(self.image_info_dict)
        else:
            similar_comic_group_cache = []
        # 合并两组漫画相似组，合并交集项+去重
        similar_comic_group = similar_comic_group_inside + similar_comic_group_cache
        similar_comic_group = function_normal.merge_intersecting_sets(similar_comic_group)
        # 将匹配结果保存到本地，用于后续读取
        function_match_result.save_result(similar_comic_group)
        # 结束后重置参数
        self.image_info_dict.clear()
        # 结束后发送信号
        self.finished('stopped but finished')  # 特殊文本stopped but finished，终止判断为TRUE但是发送finished信号而不是stopped

    def match_inside(self, image_info_dict: dict) -> list:
        """内部匹配，找出相似漫画组
        :param image_info_dict: dict，key为图片路径，value为image_info类
        :return: list，相似漫画组，内部元素为漫画路径"""
        # 获取相似度算法设置
        hash_algorithm = function_config_similar_option.hash_algorithm.get()

        # 进行匹配前对hash值进行处理（对hash中的0或1计数，在匹配时两者计数差额>阈值/2的部分直接丢弃，不需要进行匹配）
        image_info_dict_filter = function_image_hash.filter_hash_dict(image_info_dict, hash_algorithm)
        compare_image_info_dict = image_info_dict_filter.copy()

        """以下方式实际测试时发现问题：需匹配的数量较大时，compare_groups会非常非常占用内存，所以不再预先创建匹配组，而是将对比数据固定
        # 多进程的imap方法只支持传递一个可变参数给指定函数，所以两个可变参数需要合并为一组，在函数内部进行拆分
        # 匹配前在对比字典中删除当前项，防止后续重复比对，序列越往后对比量越少速度越快
        compare_groups = []
        _temp_dict = compare_image_info_dict  # 临时字典，用于删除key
        for fake_image_path, image_info in image_info_dict_filter.items():
            _temp_dict.pop(fake_image_path)
            _group = (image_info, _temp_dict.copy())
            compare_groups.append(_group)
        """

        # 多进程匹配
        similar_comic_group = self.multi_match(image_info_dict_filter, compare_image_info_dict)  # 最终的相似漫画组
        """未使用多进程的原版方法
        # 内部匹配
        similar_comic_group = list()  # 最终的相似漫画组，内部元素为元组，元组的内部元素为漫画路径
        for index, (fake_image_path, image_info) in enumerate(image_info_dict_filter.copy().items(), start=1):
            if self._stop_code:
                break
            self.signal_rate.emit(f'{index}/{len(image_info_dict_filter)}')
            # 匹配前在对比字典中删除当前项，防止后续重复比对，序列越往后对比量越少速度越快
            if fake_image_path in compare_image_info_dict:
                compare_image_info_dict.pop(fake_image_path)
            similar_image_info_dict = function_image_hash.filter_similar_group(image_info, compare_image_info_dict,
                                                                               hash_algorithm, hash_hamming_distance)
            # 根据相似算法设置，判断是否使用ssim进行进一步校验
            if similar_image_info_dict and ssim_enable:
                similar_image_info_dict = self.compare_ssim(image_info, similar_image_info_dict, resize_image_size,
                                                            ssim_threshold)
            # 提取相似组内的漫画路径
            comics = set()
            for _, _image_info in similar_image_info_dict.items():
                comic_path = _image_info.comic_path
                comics.add(comic_path)
            # 检查转换的漫画组，如果组内仅有一个元素则丢弃
            if len(comics) > 1:
                similar_comic_group.append(comics)

        return similar_comic_group"""

        return similar_comic_group

    def match_cache(self, image_info_dict: dict) -> list:
        """与数据库中的缓存数据匹配，找出相似漫画组
        :param image_info_dict: dict，key为图片路径，value为image_info类
        :return: list，相似漫画组，内部元素为集合，集合内部元素为漫画路径"""
        # 获取相似度算法设置
        hash_algorithm = function_config_similar_option.hash_algorithm.get()
        resize_image_size = function_config_similar_option.image_size.get()

        # 读取数据库缓存数据
        cache_image_info_dict = class_image_info.read_db(resize_image_size ** 2)

        # 剔除缓存中与需匹配的图片信息字典重叠的部分
        for c_image_path in image_info_dict:
            if c_image_path in cache_image_info_dict:
                cache_image_info_dict.pop(c_image_path)

        # 进行匹配前对hash值进行处理（对hash中的0或1计数，在匹配时两者计数差额>阈值/2的部分直接丢弃，不需要进行匹配）
        image_info_dict_filter = function_image_hash.filter_hash_dict(image_info_dict, hash_algorithm)
        compare_image_info_dict = function_image_hash.filter_hash_dict(cache_image_info_dict, hash_algorithm)

        """以下方式实际测试时发现问题：需匹配的数量较大时，compare_groups会非常非常占用内存，所以不再预先创建匹配组，而是将对比数据固定
        # 多进程的imap方法只支持传递一个可变参数给指定函数，所以两个可变参数需要合并为一组，在函数内部进行拆分
        compare_groups = []
        for _, image_info in image_info_dict_filter.items():
            _group = (image_info, compare_image_info_dict)
            compare_groups.append(_group)
        """

        # 多进程匹配
        similar_comic_group = self.multi_match(image_info_dict_filter, compare_image_info_dict)  # 最终的相似漫画组
        """未使用多进程的原版方法
        # 进行匹配
        similar_comic_group = list()  # 最终的相似漫画组
        for index, (fake_image_path, image_info) in enumerate(image_info_dict_filter.copy().items(), start=1):
            if self._stop_code:
                break
            self.signal_rate.emit(f'{index}/{len(image_info_dict_filter)}')
            similar_image_info_dict = function_image_hash.filter_similar_group(image_info, compare_image_info_dict,
                                                                               hash_algorithm, hash_hamming_distance)
            # 根据相似算法设置，判断是否使用ssim进行进一步校验
            if similar_image_info_dict and ssim_enable:
                similar_image_info_dict = self.compare_ssim(image_info, similar_image_info_dict, resize_image_size,
                                                            ssim_threshold)
            # 提取相似组内的漫画路径
            comics = set()
            for _, _image_info in similar_image_info_dict.items():
                comic_path = _image_info.comic_path
                comics.add(comic_path)
            # 检查转换的漫画组，如果组内仅有一个元素则丢弃
            if len(comics) > 1:
                similar_comic_group.append(comics)

        return similar_comic_group"""

        return similar_comic_group

    def multi_match(self, image_info_dict: dict, compare_image_info_dict: dict):
        """多进程匹配
        :param image_info_dict: dict，需处理的image_info_dict
        :param compare_image_info_dict: dict，用于对比匹配的image_info_dict"""
        # 获取相似度算法设置
        hash_algorithm = function_config_similar_option.hash_algorithm.get()
        resize_image_size = function_config_similar_option.image_size.get()
        threads_count = function_config_similar_option.threads.get()
        threshold_hash = function_config_similar_option.similarity_threshold.get_hash_hamming_distance()
        ssim_enable = function_config_similar_option.ssim.get()
        ssim_threshold = function_config_similar_option.similarity_threshold.get_ssim_threshold()
        match_similar = function_config_similar_option.match_similar.get()

        _total_count = len(image_info_dict)

        # 启用多进程
        similar_comic_group = list()  # 最终的相似漫画组
        with Pool(processes=threads_count) as pool:
            # 使用partial固定部分参数
            calculate_partial = partial(self.filter_similar_group, compare_image_info_dict=compare_image_info_dict,
                                        compare_hash=hash_algorithm,
                                        threshold_hamming_distance=threshold_hash, ssim_enable=ssim_enable,
                                        resize_image_size=resize_image_size, ssim_threshold=ssim_threshold,
                                        match_similar=match_similar)
            # 设置多进程任务：pool.imap()为异步传参，imap中的第一个参数为执行的函数，第二个参数为可迭代对象（用于传参）
            try:
                for index, similar_image_info_dict in enumerate(pool.imap(calculate_partial, image_info_dict.values())):
                    if self._stop_code:
                        break
                    self.signal_rate.emit(f'{index + 1}/{_total_count}')
                    # 提取相似组内的漫画路径
                    comics = set()
                    for _, _image_info in similar_image_info_dict.items():
                        comic_path = _image_info.comic_path
                        comics.add(comic_path)
                    # 检查转换的漫画组，如果组内仅有一个元素则丢弃
                    if len(comics) > 1:
                        similar_comic_group.append(comics)
            except FileNotFoundError:
                pass

        return similar_comic_group

    @staticmethod
    def filter_similar_group(image_info: ImageInfo, compare_image_info_dict: dict, compare_hash: str,
                             threshold_hamming_distance: int,
                             ssim_enable: bool, resize_image_size: int, ssim_threshold: float, match_similar: bool):
        """用于多线程中转，拆分元组"""
        # 如果选中的仅匹配相似文件名项目的选项，则先对对比字典进行一次筛选处理，剔除非相似文件名项目
        if match_similar:
            compare_image_info_dict = function_image_hash.filter_unsimilar_items(image_info, compare_image_info_dict,
                                                                                 threshold_hamming_distance)

        similar_image_info_dict = function_image_hash.filter_similar_group(image_info, compare_image_info_dict,
                                                                           compare_hash, threshold_hamming_distance)

        # 根据相似算法设置，判断是否使用ssim进行进一步校验
        if similar_image_info_dict and ssim_enable:
            similar_image_info_dict = function_ssim.compare_ssim(image_info, similar_image_info_dict, resize_image_size,
                                                                 ssim_threshold)

        return similar_image_info_dict
