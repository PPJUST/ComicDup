import os

import natsort
from PySide6.QtCore import *


class ThreadCheckFolder(QThread):
    signal_schedule_check_folder = Signal(str)

    def __init__(self):
        super().__init__()
        self.dirpath_list = []
        self.comic_dir_dict = dict()  # 格式：{文件夹路径:(排序后的内部图片路径), ...}
        self.archive_set = set()  # 格式：(压缩包路径, ...)

    def set_dirpath_list(self, dirpath_list):
        self.dirpath_list = set(dirpath_list)

    def run(self):
        total_folder = len(self.dirpath_list)
        check_dir_dict = dict()  # {文件夹路径:{'dir':set(), 'image':set(), 'archive':set()}...}
        image_suffix = ['.jpg', '.png', 'webp']  # 取后4位
        archive_suffix = ['zip', 'rar', '.7z']  # 取后3位
        # 遍历所有文件，找出需要的文件
        for index, checkpath in enumerate(self.dirpath_list, start=1):
            self.signal_schedule_check_folder.emit(f'{index}/{total_folder}')
            for dir_path, dirnames, filenames in os.walk(checkpath):
                # 找出所有文件夹
                for dirname in dirnames:
                    dirpath = os.path.normpath(os.path.join(dir_path, dirname))
                    # 文件夹写入字典
                    if dirpath not in check_dir_dict:
                        check_dir_dict[dirpath] = {'dir': set(), 'image': set(), 'archive': set()}
                    # 父文件夹写入字典，并添加子文件夹数据
                    parent_dir = os.path.split(dirpath)[0]
                    if parent_dir not in check_dir_dict:
                        check_dir_dict[parent_dir] = {'dir': set(), 'image': set(), 'archive': set()}
                    check_dir_dict[parent_dir]['dir'].add(dirpath)
                # 找出所有文件
                for filename in filenames:
                    filepath = os.path.normpath(os.path.join(dir_path, filename))
                    dirpath = os.path.split(filepath)[0]
                    if dirpath not in check_dir_dict:
                        check_dir_dict[dirpath] = {'dir': set(), 'image': set(), 'archive': set()}
                    """改用后缀名判断，加快速度但是不精确
                    if is_image(filepath):
                        check_dir_dict[dirpath]['image'].add(filepath)
                    elif is_archive(filepath):
                        check_dir_dict[dirpath]['archive'].add(filepath)
                    """
                    if filepath[-4:].lower() in image_suffix:
                        check_dir_dict[dirpath]['image'].add(filepath)
                    elif filepath[-3:].lower() in archive_suffix:
                        check_dir_dict[dirpath]['archive'].add(filepath)

        # 检查字典，筛选出需要的压缩包和文件夹
        final_archive_set = set()
        final_comic_dir_dict = dict()  # {文件夹路径:[内部所有图片文件路径]...}
        for key_dirpath, data_dict in check_dir_dict.items():
            value_dir = data_dict['dir']
            value_image = data_dict['image']
            value_archive = data_dict['archive']
            if value_archive:  # 内部有压缩包则不视为漫画文件夹
                final_archive_set.update(value_archive)
                continue
            elif value_dir:  # 内部有文件夹则不视为漫画文件夹
                continue
            else:
                if len(value_image) < 4:  # 内部图片数<4则不视为漫画文件夹
                    continue
                sorted_image = natsort.natsorted(list(value_image))
                final_comic_dir_dict[key_dirpath] = sorted_image

        self.comic_dir_dict = final_comic_dir_dict
        self.archive_set = final_archive_set

    def get_result(self):
        return self.comic_dir_dict, self.archive_set
