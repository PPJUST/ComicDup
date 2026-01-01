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
        print('正在保存漫画信息到本地数据库')
        db_fingerprint_list = self.db_comic_info.get_fingerprint_list()
        print('提取数据库指纹', db_fingerprint_list)
        db_path_fingerprint_list = self.db_comic_info.get_path_fingerprint_list()
        print('提取数据库指纹+路径', db_path_fingerprint_list)
        for comic_info in self.comic_info_list:
            # 在保存漫画信息前，考虑已存在于数据库中的项目
            _check_tuple = (comic_info.filepath, comic_info.fingerprint)
            is_comic_exist_db = comic_info.fingerprint in db_fingerprint_list
            if is_comic_exist_db:  # 存在则分情况处理
                is_need_add = _check_tuple not in db_path_fingerprint_list  # 如果指纹存在，但是(路径, 指纹)不存在，则可能是新增的相同漫画或旧漫画已经被移动
                if is_need_add:
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice,
                                                f'{comic_info.filename}可能已被移动，尝试更新数据库')
                    comic_path_deleted = self.db_comic_info.update_comic_moved(comic_info)
                    if comic_path_deleted:  # 如果返回了删除的漫画路径，则说明该漫画已被移动，同步移动图片数据库中的对应项
                        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'更新图片数据库中对应的漫画数据')
                        self.db_image_info.update_belong_comic_moved(comic_info.fingerprint,
                                                                     old_comic_path=comic_path_deleted,
                                                                     new_comic_path=comic_info.filepath)
                    else:  # 否则，为新增了相同漫画的情形
                        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'保存{comic_info.filename}到数据库')
                        self.db_comic_info.add(comic_info)
                else:  # 已存在且未移动则跳过
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'{comic_info.filename}已存在于数据库，跳过更新')
                    continue
            else:  # 不存在则新增
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'保存{comic_info.filename}到数据库')
                self.db_comic_info.add(comic_info)

        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '完成保存漫画信息到本地数据库')
        self.finished()

    def save_comic_info_without_infotips(self, comic_info: ComicInfoBase):
        """保存漫画信息类，但不进行提示"""
        print('保存漫画信息类，但不进行提示')
        # 提取数据库中所有项目的指纹，用于判断漫画是否已存在于数据库但本地文件已被移动
        db_fingerprint_list = self.db_comic_info.get_fingerprint_list()
        db_path_fingerprint_list = self.db_comic_info.get_path_fingerprint_list()
        # 在保存漫画信息前，考虑已存在于数据库中的项目
        _check_tuple = (comic_info.filepath, comic_info.fingerprint)
        is_comic_exist_db = comic_info.fingerprint in db_fingerprint_list
        if is_comic_exist_db:  # 存在则分情况处理
            is_need_add = _check_tuple not in db_path_fingerprint_list  # 如果指纹存在，但是(路径, 指纹)不存在，则可能是新增的相同漫画或旧漫画已经被移动
            if is_need_add:
                comic_path_deleted = self.db_comic_info.update_comic_moved(comic_info)
                if comic_path_deleted:  # 如果返回了删除的漫画路径，则说明该漫画已被移动，同步移动图片数据库中的对应项
                    self.db_image_info.update_belong_comic_moved(comic_info.fingerprint,
                                                                 old_comic_path=comic_path_deleted,
                                                                 new_comic_path=comic_info.filepath)
                else:  # 否则，为新增了相同漫画的情形
                    self.db_comic_info.add(comic_info)
            else:  # 已存在且未移动则跳过
                pass
        else:  # 不存在则新增
            self.db_comic_info.add(comic_info)
