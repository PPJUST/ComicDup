# 子线程-对比图片hash
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

import lzytools.image

from common.class_runtime import TypeRuntimeInfo
from thread.thread_pattern import ThreadPattern


class ThreadCompareHash(ThreadPattern):
    """子线程-对比图片hash"""

    def __init__(self):
        super().__init__()
        self.step_index = 4
        self.step_info = '对比图片hash'

        # 需要匹配的hash值列表
        self.hash_list: List[str] = []
        # 相似hash组列表
        self.similar_hash_group: List[List[str]] = []

        # 用于匹配的缓存hash数据
        self.is_match_cache = False  # 是否匹配缓存数据
        self.cache_hash_list: List[str] = []

        # 判断为相似的汉明距离上限
        self.hamming_distance = 10

    def get_similar_hash_group(self):
        """获取相似hash组列表"""
        similar_hash_group = self.similar_hash_group
        self.clear()
        return similar_hash_group

    def set_hash_list(self, hash_list: list):
        """设置需要匹配的hash值列表"""
        hash_list = self.sort_hash(hash_list)
        self.hash_list = hash_list

    def set_is_match_cache(self, is_match_cache: bool):
        """设置是否匹配缓存数据"""
        self.is_match_cache = is_match_cache
    def get_is_match_cache(self):
        """获取是否匹配缓存数据"""
        return self.is_match_cache

    def set_cache_hash_list(self, cache_hash_list: List[str]):
        """设置用于匹配的缓存hash数据"""
        self.cache_hash_list = cache_hash_list

    def set_hamming_distance(self, hamming_distance: int):
        """设置最大汉明距离"""
        self.hamming_distance = hamming_distance

    def clear(self):
        """清空数据"""
        self.hash_list = []
        self.similar_hash_group = []

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始对比图片相似度')
        print(f'启动线程池 对比图片hash，线程数量：{self.max_workers}')

        total = len(self.hash_list)
        if total == 0:
            self._finish_compare()
            return

        # 使用线程池进行并发处理
        completed_count = 0

        # 生成用于匹配的hash值列表
        match_hash_list = self.hash_list.copy()
        # 如果需要匹配缓存hash值，则写入匹配列表中
        if self.is_match_cache:
            match_hash_list.extend(self.cache_hash_list)
            match_hash_list = self.sort_hash(match_hash_list)

        # 去重匹配列表并排序
        match_hash_list = list(set(match_hash_list))
        match_hash_list = self.sort_hash(match_hash_list)

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有任务
            # note 线程公用匹配列表，请勿在匹配方法中修改该列表
            futures = {executor.submit(self._compare, hash_, match_hash_list): hash_ for hash_ in self.hash_list}

            # 处理完成的任务
            for future in as_completed(futures):
                if self._is_stop:
                    executor.shutdown(wait=False, cancel_futures=True)
                    break

                hash_ = futures[future]
                try:
                    similar_group = future.result()
                    # 即使只有其自身，仍旧写入相似组，因为可能存在漫画的复制品，导致hash值相同，但是跳过空值（纯色页）
                    if similar_group:
                        self.similar_hash_group.append(similar_group)
                        completed_count += 1
                        self.SignalRate.emit(f'{completed_count}/{total}')
                except Exception as e:
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, f'对比{hash_}失败：{str(e)}')

            self._finish_compare()

    @staticmethod
    def sort_hash(hash_list: list):
        """排序hash列表"""
        # 按hash值中0的个数对其进行排序，在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，两个hash值的汉明距离不可能再低于阈值
        return sorted(hash_list, key=lambda x: x.count('0'))

    def _finish_compare(self):
        """完成对比后的处理"""
        print('结束线程池 对比图片hash')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '全部图片对比完成')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'共匹配到{len(self.similar_hash_group)}组相似组')
        self.finished()

    def _compare(self, hash_: str, match_hash_list: List[str]):
        """对比单个hash值与其他hash值的相似度"""
        similar = {hash_}  # 集合，用于去重

        # 统计需匹配的hash中0和1的个数，如果占比大于90%，则判断为纯色图片，不进行后续匹配
        zero_count = hash_.count('0')
        if zero_count / len(hash_) > 0.9 or zero_count / len(hash_) < 0.1:
            return None

        # 执行匹配
        zero_count = hash_.count('0')
        for hash_compare in match_hash_list:
            # 提前过滤不可能相似的hash值
            # 在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，两个hash值的汉明距离不可能再低于阈值
            # 因为在匹配前已经进行过排序操作，所以在出现超阈值的值后，即可终止循环
            if abs(zero_count - hash_compare.count('0')) > self.hamming_distance / 2:
                break
            distance = lzytools.image.calc_hash_hamming_distance(hash_, hash_compare)
            if distance <= self.hamming_distance:
                similar.add(hash_compare)

        return list(similar)
