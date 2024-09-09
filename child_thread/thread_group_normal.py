# 线程组 - 一般情况（正常流程，全部步骤依次完成）


from PySide6.QtCore import QObject, Signal

from child_thread.thread_analyse_comics_info import ThreadAnalyseComicsInfo
from child_thread.thread_calc_hash import ThreadCalcHash
from child_thread.thread_extract_comic import ThreadExtractComic
from child_thread.thread_match import ThreadMatch


class ThreadGroupNormal(QObject):
    """线程组 - 一般情况（正常流程，全部步骤依次完成）"""
    signal_step = Signal(str, name='当前步骤的名称')
    signal_rate = Signal(str, name='内部进度')
    signal_finished = Signal(object, name='结束')

    def __init__(self, parent=None):
        super().__init__(parent)
        # 提取符合条件的所有漫画文件夹和压缩包列表
        self.thread_extract_comic = ThreadExtractComic()
        self.thread_extract_comic.signal_finished.connect(self._start_thread_analyse_comics_info)
        self.thread_extract_comic.signal_step.connect(self.update_schedule_total)
        self.thread_extract_comic.signal_rate.connect(self.update_schedule_step)

        # 分析漫画信息
        self.thread_analyse_comics_info = ThreadAnalyseComicsInfo()
        self.thread_analyse_comics_info.signal_finished.connect(self._start_thread_calc_hash)
        self.thread_analyse_comics_info.signal_step.connect(self.update_schedule_total)
        self.thread_analyse_comics_info.signal_rate.connect(self.update_schedule_step)

        # 计算漫画中图片的hash
        self.thread_calc_hash = ThreadCalcHash()
        self.thread_calc_hash.signal_finished.connect(self._start_thread_match)
        self.thread_calc_hash.signal_step.connect(self.update_schedule_total)
        self.thread_calc_hash.signal_rate.connect(self.update_schedule_step)

        # 匹配图片hash，得到一个相似漫画组list
        self.thread_match = ThreadMatch()
        self.thread_match.signal_finished.connect(self.signal_finished.emit)
        self.thread_match.signal_step.connect(self.update_schedule_total)
        self.thread_match.signal_rate.connect(self.update_schedule_step)

    def start(self, folders: list):
        self._start_thread_extract_comic(folders)

    def stop(self):
        """设置子线程的停止参数"""
        self.thread_extract_comic.set_stop()
        self.thread_analyse_comics_info.set_stop()
        self.thread_calc_hash.set_stop()
        self.thread_match.set_stop()

    def _start_thread_extract_comic(self, folders: list):
        """启用子线程-提取漫画路径"""
        self.thread_extract_comic.set_folders(folders)
        self.thread_extract_comic.start()

    def _start_thread_analyse_comics_info(self, comics: list):
        """启用子线程-分析漫画信息"""
        self.thread_analyse_comics_info.set_comics(comics)
        self.thread_analyse_comics_info.start()

    def _start_thread_calc_hash(self, comics: list):
        """启用子线程-计算图片hash"""
        self.thread_calc_hash.set_comics(comics)
        self.thread_calc_hash.start()

    def _start_thread_match(self, image_info_dict: dict):
        """启用子线程-匹配图片hash"""
        self.thread_match.set_image_info_dict(image_info_dict)
        self.thread_match.start()

    def update_schedule_total(self, text: str):
        """更新总进度"""
        self.signal_step.emit(text)

    def update_schedule_step(self, text: str):
        """更新步骤进度"""
        self.signal_rate.emit(text)
