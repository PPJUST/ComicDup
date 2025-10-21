# 子线程-保存漫画信息到数据库

from typing import List

from common.class_comic import ComicInfoBase
from common.class_runtime import TypeRuntimeInfo
from common.function_db_comic_info import DBComicInfo
from common.function_db_image_info import DBImageInfo
from thread.thread_pattern import ThreadPattern


class ThreadSaveComic(ThreadPattern):
    """子线程-保存漫画信息到数据库"""

    def __init__(self):
        super().__init__()
        self.step_index = 2
        self.step_info = '保存漫画信息到数据库'

        # 需要保存的漫画信息列表
        self.comic_info_list: List[ComicInfoBase] = []
        # 漫画数据库
        self.db_comic_info: DBComicInfo = None
        # 图片数据库
        self.db_image_info: DBImageInfo = None

    def set_comic_info_list(self, comic_info_list):
        self.comic_info_list = comic_info_list

    def set_db_comic_info(self, db_comic_info: DBComicInfo):
        self.db_comic_info = db_comic_info

    def set_db_image_info(self, db_image_info: DBImageInfo):
        self.db_image_info = db_image_info

    def get_comic_info_list(self):
        return self.comic_info_list

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '正在保存漫画信息到本地数据库')
        # 在保存漫画信息前，提取数据库中所有项目的(路径, 指纹)，用于判断漫画是否已经存在于数据库中
        # 提取数据库中所有项目的指纹，用于判断漫画是否已存在于数据库但本地文件已被移动
        db_fingerprint_list = self.db_comic_info.get_fingerprint_list()
        db_path_fingerprint_list = self.db_comic_info.get_path_fingerprint_list()
        for comic_info in self.comic_info_list:
            # 在保存漫画信息前，考虑已存在于数据库中的项目，具体逻辑参考流程图
            _check_tuple = (comic_info.filepath, comic_info.fingerprint)
            is_comic_exist_db = _check_tuple in db_path_fingerprint_list
            if not is_comic_exist_db:  # 不存在则新增
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'保存{comic_info.filename}到数据库')
                comic_info.save_preview_image()  # 新增前保存预览图
                self.db_comic_info.add(comic_info)
            else:
                is_comic_moved_db = comic_info.fingerprint in db_fingerprint_list  # 指纹存在，但是(路径, 指纹)不存在，则说明本地文件已经被移动
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
        self.finished()
