# 子线程-搜索符合条件的文件夹类/压缩文件类漫画

import os

import lzytools.file
import natsort

from common import function_file, function_archive
from thread.thread_pattern import ThreadPattern


class ThreadSearchComic(ThreadPattern):
    """子线程-搜索符合条件的文件夹类/压缩文件类漫画"""

    def __init__(self):
        super().__init__()
        self.step_index = 1
        self.step_info = '搜索漫画'

        # 搜素列表
        self.search_list = []
        # 搜索到的漫画清单
        self.comics_path = []

        # 漫画识别条件
        self.pages_lower_limit = 4  # 漫画页数下限
        self.is_check_archive = False  # 是否识别压缩文件类漫画
        self.is_allow_other_filetypes = False  # 是否允许包含其他类型的文件

    def get_comics_path(self):
        """获取搜索到的漫画清单"""
        return self.comics_path

    def set_search_list(self, paths: list):
        """设置需要搜索的路径"""
        self.search_list = natsort.os_sorted(paths)

    def set_pages_lower_limit(self, limit: int):
        """设置漫画页数下限"""
        self.pages_lower_limit = limit

    def set_is_check_archive(self, is_enable: bool):
        """设置是否识别压缩文件类漫画"""
        self.is_check_archive = is_enable

    def set_is_allow_other_filetypes(self, is_enable: bool):
        """设置是否允许包含其他类型的文件"""
        self.is_allow_other_filetypes = is_enable

    def clear(self):
        """清空数据"""
        self.search_list.clear()
        self.comics_path.clear()

    def run(self):
        super().run()
        print('开始子线程 搜索漫画')
        # 剔除搜索路径中包含的子路径
        search_list = lzytools.file.remove_subpaths(self.search_list)

        # 提取搜索列表中的所有文件路径
        files_in_search_list = lzytools.file.get_files_in_paths(search_list)

        # 将提取的文件按父目录写入一个字典
        dir_dict = dict()
        for file in files_in_search_list:
            dir_ = os.path.dirname(file)
            if dir_ not in dir_dict:
                dir_dict[dir_] = set()
            dir_dict[dir_].add(file)

        # 筛选符合条件的漫画
        comics_path = set()
        # 搜索文件夹类漫画
        for dir_, files in dir_dict.items():
            if not os.path.exists(dir_):
                continue
            # 如果文件夹中存在子文件夹，则不视为漫画
            if len(os.listdir(dir_)) != len(files):
                continue
            # 提取文件夹中的所有图片
            images = [i for i in files if function_file.is_image_by_filename(i)]
            # 检查图片数量下限
            if len(images) < self.pages_lower_limit:
                continue
            # 检查是否允许包含其他类型的文件
            if not self.is_allow_other_filetypes and len(images) != len(files):
                continue
            comics_path.add(dir_)

        # 搜索压缩文件类漫画
        if self.is_check_archive:
            # 提取文件列表中的压缩文件
            archives = [i for i in files_in_search_list if function_archive.is_archive_by_filename(i)]
            for archive in archives:
                if not os.path.exists(archive):
                    continue
                # 提取压缩文件中的所有图片
                images = function_archive.get_images_in_archive(archive)
                # 检查图片数量下限
                if len(images) < self.pages_lower_limit:
                    continue
                # 检查是否允许包含其他类型的文件
                # if not self.is_allow_other_filetypes and len(images) != len(files):
                #     continue
                comics_path.add(archive)

        # 赋值变量
        self.comics_path = natsort.os_sorted(list(comics_path))

        # 结束后发送信号
        print('搜索到的漫画', self.comics_path)
        print('结束子线程 搜索漫画')
        self.finished()
