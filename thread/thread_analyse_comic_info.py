# 子线程-分析漫画信息
from typing import Dict

import natsort

from common.class_comic import ComicInfo
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
        # 遍历列表，提取信息
        for index, comic in enumerate(self.comics, start=1):
            if self._is_stop:
                break
            self.SignalRate.emit(f'{index}/{len(self.comics)}')
            comic_info = ComicInfo(comic)
            self.comic_info_dict[comic] = comic_info

        # 保存到本地缓存中
        # 备忘录

        # 结束后发送信号
        self.finished()
