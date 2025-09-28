# 子线程-分析漫画信息
from typing import Dict

import natsort

from common.class_comic import ComicInfo
from common.class_runtime import TypeRuntimeInfo
from thread.thread_pattern import ThreadPattern


class ThreadAnalyseComicInfo(ThreadPattern):
    """子线程-分析漫画信息"""

    def __init__(self):
        super().__init__()
        self.step_index = 2
        self.step_info = '分析漫画信息'

        # 漫画列表
        self.comics = []
        # 漫画信息字典
        self.comic_info_dict: Dict[str, ComicInfo] = dict()

    def get_comic_info_dict(self):
        """获取漫画信息类字典"""
        return self.comic_info_dict

    def set_comics(self, comics: list):
        self.comics = natsort.os_sorted(comics)

    def clear(self):
        """清空数据"""
        self.comics.clear()
        self.comic_info_dict.clear()

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始分析漫画信息')
        print('启动子线程 分析漫画信息')
        # 遍历列表，提取信息
        for index, comic in enumerate(self.comics, start=1):
            if self._is_stop:
                break
            self.SignalRate.emit(f'{index}/{len(self.comics)}')
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'开始分析：{comic}')
            comic_info = ComicInfo(comic)
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'完成分析：{comic}')
            self.comic_info_dict[comic] = comic_info

        # 结束后发送信号
        print('提取的漫画信息', self.comic_info_dict)
        print('结束子线程 分析漫画信息')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '全部漫画信息完成分析')
        self.finished()
