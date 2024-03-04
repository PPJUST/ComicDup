# 子线程-检查文件夹，筛选出符合要求的漫画文件夹/压缩包

from module import function_cache_thread
from module import function_comic
from module import function_config
from thread.thread_model import ThreadModel


class ThreadCheckFolder(ThreadModel):
    """子线程-检查文件夹，筛选出符合要求的漫画文件夹/压缩包"""

    def __init__(self):
        super().__init__()
        self.step = '1/6 检查文件夹'
        self.check_folders = None

    def run(self):
        super().run()
        # 获取设置
        if self.check_folders:
            check_folders = self.check_folders
        else:
            check_folders = function_config.get_select_folders()
        # 遍历文件夹
        all_comic_folders = set()
        all_archives = set()
        for index_rate, dirpath in enumerate(check_folders, start=1):
            if self.code_stop:
                break
            self.signal_rate.emit(f'{index_rate}/{len(check_folders)}')
            comic_folders, archives = function_comic.filter_comic_folder_and_archive(dirpath)
            all_comic_folders.update(comic_folders)
            all_archives.update(archives)
        # 保存到本地
        function_cache_thread.save_comic_folders(all_comic_folders)
        function_cache_thread.save_archives(all_archives)
        # 重置参数
        self.check_folders = None
        # 发送结束信号
        if self.code_stop:
            self.signal_stopped.emit()
        else:
            self.signal_finished.emit()
