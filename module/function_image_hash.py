# 图片哈希相关方法
import io
import os
from typing import Union

import imagehash
from PIL import Image

from class_.class_image_info import ImageInfo
from module import function_archive

Image.MAX_IMAGE_PIXELS = None  # 解除pillow库的图片最大尺寸限制
_DEFAULT_HASH_DICT = {'ahash': None, 'phash': None, 'dhash': None}


def calc_image_hash(image_info: ImageInfo, calc_hash: str = 'all', resize_side: int = 8):
    """计算图片hash
    :param image_info: 图片信息类
    :param calc_hash: 计算的hash类型，ahash/phash/dhash/all
    :param resize_side: 修改图片尺寸的宽/高
    """
    hash_dict = _DEFAULT_HASH_DICT.copy()

    comic_type = image_info.type
    if comic_type == 'folder':
        image_path = image_info.path
        print('计算图片hash', image_path)
        hash_dict = _calc_hash(image_path, calc_hash, resize_side)
    elif comic_type == 'archive':
        image_path_in_archive = image_info.path
        archive_path = image_info.comic_path
        print('计算图片hash', archive_path, image_path_in_archive)
        img_bytes = function_archive.read_image(archive_path, image_path_in_archive)
        hash_dict = _calc_hash(img_bytes, calc_hash, resize_side)

    return hash_dict


def _calc_hash(image: Union[str, bytes], calc_hash: str = 'all', resize_side: int = 8):
    """计算图片hash
    :param image: 本地图片路径str/bytes图片对象
    :param calc_hash: 计算的hash类型，ahash/phash/dhash/all
    :param resize_side: 修改图片尺寸的宽/高
    """
    hash_dict = _DEFAULT_HASH_DICT.copy()

    try:
        if isinstance(image, str) and os.path.exists(image):  # 传入图片的路径时，直接读取
            image_pil = Image.open(image)
        elif isinstance(image, bytes):  # 传入字节时（从压缩包读取的图片），转换后读取
            image_pil = Image.open(io.BytesIO(image))
        else:
            return hash_dict
        image_pil = image_pil.convert('L')
        image_pil = image_pil.resize(size=(resize_side, resize_side))
    except:  # 如果图片损坏，会抛出异常OSError: image file is truncated (4 bytes not processed)
        return hash_dict

    # 计算均值哈希
    if calc_hash == 'ahash' or calc_hash == 'all':
        ahash = imagehash.average_hash(image_pil, hash_size=resize_side)
        ahash_str = _hash_numpy2str(ahash)
        hash_dict['ahash'] = ahash_str
    # 感知哈希
    if calc_hash == 'phash' or calc_hash == 'all':
        phash = imagehash.phash(image_pil, hash_size=resize_side)
        phash_str = _hash_numpy2str(phash)
        hash_dict['phash'] = phash_str
    # 差异哈希
    if calc_hash == 'dhash' or calc_hash == 'all':
        dhash = imagehash.dhash(image_pil, hash_size=resize_side)
        dhash_str = _hash_numpy2str(dhash)
        hash_dict['dhash'] = dhash_str

    image_pil.close()

    return hash_dict


def _hash_numpy2str(hash_numpy: Union[imagehash.NDArray, imagehash.ImageHash]):
    """将哈希值的numpy数组(imagehash.hash)转换为二进制字符串"""
    if not hash_numpy:
        return None
    if isinstance(hash_numpy, imagehash.ImageHash):
        hash_numpy = hash_numpy.hash

    hash_str = ''
    for row in hash_numpy:
        for col in row:
            if col:
                hash_str += '1'
            else:
                hash_str += '0'

    return hash_str


def _calc_hash_similar(hash_1: str, hash_2: str):
    """计算两个字符串哈希值之间的相似度（0~1)"""
    hash_int1 = int(hash_1, 2)
    hash_int2 = int(hash_2, 2)
    # 使用异或操作计算差异位数
    diff_bits = bin(hash_int1 ^ hash_int2).count('1')
    # 计算相似性
    similarity = 1 - diff_bits / len(hash_1)

    return similarity


def _calc_hamming_distance(hash_1: str, hash_2: str):
    """计算两个字符串哈希值之间的汉明距离"""
    hamming_distance = sum(ch1 != ch2 for ch1, ch2 in zip(hash_1, hash_2))
    return hamming_distance


def filter_hash_dict(image_info_dict: dict, hash_: str):
    """筛选hash字典（剔除失效项、hash为None的项、剔除纯色图像），并排序（对hash中的0或1计数，并按该计数排序）
    :param image_info_dict: dict，key为图片路径，value为image_info类
    :param hash_: 排序的hash类型
    :return: 排序后的字典（在image_info类中添加了一个新的key:zero_count）
    """
    image_info_dict_filter = {}
    # 在image_info类中添加一个新的key:zero_count
    for image_path, image_info in image_info_dict.items():
        hash_str = image_info.get_hash(hash_)
        if not hash_str or len(hash_str) < 16:  # 剔除None项
            continue

        zero_count = hash_str.count('0')
        if zero_count == len(hash_str):  # 剔除纯色图像（哈希值全为0）
            continue

        image_info.zero_count = zero_count
        image_info_dict_filter[image_path] = image_info

    # 升序排列
    image_info_dict_sorted = dict(sorted(image_info_dict_filter.items(), key=lambda item: item[1].zero_count))

    return image_info_dict_sorted


def filter_similar_group(image_info: ImageInfo, compare_image_info_dict: dict, compare_hash: str,
                         threshold_hamming_distance: int) -> dict:
    """筛选出相似hash的相似组
    :param image_info: 需要进行对比的图片信息ImageInfo类
    :param compare_image_info_dict: 用于比对的图片信息字典，key为虚拟图片路径，value为ImageInfo类
    :param compare_hash: 用于对比的hash类型
    :param threshold_hamming_distance: hash值之间的汉明距离的阈值
    :return: 相似的图片信息字典，key为虚拟图片路径，value为ImageInfo类"""
    print('匹配hash，主路径', image_info.comic_path, image_info.path)
    similar_image_info_dict = dict()
    # 提取检查项
    current_fake_image_path = image_info.fake_path
    current_hash_str = image_info.get_hash(compare_hash)
    current_zero_count = image_info.zero_count
    # 遍历对比字典
    for _, compare_image_info in compare_image_info_dict.items():
        compare_fake_image_path = compare_image_info.fake_path
        compare_hash_str = compare_image_info.get_hash(compare_hash)
        compare_zero_count = compare_image_info.zero_count

        # 对比前检查zero_count的差额，如果差额超限则提前结束循环（限制为选定的汉明距离/2（假设0/1差异各占一半））
        limit_zero_count = threshold_hamming_distance / 2
        diff_zero_count = compare_zero_count - current_zero_count  # 升序排列，所以后-前
        if diff_zero_count < - limit_zero_count:  # 升序排列，所以<limit时跳过，>limit时结束循环
            continue
        elif diff_zero_count > limit_zero_count:
            break

        # 对比
        hamming_distance = _calc_hamming_distance(current_hash_str, compare_hash_str)
        if hamming_distance <= threshold_hamming_distance:
            similar_image_info_dict[compare_fake_image_path] = compare_image_info

    # 相似组内添加需要对比的项后进行数量检查
    similar_image_info_dict[current_fake_image_path] = image_info
    if len(similar_image_info_dict) == 1:
        return dict()
    else:
        return similar_image_info_dict
