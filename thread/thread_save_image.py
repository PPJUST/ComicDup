# 子线程-保存图片信息到数据库

from typing import List

from common.class_image import ImageInfoBase
from common.class_runtime import TypeRuntimeInfo
from common.function_db_image_info import DBImageInfo
from thread.thread_pattern import ThreadPattern


class ThreadSaveImage(ThreadPattern):
    """子线程-保存图片信息到数据库"""

    def __init__(self):
        super().__init__()
        self.step_index = 2
        self.step_info = '保存图片信息到数据库'

        # 需要保存的漫画信息列表
        self.image_info_list: List[ImageInfoBase] = None
        # 图片数据库
        self.db_image_info: DBImageInfo = None

    def set_image_info_list(self, image_info_list):
        self.image_info_list = image_info_list

    def set_db_image_info(self, db_image_info: DBImageInfo):
        self.db_image_info = db_image_info

    def get_image_info_list(self):
        return self.image_info_list

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '正在保存图片信息到本地数据库')
        for image_info in self.image_info_list:
            self.db_image_info.add(image_info)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '完成保存图片信息到本地数据库')
        self.finished()
