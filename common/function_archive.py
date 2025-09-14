import os

import lzytools.archive

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
