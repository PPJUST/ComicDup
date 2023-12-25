import os

import natsort
from PySide6.QtCore import *

from satic_function import extract_image_from_archive, get_folder_size


class ThreadExtractImage(QThread):
    signal_schedule_extract_image = Signal(str)
    signal_finished = Signal(dict, dict)

    def __init__(self):
        super().__init__()
        self.comic_dir_dict = dict()
        self.archive_set = set()
        self.need_image_number = 1

    def set_comic_dir_dict(self, comic_dir_dict):
        self.comic_dir_dict = comic_dir_dict

    def set_archive_set(self, archive_set):
        self.archive_set = archive_set

    def set_need_image_number(self, need_image_number):
        self.need_image_number = need_image_number

    def run(self):
        image_data_dict = dict()  # 图片对应的数据字典 {图片文件:{origin_path:...}, ...}
        comic_data_dict = dict()  # 源文件对应的数据字典 {源文件/文件夹:{preview:..., filetype/image_number/filesize}, ...}

        total_dir = len(self.comic_dir_dict)
        total_archive = len(self.archive_set)

        # 解压压缩包中的指定数量图片文件，并写入字典数据
        for index, archivefile in enumerate(self.archive_set, start=1):
            self.signal_schedule_extract_image.emit(f'{index}/{total_archive}')
            extract_image_list, image_count_archive = extract_image_from_archive(archivefile, self.need_image_number)
            if extract_image_list:
                # 写入图片对应的数据字典
                for i in extract_image_list:
                    if i not in image_data_dict:
                        image_data_dict[i] = dict()
                    image_data_dict[i]['origin_path'] = archivefile

                # 写入源文件对应的数据字典
                if archivefile not in comic_data_dict:
                    comic_data_dict[archivefile] = dict()
                comic_data_dict[archivefile]['preview'] = natsort.natsorted(list(extract_image_list))[0]
                comic_data_dict[archivefile]['filetype'] = 'archive'
                comic_data_dict[archivefile]['image_number'] = image_count_archive
                comic_data_dict[archivefile]['filesize'] = os.path.getsize(archivefile)

        # 获取文件夹中的指定数量图片文件，并写入字典数据
        index = 0
        for dirpath, image_list in self.comic_dir_dict.items():
            index += 1
            self.signal_schedule_extract_image.emit(f'{index}/{total_dir}')
            image_count_in_dir = len(image_list)
            # 提取指定数量的图片路径
            calc_image_list = []
            for i in range(self.need_image_number):
                calc_image_list.append(image_list[i])
            # 写入图片对应的数据字典
            for i in calc_image_list:
                image_data_dict[i] = dict()
                image_data_dict[i]['origin_path'] = dirpath

            # 写入源文件对应的数据字典
            if dirpath not in comic_data_dict:
                comic_data_dict[dirpath] = dict()
            comic_data_dict[dirpath]['preview'] = natsort.natsorted(calc_image_list)[0]
            comic_data_dict[dirpath]['filetype'] = 'folder'
            comic_data_dict[dirpath]['image_number'] = image_count_in_dir
            comic_data_dict[dirpath]['filesize'] = get_folder_size(dirpath)

        self.signal_finished.emit(comic_data_dict, image_data_dict)
