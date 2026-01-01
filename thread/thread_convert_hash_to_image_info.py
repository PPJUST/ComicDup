# 子线程-转换hash值为图片信息类
import itertools
from typing import List

import lzytools_image

from common.class_config import TYPES_HASH_ALGORITHM, TYPES_ENHANCE_ALGORITHM
from common.class_image import ImageInfoBase
from common.class_runtime import TypeRuntimeInfo
from common.function_db_image_info import DBImageInfo
from thread.thread_pattern import ThreadPattern


class ThreadConvertHashToImageInfo(ThreadPattern):
    """子线程-转换hash值为图片信息类"""

    def __init__(self):
        super().__init__()
        self.step_index = 5
        self.step_info = '转换hash值为图片信息类'

        # 需要转换的hash列表
        self.hash_group: List[List[str]] = None
        # 转换后的图片信息列表
        self.image_info_group: List[List[ImageInfoBase]] = None
        # hash值类型
        self.hash_type: TYPES_HASH_ALGORITHM = None
        # 图片数据库
        self.db_image_info: DBImageInfo = None

        # 是否使用增强算法再校验
        self.is_enhance_compare: bool = False
        # 增强算法类型
        self.enhance_algorithm: TYPES_ENHANCE_ALGORITHM = None
        # 相似度阈值
        self.threshold: float = None

    def set_hash_group(self, hash_group):
        self.hash_group = hash_group

    def set_hash_type(self, hash_type: TYPES_HASH_ALGORITHM):
        self.hash_type = hash_type

    def set_db_image_info(self, db_image_info: DBImageInfo):
        self.db_image_info = db_image_info

    def set_is_enhance_compare(self, is_enable: bool):
        self.is_enhance_compare = is_enable

    def set_enhance_algorithm(self, enhance_algorithm: TYPES_ENHANCE_ALGORITHM):
        self.enhance_algorithm = enhance_algorithm

    def set_threshold(self, threshold: float):
        if threshold > 1:
            threshold = threshold / 100
        self.threshold = threshold

    def get_image_info_group(self):
        return self.image_info_group

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '将hash值相似组转换为对应的图片信息类组')
        # hash组格式：[[hash1, hash2, hash3], [hash4, hash5, hash6]]
        # 先转换为漫画路径格式
        print('转换hash值为图片信息类')
        print('需要转换的hash值', self.hash_group)
        self.image_info_group = []
        for h_group in self.hash_group:
            i_group = set()
            for hash_ in h_group:
                image_infos = self.get_image_info_by_hash(hash_, self.hash_type)
                i_group.update(image_infos)
            # 是否进行增强算法再校验
            if self.is_enhance_compare:
                i_group = self.enhance_compare_ssim(i_group)
            if i_group and len(i_group) >= 2:
                self.image_info_group.append(list(i_group))
        print('转换结果', self.image_info_group)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'共完成{len(self.image_info_group)}组的转换')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '完成将hash值相似组转换为对应的图片信息类组')
        self.finished()

    def get_image_info_by_hash(self, hash_: str, hash_type: TYPES_HASH_ALGORITHM):
        """根据hash值获取对应的图片信息类（列表）"""
        # 由于一个hash值可能对应多个图片，因此返回一个列表
        image_infos = self.db_image_info.get_image_info_by_hash(hash_, hash_type)
        print('将hash值转换为对应的图片')
        print('hash值', hash_)
        return image_infos

    def enhance_compare_ssim(self, image_infos: List[ImageInfoBase]):
        """增强算法SSIM再校验"""
        image_infos_filter = set()
        # 生成两两组合的不重复项的列表
        group_combinations = itertools.combinations(image_infos, 2)

        # 对列表中的每对图片信息组进行相似计算
        for group_comb in group_combinations:
            # 读取为numpy数组图片对象
            image_1_numpy = group_comb[0].get_numpy_image()
            image_2_numpy = group_comb[1].get_numpy_image()
            # 计算相似度
            similarity = lzytools_image.calc_ssim(image_1_numpy, image_2_numpy)
            # 相似度大于阈值，则保留图片信息组，否则丢弃
            if similarity >= self.threshold:
                image_infos_filter.update(group_comb)

        return image_infos_filter

    def enhance_compare_orb(self, image_infos: List[ImageInfoBase]):
        """增强算法ORB再校验"""
        pass  # 不使用ORB算法，计算太慢了
