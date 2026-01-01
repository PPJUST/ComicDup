# 子线程-转换hash值为图片信息类

from typing import List

from common.class_config import TYPES_HASH_ALGORITHM
from common.class_image import ImageInfoBase
from common.class_runtime import TypeRuntimeInfo
from common.function_db_image_info import DBImageInfo
from thread.thread_pattern import ThreadPattern


# todo 增强算法的校验在这里完成

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

    def set_hash_group(self, hash_group):
        self.hash_group = hash_group

    def set_hash_type(self, hash_type: TYPES_HASH_ALGORITHM):
        self.hash_type = hash_type

    def set_db_image_info(self, db_image_info: DBImageInfo):
        self.db_image_info = db_image_info

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
            if len(i_group) >= 2:
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
