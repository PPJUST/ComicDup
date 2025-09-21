# 子线程-计算图片hash
from typing import Dict

import natsort

from common.class_comic import ImageInfo
from common.class_config import SimilarAlgorithm, TYPES_HASH_ALGORITHM
from thread.thread_pattern import ThreadPattern


class ThreadAnalyseImageInfo(ThreadPattern):
    """子线程-计算图片hash"""

    def __init__(self):
        super().__init__()
        self.step_index = 3
        self.step_info = '计算图片hash'

        # 图片列表
        self.images = []
        # 图片hash字典
        self.image_info_dict: Dict[str, ImageInfo] = dict()

        # 计算的图片hash类型
        self.hash_type = SimilarAlgorithm.dHash()
        # 图片hash长度
        self.hash_length = 64

    def get_image_info_dict(self):
        """获取图片信息字典"""
        return self.image_info_dict

    def set_images(self, images: list):
        """设置需要计算hash的图片列表"""
        self.images = natsort.os_sorted(images)

    def set_hash_type(self, hash_type: TYPES_HASH_ALGORITHM):
        """设置需要计算的图片hash类型"""
        self.hash_type = hash_type

    def set_hash_length(self, length: int):
        """设置需要计算的图片hash类型"""
        self.hash_length = length

    def clear(self):
        """清空数据"""
        self.images.clear()
        self.image_info_dict.clear()

    def run(self):
        super().run()
        for index, image_path in enumerate(self.images, start=1):
            image_info = ImageInfo(image_path)
            image_info.calc_hash(self.hash_type, self.hash_length)  # 计算指定hash值
            self.image_info_dict[image_path] = image_info

        # 结束后发送信号
        self.finished()
