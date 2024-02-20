# 配置文件相关方法
import configparser
import os.path

from constant import CONFIG_FILE, CACHE_FOLDER, RESIZE_IMAGE_ACCURACY


def check_config_exist():
    """检查配置文件是否存在，不存在则新建"""
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w', encoding='utf-8') as cw:
            config = configparser.ConfigParser()
            config.read(CONFIG_FILE, encoding='utf-8')
            # 基础设置
            config.add_section('setting')
            config.set('setting', 'mode_hash', 'ahash')
            config.set('setting', 'threshold_hash', '85')
            config.set('setting', 'mode_ssim', 'True')
            config.set('setting', 'threshold_ssim', '85')
            config.set('setting', 'extract_image_number', '1')
            config.set('setting', 'thread_number', '1')
            # 缓存选择的文件夹
            config.add_section('cache_folder')
            config.set('cache_folder', 'paths', '')
            # 需要匹配的文件夹
            config.add_section('select_folder')
            config.set('select_folder', 'paths', '')
            # 预览dialog宽高
            config.add_section('preview_widget_wh')
            config.set('preview_widget_wh', 'width', '900')
            config.set('preview_widget_wh', 'height', '600')

            config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))

            cw.close()

    if not os.path.exists(CACHE_FOLDER):
        os.mkdir(CACHE_FOLDER)


def get_preview_widget_wh():
    """获取设置项-预览控件宽高"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    width = int(config.get('preview_widget_wh', 'width'))
    height = int(config.get('preview_widget_wh', 'height'))

    return width, height


def reset_preview_widget_wh(width: int, height: int):
    """重设设置项-预览控件宽高"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('preview_widget_wh', 'width', str(width))
    config.set('preview_widget_wh', 'height', str(height))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_mode_hash():
    """获取设置项-hash算法"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    mode_hash = config.get('setting', 'mode_hash')

    return mode_hash


def reset_mode_hash(mode_hash):
    """重设设置项-hash算法"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('setting', 'mode_hash', mode_hash)
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_threshold_hash():
    """获取设置项-hash阈值"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    threshold_hash_percent = config.get('setting', 'threshold_hash')
    # 取得的阈值为百位数，需要转换为汉明距离单位
    threshold_hash = (1 - int(threshold_hash_percent) / 100) * RESIZE_IMAGE_ACCURACY * RESIZE_IMAGE_ACCURACY
    # 设100%相似度时，汉明距离为5，0%相似度时，汉明距离为50，以此建立方程式
    # threshold_hash = 50 - 45 * int(threshold_hash_percent) / 100

    return threshold_hash


def get_threshold_hash_percent():
    """获取设置项-hash阈值（百位数）"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    threshold_hash_percent = config.get('setting', 'threshold_hash')

    return int(threshold_hash_percent)


def reset_threshold_hash(threshold_hash: int):
    """重设设置项-hash阈值"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('setting', 'threshold_hash', str(threshold_hash))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_mode_ssim():
    """获取设置项-ssim"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    mode_ssim = config.get('setting', 'mode_ssim')

    if mode_ssim == 'True':
        return True
    else:
        return False


def reset_mode_ssim(mode_ssim: bool):
    """重设设置项-ssim"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('setting', 'mode_ssim', str(mode_ssim))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_threshold_ssim():
    """获取设置项-ssim阈值"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    threshold_ssim_percent = config.get('setting', 'threshold_ssim')
    # 取得的阈值为百位数，需要/100
    threshold_ssim = int(threshold_ssim_percent) / 100

    return threshold_ssim


def get_threshold_ssim_percent():
    """获取设置项-ssim阈值（百位数）"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    threshold_ssim_percent = config.get('setting', 'threshold_ssim')

    return int(threshold_ssim_percent)


def reset_threshold_ssim(threshold_ssim: int):
    """重设设置项-ssim阈值"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('setting', 'threshold_ssim', str(threshold_ssim))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_extract_image_number():
    """获取设置项-提取图片数"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    extract_image_number = config.get('setting', 'extract_image_number')

    return int(extract_image_number)


def reset_extract_image_number(extract_image_number: int):
    """重设设置项-提取图片数"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('setting', 'extract_image_number', str(extract_image_number))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_thread_number():
    """获取设置项-线程数"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    thread_number = config.get('setting', 'thread_number')

    return int(thread_number)


def reset_thread_number(thread_number: int):
    """重设设置项-线程数"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('setting', 'thread_number', str(thread_number))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_cache_folder():
    """获取设置项-缓存文件夹"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    cache_folder = config.get('cache_folder', 'paths')
    if cache_folder:
        cache_folders = cache_folder.split('|')
        return cache_folders
    else:
        return []


def reset_cache_folder(cache_folders: list):
    """重设设置项-缓存文件夹"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('cache_folder', 'paths', '|'.join(cache_folders))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))


def get_select_folders():
    """获取设置项-选中的文件夹"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    select_folder = config.get('select_folder', 'paths')
    if select_folder:
        select_folders = select_folder.split('|')
        return select_folders
    else:
        return []


def reset_select_folders(select_folder: list):
    """重设设置项-选中的文件夹"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding='utf-8')
    config.set('select_folder', 'paths', '|'.join(select_folder))
    config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))
