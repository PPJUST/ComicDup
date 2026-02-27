import os

import natsort
from PIL import Image

Image.MAX_IMAGE_PIXELS = None  # 解除pillow库的图片最大尺寸限制


def is_image_by_filename(filepath: str):
    """通过文件名判断文件是否为图片"""
    image_suffix = ['.jpg', '.png', '.webp', '.jpeg']
    suffix = os.path.splitext(filepath)[1].lower()
    if suffix in image_suffix:
        return True
    else:
        return False


def get_images_in_folder(dirpath: str) -> list:
    """获取文件夹内所有图片的路径列表（仅一级子文件）"""
    # 提取文件名
    filenames = os.listdir(dirpath)
    # 组合路径
    files = [os.path.normpath(os.path.join(dirpath, i)) for i in filenames]
    # 检查文件类型
    images = []
    for file in files:
        if is_image_by_filename(file):
            images.append(file)
    # 排序
    images = natsort.os_sorted(images)

    return images


def format_bytes_size(bytes_size: int) -> str:
    """将字节数转换为可读字符串，自动转为B/KB/MB/GB大小，保留两位小数"""
    # 定义单位和对应的转换系数
    units = [('GB', 1024 ** 3),
             ('MB', 1024 ** 2),
             ('KB', 1024),
             ('B', 1)
             ]

    # 遍历单位，找到合适的转换单位
    for unit, factor in units:
        if bytes_size >= factor:
            format_size = bytes_size / factor  # 转换为当前单位
            format_size = round(format_size, 2)  # 保留两位小数
            format_str = f'{format_size}{unit}'
            return format_str

    # 如果小于1字节，直接返回0B
    return '0B'


def save_preview_image(origin_image_path: str, preview_image_path: str, height_zoom_out: int = 128):
    """保存指定图片的预览小图
    :param origin_image_path: 需要保存的图片路径
    :param preview_image_path: 预览小图存放的路径
    :param height_zoom_out: 缩放的图片高度"""
    image = Image.open(origin_image_path)
    # 清除元数据
    image.info.clear()
    # 转换图像模式，防止报错OSError: cannot write mode P as JPEG
    image = image.convert('RGB')
    # 缩小尺寸
    width, height = image.size
    resize_width = int(height_zoom_out * width / height)
    image = image.resize((resize_width, height_zoom_out), Image.LANCZOS)
    # 保存到本地
    image.save(preview_image_path)
    image.close()

    return preview_image_path
