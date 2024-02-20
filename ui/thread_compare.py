# 进行相似比较的子线程
import os

from PySide6.QtCore import QThread, Signal

from module import function_cache_comicdata
from module import function_cache_hash
from module import function_cache_similargroup
from module import function_comic
from module import function_config
from module import function_hash
from module import function_normal
from module import function_ssim
from module.class_comic_data import ComicData


class ThreadCompare(QThread):
    """进行相似比较的子线程"""
    signal_start_thread = Signal()
    signal_schedule_step = Signal(str)
    signal_schedule_rate = Signal(str)
    signal_finished = Signal()

    def __init__(self):
        super().__init__()
        self.code_stop = False

    def run(self):
        self.signal_start_thread.emit()
        self.code_stop = False
        # 获取设置
        check_folders = function_config.get_select_folders()
        threshold_ssim = function_config.get_threshold_ssim()
        threshold_hamming_distance = function_config.get_threshold_hash()
        extract_image_number = function_config.get_extract_image_number()
        mode_hash = function_config.get_mode_hash()
        mode_ssim = function_config.get_mode_ssim()

        self.signal_schedule_step.emit('1/6 检查文件夹')
        # 提取符合要求的漫画文件夹和压缩包
        all_comic_folders = set()
        all_archives = set()
        for index_rate, dirpath in enumerate(check_folders, start=1):
            if self.code_stop:
                return
            self.signal_schedule_rate.emit(f'{index_rate}/{len(check_folders)}')
            comic_folders, archives = function_comic.filter_comic_folder_and_archive(dirpath)
            all_comic_folders.update(comic_folders)
            all_archives.update(archives)

        self.signal_schedule_step.emit('2/6 提取漫画数据')
        # 遍历两个列表，并提取漫画数据
        comics_data = {}
        all_files = all_comic_folders.union(all_archives)
        for index_rate, path in enumerate(all_files, start=1):
            if self.code_stop:
                return
            self.signal_schedule_rate.emit(f'{index_rate}/{len(all_files)}')
            comic_class = ComicData()
            comic_class.set_path(path)
            comic_class.set_calc_number(extract_image_number)
            comics_data[path] = comic_class

        # 保存漫画数据
        function_cache_comicdata.save_comics_data_pickle(comics_data)

        self.signal_schedule_step.emit('3/6 计算Hash')
        # 读取本地hash缓存(读取到的数据不考虑path是否已经失效)
        cache_image_data_dict = function_cache_hash.read_hash_cache()

        # 建立当前任务的图片hash字典
        image_data_dict = {}
        for index_rate, comic_class in enumerate(comics_data.values(), start=1):
            if self.code_stop:
                return
            self.signal_schedule_rate.emit(f'{index_rate}/{len(comics_data)}')
            comic_path = comic_class.path
            calc_hash_images = comic_class.calc_hash_images
            for image in calc_hash_images:
                # 生成基本数据
                image_filesize = os.path.getsize(image)
                image_data_dict[image] = {'comic_path': comic_path, 'filesize': image_filesize}
                # 计算hash
                image_hash = None
                if image in cache_image_data_dict and image_filesize == cache_image_data_dict[image]['filesize']:
                    image_hash = cache_image_data_dict[image][mode_hash]
                if not image_hash:
                    image_hash = function_hash.calc_image_hash(image, mode_hash)[mode_hash]
                image_data_dict[image][mode_hash] = image_hash

        # 将当前任务的图片数据字典更新写入hash缓存
        function_cache_hash.update_hash_cache(image_data_dict)

        self.signal_schedule_step.emit('4/6 排序Hash')
        # 向dict中增加键值对hash_count0，并按该key升序排列，最后进行查重（统计hash中0的个数，用于确定需要对比的图片范围）
        # 相似对比方式为在当前hash字典内部对比+与缓存对比
        # 先在缓存dict中剔除两个dict的重复项
        for c_image, c_data_dict in image_data_dict.items():
            if c_image in cache_image_data_dict:
                cache_image_data_dict.pop(c_image)
        # 再向两个dict中添加hash_count0键
        image_data_dict = function_hash.add_count_key_to_dict(image_data_dict, mode_hash)
        cache_image_data_dict = function_hash.add_count_key_to_dict(cache_image_data_dict, mode_hash)

        # 最后遍历需要匹配的图片列表
        similar_groups = []  # 全部的相似组列表（漫画路径）
        # 和其自身匹配
        self.signal_schedule_step.emit('5/6 相似匹配(内部)')
        index_rate = 0
        compare_image_data_dict = image_data_dict.copy()
        for image, hash_dict in image_data_dict.items():
            index_rate += 1
            if self.code_stop:
                return
            self.signal_schedule_rate.emit(f'{index_rate}/{len(image_data_dict)}')
            current_dict = {image: hash_dict}
            compare_image_data_dict.pop(image)  # 每次都删除当前图片项，避免重复对比
            similar_hash_group = function_hash.filter_similar_hash_group(current_dict, compare_image_data_dict,
                                                                         threshold_hamming_distance)
            # 剔除不存在的路径
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
                    comic_path = image_data_dict[image_path]['comic_path']
                    similar_comic_group.add(comic_path)

                # 检查漫画相似组集合，如果仅有一项则跳过
                if len(similar_comic_group) > 1:
                    similar_groups.append(similar_comic_group)
        # 备忘录：两种匹配方法考虑抽象为一个通用方法
        # 和缓存匹配
        self.signal_schedule_step.emit('6/6 相似匹配(缓存)')
        index_rate = 0
        for image, hash_dict in image_data_dict.items():
            index_rate += 1
            if self.code_stop:
                return
            self.signal_schedule_rate.emit(f'{index_rate}/{len(image_data_dict)}')
            current_dict = {image: hash_dict}
            similar_hash_group = function_hash.filter_similar_hash_group(current_dict, cache_image_data_dict,
                                                                         threshold_hamming_distance)
            # 剔除不存在的路径
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
                        comic_path = cache_image_data_dict[image_path]['comic_path']
                    except KeyError:  # 缓存字典已经删除重复项，如果未找到则需要在内部字典查找
                        comic_path = image_data_dict[image_path]['comic_path']
                    similar_comic_group.add(comic_path)

                # 检查漫画相似组集合，如果仅有一项则跳过
                if len(similar_comic_group) > 1:
                    similar_groups.append(similar_comic_group)

        # 处理相似组列表，去重+合并交集项
        similar_groups = function_normal.merge_intersecting_sets(similar_groups)

        # 保存相似组结果到本地，并发送信号
        function_cache_similargroup.save_similar_groups_pickle(similar_groups)
        self.signal_finished.emit()
