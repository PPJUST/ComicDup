import io
import os
import zipfile
from typing import Union

import lzytools.archive
import natsort
import rarfile
from PIL import Image

from common import function_file


def is_archive_by_filename(filepath: str):
    """通过文件名判断文件是否为压缩文件"""
    image_suffix = ['.zip', '.rar']
    suffix = os.path.splitext(filepath)[1].lower()
    if suffix in image_suffix:
        return True
    else:
        return False


def get_images_in_archive(archive: str):
    """获取压缩包文件所有图片的路径列表（仅支持zip和rar）"""
    # 提取压缩文件信息
    infolist = lzytools.archive.get_infolist(archive)
    # 提取内部路径
    files = [i.filename for i in infolist]
    # 检查文件类型
    images = []
    for file in files:
        if function_file.is_image_by_filename(file):
            images.append(file)
    # 排序
    images = natsort.os_sorted(images)

    return images


def get_archive_real_size(archive: str) -> int:
    """获取一个压缩文件的真实大小（解压后的）"""
    # 提取压缩文件信息
    infolist = lzytools.archive.get_infolist(archive)
    # 计算文件大小
    total_size = 0
    for info in infolist:
        total_size += info.file_size

    return total_size


def save_preview_image(archive: str, image_path_inside: str, preview_image_path: str,
                       height_zoom_out: int = 128) -> str:
    """保存解压文件中指定图片的预览小图
    :param archive: 压缩文件路径
    :param image_path_inside: 需要保存的压缩包内图片的内部路径
    :param preview_image_path: 预览小图存放的路径
    :param height_zoom_out: 缩放的图片高度"""
    image_bytes = lzytools.archive.read_image(archive, image_path_inside)
    image = Image.open(io.BytesIO(image_bytes))
    # 转换图像模式，防止报错OSError: cannot write mode P as JPEG
    image = image.convert('RGB')
    # 缩小尺寸
    width, height = image.size
    resize_width = int(height_zoom_out * width / height)
    image = image.resize((resize_width, height_zoom_out), Image.LANCZOS)
    # 清除清除所有元数据，保存到本地
    image.info.clear()
    image.save(preview_image_path)

    return preview_image_path


def get_filesize_inside(archive_path: str, filepath_inside: str) -> int:
    """获取压缩文件中指定文件的大小（解压后的，字节bytes）"""
    infolist = lzytools.archive.get_infolist(archive_path)
    for info in infolist:
        info: Union[zipfile.ZipInfo, rarfile.RarInfo]
        path = info.filename
        if filepath_inside == path:
            size = info.file_size
            return size

    return 0  # 兜底
