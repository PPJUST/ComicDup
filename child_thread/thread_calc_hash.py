# 子线程-计算图片hash
import os
from functools import partial
from multiprocessing import Pool

from child_thread.thread_pattern import ThreadPattern
from class_ import class_comic_info, class_image_info
from class_.class_comic_info import ComicInfo
from class_.class_image_info import ImageInfo
from module import function_config_similar_option, function_image_hash


class ThreadCalcHash(ThreadPattern):
    """子线程-计算图片hash"""

    def __init__(self):
        super().__init__()
        self._step = '计算图片hash'
        self.comics = []

    def set_comics(self, comics: list):
        self.comics = comics

    def run(self):
        super().run()
        # 获取相似度算法设置
        extract_images_count = function_config_similar_option.extract_images.get()
        resize_image_size = function_config_similar_option.image_size.get()

        # 获取需要计算hash的图片清单及其信息
        calc_image_info_dict = dict()
        cache_comic_info_dict = class_comic_info.read_db()
        for comic in self.comics:
            if not os.path.exists(comic):  # 漫画不存在时，直接跳过
                continue
            comic_info: ComicInfo = cache_comic_info_dict[comic]
            for image in comic_info.images[:extract_images_count]:
                image_info = ImageInfo(image)
                image_info.update_comic_info(comic_info)
                calc_image_info_dict[image_info.fake_path] = image_info  # 注意，key为图片虚拟路径

        # 读取本地图片信息数据库
        cache_image_info_dict = class_image_info.read_db(hash_length=resize_image_size ** 2)

        # 如果需计算hash的图片任务已经存在于数据库中，则更新至数据库中的数据
        for (fake_image_path, _the_image_info) in calc_image_info_dict.copy().items():
            if fake_image_path in cache_image_info_dict:  # 数据库中存在，校验为同一个文件后替换
                cache_image_info = cache_image_info_dict[fake_image_path]
                if _the_image_info.filesize == cache_image_info.filesize:
                    calc_image_info_dict[fake_image_path] = cache_image_info

        # 计算任务中的图片hash
        calc_image_info_dict = self.multi_calc_hash(calc_image_info_dict)
        """未使用多进程的原版方法
        # 计算任务中的图片hash
        for index, (fake_image_path, _the_image_info) in enumerate(calc_image_info_dict.copy().items(), start=1):
            _the_image_info: ImageInfo
            if self._stop_code:
                break
            self.signal_rate.emit(f'{index}/{len(calc_image_info_dict)}')
            image_hash = _the_image_info.get_hash(hash_algorithm)
            if not image_hash:  # 不存在对应hash时，进行计算
                hash_dict = function_image_hash.calc_image_hash(_the_image_info, calc_hash=hash_algorithm,
                                                                resize_side=resize_image_size)
                # 更新类中的hash
                calc_image_info_dict[fake_image_path].update_hash(hash_dict)
        """

        # 将当前任务计算完成的数据更新至数据库（当前计算的数据为空数据+对应的数据库数据+新计算的数据，总是比数据库中的数据新）
        class_image_info.update_db(calc_image_info_dict)

        # 结束后重置参数
        self.comics.clear()

        # 结束后发送信号
        self.finished(calc_image_info_dict)

    def multi_calc_hash(self, image_info_dict: dict):
        """多进程计算hash"""
        image_info_dict = image_info_dict.copy()
        # 获取相似度算法设置
        hash_algorithm = function_config_similar_option.hash_algorithm.get()
        resize_image_size = function_config_similar_option.image_size.get()
        threads_count = function_config_similar_option.threads.get()

        # 剔除已经存在对应hash的项，减少计算任务
        calc_image_info_dict = {}  # 需要计算hash的任务字典
        for fake_image_path, _the_image_info in image_info_dict.items():
            _the_image_info: ImageInfo
            image_hash = _the_image_info.get_hash(hash_algorithm)
            if not image_hash:
                calc_image_info_dict[fake_image_path] = _the_image_info

        # 启用多进程
        with Pool(processes=threads_count) as pool:
            # 使用partial固定部分参数
            calculate_partial = partial(function_image_hash.calc_image_hash, calc_hash=hash_algorithm,
                                        resize_side=resize_image_size)
            # 设置多进程任务：pool.imap()为异步传参，imap中的第一个参数为执行的函数，第二个参数为可迭代对象（用于传参）
            for index, hash_dict in enumerate(pool.imap(calculate_partial, calc_image_info_dict.copy().values())):
                if self._stop_code:
                    break
                self.signal_rate.emit(f'{index + 1}/{len(calc_image_info_dict)}')
                the_key = list(calc_image_info_dict.keys())[index]
                calc_image_info_dict[the_key].update_hash(hash_dict)

        image_info_dict.update(calc_image_info_dict)  # 合并字典

        return image_info_dict
