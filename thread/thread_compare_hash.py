# 子线程-对比图片hash
from typing import List

import lzytools.image

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
        return self.similar_hash_group

    def set_hash_list(self, hash_list: list):
        """设置需要匹配的hash值列表"""
        hash_list = self.sort_hash(hash_list)
        self.hash_list = hash_list

    def set_hamming_distance(self, hamming_distance: int):
        """设置最大汉明距离"""
        self.hamming_distance = hamming_distance

    def clear(self):
        """清空数据"""
        self.hash_list.clear()
        self.similar_hash_group.clear()

    def run(self):
        super().run()
        print('开始子线程 对比图片hash')
        self.similar_hash_group = []
        match_hash_list = self.hash_list.copy()
        for hash_ in self.hash_list:
            similar = [hash_]
            match_hash_list.remove(hash_)
            zero_count = hash_.count('0')
            for hash_compare in match_hash_list:
                # 在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，两个hash值的汉明距离不可能再低于阈值
                if abs(zero_count - hash_compare.count('0')) > self.hamming_distance / 2:
                    break
                distance = lzytools.image.calc_hash_hamming_distance(hash_, hash_compare)
                if distance <= self.hamming_distance:
                    similar.append(hash_compare)
            if len(similar) >= 2:
                self.similar_hash_group.append(similar)

        # 结束后发送信号
        print('获取的相似hash组', self.similar_hash_group)
        print('结束子线程 对比图片hash')
        self.finished()

    @staticmethod
    def sort_hash(hash_list: list):
        """排序hash列表"""
        # 按hash值中0的个数对其进行排序，在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，两个hash值的汉明距离不可能再低于阈值
        return sorted(hash_list, key=lambda x: x.count('0'))
