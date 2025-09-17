# 子线程-使用SSIM相似度计算相似度
from typing import List

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
        self. threshold = 90

    def set_image_group(self, image_group: list):
        """需要匹配的图片组列表"""
        self.image_group = image_group


    def set_threshold(self, threshold: int):
        """设置相似度下限"""
        self.threshold = threshold

    def run(self):
        super().run()
















        # 保存到本地缓存中
        # 备忘录

        # 结束后发送信号
        self.finished()
