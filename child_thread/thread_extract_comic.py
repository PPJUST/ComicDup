# 子线程-提取符合规则的漫画文件夹/压缩包
import natsort

from child_thread.thread_pattern import ThreadPattern
from module import function_extract_comic, function_normal


class ThreadExtractComic(ThreadPattern):
    """提取符合规则的漫画文件夹/压缩包"""

    def __init__(self):
        super().__init__()
        self._step = '检查文件夹'
        self.dirpaths = []

    def set_folders(self, dirpaths: list):
        self.dirpaths = natsort.natsorted(dirpaths)

    def run(self):
        super().run()
        # 先剔除文件夹列表中的子文件夹
        dirpaths_filter = function_normal.filter_child_folder(self.dirpaths)
        # 遍历文件夹
        comics = set()
        for index, dirpath in enumerate(dirpaths_filter, start=1):
            if self._stop_code:
                break
            self.signal_rate.emit(f'{index}/{len(dirpaths_filter)}')
            comics_ = function_extract_comic.extract_comics(dirpath)
            comics.update(comics_)
        # 结束后重置参数
        self.dirpaths.clear()
        # 结束后发送信号
        self.finished(comics)
