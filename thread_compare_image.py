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

    def order_image_data_dict_by_count(self):
        """根据哈希值中0个数排序整个字典"""
        image_path_list = []
        phash_count0_list = []
        for image_path, image_data in self.image_data_dict.items():
            phash_count0 = image_data['phash_count0']
            image_path_list.append(image_path)
            phash_count0_list.append(phash_count0)

        join_list = zip(image_path_list, phash_count0_list)
        join_list_sorted = sorted(join_list, key=lambda x: x[1])
        image_path_list_sorted = [i[0] for i in join_list_sorted]

        image_data_dict_sorted = {}
        for key in image_path_list_sorted:
            image_data_dict_sorted[key] = self.image_data_dict[key]
        self.image_data_dict = image_data_dict_sorted

    def run(self):
        """传入数据字典，对比其中的图片，查找相似项"""
        similar_group_list = []  # 相似组列表 [(源文件1,源文件2), (...)...]
        all_image_list = list(self.image_data_dict.keys())
        total_group = len(all_image_list) - 1
        # 提取检查的图
        for index, key in enumerate(all_image_list[:-1]):  # 最后一张图不需要进行检查
            self.signal_schedule_compare_image.emit(f'{index + 1}/{total_group}')
            key_origin = self.image_data_dict[key]['origin_path']
            key_phash = self.image_data_dict[key]['phash']
            key_phash_count0 = self.image_data_dict[key]['phash_count0']
            # 提取对比的图
            for compare in all_image_list[index + 1:]:  # 其后的所有图都需要对比
                compare_origin = self.image_data_dict[compare]['origin_path']
                compare_phash = self.image_data_dict[compare]['phash']
                compare_phash_count0 = self.image_data_dict[compare]['phash_count0']
                # 检查phash中0的个数，如果超限则提前结束循环
                limit_count = self.mode_phash / 2  # 限制为选定的哈希值差额/2（0/1差异各占一半）
                try:
                    diff_count = compare_phash_count0 - key_phash_count0  # 数据字典已经按count值升序排序
                except TypeError:  # 防止None相减 TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
                    break
                if diff_count > limit_count:
                    break

                # 检查是否为同一源文件，是则跳过
                if key_origin == compare_origin:
                    continue
                # 对比hash值
                similar_check = []  # 存放bool值，通过内部True的个数来判断是否为相似
                if self.mode_phash:
                    if key_phash is not None and compare_phash is not None:
                        dist_phash = satic_function.calc_two_hash_str_hamming_distance(key_phash, compare_phash)
                        if dist_phash <= self.mode_phash:
                            similar_check.append(True)
                        else:
                            similar_check.append(False)
                    else:
                        similar_check.append(False)

                # 判断hash对比结果
                if True in similar_check:
                    if self.mode_ssim:
                        ssim = satic_function.calc_images_ssim(key, compare)
                        if ssim >= self.mode_ssim:
                            similar_group_list.append((key_origin, compare_origin))
                    else:
                        similar_group_list.append((key_origin, compare_origin))
        # 处理相似组列表（去重、合并交集项）
        similar_group_list = satic_function.merge_intersecting_tuples(similar_group_list)

        self.signal_finished.emit(similar_group_list)


""" 2024.01.08调整 只使用phash，原有run函数弃用
    def run(self):
        # 传入数据字典，对比其中的图片，查找相似项
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
"""
