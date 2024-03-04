# 子线程-比较图片hash
import os

from module import function_cache_hash
from module import function_cache_similargroup
from module import function_cache_thread
from module import function_config
from module import function_hash
from module import function_normal
from module import function_ssim
from thread.thread_model import ThreadModel


class ThreadCompareHash(ThreadModel):
    """子线程-比较图片hash"""

    def __init__(self):
        super().__init__()
        self.step = '5/6 相似匹配'

    def run(self):
        super().run()
        # 获取设置
        mode_hash = function_config.get_mode_hash()
        # 读取缓存数据
        image_data_dict = function_cache_thread.read_current_image_data_dict()
        cache_image_data_dict = function_cache_hash.read_hash_cache()
        # 在缓存dict中剔除两个字典的重复项（在当前hash字典内部对比+与缓存对比，剔除重复项以防止重复匹配）
        for c_image, c_data_dict in image_data_dict.items():
            if c_image in cache_image_data_dict:
                cache_image_data_dict.pop(c_image)
        # 向两个字典中添加hash_count0键，并升序排序（统计hash中0的个数，用于确定需要对比的图片范围）
        image_data_dict = function_hash.add_count_key_to_dict(image_data_dict, mode_hash)
        cache_image_data_dict = function_hash.add_count_key_to_dict(cache_image_data_dict, mode_hash)
        # 进行两组相似匹配
        similar_groups = []
        # 和其自身匹配
        self.signal_step.emit('5/6 相似匹配(内部)')
        groups_a = self.compare_hash(image_data_dict, image_data_dict.copy())
        similar_groups += groups_a
        # 和缓存匹配
        self.signal_step.emit('6/6 相似匹配(缓存)')
        groups_b = self.compare_hash(image_data_dict, cache_image_data_dict)
        similar_groups += groups_b
        # 处理相似组列表，去重+合并交集项
        similar_groups = function_normal.merge_intersecting_sets(similar_groups)
        # 保存到本地
        function_cache_similargroup.save_similar_groups_pickle(similar_groups)
        # 发送结束信号
        if self.code_stop:
            self.signal_stopped.emit()
        else:
            self.signal_finished.emit()

    def compare_hash(self, image_data_dict, compare_image_data_dict):
        """对比图片hash"""
        threshold_ssim = function_config.get_threshold_ssim()
        threshold_hamming_distance = function_config.get_threshold_hash()
        mode_ssim = function_config.get_mode_ssim()

        similar_groups = []  # 全部的相似组列表（漫画路径）
        # 和其自身匹配
        index_rate = 0
        for image, hash_dict in image_data_dict.items():
            index_rate += 1
            if self.code_stop:
                break
            self.signal_rate.emit(f'{index_rate}/{len(image_data_dict)}')
            current_dict = {image: hash_dict}
            if image in compare_image_data_dict:  # 每次都删除当前图片项，避免重复对比
                compare_image_data_dict.pop(image)
            if not os.path.exists(image):  # 跳过无效项
                continue
            similar_hash_group = function_hash.filter_similar_hash_group(current_dict, compare_image_data_dict,
                                                                         threshold_hamming_distance)
            # 剔除结果中路径已失效的项
            if similar_hash_group:
                similar_hash_group_copy = similar_hash_group.copy()
                for path in similar_hash_group_copy:
                    if not os.path.exists(path):
                        similar_hash_group.remove(path)

            # 使用ssim再次筛选
            if similar_hash_group and mode_ssim:
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
                    try:
                        comic_path = image_data_dict[image_path]['comic_path']
                    except KeyError:
                        comic_path = compare_image_data_dict[image_path]['comic_path']
                    similar_comic_group.add(comic_path)

                # 检查漫画相似组集合，如果仅有一项则跳过
                if len(similar_comic_group) > 1:
                    similar_groups.append(similar_comic_group)

        return similar_groups
