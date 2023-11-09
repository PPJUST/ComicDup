"""
思路：
√1. 抓取图片（1~2张），保存到指定文件夹，并建立字典（建立图与源文件的对应关系）
√2. 计算每张图片的特征值（暂定：边缘检测lap算子-用于粗略分组，均值hash值-用于再分组）
√3. 按lap算子值排序字典
√4. 遍历匹配，每张图片先匹配lap阈值范围内，再匹配hash差值阈值范围内，最后ssim对比
√5. 显示结果，逐个处理
"""
import os
import random
import shutil
import string
import subprocess
import sys
import time

import cv2
import imagehash
import natsort
import numpy
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from tqdm import tqdm

copy_folder = 'copy_image'
data_dict = {}  # 键值对：复制的图片名:{image_path:该复制文件所在路径, origin:源文件, laplacian:..., canny_ratio:..., ahash:..., phash:...}
path_7zip = '7-Zip/7z.exe'
check_pic_count = 1
threshold_lap = 1000
threshold_canny = 5
threshold_ahash = 20
threshold_phash = 20
threshold_ssim = 0.9


def check_copy_folder():
    """清空存放复制图片的文件夹"""
    if os.path.exists(copy_folder):
        for i in os.listdir(copy_folder):
            fullpath = os.path.join(copy_folder, i)
            os.remove(fullpath)
    else:
        os.mkdir(copy_folder)


def is_image(filepath):
    """检查路径文件是否为图片"""
    if not os.path.exists(filepath):
        return False
    elif os.path.isdir(filepath):
        return False
    else:
        file_suffix = os.path.splitext(filepath)[1][1:].lower()  # 提取文件后缀名
        suffix_type = ['jpg', 'png', 'webp']
        if file_suffix in suffix_type:
            return True
        else:
            return False


def is_archive(filepath: str) -> bool:
    """判断文件是否为压缩包
    传参：filepath 文件路径str
    返回值 bool"""
    if not os.path.exists(filepath):
        return False
    elif os.path.isdir(filepath):
        return False
    else:
        file_suffix = os.path.splitext(filepath)[1][1:].lower()  # 提取文件后缀名
        suffix_type = ['zip', 'tar', 'rar', 'gz', '7z', 'xz', 'iso']  # 通过后缀名判断是否为压缩文件
        if file_suffix in suffix_type:
            return True
        else:
            return False


def create_random_string(length: int):
    """生成一个指定长度的随机字符串（小写英文+数字）
    传参：length 字符串的长度
    返回值：生成的str"""
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choices(characters, k=length))

    return random_string


def copy_image_from_dir(dirpath: str):
    """复制文件夹中的图片到指定文件夹"""
    if os.path.isdir(dirpath):
        # 提取文件夹中的图片完整路径
        image_filelist = []
        for i in os.listdir(dirpath):
            fullpath = os.path.normpath(os.path.join(dirpath, i))
            if is_image(fullpath):
                image_filelist.append(fullpath)
        image_filelist = natsort.natsorted(image_filelist)
        # 复制指定数量的图片
        if check_pic_count > len(image_filelist):
            copy_number = len(image_filelist)
        else:
            copy_number = check_pic_count
        for index in range(copy_number):
            origin_image = image_filelist[index]
            suffix = os.path.splitext(origin_image)[1]
            new_name = create_random_string(16) + suffix
            copy_image = os.path.join(copy_folder, new_name)
            shutil.copyfile(origin_image, copy_image)
            if new_name not in data_dict:
                data_dict[new_name] = {}
            data_dict[new_name]['image_path'] = copy_image
            data_dict[new_name]['origin'] = dirpath
    else:
        print(f'{dirpath} 不是文件夹')


def copy_image_from_archive(filepath: str):
    """复制压缩包中的图片到指定文件夹"""
    if is_archive(filepath):
        # 提取压缩包内结构
        command_l = [path_7zip, "l", filepath]
        process_l = subprocess.run(command_l,
                                   stdout=subprocess.PIPE,
                                   creationflags=subprocess.CREATE_NO_WINDOW,
                                   text=True,
                                   universal_newlines=True)
        if process_l.returncode == 0:
            line_archive = process_l.stdout.split('\n')
            # 提取出其中的图片文件列表
            """
            Date      Time    Attr         Size   Compressed  Name
            ------------------- ----- ------------ ------------  ------------------------
            2023-11-03 15:49:27 ....A         6847         6847  1.xlsx
            """
            fileline_archive = [i for i in line_archive if i.find('....A') != -1]
            image_archive = []
            for line in fileline_archive:
                split_1 = line.split()
                find_start_text = split_1[5]
                split_2 = line.split(' ')
                find_start_index = split_2.index(find_start_text)
                file_archive = ' '.join(split_2[find_start_index:]).strip()
                for suffix in ['.jpg', '.png', '.webp']:
                    if suffix in file_archive.lower():  # 筛选出图片文件
                        image_archive.append(file_archive)
            image_archive = natsort.natsorted(image_archive)
            # 解压
            if check_pic_count > len(image_archive):
                copy_number = len(image_archive)
            else:
                copy_number = check_pic_count
            for index in range(copy_number):
                need_extract_image = image_archive[index]
                command_e = [path_7zip, "e", filepath, need_extract_image, '-o' + copy_folder]
                process_e = subprocess.run(command_e,
                                           stdout=subprocess.PIPE,
                                           creationflags=subprocess.CREATE_NO_WINDOW,
                                           text=True,
                                           universal_newlines=True)
                if process_e.returncode == 0:
                    e_stdout = process_e.stdout
                    if 'No files to process' in e_stdout:
                        print('压缩包可能包含特殊字符，无法进行解压，已跳过')
                    else:
                        image_name = need_extract_image.split('\\')[-1]
                        extract_image = os.path.join(copy_folder, image_name)
                        suffix = os.path.splitext(extract_image)[1]
                        new_name = create_random_string(16) + suffix
                        new_file = os.path.join(copy_folder, new_name)
                        os.rename(extract_image, new_file)
                        if new_name not in data_dict:
                            data_dict[new_name] = {}
                        data_dict[new_name]['image_path'] = new_file
                        data_dict[new_name]['origin'] = filepath
    else:
        print(f'{filepath} 不是压缩包')


def calc_laplacian(image_numpy):
    """计算numpy图片的lap算子值"""
    laplacian_score = cv2.Laplacian(image_numpy, cv2.CV_64F).var()

    return laplacian_score


def calc_canny(image_numpy):
    """计算numpy图片的canny边缘检测白色像素占比"""
    edges = cv2.Canny(image_numpy, 50, 150)
    total_pixels = edges.shape[0] * edges.shape[1]
    white_pixels = cv2.countNonZero(edges)
    white_ratio = white_pixels / total_pixels * 100
    return white_ratio


def calc_hash(image):
    """计算路径图片的均值hash，感知hash"""
    image_pil = Image.open(image)
    # ahash = imagehash.average_hash(image_pil)  # 均值hash
    ahash = None
    phash = imagehash.phash(image_pil)  # 感知hash

    return ahash, phash


def convert_image_to_numpy(image_file, convert_gray=False):
    """将路径对应的图片转换为numpy图片对象"""
    image_numpy = cv2.imdecode(numpy.fromfile(image_file, dtype=numpy.uint8), -1)
    if convert_gray:
        try:
            gray_image_numpy = cv2.cvtColor(image_numpy, cv2.COLOR_BGR2GRAY)
        except cv2.error:
            gray_image_numpy = image_numpy
        return gray_image_numpy
    else:
        return image_numpy


def calc_ssim(image_1, image_2):
    gray_image_numpy_1 = convert_image_to_numpy(image_1, convert_gray=True)
    image_resize_1 = cv2.resize(gray_image_numpy_1, (10, 10))
    gray_image_numpy_2 = convert_image_to_numpy(image_2, convert_gray=True)
    image_resize_2 = cv2.resize(gray_image_numpy_2, (10, 10))
    ssim_value = ssim(image_resize_1, image_resize_2)

    return ssim_value


def get_attribute(image_name):
    """计算路径图片的特征值"""
    image = data_dict[image_name]['image_path']
    # gray_image_numpy = convert_image_to_numpy(image, convert_gray=True)
    # 计算边缘特征
    # laplacian = calc_laplacian(gray_image_numpy)
    # canny_ratio = calc_canny(gray_image_numpy)
    # 计算均值hash，感知hash
    ahash, phash = calc_hash(image)

    # 写入字典
    # data_dict[image_name]['laplacian'] = laplacian
    # data_dict[image_name]['canny_ratio'] = canny_ratio
    # data_dict[image_name]['ahash'] = ahash
    data_dict[image_name]['phash'] = phash


def sort_data_dict():
    """根据某特征值排序数据字典"""
    global data_dict
    data_dict_sorted = {}
    # 排序
    temp_dict = {}
    temp_list = []
    for key, key_data in data_dict.items():
        char = key_data['laplacian']
        char_with_key = f'{char} - {key}'
        temp_dict[char_with_key] = key
        temp_list.append(char_with_key)
    temp_list_sorted = natsort.natsorted(temp_list)[::-1]
    # 还原
    for i in temp_list_sorted:
        origin_key = temp_dict[i]
        data_dict_sorted[origin_key] = data_dict[origin_key]
    data_dict = data_dict_sorted


def find_similar_group():
    """遍历数据，找出相似图片组，返回dict格式 主图：[相似图1, 相似图2...]"""
    similar_image_group = {}
    keys_list = list(data_dict.keys())
    key_index = -1  # 主图索引
    for key in tqdm(keys_list[:-1], file=sys.stdout):  # 主图
        key_index += 1
        key_image_path = data_dict[key]['image_path']
        key_origin = data_dict[key]['origin']
        tqdm.write(f'主图【{key_origin}】，检查中')
        # key_laplacian = data_dict[key]['laplacian']
        # key_canny_ratio = data_dict[key]['canny_ratio']
        # key_ahash = data_dict[key]['ahash']
        key_phash = data_dict[key]['phash']
        for compare in tqdm(keys_list[key_index + 1:], file=sys.stdout):  # 对比图
            compare_image_path = data_dict[compare]['image_path']
            compare_origin = data_dict[compare]['origin']
            tqdm.write(f'对比图【{compare_origin}】')
            # compare_laplacian = data_dict[compare]['laplacian']
            # compare_canny_ratio = data_dict[compare]['canny_ratio']
            # compare_ahash = data_dict[compare]['ahash']
            compare_phash = data_dict[compare]['phash']
            # 计算特征值的差额
            # dis_laplacian = abs(key_laplacian - compare_laplacian)
            # dis_canny = abs(key_canny_ratio - compare_canny_ratio)
            # dis_ahash = abs(key_ahash - compare_ahash)
            dis_phash = abs(key_phash - compare_phash)
            # print(f'dis_laplacian {dis_laplacian}')
            # print(f'dis_canny {dis_canny}')
            # print(f'dis_ahash {dis_ahash}')
            # print(f'dis_phash {dis_phash}')

            # 判断
            # if dis_canny > threshold_canny:
            #     break
            if dis_phash < threshold_phash:  # 不再使用均值hash判断
                ssim_value = calc_ssim(key_image_path, compare_image_path)
                if ssim_value > threshold_ssim:
                    if key not in similar_image_group:
                        similar_image_group[key] = []
                    similar_image_group[key].append(compare)
    return similar_image_group


def save_similar_result(similar_group_dict):
    """保存相似组结果"""
    st_time = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
    with open(f'相似组结果 {st_time}.txt', 'w', encoding='utf-8') as rw:
        for key, value in similar_group_dict.items():
            rw.write('------------------------------\n')
            rw.write('主文件：\n')
            rw.write(key + '\n')
            rw.write('相似文件：\n')
            rw.write('\n'.join(value) + '\n\n')


def deal_similar_group(similar_image_group):
    """处理相似组"""
    # 生成一个新字典，并合并相同源文件项
    similar_group_file = {}  # {主图源文件:(相似图1源文件, ...)}
    for key, similar_list in similar_image_group.items():
        key_origin = data_dict[key]['origin']
        compare_origin_list = [data_dict[i]['origin'] for i in similar_list]
        if key_origin not in similar_group_file:
            similar_group_file[key_origin] = set()  # 集合去重
        similar_group_file[key_origin].update(compare_origin_list)
    # 处理前先保存结果
    print('----------保存查重结果到txt----------')
    save_similar_result(similar_group_file)
    # 正式开始处理
    print(
        '\n如何处理文件的说明：\n1.直接按下回车：同时打开主文件和相似文件（打开后自己需手动处理）\n2.输入任意字符后回车：跳过当前组')
    for key, similar_list in tqdm(similar_group_file.items(),
                                  bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} 处理相似组'):
        print(f'当前组：【{key}】，【{similar_list}】')
        mode = input('输入:')
        if mode == '':
            os.startfile(key)
            for i in similar_list:
                os.startfile(i)
            print('已打开全部需要处理的文件，请手工处理后继续检查下一个组\n')
        else:
            print('跳过当前组\n')
    print('已完成全部相似组的处理，5秒后返回主页')
    for _ in tqdm(range(5), bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} 等待秒数'):
        time.sleep(1)


def input_dirpath():
    """输入文件夹路径，并进行处理"""
    print('输入文件夹路径后回车，在全部输入路径完成后输入"run"后回车即可正式执行')
    dirpath_set = set()
    while True:
        input_text = input('输入：')
        if input_text.lower() == 'run':
            break
        else:
            dirpath_set.add(input_text.strip())

    # 检查规范
    dirpath_list = []
    for i in dirpath_set:
        if os.path.exists(i) and os.path.isdir(i):
            dirpath_list.append(i)

    return dirpath_list


def check_dir_is_std(dirpath):
    """检查文件夹符合标准（内部>4图片+无子文件夹）"""
    pic_count = 0
    for i in os.listdir(dirpath):
        fullpath = os.path.join(dirpath, i)
        if os.path.isdir(fullpath):
            return False
        elif is_image(fullpath):
            pic_count += 1
    if pic_count >= 4:
        return True
    else:
        return False


def walk_dirpath(dirpath_list):
    """遍历输入的文件夹，找出需要处理的文件夹/压缩包"""
    print('遍历输入的文件夹路径，寻找需要处理的文件夹/压缩包中')
    find_dir_set = set()  # 集合去重
    find_archive_set = set()
    find_image_set = set()
    # 遍历所有文件，找出其中的压缩文件和图片文件
    for checkpath in dirpath_list:
        for dir_path, dirnames, filenames in os.walk(checkpath):
            for filename in filenames:
                file = os.path.normpath(os.path.join(dir_path, filename))
                if is_archive(file):
                    find_archive_set.add(file)
                elif is_image(file):
                    find_image_set.add(file)
    # 根据图片路径，提取其上级文件夹
    temp_dir_set = set()
    for image in find_image_set:
        parent_dir = os.path.split(image)[0]
        temp_dir_set.add(parent_dir)
    for i in temp_dir_set:
        if check_dir_is_std(i):
            find_dir_set.add(i)

    return find_dir_set, find_archive_set


def set_arg():
    """设置参数"""
    global copy_folder, path_7zip, check_pic_count
    global threshold_lap, threshold_canny, threshold_ahash, threshold_phash, threshold_ssim
    while True:
        print('当前参数设置项，输入数字并回车后重新设置对应设置项：')
        print('输入"q"回车后返回主页')
        print(f'1.复制图片临时文件夹路径:{copy_folder}')
        print(f'2.7z.exe路径:{path_7zip}')
        print(f'3.每个文件夹/压缩包提取图片数:{check_pic_count}')
        print(f'4.图片特征值阈值-laplacian:{threshold_lap}')
        print(f'5.图片特征值阈值-canny边缘检测:{threshold_canny}')
        print(f'6.图片特征值阈值-均值hash:{threshold_ahash}')
        print(f'7.图片特征值阈值-感知hash:{threshold_phash}')
        print(f'8.图片特征值阈值-SSIM相似度:{threshold_ssim}')
        code = input('请按规则输入，任何不规范输入都将导致报错\n')
        if code == '1':
            copy_folder = input('输入文件夹路径\n')
        elif code == '2':
            path_7zip = input('输入文件路径\n')
        elif code == '3':
            check_pic_count = int(input('输入正整数\n'))
        elif code == '4':
            threshold_lap = int(input('输入正整数\n'))
        elif code == '5':
            threshold_canny = int(input('输入正整数\n'))
        elif code == '6':
            threshold_ahash = int(input('输入正整数\n'))
        elif code == '7':
            threshold_phash = int(input('输入正整数\n'))
        elif code == '8':
            threshold_ssim = float(input('输入0~1的浮点数\n'))
        elif code == 'q':
            break


def main():
    info = """
    --------------------------------------------------------------
    当前版本：v0.0.2
    版本说明：当前版本仅为测试版，还没有考虑好是否制作GUI以及其外观布局、具体的相似文件处理逻辑和一些方便使用的细节内容以及报错的处理，但是基本上能够正常使用了，大体的逻辑没有问题，后期看需求慢慢改了
    --------------------------------------------------------------
    功能：基于图片特征来搜索相似/重复的（高低分辨率、不同汉化组的同一本）本子，而非基于文件名，所以查重速度比较慢；支持文件夹和压缩包
    --------------------------------------------------------------
    使用说明：按照提示即可
    程序逻辑：选择文件夹->程序自动复制文件夹/压缩包中的n张图片->计算图片特征值->对比图片特征值并进行相似对比->完成全部对比后，自动打开文件夹，用户手动处理相似组
    程序逻辑（脱水版）：取本子的某几张图，对比这些图是否相似，来判断是否为同一本
    --------------------------------------------------------------
    其他说明：本工具不会删除任何的源文件，只会删除自动复制的图片文件；并且具体的重复项处理需要手工干预，本工具只帮忙找出来而不做任何处理
    其他说明：计算的图片特征：1.laplacian算子(分组用，已弃用) 2.Canny边缘检测(分组用，已弃用) 3.均值hash(相似判断，已弃用) 4.感知hash(相似判断) 5.SSIM相似度(相似判断)
    其他说明：参数-提取图片数 的作用是选择复制多少张图片，考虑到某些本子有封面而有些没有封面，可以设置为2，但是会极大的增加计算量（不止翻倍）
    --------------------------------------------------------------
    注意：由于能力问题，我无法解决7zip的stdout流编码问题，所以【无法解压含特殊字符的压缩包】，会跳过这类压缩包不进行检查
    --------------------------------------------------------------
    """

    command_text = """
    输入对应数字回车后执行：
    1.正式执行（需输入文件夹路径）
    2.参数设置
    3.退出
    """
    print(info)
    while True:
        data_dict.clear()  # 重置数据字典
        code = input(command_text)
        if code == '1':
            # 清空临时文件夹
            print('----------清空临时文件夹----------')
            check_copy_folder()
            # 输入路径
            dirpath_list = input_dirpath()
            # 提取需要检查的文件夹、压缩包
            print('----------提取需要检查的数据----------')
            need_check_dirpaths, need_check_archives = walk_dirpath(dirpath_list)
            # 复制图片
            for i in tqdm(need_check_dirpaths, file=sys.stdout):
                copy_image_from_dir(i)
                tqdm.write(f'已复制【{i}】中的图片')
            for i in tqdm(need_check_archives, file=sys.stdout):
                copy_image_from_archive(i)
                tqdm.write(f'已复制【{i}】中的图片')
            # 读取图片特征值
            for image_name in tqdm(os.listdir(copy_folder), file=sys.stdout):
                get_attribute(image_name)
                origin = data_dict[image_name]['origin']
                tqdm.write(f'已读取【{origin}】的特征值')
            # 排序字典
            # sort_data_dict()
            # 查找重复组
            print('----------查找重复项----------')
            similar_image_group = find_similar_group()
            # 处理重复组
            print('----------处理重复组----------')
            deal_similar_group(similar_image_group)
            # 清空临时文件夹
            print('----------清空临时文件夹----------')
            check_copy_folder()
        elif code == '2':
            set_arg()
        elif code == '3':
            quit()


if __name__ == '__main__':
    main()
