import os

import natsort
from PySide6.QtCore import *

import satic_function
from thread_check_folder import CheckFolderQthread
from thread_compare_image import CompareImageQthread


class CompareQthread(QThread):
    signal_compare_result = Signal(list, dict)  # 发送相似组结果列表
    signal_stop = Signal()  # 发送停止信号（被终止或完成）
    signal_schedule = Signal(str, str)  # 发送进度信息（类型str，进度文本str）

    def __init__(self):
        super().__init__()
        # 设置初始变量
        self.check_folder_list = None
        self.need_image_number = None
        self.mode_ahash = None
        self.mode_phash = None
        self.mode_dhash = None
        self.mode_ssim = None
        self.stop_code = False

    def reset_var(self):
        self.check_folder_list = None
        self.need_image_number = None
        self.mode_ahash = None
        self.mode_phash = None
        self.mode_dhash = None
        self.mode_ssim = None
        self.stop_code = False

    def set_check_folder_list(self, check_folder_list):
        self.check_folder_list = check_folder_list

    def set_need_image_number(self, image_number):
        self.need_image_number = image_number

    def set_mode_ahash(self, mode_ahash):
        self.mode_ahash = mode_ahash

    def set_mode_phash(self, mode_phash):
        self.mode_phash = mode_phash

    def set_mode_dhash(self, mode_dhash):
        self.mode_dhash = mode_dhash

    def set_mode_ssim(self, mode_ssim):
        self.mode_ssim = mode_ssim

    def set_stop_code(self):
        self.stop_code = True

    def run(self):
        """正式执行"""
        """
        第1步
        """
        self.signal_schedule.emit('步骤', '1/4 检查文件夹')
        # 提取文件夹中符合要求的文件夹、压缩包
        check_folder = CheckFolderQthread()
        check_folder.set_dirpath_list(self.check_folder_list)
        check_folder.signal_schedule_check_folder.connect(self.send_signal_index)
        check_folder.start()
        check_folder.wait()
        comic_dir_dict, archive_set = check_folder.get_result()

        """
        第2步
        """
        # 设置对应的字典，格式为{图片文件:{源文件:..., hash值:...}...}
        image_data_dict = dict()  # 图片对应的数据字典
        origin_data_dict = dict()  # 源文件对应的数据字典
        total_dir = len(comic_dir_dict)
        total_archive = len(archive_set)
        self.signal_schedule.emit('步骤', '2/4 提取图片')
        # 解压压缩包中的指定数量图片文件，并写入字典数据
        for index, archivefile in enumerate(archive_set, start=1):
            self.send_signal_index(f'{index}/{total_archive}')
            if self.stop_code:
                return self.signal_stop.emit()
            extract_image_list, image_count_archive = satic_function.extract_image_from_archive(archivefile,
                                                                                                self.need_image_number)
            if extract_image_list:  # 如果压缩包中有特殊字符，则返回的列表为空
                # 写入图片对应的数据字典
                for i in extract_image_list:
                    if i not in image_data_dict:
                        image_data_dict[i] = dict()
                    image_data_dict[i]['origin_path'] = archivefile

                # 写入源文件对应的数据字典
                if archivefile not in origin_data_dict:
                    origin_data_dict[archivefile] = dict()
                origin_data_dict[archivefile]['preview'] = natsort.natsorted(list(extract_image_list))[0]
                origin_data_dict[archivefile]['filetype'] = 'archive'
                origin_data_dict[archivefile]['image_number'] = image_count_archive
                origin_data_dict[archivefile]['filesize'] = os.path.getsize(archivefile)
        # 获取文件夹中的指定数量图片文件，并写入字典数据
        index = 0
        for dirpath, image_list in comic_dir_dict.items():
            index += 1
            self.send_signal_index(f'{index}/{total_dir}')
            if self.stop_code:
                return self.signal_stop.emit()
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
            if dirpath not in origin_data_dict:
                origin_data_dict[dirpath] = dict()
            origin_data_dict[dirpath]['preview'] = natsort.natsorted(calc_image_list)[0]
            origin_data_dict[dirpath]['filetype'] = 'folder'
            origin_data_dict[dirpath]['image_number'] = image_count_in_dir
            origin_data_dict[dirpath]['filesize'] = satic_function.get_folder_size(dirpath)

        """
        第3.1步
        """
        self.signal_schedule.emit('步骤', '3/4 提取图片特征缓存')
        # 提取图片特征缓存
        file_cache_data = satic_function.check_hash_cache()

        """
        第3.2步
        """
        self.signal_schedule.emit('步骤', '3/4 计算图片特征')
        # 计算图片hash值
        image_data_dict_copy = image_data_dict.copy()
        total_data = len(image_data_dict)
        for index, image in enumerate(image_data_dict):
            self.send_signal_index(f'{index}/{total_data}')
            if self.stop_code:
                return self.signal_stop.emit()
            hash_dict = {'ahash': None, 'phash': None, 'dhash': None}
            # 提取缓存中已有的hash数据
            origin_path = image
            cache_ahash, cache_phash, cache_dhash = None, None, None
            if origin_path in file_cache_data:
                cache_ahash = file_cache_data[origin_path]['ahash']
                cache_phash = file_cache_data[origin_path]['phash']
                cache_dhash = file_cache_data[origin_path]['dhash']
            if self.mode_ahash:
                if cache_ahash:
                    hash_dict['ahash'] = cache_ahash
                else:
                    hash_dict['ahash'] = satic_function.get_image_attr(image, mode_hash='ahash')
            if self.mode_phash:
                if cache_phash:
                    hash_dict['phash'] = cache_phash
                else:
                    hash_dict['phash'] = satic_function.get_image_attr(image, mode_hash='phash')
            if self.mode_dhash:
                if cache_dhash:
                    hash_dict['dhash'] = cache_dhash
                else:
                    hash_dict['dhash'] = satic_function.get_image_attr(image, mode_hash='dhash')
            image_data_dict_copy[image].update(hash_dict)
        image_data_dict = image_data_dict_copy

        """
        第3.3步
        """
        self.signal_schedule.emit('步骤', '3/4 保存图片特征')
        # 保存图片特征（只保存源文件为文件夹的图片数据）
        save_cache_data = {}  # {源文件路径:{'filesize':int, 'ahash':'str', ...}...}
        for image in image_data_dict:
            origin_path = image_data_dict[image]['origin_path']
            if os.path.isdir(origin_path):
                filesize = os.path.getsize(image)
                ahash = image_data_dict[image]['ahash']
                phash = image_data_dict[image]['phash']
                dhash = image_data_dict[image]['dhash']
                save_cache_data[image] = {'filesize': filesize, 'ahash': ahash, 'phash': phash, 'dhash': dhash}
        satic_function.update_hash_cache(save_cache_data)

        """
        第4步
        """
        self.signal_schedule.emit('步骤', '4/4 对比图片特征')
        # 对比hash值，查找相似项
        compare_image = CompareImageQthread()
        compare_image.set_args(image_data_dict, mode_ahash=self.mode_ahash,
                               mode_phash=self.mode_phash,
                               mode_dhash=self.mode_dhash, mode_ssim=self.mode_ssim)
        compare_image.signal_schedule_compare_image.connect(self.send_signal_index)
        compare_image.start()
        compare_image.wait()
        similar_group_list = compare_image.get_result()

        self.signal_schedule.emit('步骤', '-/- 结束')
        self.signal_compare_result.emit(similar_group_list, origin_data_dict)
        self.signal_stop.emit()

    def send_signal_index(self, text):
        """子进度"""
        self.signal_schedule.emit('子进度', text)
