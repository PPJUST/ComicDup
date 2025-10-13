# 子线程-刷新漫画信息数据库

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

import natsort

from common import function_archive
from common.class_comic import FolderComicInfo, ArchiveComicInfo, ComicInfoBase
from common.class_runtime import TypeRuntimeInfo
from common.function_db_comic_info import DBComicInfo
from thread.thread_pattern import ThreadPattern


class ThreadRefreshComicDB(ThreadPattern):
    """子线程-刷新漫画信息数据库"""

    def __init__(self):
        super().__init__()
        self.step_index = 1
        self.step_info = '刷新漫画信息数据库'

        # 漫画路径列表
        self.comics_path = []
        # 漫画信息数据库对象
        self.comics_db: DBComicInfo = None

    def set_comics_path(self, comics_path: list):
        """设置需要更新的漫画路径列表"""
        self.comics_path = natsort.os_sorted(comics_path)

    def set_comic_db(self, comics_db: DBComicInfo):
        """设置漫画信息数据库对象"""
        self.comics_db = comics_db

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始刷新漫画信息数据库')
        print('开始子线程 刷新漫画信息数据库')

        # 分类漫画类型，拆分为文件夹类和压缩文件类
        folder_comics = []
        archive_comics = []
        for comic_path in self.comics_path:
            if os.path.isdir(comic_path):
                folder_comics.append(comic_path)
            elif os.path.isfile(comic_path) and function_archive.is_archive_by_filename(comic_path):
                archive_comics.append(comic_path)
        comics = folder_comics + archive_comics

        total = len(comics)
        if total == 0:
            return

        comic_info_dict = dict()
        # 使用线程池进行并发处理
        completed_count = 0
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有任务
            futures = {executor.submit(self._analyse, comic_path): comic_path for comic_path in comics}

            # 处理完成的任务
            for future in as_completed(futures):
                if self._is_stop:
                    executor.shutdown(wait=False, cancel_futures=True)
                    break

                comic_path = futures[future]
                try:
                    comic_info = future.result()
                    comic_info_dict[comic_path] = comic_info
                    completed_count += 1
                except Exception as e:
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, f'分析{comic_path}失败：{str(e)}')

        self.update_db(list(comic_info_dict.values()))

    def update_db(self, comic_info_list: List[ComicInfoBase]):
        """更新数据库"""
        for comic_info in comic_info_list:
            self.comics_db.refresh(comic_info)

    def _analyse(self, comic_path: str):
        """分析漫画信息（供线程池调用）"""
        # 根据不同漫画类型，实例化不同的漫画信息类
        if os.path.isdir(comic_path):
            comic_info = FolderComicInfo(comic_path)
        elif os.path.isfile(comic_path):
            comic_info = ArchiveComicInfo(comic_path)
        else:
            raise Exception(f'{comic_path} 类型错误')

        return comic_info
