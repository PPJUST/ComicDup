from PySide6.QtCore import *

import satic_function


class ThreadCompareImage(QThread):
    signal_schedule_compare_image = Signal(str)
    signal_finished = Signal(list)

    def __init__(self):
        super().__init__()
        self.image_data_dict = dict()
        self.mode_ahash = 0
        self.mode_phash = 0
        self.mode_dhash = 0
        self.mode_ssim = 0

    def set_image_data_dict(self, image_data_dict=None):
        if image_data_dict is None:
            image_data_dict = dict()
        self.image_data_dict = image_data_dict

    def set_mode_compare(self, mode_ahash=0, mode_phash=0, mode_dhash=0, mode_ssim=0):
        self.mode_ahash = mode_ahash
        self.mode_phash = mode_phash
        self.mode_dhash = mode_dhash
        self.mode_ssim = mode_ssim

    def run(self):
        """传入数据字典，对比其中的图片，查找相似项"""
        similar_group_list = []  # 相似组列表 [(源文件1,源文件2), (...)...]
        all_image_list = list(self.image_data_dict.keys())
        total_group = len(all_image_list) - 1
        # 提取检查的图
        for index, key in enumerate(all_image_list[:-1]):  # 最后一张图不需要进行检查
            self.signal_schedule_compare_image.emit(f'{index + 1}/{total_group}')
            key_origin = self.image_data_dict[key]['origin_path']
            key_ahash = self.image_data_dict[key]['ahash']
            key_phash = self.image_data_dict[key]['phash']
            key_dhash = self.image_data_dict[key]['dhash']
            # 提取对比的图
            for compare in all_image_list[index + 1:]:  # 其后的所有图都需要对比
                compare_origin = self.image_data_dict[compare]['origin_path']
                compare_ahash = self.image_data_dict[compare]['ahash']
                compare_phash = self.image_data_dict[compare]['phash']
                compare_dhash = self.image_data_dict[compare]['dhash']
                # 检查是否为同一源文件，是则跳过
                if key_origin == compare_origin:
                    continue
                # 对比hash值
                similar_check = []  # 存放bool值，通过内部True的个数来判断是否为相似
                if self.mode_ahash:
                    if key_ahash is not None and compare_ahash is not None:
                        dist_ahash = satic_function.calc_two_hash_str_hamming_distance(key_ahash, compare_ahash)
                        if dist_ahash <= self.mode_ahash:
                            similar_check.append(True)
                        else:
                            similar_check.append(False)
                    else:
                        similar_check.append(False)

                if self.mode_phash:
                    if key_phash is not None and compare_phash is not None:
                        dist_phash = satic_function.calc_two_hash_str_hamming_distance(key_phash, compare_phash)
                        if dist_phash <= self.mode_phash:
                            similar_check.append(True)
                        else:
                            similar_check.append(False)
                    else:
                        similar_check.append(False)

                if self.mode_dhash:
                    if key_dhash is not None and compare_dhash is not None:
                        dist_dhash = satic_function.calc_two_hash_str_hamming_distance(key_dhash, compare_dhash)
                        if dist_dhash <= self.mode_dhash:
                            similar_check.append(True)
                        else:
                            similar_check.append(False)
                    else:
                        similar_check.append(False)
                # 判断hash对比结果
                if True in similar_check:
                    if self.mode_ssim:
                        ssim = satic_function.calc_images_ssim(key_origin, compare_origin)
                        if ssim >= self.mode_ssim:
                            similar_group_list.append((key_origin, compare_origin))
                    else:
                        similar_group_list.append((key_origin, compare_origin))
        # 处理相似组列表（去重、合并交集项）
        similar_group_list = satic_function.merge_intersecting_tuples(similar_group_list)

        self.signal_finished.emit(similar_group_list)
