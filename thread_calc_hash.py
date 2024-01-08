from PySide6.QtCore import *

from satic_function import get_image_attr


class ThreadCalcHash(QThread):
    signal_schedule_calc_hash = Signal(str)
    signal_finished = Signal(dict)

    def __init__(self):
        super().__init__()
        self.image_data_dict = dict()
        self.comic_cache_data = dict
        self.mode_ahash = 0
        self.mode_phash = 0
        self.mode_dhash = 0

    def set_image_data_dict(self, image_data_dict):
        self.image_data_dict = image_data_dict

    def set_comic_cache_data(self, comic_cache_data):
        self.comic_cache_data = comic_cache_data

    def set_mode_hash(self, mode_ahash=0, mode_phash=0, mode_dhash=0):
        self.mode_ahash = mode_ahash
        self.mode_phash = mode_phash
        self.mode_dhash = mode_dhash

    def run(self):
        new_image_data_dict = self.image_data_dict.copy()  # image_data_dict的扩展，添加了更多的键值对
        total_data = len(self.image_data_dict)
        for index, image in enumerate(self.image_data_dict):
            self.signal_schedule_calc_hash.emit(f'{index}/{total_data}')
            hash_dict = {'ahash': None, 'phash': None, 'dhash': None,
                         'ahash_count0': None, 'phash_count0': None, 'dhash_count0': None}
            # 提取缓存中已有的hash数据
            origin_path = image
            cache_ahash, cache_phash, cache_dhash = None, None, None
            if origin_path in self.comic_cache_data:
                cache_ahash = self.comic_cache_data[origin_path]['ahash']
                cache_phash = self.comic_cache_data[origin_path]['phash']
                cache_dhash = self.comic_cache_data[origin_path]['dhash']
            if self.mode_ahash:
                if cache_ahash:
                    hash_dict['ahash'] = cache_ahash
                    hash_dict['ahash_count0'] = cache_ahash.count('0')
                else:
                    ahash = get_image_attr(image, mode_hash='ahash')
                    hash_dict['ahash'] = ahash
                    hash_dict['ahash_count0'] = ahash.count('0')
            if self.mode_phash:
                if cache_phash:
                    hash_dict['phash'] = cache_phash
                    hash_dict['phash_count0'] = cache_phash.count('0')
                else:
                    phash = get_image_attr(image, mode_hash='phash')
                    hash_dict['phash'] = phash
                    hash_dict['phash_count0'] = phash.count('0')
            if self.mode_dhash:
                if cache_dhash:
                    hash_dict['dhash'] = cache_dhash
                    hash_dict['dhash_count0'] = cache_dhash.count('0')
                else:
                    dhash = get_image_attr(image, mode_hash='dhash')
                    hash_dict['dhash'] = dhash
                    hash_dict['dhash_count0'] = dhash.count('0')

            new_image_data_dict[image].update(hash_dict)

        self.signal_finished.emit(new_image_data_dict)
