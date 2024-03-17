# 子线程-分析漫画数据

from module import function_cache_comicdata, function_cache_thread
from module import function_config
from module.class_comic_data import ComicData
from thread.thread_model import ThreadModel


class ThreadAnalyseComicsData(ThreadModel):
    """子线程-分析漫画数据"""

    def __init__(self):
        super().__init__()
        self.step = '2/6 提取漫画数据'

    def run(self):
        super().run()
        # 获取设置
        extract_image_number = function_config.get_extract_image_number()
        comic_folders = function_cache_thread.read_comic_folders()
        archives = function_cache_thread.read_archives()
        all_files = comic_folders.union(archives)
        # 遍历文件夹
        comics_data = {}
        for index_rate, path in enumerate(all_files, start=1):
            if self.code_stop:
                break
            self.signal_rate.emit(f'{index_rate}/{len(all_files)}')
            comic_class = ComicData()
            comic_class.set_path(path)
            comic_class.set_calc_number(extract_image_number)
            comics_data[path] = comic_class
        # 保存到本地
        function_cache_comicdata.save_comics_data_pickle(comics_data)
        function_cache_comicdata.update_comics_data_pickle(comics_data)
        # 发送结束信号
        if self.code_stop:
            self.signal_stopped.emit()
        else:
            self.signal_finished.emit()
