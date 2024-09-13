# 压缩包相关方法
import io
import os
import zipfile
from typing import Union

import natsort
import rarfile
from PIL import Image, ImageFile

from constant import _PREVIEW_DIRPATH
from module import function_normal

ImageFile.LOAD_TRUNCATED_IMAGES = True  # 允许加载截断的图像 防止报错OSError: image file is truncated (4 bytes not processed)


def get_archive_real_size(archive_path: str) -> int:
    """获取一个压缩包的真实文件大小（解压后的）"""
    total_size = 0
    infolist = _get_infolist(archive_path)
    for info in infolist:
        info: Union[zipfile.ZipInfo, rarfile.RarInfo]
        total_size += info.file_size

    return total_size


def get_filenames(archive_path: str) -> list:
    """获取压缩包内部结构list（仅支持zip和rar）"""
    infolist = _get_infolist(archive_path)
    filenames = [i.filename for i in infolist]
    return filenames


def get_images(archive_path: str):
    """获取压缩包内部图片的路径list（仅支持zip和rar）"""
    structure_list = get_filenames(archive_path)
    images = [i for i in structure_list if function_normal.guess_filetype(i) == 'image']
    return images


def get_image_size(archive_path: str, image_path_in_archive: str) -> int:
    """获取压缩包中图片的文件大小（单位字节）"""
    # 方法1 读取压缩包中的图片对象，计算字节数
    """
    img_data = read_image(archive_path, image_path_in_archive)
    size = len(img_data)
    return size
    """

    # 方法2 直接读取压缩包信息，返回对应项的信息
    infolist = _get_infolist(archive_path)
    for info in infolist:
        info: Union[zipfile.ZipInfo, rarfile.RarInfo]
        path = info.filename
        if image_path_in_archive == path:
            size = info.file_size
            return size
    return 0  # 兜底


def read_image(archive_path: str, image_path_in_archive: str) -> bytes:
    """读取压缩包中的图片，并返回一个bytes图片对象"""
    try:
        archive_file = zipfile.ZipFile(archive_path)
    except zipfile.BadZipFile:
        try:
            archive_file = rarfile.RarFile(archive_path)
        except rarfile.NotRarFile:
            return b''

    img_data = archive_file.read(image_path_in_archive)
    archive_file.close()

    return img_data


def save_image_as_preview(archive_path: str, image_path_in_archive: str) -> str:
    """保存压缩包中的图片到本地缓存目录（固定高度200px）
    :return: 保存的本地图片路径"""
    img_bytes = read_image(archive_path, image_path_in_archive)
    image = Image.open(io.BytesIO(img_bytes))
    # 转换图像模式，防止报错OSError: cannot write mode P as JPEG
    image = image.convert('RGB')
    # 缩小尺寸，减少空间占用
    width, height = image.size
    resize_height = 200  # 固定图片高度为200，宽度自适应
    resize_width = int(resize_height * width / height)
    image = image.resize((resize_width, resize_height))
    # 保存到本地缓存目录
    save_path = (_PREVIEW_DIRPATH + os.sep +
                 function_normal.create_random_string() + os.path.splitext(image_path_in_archive)[1])
    save_path = os.path.normpath(save_path)
    image.save(save_path)

    return save_path


def _get_infolist(archive_path: str) -> list:
    """获取压缩包内部信息list（仅支持zip和rar）"""
    try:
        archive_file = zipfile.ZipFile(archive_path)
    except zipfile.BadZipFile:
        try:
            archive_file = rarfile.RarFile(archive_path)
        except rarfile.NotRarFile:
            return []

    infolist = archive_file.infolist()  # 中文等字符会变为乱码
    return infolist


def get_images_from_archive(archive: str) -> list:
    """提取压缩包内的所有图片路径"""
    images = get_images(archive)
    images = natsort.natsorted(images)
    return images
