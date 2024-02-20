# 图片哈希的相关方法
import os

import imagehash
from PIL import Image

from constant import RESIZE_IMAGE_ACCURACY
from module import function_normal

Image.MAX_IMAGE_PIXELS = None


def calc_image_hash(image_file, calc_hash: str = 'all'):
    """计算图片的哈希值
    :param image_file: 图片文件的路径
    :param calc_hash: 计算的hash类型，ahash/phash/dhash/all
    """
    function_normal.print_function_info()
    image_pil = Image.open(image_file)
    grey_image = image_pil.convert('L')  # 转灰度图
    resize_image_pil = grey_image.resize(size=(RESIZE_IMAGE_ACCURACY, RESIZE_IMAGE_ACCURACY))

    pic_hash_dict = {'ahash': None, 'phash': None, 'dhash': None}
    # 均值哈希
    if calc_hash == 'ahash' or calc_hash == 'all':
        hash_a = imagehash.average_hash(resize_image_pil, hash_size=RESIZE_IMAGE_ACCURACY)
        hash_a_str = _hash_numpy2str(hash_a)
        pic_hash_dict['ahash'] = hash_a_str
    # 感知哈希
    if calc_hash == 'phash' or calc_hash == 'all':
        hash_p = imagehash.phash(resize_image_pil, hash_size=RESIZE_IMAGE_ACCURACY)
        hash_p_str = _hash_numpy2str(hash_p)
        pic_hash_dict['phash'] = hash_p_str
    # 差异哈希
    if calc_hash == 'dhash' or calc_hash == 'all':
        hash_d = imagehash.dhash(resize_image_pil, hash_size=RESIZE_IMAGE_ACCURACY)
        hash_d_str = _hash_numpy2str(hash_d)
        pic_hash_dict['dhash'] = hash_d_str

    return pic_hash_dict


def _hash_numpy2str(hash_numpy):
    """将哈希值的numpy数组(imagehash.hash)转换为二进制字符串"""
    if not hash_numpy:
        return None

    if type(hash_numpy) is imagehash.ImageHash:
        hash_numpy = hash_numpy.hash

    hash_str = ''
    for row in hash_numpy:
        for col in row:
            if col:
                hash_str += '1'
            else:
                hash_str += '0'

    return hash_str


def _calc_hash_similar(hash_str1, hash_str2):
    """计算两个字符串哈希值之间的相似度"""
    hash_int1 = int(hash_str1, 2)
    hash_int2 = int(hash_str2, 2)
    # 使用异或操作计算差异位数
    diff_bits = bin(hash_int1 ^ hash_int2).count('1')
    # 计算相似性
    similarity = 1 - diff_bits / len(hash_str1)

    return similarity


def _calc_hash_hamming_distance(hash_str1, hash_str2):
    """计算两个字符串哈希值之间的汉明距离"""
    hamming_distance = sum(ch1 != ch2 for ch1, ch2 in zip(hash_str1, hash_str2))
    return hamming_distance


def add_count_key_to_dict(image_data_dict: dict, calc_hash: str):
    """在字典中添加hash_count0键，根据该键升序排列字典（并剔除None项，替换hash键名）
    :param image_data_dict: 图片数据字典
    :param calc_hash: 计算的hash类型
    :return: 添加了count键并升序后的图片哈希字典
    """
    new_image_data_dict = {}
    # 添加新key
    for image, data_dict in image_data_dict.items():
        hash_str = data_dict[calc_hash]
        if hash_str:  # 剔除None项
            data_dict['hash_count0'] = hash_str.count('0')
            data_dict['hash'] = hash_str
            new_image_data_dict[image] = data_dict

    # 升序排列
    image_path_list = []
    hash_count0_list = []
    for image, hash_dict in new_image_data_dict.items():
        hash_count0 = hash_dict['hash_count0']
        image_path_list.append(image)
        hash_count0_list.append(hash_count0)

    join_list = zip(image_path_list, hash_count0_list)
    join_list_sorted = sorted(join_list, key=lambda x: x[1])
    image_path_list_sorted = [i[0] for i in join_list_sorted]

    new_image_data_dict_sorted = {}
    for key in image_path_list_sorted:
        new_image_data_dict_sorted[key] = new_image_data_dict[key]

    return new_image_data_dict_sorted


def filter_similar_hash_group(image_data_dict: dict, compare_data_dict: dict, threshold_hamming_distance: int):
    """查找相似的hash组（传入的字典为处理后的单个hash值的字典
    :param image_data_dict: 图片数据字典，仅包含一个键值对（检查项）
    :param compare_data_dict: 对比的图片数据字典
    :param threshold_hamming_distance: hash值汉明距离最大限制值"""
    function_normal.print_function_info()
    similar_hash_group = set()
    # 提取检查项
    current_image = list(image_data_dict.keys())[0]
    current_hash = image_data_dict[current_image]['hash']
    current_hash_count0 = image_data_dict[current_image]['hash_count0']
    # 遍历对比项
    for compare_image, comp_data_dict in compare_data_dict.items():
        compare_hash = comp_data_dict['hash']
        compare_hash_count0 = comp_data_dict['hash_count0']
        compare_filesize = comp_data_dict['filesize']
        # 跳过其自身
        if current_image == compare_image:
            continue
        # 检查hash中0的个数的差额，如果超限则提前结束循环
        limit_count0 = threshold_hamming_distance / 2  # 限制为选定的汉明距离/2（假设0/1差异各占一半）
        diff_count0 = compare_hash_count0 - current_hash_count0
        # 数据字典已经按count0值升序排序，所以<limit时跳过，>limit时结束循环
        if diff_count0 < - limit_count0:
            continue
        elif diff_count0 > limit_count0:
            break
        else:
            hamming_distance = _calc_hash_hamming_distance(current_hash, compare_hash)
            if hamming_distance <= threshold_hamming_distance:
                # 检查当前图片是否存在以及是否为计算hash值时的图片，否则跳过
                if os.path.exists(compare_image) and compare_filesize == os.path.getsize(compare_image):
                    similar_hash_group.add(compare_image)

    return similar_hash_group
