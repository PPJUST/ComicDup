# 子线程-分析漫画信息
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List

import natsort

from common.class_comic import ComicInfoBase, FolderComicInfo, ArchiveComicInfo
from common.class_runtime import TypeRuntimeInfo
from thread.thread_pattern import ThreadPattern


class ThreadAnalyseComicInfo(ThreadPattern):
    """子线程-分析漫画信息"""

    def __init__(self):
        super().__init__()
        self.step_index = 2
        self.step_info = '分析漫画信息'

        # 用于分析的漫画列表
        self.comics: List[str] = []
        # 分析得到的漫画信息字典
        self.comic_info_dict: Dict[str, ComicInfoBase] = dict()

    def initialize(self):
        """初始化"""
        super().initialize()
        self.comics = []
        self.comic_info_dict = dict()

    def get_comic_info_dict(self):
        """获取漫画信息类字典"""
        return self.comic_info_dict

    def set_comics(self, comics: list):
        self.comics = natsort.os_sorted(comics)

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始分析漫画信息')
        print(f'启动线程池 分析漫画信息，线程数量：{self.max_workers}')

        total = len(self.comics)
        if total == 0:
            self._finish_analyse()
            return

        # 使用线程池进行并发处理
        completed_count = 0
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有任务
            futures = {executor.submit(self._analyse, comic_path): comic_path for comic_path in self.comics}

            # 处理完成的任务
            for future in as_completed(futures):
                if self._is_stop:
                    executor.shutdown(wait=False, cancel_futures=True)
                    break

                comic_path = futures[future]
                try:
                    comic_info = future.result()
                    self.comic_info_dict[comic_path] = comic_info
                    completed_count += 1
                    self.SignalRate.emit(f'{completed_count}/{total}')
                except Exception as e:
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, f'分析{comic_path}失败：{str(e)}')

            self._finish_analyse()

    def _finish_analyse(self):
        """完成分析后的处理"""
        print('结束线程池 分析漫画信息')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '全部漫画信息完成分析')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'共完成分析{len(self.comic_info_dict)}本漫画')
        self.finished()

    def _analyse(self, comic_path: str):
        """分析漫画信息（供线程池调用）"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'开始分析：{comic_path}')
        # 根据不同漫画类型，实例化不同的漫画信息类
        if os.path.isdir(comic_path):
            comic_info = FolderComicInfo(comic_path)
        elif os.path.isfile(comic_path):
            comic_info = ArchiveComicInfo(comic_path)
        else:
            raise Exception(f'{comic_path} 类型错误')

        return comic_info
