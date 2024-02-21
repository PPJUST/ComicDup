# 进行相似比较的子线程
import os

from PySide6.QtCore import QThread, Signal

from module import function_cache_hash
from module import function_cache_similargroup
from module import function_config
from module import function_hash
from module import function_normal
from module import function_ssim


class ThreadCompareCache(QThread):
    """对缓存数据进行相似比较的子线程"""
    signal_start_thread = Signal()
    signal_schedule_step = Signal(str)
    signal_schedule_rate = Signal(str)
    signal_finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        # 获取设置
        self.signal_start_thread.emit()
        threshold_ssim = function_config.get_threshold_ssim()
        threshold_hamming_distance = function_config.get_threshold_hash()
        mode_hash = function_config.get_mode_hash()
        mode_ssim = function_config.get_mode_ssim()

        # 读取本地hash缓存(读取到的数据不考虑path是否已经失效)
        cache_image_data_dict = function_cache_hash.read_hash_cache()

        # 向dict中增加键值对hash_count0，并按该key升序排列，最后进行查重（统计hash中0的个数，用于确定需要对比的图片范围）
        # 先向字典中添加hash_count0键
        cache_image_data_dict = function_hash.add_count_key_to_dict(cache_image_data_dict, mode_hash)

        self.signal_schedule_step.emit('1/1 相似匹配')
        # 再遍历需要匹配的图片列表
        similar_groups = []  # 全部的相似组列表（漫画路径）
        index_rate = 0
        compare_image_data_dict = cache_image_data_dict.copy()
        for image, hash_dict in cache_image_data_dict.items():
            index_rate += 1
            self.signal_schedule_rate.emit(f'{index_rate}/{len(cache_image_data_dict)}')
            if not os.path.exists(image):
                continue
            current_dict = {image: hash_dict}
            compare_image_data_dict.pop(image)  # 每次都删除当前图片项，避免重复对比
            similar_hash_group = function_hash.filter_similar_hash_group(current_dict, compare_image_data_dict,
                                                                         threshold_hamming_distance)

            if mode_ssim:  # 使用ssim再次筛选
                similar_hash_group_temp = similar_hash_group.copy()
                for compare_image in similar_hash_group_temp:
                    ssim = function_ssim.calc_images_ssim(image, compare_image)
                    if ssim < threshold_ssim:
                        similar_hash_group.remove(compare_image)

            if similar_hash_group:
                # 添加其自身，并将图片路径转换为漫画路径
                similar_hash_group.add(image)
                similar_comic_group = set()
                for image_path in similar_hash_group:
                    comic_path = cache_image_data_dict[image_path]['comic_path']
                    similar_comic_group.add(comic_path)

                # 检查漫画相似组集合，如果仅有一项则跳过
                if len(similar_comic_group) > 1:
                    similar_groups.append(similar_comic_group)

        # 处理相似组列表，去重+合并交集项
        similar_groups = function_normal.merge_intersecting_sets(similar_groups)

        # 保存相似组结果到本地，并发送信号
        function_cache_similargroup.save_similar_groups_pickle(similar_groups)
        self.signal_finished.emit()
