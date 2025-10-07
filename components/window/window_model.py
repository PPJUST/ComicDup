import os
from typing import List

import lzytools.common
from PySide6.QtCore import Signal, QObject

from common.class_comic import ComicInfoBase
from common.class_config import TYPES_HASH_ALGORITHM
from common.class_image import ImageInfoBase
from common.class_runtime import TypeRuntimeInfo
from common.function_db_comic_info import DBComicInfo
from common.function_db_image_info import DBImageInfo


class WindowModel(QObject):
    """主窗口的模型组件"""
    SignalRuntimeInfo = Signal(object, str, name='运行信息')

    def __init__(self, ):
        super().__init__()
        # 连接数据库
        self.db_comic_info = DBComicInfo()
        self.db_image_info = DBImageInfo()

    def save_comic_info_to_db(self, comic_infos: List[ComicInfoBase]):
        """保存漫画信息到本地数据库中"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '正在保存漫画信息到本地数据库')
        for comic_info in comic_infos:
            # 在保存漫画信息前，考虑已存在于数据库中的项目，具体逻辑参考流程图
            is_comic_exist_db = self.db_comic_info.is_comic_exist(comic_info.filepath, comic_info.fingerprint)
            if not is_comic_exist_db:  # 不存在则新增
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'保存{comic_info.filename}到数据库')
                comic_info.save_preview_image()  # 新增前保存预览图
                self.db_comic_info.add(comic_info)
            else:
                is_comic_moved_db = self.db_comic_info.is_comic_moved(comic_info.fingerprint, comic_info.filepath)
                if not is_comic_moved_db:  # 已存在且未移动则跳过
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'{comic_info.filename}已存在于数据库，跳过')
                    continue
                else:  # 已存在且已移动，则更新漫画信息数据库和图片信息数据库
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'{comic_info.filename}数据新于数据库，更新')
                    comic_path_deleted = self.db_comic_info.update_comic_moved(comic_info)
                    if comic_path_deleted:
                        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'更新图片数据库中对应的漫画数据')
                        self.db_image_info.update_belong_comic_moved(comic_info.fingerprint,
                                                                     old_comic_path=comic_path_deleted,
                                                                     new_comic_path=comic_info.filepath)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '完成保存漫画信息到本地数据库')

    def save_image_info_to_db(self, image_infos: List[ImageInfoBase]):
        """保存图片信息到本地数据库中"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '正在保存图片信息到本地数据库')
        for image_info in image_infos:
            self.db_image_info.add(image_info)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '完成保存图片信息到本地数据库')

    def get_hash_list_from_image_infos(self, image_infos: List[ImageInfoBase], hash_type: TYPES_HASH_ALGORITHM,
                                       hash_length: int):
        """从图片信息类列表中读取图片hash值列表"""
        hash_list = []
        for image_info in image_infos:
            hash_ = image_info.get_hash(hash_type, hash_length)
            hash_list.append(hash_)

        return hash_list

    def get_hash_from_image_info(self, image_info: ImageInfoBase, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        """从图片信息类中读取图片hash值"""
        hash_ = image_info.get_hash(hash_type, hash_length)
        return hash_

    def get_image_info_by_hash(self, hash_: str, hash_type: TYPES_HASH_ALGORITHM):
        """根据hash值获取对应的图片信息类（列表）"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '将图片hash值转换为对应的图片路径')
        # 由于一个hash值可能对应多个图片，因此返回一个列表
        image_infos = self.db_image_info.get_image_info_by_hash(hash_, hash_type)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'需要转换的hash值：{hash_}')
        for _image_info in image_infos:
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'转换的图片路径：{_image_info.image_path}')
        print('将hash值转换为对应的图片')
        print('hash值', hash_)
        print('对应的图片', [i.image_path for i in image_infos])
        return image_infos

    def get_comic_info_by_image_info(self, image_info: ImageInfoBase):
        """根据图片信息类获取对应的漫画信息类"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '将图片路径转换为对应的漫画路径')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'需要转换的图片路径：{image_info.image_path}')
        comic_path = image_info.belong_comic_path
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'转换的漫画路径：{comic_path}')
        return self.get_comic_info_by_comic_path(comic_path)

    def get_comic_info_by_comic_path(self, comic_path: str):
        """根据漫画路径获取对于的漫画信息类"""
        comic_info = self.db_comic_info.get_comic_info_by_comic_path(comic_path)
        return comic_info

    def convert_hash_group_to_comic_info_group(self,
                                               hash_group: List[List[str]],
                                               hash_type: TYPES_HASH_ALGORITHM) -> List[List[ComicInfoBase]]:
        """将hash值组列表转换为对应的漫画组列表"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '将hash值相似组转换为对应的漫画路径组')
        # hash组格式：[[hash1, hash2, hash3], [hash4, hash5, hash6]]
        # 先转换为漫画路径格式
        comic_path_group = []
        for h_group in hash_group:
            p_group = set()
            for hash_ in h_group:
                image_infos = self.get_image_info_by_hash(hash_, hash_type)
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
        comic_info_group = []
        for cp_group in comic_path_group:
            ci_group = []
            for comic_path in cp_group:
                comic_info = self.get_comic_info_by_comic_path(comic_path)
                ci_group.append(comic_info)
            comic_info_group.append(ci_group)

        return comic_info_group

    def filter_comic_info_group(self, comic_info_group: List[List[ComicInfoBase]], comic_path_search_list: List[str]):
        """对转换的漫画信息类列表进行处理（由于hash转换时是根据数据库数据，可能存在多余或失效路径，需要进行一次筛选）"""
        # 剔除不在检索漫画范围内的项目以及路径失效的项目
        # 漫画组格式：[[ComicInfo1,ComicInfo2,ComicInfo3], [ComicInfo4,ComicInfo5,ComicInfo6]]
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'对相似组进行有效性筛选')
        comic_info_group_filter = []
        for group in comic_info_group:
            group: List[ComicInfoBase]
            group_filter = []
            for comic_info in group:
                path = comic_info.filepath
                if path in comic_path_search_list and os.path.exists(path):
                    group_filter.append(comic_info)
            if len(group_filter) >= 2:
                comic_info_group_filter.append(group_filter)

        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'完成相似组有效性筛选')
        return comic_info_group_filter
