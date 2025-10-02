# 子线程-对比图片hash
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
        print('开始子线程 对比图片hash')
        self.similar_hash_group = []
        match_hash_list = self.hash_list.copy()
        for index, hash_ in enumerate(self.hash_list, start=1):
            if self._is_stop:
                break
            self.SignalRate.emit(f'{index}/{len(self.hash_list)}')
            similar = {hash_}  # 集合，用于去重
            match_hash_list.remove(hash_)
            zero_count = hash_.count('0')
            for hash_compare in match_hash_list:
                # 在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，两个hash值的汉明距离不可能再低于阈值
                if abs(zero_count - hash_compare.count('0')) > self.hamming_distance / 2:
                    break
                distance = lzytools.image.calc_hash_hamming_distance(hash_, hash_compare)
                if distance <= self.hamming_distance:
                    similar.add(hash_compare)
            # 即使只有其自身，仍旧写入相似组，因为可能存在漫画的复制品，导致hash值相同
            self.similar_hash_group.append(list(similar))

        # 结束后发送信号
        print('获取的相似hash组', self.similar_hash_group)
        print('结束子线程 对比图片hash')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '全部图片对比完成')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'共匹配到{len(self.similar_hash_group)}组相似组')
        self.finished()

    @staticmethod
    def sort_hash(hash_list: list):
        """排序hash列表"""
        # 按hash值中0的个数对其进行排序，在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，两个hash值的汉明距离不可能再低于阈值
        return sorted(hash_list, key=lambda x: x.count('0'))
