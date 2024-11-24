# 配置文件的方法（相似算法）

import configparser
import math
import os

from constant import _CONFIG_FILE

_SECTION_SIMILAR_OPTION = 'similar_option'
_OPTION_HASH_ALGORITHM = 'hash_algorithm'
_DEFAULT_VALUE_HASH_ALGORITHM = 'dhash'
_OPTION_SIMILARITY_THRESHOLD = 'similarity_threshold'
_DEFAULT_VALUE_SIMILARITY_THRESHOLD = '90'
_OPTION_SSIM = 'ssim'
_DEFAULT_VALUE_SSIM = 'ENABLE'
_OPTION_CACHE = 'cache'
_DEFAULT_VALUE_CACHE = 'DISABLE'
_OPTION_MATCH_SIMILAR = 'match_similar'
_DEFAULT_VALUE_MATCH_SIMILAR = 'DISABLE'
_OPTION_EXTRACT_IMAGES = 'extract_images'
_DEFAULT_VALUE_EXTRACT_IMAGES = '1'
_OPTION_IMAGE_SIZE = 'image_size'
_DEFAULT_VALUE_IMAGE_SIZE = '8'
_OPTION_THREADS = 'threads'
_DEFAULT_VALUE_THREADS = '1'


def check_section(config_file=_CONFIG_FILE):
    """检查配置中的设置项是否存在"""
    if not os.path.exists(config_file):
        with open(config_file, 'w', encoding='utf-8'):
            pass
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    if _SECTION_SIMILAR_OPTION not in config.sections():
        config.add_section(_SECTION_SIMILAR_OPTION)
        config.set(_SECTION_SIMILAR_OPTION, _OPTION_HASH_ALGORITHM, _DEFAULT_VALUE_HASH_ALGORITHM)
        config.set(_SECTION_SIMILAR_OPTION, _OPTION_SIMILARITY_THRESHOLD, _DEFAULT_VALUE_SIMILARITY_THRESHOLD)
        config.set(_SECTION_SIMILAR_OPTION, _OPTION_SSIM, _DEFAULT_VALUE_SSIM)
        config.set(_SECTION_SIMILAR_OPTION, _OPTION_CACHE, _DEFAULT_VALUE_CACHE)
        config.set(_SECTION_SIMILAR_OPTION, _OPTION_MATCH_SIMILAR, _DEFAULT_VALUE_MATCH_SIMILAR)
        config.set(_SECTION_SIMILAR_OPTION, _OPTION_EXTRACT_IMAGES, _DEFAULT_VALUE_EXTRACT_IMAGES)
        config.set(_SECTION_SIMILAR_OPTION, _OPTION_IMAGE_SIZE, _DEFAULT_VALUE_IMAGE_SIZE)
        config.set(_SECTION_SIMILAR_OPTION, _OPTION_THREADS, _DEFAULT_VALUE_THREADS)
        config.write(open(config_file, 'w', encoding='utf-8'))


class hash_algorithm:
    """设置项-hash算法"""

    @staticmethod
    def get():
        return _get_value(_OPTION_HASH_ALGORITHM)

    @staticmethod
    def update(hash_):
        _update_value(_OPTION_HASH_ALGORITHM, hash_)


class similarity_threshold:
    """设置项-相似度阈值"""

    @staticmethod
    def get():
        return int(_get_value(_OPTION_SIMILARITY_THRESHOLD))

    @staticmethod
    def update(threshold: int):
        _update_value(_OPTION_SIMILARITY_THRESHOLD, threshold)

    @staticmethod
    def get_hash_hamming_distance():
        similarity_threshold_percent = int(_get_value(_OPTION_SIMILARITY_THRESHOLD))
        image_size_ = int(_get_value(_OPTION_IMAGE_SIZE))
        hash_hamming_distance = math.ceil(image_size_ ** 2 * (100 - similarity_threshold_percent) / 100)

        return hash_hamming_distance

    @staticmethod
    def get_ssim_threshold():
        similarity_threshold_percent = int(_get_value(_OPTION_SIMILARITY_THRESHOLD))
        ssim_threshold = similarity_threshold_percent / 100

        return ssim_threshold


class ssim:
    """设置项-是否启用ssim"""

    @staticmethod
    def get():
        ssim_ = _get_value(_OPTION_SSIM)
        if ssim_.upper() == 'ENABLE':
            return True
        elif ssim_.upper() == 'DISABLE':
            return False
        else:
            return False

    @staticmethod
    def update(is_enable: bool):
        if is_enable is True:
            text = 'ENABLE'
        else:
            text = 'DISABLE'
        _update_value(_OPTION_SSIM, text)


class cache:
    """设置项-是否匹配缓存"""

    @staticmethod
    def get():
        cache_ = _get_value(_OPTION_CACHE)
        if cache_.upper() == 'ENABLE':
            return True
        elif cache_.upper() == 'DISABLE':
            return False
        else:
            return False

    @staticmethod
    def update(is_enable: bool):
        if is_enable is True:
            text = 'ENABLE'
        else:
            text = 'DISABLE'
        _update_value(_OPTION_CACHE, text)


class match_similar:
    """设置项-是否仅匹配相似文件名的项目"""

    @staticmethod
    def get():
        similar = _get_value(_OPTION_MATCH_SIMILAR)
        if similar.upper() == 'ENABLE':
            return True
        elif similar.upper() == 'DISABLE':
            return False
        else:
            return False

    @staticmethod
    def update(is_enable: bool):
        if is_enable is True:
            text = 'ENABLE'
        else:
            text = 'DISABLE'
        _update_value(_OPTION_MATCH_SIMILAR, text)


class extract_images:
    """设置项-提取图片数"""

    @staticmethod
    def get():
        return int(_get_value(_OPTION_EXTRACT_IMAGES))

    @staticmethod
    def update(count: int):
        _update_value(_OPTION_EXTRACT_IMAGES, count)


class image_size:
    """设置项-计算图片尺寸"""

    @staticmethod
    def get():
        return int(_get_value(_OPTION_IMAGE_SIZE))

    @staticmethod
    def update(side: int):
        _update_value(_OPTION_IMAGE_SIZE, side)


class threads:
    """设置项-线程数"""

    @staticmethod
    def get():
        return int(_get_value(_OPTION_THREADS))

    @staticmethod
    def update(count: int):
        _update_value(_OPTION_THREADS, count)


def _get_value(key, section=_SECTION_SIMILAR_OPTION, config_file=_CONFIG_FILE):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    value = config.get(section, key)
    return value


def _update_value(key, value, section=_SECTION_SIMILAR_OPTION, config_file=_CONFIG_FILE):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    config.set(section, key, str(value))
    config.write(open(config_file, 'w', encoding='utf-8'))
