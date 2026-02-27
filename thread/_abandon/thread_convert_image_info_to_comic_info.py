# 子线程-转换图片信息类为漫画信息类

from typing import List

import lzytools

from common.class_comic import ComicInfoBase
from common.class_image import ImageInfoBase
from common.class_runtime import TypeRuntimeInfo
from common.function_db_comic_info import DBComicInfo
from common.function_db_image_info import DBImageInfo
from thread.thread_pattern import ThreadPattern


class ThreadConvertImageInfoToComicInfo(ThreadPattern):
    """子线程-转换图片信息类为漫画信息类"""

    def __init__(self):
        super().__init__()
        self.step_index = 2
        self.step_info = '转换图片信息类为漫画信息类'

        # 需要转换的图片信息类列表
        self.image_info_group: List[List[ImageInfoBase]] = None
        # 转换后的漫画信息列表
        self.comic_info_group: List[List[ComicInfoBase]] = None
        # 漫画数据库
        self.db_comic_info: DBComicInfo = None
        # 图片数据库
        self.db_image_info: DBImageInfo = None

    def set_image_info_group(self, image_info_group: List[List[ImageInfoBase]]):
        self.image_info_group = image_info_group

    def set_db_comic_info(self, db_comic_info: DBComicInfo):
        self.db_comic_info = db_comic_info

    def set_db_image_info(self, db_image_info: DBImageInfo):
        self.db_image_info = db_image_info

    def get_comic_info_group(self):
        return self.comic_info_group

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '将图片信息类组转换为对应的漫画路径组')
        # 图片信息类组格式：[[ImageInfo1, ImageInfo2, ImageInfo3], [ImageInfo4, ImageInfo5, ImageInfo6]]
        # 先转换为漫画路径格式
        print('转换图片信息类为漫画路径')
        comic_path_group = []
        for group in self.image_info_group:
            p_group = set()
            for image_info in group:
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
                if comic_info:
                    ci_group.append(comic_info)
            self.comic_info_group.append(ci_group)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '完成将图片信息类组转换为对应的漫画路径组')
        self.finished()
