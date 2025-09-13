import os


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

    return images
