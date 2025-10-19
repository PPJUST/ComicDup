# 图片相关方法
import io
import math
from typing import Union

import lzytools
import lzytools.archive
import lzytools.file
import lzytools.image
from PIL import Image

from common.class_config import TYPES_HASH_ALGORITHM


def calc_image_hash(image_path: str, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
    """计算本地图片的hash值"""
    # 创建ImageFile对象
    image_pil = Image.open(image_path)

    # 提取hash值
    if not isinstance(hash_type, str):
        hash_type: str = hash_type.text

    # 提取计算hash时的图片缩放尺寸
    if hash_length <= 20:
        hash_size = hash_length
    else:
        hash_size = int(math.sqrt(hash_length))

    # 计算hash（字典）
    hash_dict = lzytools.image.calc_hash(image_pil, hash_type, hash_size)
    image_pil.close()

    # 提取需要的hash值
    hash_ = hash_dict[hash_type.lower()]

    return hash_


def calc_archive_image_hash(archive_path: str, inside_image_path: str, hash_type: TYPES_HASH_ALGORITHM,
                            hash_length: int):
    """计算本地压缩文件内图片的的hash值"""
    # 读取压缩文件中的图片
    image_bytes = lzytools.archive.read_image(archive_path, inside_image_path)

    # 将bytes读取到内存流中
    bytes_io = io.BytesIO(image_bytes)

    #  使用 PIL 打开内存流，创建ImageFile对象
    image_pil = Image.open(bytes_io)

    # 提取hash值
    if not isinstance(hash_type, str):
        hash_type: str = hash_type.text

    # 提取计算hash时的图片缩放尺寸
    if hash_length <= 20:
        hash_size = hash_length
    else:
        hash_size = int(math.sqrt(hash_length))

    # 计算hash（字典）
    hash_dict = lzytools.image.calc_hash(image_pil, hash_type, hash_size)
    image_pil.close()

    # 提取需要的hash值
    hash_ = hash_dict[hash_type.lower()]

    return hash_
