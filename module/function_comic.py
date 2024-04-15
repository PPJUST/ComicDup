# 漫画相关处理的方法
import os
import shutil
import time
import zipfile

import natsort
import rarfile
from PIL import Image

from constant import EXTRACT_TEMP_IMAGE_FOLDER, TEMP_IMAGE_FOLDER, RESIZE_IMAGE_HEIGHT
from module import function_normal

Image.MAX_IMAGE_PIXELS = None


def filter_comic_folder_and_archive(check_dirpath):
    """从文件夹中筛选出符合要求的漫画文件夹和所有压缩包"""
    function_normal.print_function_info()
    folder_structure_dict = dict()  # 文件夹内部文件类型 {文件夹路径:{'dir':set(), 'image':set(), 'archive':set()}, ...}

    for dirpath, dirnames, filenames in os.walk(check_dirpath):
        # 提取所有文件夹，建立字典的key
        for dirname in dirnames:
            dirpath_join = os.path.normpath(os.path.join(dirpath, dirname))
            # 字典中添加当前文件夹key
            if dirpath_join not in folder_structure_dict:
                folder_structure_dict[dirpath_join] = {'dir': set(), 'image': set(), 'archive': set()}
            # 字典中添加父目录key，并添加value
            parent_dir = os.path.split(dirpath_join)[0]
            if parent_dir not in folder_structure_dict:
                folder_structure_dict[parent_dir] = {'dir': set(), 'image': set(), 'archive': set()}
            folder_structure_dict[parent_dir]['dir'].add(dirpath_join)

        # 提取所有文件，写入字典的value
        for filename in filenames:
            filepath_join = os.path.normpath(os.path.join(dirpath, filename))
            parent_dir = os.path.split(filepath_join)[0]
            if parent_dir not in folder_structure_dict:
                folder_structure_dict[parent_dir] = {'dir': set(), 'image': set(), 'archive': set()}
            # 根据文件类型写入不同的key
            filetype = function_normal.check_filetype(filepath_join)
            if filetype == 'image':
                folder_structure_dict[parent_dir]['image'].add(filepath_join)
            elif filetype == 'archive':
                folder_structure_dict[parent_dir]['archive'].add(filepath_join)

    # 检查字典，筛选出符合条件的漫画文件夹（内部图片文件数>=4且无压缩包和子文件夹）和所有压缩包
    archives = set()  # 所有压缩包路径的集合，压缩包不做判断
    comic_folders = set()  # 符合条件的漫画文件夹集合
    for dirpath, inside_structure in folder_structure_dict.items():
        inside_dirs = inside_structure['dir']
        inside_images = inside_structure['image']
        inside_archives = inside_structure['archive']

        if inside_archives:
            archives.update(inside_archives)
        elif inside_dirs:
            continue
        elif len(inside_images) >= 4:
            comic_folders.add(dirpath)

    return comic_folders, archives


def count_archive_image(archive: str):
    """统计压缩包内图片数量"""
    function_normal.print_function_info()
    try:
        archive_file = zipfile.ZipFile(archive)
    except zipfile.BadZipFile:
        try:
            archive_file = rarfile.RarFile(archive)
        except rarfile.NotRarFile:
            return 0

    files = archive_file.namelist()  # 中文会变为乱码，可以考虑转utf-8编码
    image_count = 0
    for file in files:
        if function_normal.check_filetype(file) == 'image':
            image_count += 1

    return image_count


def get_archive_images(archive: str):
    """提取压缩包内图片路径list"""
    function_normal.print_function_info()
    try:
        archive_file = zipfile.ZipFile(archive)
    except zipfile.BadZipFile:
        try:
            archive_file = rarfile.RarFile(archive)
        except rarfile.NotRarFile:
            return 0

    files = archive_file.namelist()  # 中文会变为乱码，可以考虑转utf-8编码
    images_in_archive = []
    for file in files:
        if function_normal.check_filetype(file) == 'image':
            images_in_archive.append(file)

    return natsort.natsorted(images_in_archive)


def read_image_in_archive(archive, image_path):
    """读取压缩包中的图片对象"""
    function_normal.print_function_info()
    try:
        archive_file = zipfile.ZipFile(archive)
    except zipfile.BadZipFile:
        try:
            archive_file = rarfile.RarFile(archive)
        except rarfile.NotRarFile:
            return 0

    img_data = archive_file.read(image_path)
    archive_file.close()

    return img_data


def extract_archive_image(archive: str, extract_number=0):
    """解压zip/rar压缩包中的指定数量的图片"""
    function_normal.print_function_info()
    try:
        archive_file = zipfile.ZipFile(archive)
    except zipfile.BadZipFile:
        try:
            archive_file = rarfile.RarFile(archive)
        except rarfile.NotRarFile:
            return False

    files = archive_file.namelist()  # 中文会变为乱码，可以考虑转utf-8编码
    images_in_archive = []
    for file in files:
        if function_normal.check_filetype(file) == 'image':
            images_in_archive.append(file)
    images_in_archive = natsort.natsorted(images_in_archive)

    extract_images = []
    for index in range(extract_number):
        # 解压
        need_extract_image = images_in_archive[index]
        local_image_file = archive_file.extract(need_extract_image, EXTRACT_TEMP_IMAGE_FOLDER)
        local_image_file = os.path.normpath(local_image_file)

        # 在改名前需要判断是否存在，不然后续的移动有时会在图片解压前执行而报错
        timeout = 5
        start_time = time.time()
        while True:
            if os.path.exists(local_image_file):
                break
            current_time = time.time()
            runtime = current_time - start_time
            if runtime >= timeout:
                raise Exception(f"解压文件 {archive} 失败")

        # 移动并改名
        suffix = os.path.splitext(local_image_file)[1]
        new_name = f'{index}_' + function_normal.create_random_string(16) + suffix
        new_filepath = os.path.normpath(os.path.join(TEMP_IMAGE_FOLDER, new_name))
        shutil.move(local_image_file, new_filepath)
        extract_images.append(new_filepath)
        resize_image(new_filepath)

    archive_file.close()

    return extract_images


def resize_image(image_path: str):
    """调整图片大小"""
    image = Image.open(image_path)
    width, height = image.size
    resize_height = RESIZE_IMAGE_HEIGHT
    resize_width = int(resize_height * width / height)
    try:
        image = image.resize((resize_width, resize_height))
        image.save(image_path)
    except OSError:
        pass
    image.close()
