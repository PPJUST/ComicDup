# 计算ssim相似度的相关方法
import io
from typing import Union

import cv2
import numpy
from PIL import Image

from class_.class_image_info import ImageInfo


def compare_ssim(image_info: ImageInfo, compare_image_info_dict: dict, resize_image_size: int,
                 threshold: float) -> dict:
    """图片与路径组内图片进行比对，使用ssim进行校验
    :param image_info: 需要对比的图片信息类
    :param compare_image_info_dict: dict，用于比对的图片信息字典，key为虚拟图片路径，value为ImageInfo类
    :param resize_image_size: int，图片的计算尺寸
    :param threshold: float，相似度阈值
    :return: 相似的图片信息字典，key为虚拟图片路径，value为ImageInfo类"""
    similar_image_info_dict = dict()
    current_image_bytes = image_info.get_image_bytes()
    for compare_fake_image_path, compare_image_info in compare_image_info_dict.items():
        compare_image_bytes = compare_image_info.get_image_bytes()
        similar = _calc_images_ssim(current_image_bytes, compare_image_bytes, size=resize_image_size)
        if similar >= threshold:
            similar_image_info_dict[compare_fake_image_path] = compare_image_info

    return similar_image_info_dict


def _image_to_numpy(image_file: str, size: int = 8):
    """将本地图片转换为numpy图片对象"""
    image_numpy = cv2.imdecode(numpy.fromfile(image_file, dtype=numpy.uint8), -1)
    image_numpy = cv2.resize(image_numpy, dsize=(size, size))

    try:
        image_numpy = cv2.cvtColor(image_numpy, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        pass

    return image_numpy


def _bytes_to_numpy(image_bytes: bytes, size: int = 8):
    """将bytes图片对象转换为numpy图片对象"""
    image_bytes = io.BytesIO(image_bytes)  # 转为文件对象
    image = Image.open(image_bytes)  # 转PIL.Image
    image_numpy = numpy.array(image)  # 转NumPy数组
    image_numpy = cv2.resize(image_numpy, dsize=(size, size))

    try:
        image_numpy = cv2.cvtColor(image_numpy, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        pass

    return image_numpy


def _calc_images_ssim(image_1: Union[str, bytes], image_2: Union[str, bytes], size=8) -> float:
    """计算两张图片的ssim相似度（0~1，越大越相似）"""
    # 转换图片格式
    if isinstance(image_1, str):  # 传入图片路径时
        image_numpy1 = _image_to_numpy(image_1, size)
    elif isinstance(image_1, bytes):  # 传入字节时（从压缩包读取的图片）
        image_numpy1 = _bytes_to_numpy(image_1, size)
    else:
        return 0
    if isinstance(image_2, str):  # 传入图片路径时
        image_numpy2 = _image_to_numpy(image_2, size)
    elif isinstance(image_2, bytes):  # 传入字节时（从压缩包读取的图片）
        image_numpy2 = _bytes_to_numpy(image_2, size)
    else:
        return 0

    # 计算均值、方差和协方差
    mean1, mean2 = numpy.mean(image_numpy1), numpy.mean(image_numpy2)
    var1, var2 = numpy.var(image_numpy1), numpy.var(image_numpy2)
    covar = numpy.cov(image_numpy1.flatten(), image_numpy2.flatten())[0][1]

    # 设置常数
    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2

    # 计算SSIM
    numerator = (2 * mean1 * mean2 + c1) * (2 * covar + c2)
    denominator = (mean1 ** 2 + mean2 ** 2 + c1) * (var1 + var2 + c2)
    ssim = numerator / denominator

    return ssim
