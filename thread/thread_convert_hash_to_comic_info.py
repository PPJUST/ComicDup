# 子线程-保存图片信息到数据库

from typing import List

import lzytools.common

from common.class_comic import ComicInfoBase
from common.class_config import TYPES_HASH_ALGORITHM
from common.class_runtime import TypeRuntimeInfo
from common.function_db_comic_info import DBComicInfo
from common.function_db_image_info import DBImageInfo
from thread.thread_pattern import ThreadPattern


class ThreadConvertHashToComicInfo(ThreadPattern):
    """子线程-转换hash值为漫画信息类"""

    def __init__(self):
        super().__init__()
        self.step_index = 2
        self.step_info = '转换hash值为漫画信息类'

        # 需要转换的hash列表
        self.hash_group: List[List[str]] = None
        # 转换后的漫画信息列表
        self.comic_info_group: List[List[ComicInfoBase]] = None
        # hash值类型
        self.hash_type: TYPES_HASH_ALGORITHM = None
        # 漫画数据库
        self.db_comic_info: DBComicInfo = None
        # 图片数据库
        self.db_image_info: DBImageInfo = None

    def set_hash_group(self, hash_group):
        self.hash_group = hash_group

    def set_hash_type(self, hash_type: TYPES_HASH_ALGORITHM):
        self.hash_type = hash_type

    def set_db_comic_info(self, db_comic_info: DBComicInfo):
        self.db_comic_info = db_comic_info

    def set_db_image_info(self, db_image_info: DBImageInfo):
        self.db_image_info = db_image_info

    def get_comic_info_group(self):
        return self.comic_info_group

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '将hash值相似组转换为对应的漫画路径组')
        # hash组格式：[[hash1, hash2, hash3], [hash4, hash5, hash6]]
        # 先转换为漫画路径格式
        comic_path_group = []
        for h_group in self.hash_group:
            p_group = set()
            for hash_ in h_group:
                image_infos = self.get_image_info_by_hash(hash_, self.hash_type)
                for image_info in image_infos:
                    comic_path = image_info.belong_comic_path
                    p_group.add(comic_path)
            if len(p_group) >= 2:
                comic_path_group.append(list(p_group))
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'共完成{len(comic_path_group)}组的转换')
        #  然后合并有交集的项目（用于整合组间相似项）
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'合并有交集的相似组')
        comic_path_group = lzytools.common.merge_intersection_item(comic_path_group)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'合并为{len(comic_path_group)}组')
        # 最后转换为漫画信息类格式
        self.comic_info_group = []
        for cp_group in comic_path_group:
            ci_group = []
            for comic_path in cp_group:
                comic_info = self.db_comic_info.get_comic_info_by_comic_path(comic_path)
                ci_group.append(comic_info)
            self.comic_info_group.append(ci_group)

        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '完成将hash值相似组转换为对应的漫画路径组')
        self.finished()

    def get_image_info_by_hash(self, hash_: str, hash_type: TYPES_HASH_ALGORITHM):
        """根据hash值获取对应的图片信息类（列表）"""
        # 由于一个hash值可能对应多个图片，因此返回一个列表
        image_infos = self.db_image_info.get_image_info_by_hash(hash_, hash_type)
        print('将hash值转换为对应的图片')
        print('hash值', hash_)
        return image_infos
