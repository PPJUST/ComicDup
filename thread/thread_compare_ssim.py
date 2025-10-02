# 子线程-使用SSIM相似度计算相似度
import itertools
from typing import List

import lzytools.image

from thread.thread_pattern import ThreadPattern


class ThreadCompareSSIM(ThreadPattern):
    """子线程-使用SSIM相似度计算相似度"""

    def __init__(self):
        super().__init__()
        self.step_index = 5
        self.step_info = '计算SSIM相似度'

        # 需要匹配的图片组列表
        self.image_group: List[List[str]] = []
        # 相似图片组列表
        self.similar_image_group: List[List[str]] = []

        # 判断为相似的相似度下限
        self.threshold = 90

    def get_similar_image_group(self):
        """获取相似图片组列表"""
        similar_image_group = self.similar_image_group
        self.clear()
        return similar_image_group

    def set_image_group(self, image_group: list):
        """需要匹配的图片组列表"""
        self.image_group = image_group

    def set_threshold(self, threshold: int):
        """设置相似度下限"""
        self.threshold = threshold

    def clear(self):
        """清空数据"""
        self.image_group = []
        self.similar_image_group = []

    def run(self):
        super().run()
        for group in self.image_group:
            # 生成两两组合的不重复项的列表
            group_combinations = itertools.combinations(group, 2)
            # 对列表中的每对图片进行相似计算
            for group_comb in group_combinations:
                # 计算相似度
                image_1_numpy = lzytools.image.read_image_to_numpy(group_comb[0])
                image_2_numpy = lzytools.image.read_image_to_numpy(group_comb[1])
                similarity = lzytools.image.calc_ssim(image_1_numpy, image_2_numpy)
                # 判断相似度是否满足要求
                if similarity >= self.threshold:
                    # 相似度高于阈值则加入相似图片组列表
                    self.similar_image_group.append(group_comb)

        # 结束后发送信号
        self.finished()
