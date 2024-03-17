# 子线程-计算图片hash
import os

from module import function_cache_comicdata, function_cache_thread
from module import function_cache_hash
from module import function_config
from module import function_hash
from thread.thread_model import ThreadModel


class ThreadCalcHash(ThreadModel):
    """子线程-计算图片hash"""

    def __init__(self):
        super().__init__()
        self.step = '3/6 计算Hash'

    def run(self):
        super().run()
        # 获取设置
        mode_hash = function_config.get_mode_hash()
        # 读取当前漫画set任务缓存
        comics_data = function_cache_comicdata.read_current_comics_data_pickle()
        # 读取本地hash缓存(读取到的数据暂时不考虑路径是否已经失效)
        cache_image_data_dict = function_cache_hash.read_hash_cache()
        # 建立当前任务的图片hash字典
        image_data_dict = {}
        for index_rate, comic_class in enumerate(comics_data.values(), start=1):
            if self.code_stop:
                break
            self.signal_rate.emit(f'{index_rate}/{len(comics_data)}')
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
        function_cache_thread.save_current_image_data_dict(image_data_dict)
        function_cache_hash.update_hash_cache(image_data_dict)
        # 发送结束信号
        if self.code_stop:
            self.signal_stopped.emit()
        else:
            self.signal_finished.emit()
