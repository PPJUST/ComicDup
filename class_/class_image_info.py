# 图片信息类及其数据库的相关方法
"""
图片信息的sqlite数据库：存储图片的路径、文件大小、文件类型（是否是在压缩包内）、3种hash值、对应的漫画路径
读取的数据统一用image_info_dict变量
"""
import os
import sqlite3
from typing import Union

from class_.class_comic_info import ComicInfo
from constant import _IMAGE_INFO_DB
from module import function_archive, function_normal

_TABLE_NAME = 'ImageInfo'  # 数据表名称
_KEY_PATH = 'path'  # 键-图片路径（真实路径）
_KEY_FAKE_PATH = 'fake_path'  # 虚拟路径，仅用于检索与查重（主要处理压缩包类的漫画内的图片路径，将漫画路径与内部路径拼接）
_KEY_FILESIZE = 'filesize'  # 键-图片大小
_KEY_COMIC_PATH = 'comic_path'  # 键-图片对应的漫画路径
_KEY_TYPE = 'type'  # 键-漫画类型（‘folder'/'archive'）
_KEY_AHASH = 'ahash_'
_KEY_AHASH_64 = f'{_KEY_AHASH}{8 * 8}'
_KEY_AHASH_144 = f'{_KEY_AHASH}{12 * 12}'
_KEY_AHASH_256 = f'{_KEY_AHASH}{16 * 16}'
_KEY_PHASH = 'phash_'
_KEY_PHASH_64 = f'{_KEY_PHASH}{8 * 8}'
_KEY_PHASH_144 = f'{_KEY_PHASH}{12 * 12}'
_KEY_PHASH_256 = f'{_KEY_PHASH}{16 * 16}'
_KEY_DHASH = 'dhash_'
_KEY_DHASH_64 = f'{_KEY_DHASH}{8 * 8}'
_KEY_DHASH_144 = f'{_KEY_DHASH}{12 * 12}'
_KEY_DHASH_256 = f'{_KEY_DHASH}{16 * 16}'


class ImageInfo:
    def __init__(self, image_path):
        self.path = image_path  # 路径
        self.fake_path = image_path  # 虚拟路径，仅用于检索与查重（主要处理压缩包类的漫画内的图片路径，将漫画路径与内部路径拼接）
        self.filesize = 0  # 图片大小
        self.type = ''  # 漫画类型，'folder'/'archive'
        self.ahash = ''
        self.dhash = ''
        self.phash = ''
        self.comic_path = ''  # 图片对应的漫画路径

        self.zero_count = None  # 指定hash中0的个数，仅用于排序

    def update_comic_info(self, _comic_info: ComicInfo):
        """根据ComicInfo类更新图片信息"""
        self.comic_path = _comic_info.path
        self.type = _comic_info.filetype

        # 设置虚拟路径
        self._set_fake_path()

        # 设置图片大小
        self.filesize = self._get_image_size()

    def is_exist(self) -> bool:
        """检验图片是否有效"""
        if self.type == 'folder':
            if os.path.exists(self.path):
                local_filesize = function_normal.get_size(self.path)
                return local_filesize == self.filesize
        elif self.type == 'archive':
            if os.path.exists(self.comic_path):
                local_filesize = function_archive.get_image_size(self.comic_path, self.path)
                return local_filesize == self.filesize

        return False

    def get_image_bytes(self) -> bytes:
        """读取bytes图片对象"""
        if self.type == 'folder':
            with open(self.path, 'rb') as pr:
                img_bytes = pr.read()
                return img_bytes
        elif self.type == 'archive':
            img_bytes = function_archive.read_image(self.comic_path, self.path)
            return img_bytes
        else:
            return b''

    def update_hash(self, hash_dict: dict):
        """根据hash字典更新hash"""
        self.ahash = hash_dict['ahash']
        self.phash = hash_dict['phash']
        self.dhash = hash_dict['dhash']

    def get_hash(self, hash_: str) -> Union[str, None]:
        """获取指定的hash值"""
        if hash_ == 'ahash':
            return self.ahash
        elif hash_ == 'phash':
            return self.phash
        elif hash_ == 'dhash':
            return self.dhash
        else:
            return None

    def set_filesize(self, filesize: int):
        """设置大小（不更新其他参数）"""
        self.filesize = filesize

    def set_type(self, type_: str):
        """设置类型（不更新其他参数）"""
        self.type = type_
        self._set_fake_path()

    def set_ahash(self, ahash: str):
        """设置hash（不更新其他参数）"""
        self.ahash = ahash

    def set_phash(self, phash: str):
        """设置hash（不更新其他参数）"""
        self.phash = phash

    def set_dhash(self, dhash: str):
        """设置hash（不更新其他参数）"""
        self.dhash = dhash

    def set_comic_path(self, comic_path):
        """设置漫画路径（不更新其他参数）"""
        self.comic_path = comic_path
        self._set_fake_path()

    def _set_fake_path(self):
        """设置虚拟路径"""
        if self.type == 'archive':
            self.fake_path = os.path.normpath(os.path.join(self.comic_path, self.path))  # 拼接虚拟路径
        elif self.type == 'archive':
            self.fake_path = self.path

    def _get_image_size(self) -> int:
        """获取图片文件大小"""
        if self.type == 'folder':
            filesize = os.path.getsize(self.path)
        elif self.type == 'archive':
            filesize = function_archive.get_image_size(self.comic_path, self.path)
        else:
            return 0

        return filesize


def create_default_sqlite():
    """创建初始数据库"""
    if not os.path.exists(_IMAGE_INFO_DB):
        conn = sqlite3.connect(_IMAGE_INFO_DB)
        cursor = conn.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} '
                       f'({_KEY_FAKE_PATH} TEXT Primary KEY, {_KEY_PATH} TEXT, {_KEY_FILESIZE} INTEGER, '
                       f'{_KEY_COMIC_PATH} TEXT, {_KEY_TYPE} TEXT, '
                       f'{_KEY_AHASH_64} TEXT,{_KEY_AHASH_144} TEXT,{_KEY_AHASH_256} TEXT, '
                       f'{_KEY_PHASH_64} TEXT,{_KEY_PHASH_144} TEXT,{_KEY_PHASH_256} TEXT, '
                       f'{_KEY_DHASH_64} TEXT,{_KEY_DHASH_144} TEXT,{_KEY_DHASH_256} TEXT'
                       f')')


def read_db(hash_length: int = 64):
    """读取数据库中所有图片的指定长度hash数据
    :param hash_length: int，hash值的长度
    :return: dict，key为图片虚拟路径，value为image_info类"""
    function_normal.print_function_info()
    # 读取数据库
    conn = sqlite3.connect(_IMAGE_INFO_DB)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {_TABLE_NAME}')
    data = cursor.fetchall()
    columns_name = [i[0] for i in cursor.description]
    data_dict = [dict(zip(columns_name, row)) for row in data]
    # 写入字典
    image_info_dict = {}
    for item_dict in data_dict:
        image_path = item_dict[_KEY_PATH]
        image_info = ImageInfo(image_path)
        image_info.set_filesize(int(item_dict[_KEY_FILESIZE]))
        image_info.set_comic_path(item_dict[_KEY_COMIC_PATH])
        image_info.set_type(item_dict[_KEY_TYPE])
        # 处理hash值为None的文本值的情况，将其转换为NoneType
        ahash_ = item_dict[f'{_KEY_AHASH}{hash_length}']
        if ahash_ == 'None':
            ahash_ = None
        image_info.set_ahash(ahash_)
        phash_ = item_dict[f'{_KEY_PHASH}{hash_length}']
        if phash_ == 'None':
            phash_ = None
        image_info.set_phash(phash_)
        dhash_ = item_dict[f'{_KEY_DHASH}{hash_length}']
        if dhash_ == 'None':
            dhash_ = None
        image_info.set_dhash(dhash_)

        # 写入字典（注意：key为图片虚拟路径）
        image_info_dict[image_info.fake_path] = image_info

    return image_info_dict


def update_db(image_info_dict: dict):
    """更新数据库（增量更新）
    :param image_info_dict: dict，key为虚拟图片路径，value为image_info类"""
    function_normal.print_function_info()
    # 读取数据库中的所有图片路径
    conn = sqlite3.connect(_IMAGE_INFO_DB)
    cursor = conn.cursor()
    cursor.execute(f'SELECT {_KEY_FAKE_PATH} FROM {_TABLE_NAME}')
    data = cursor.fetchall()
    cache_image_paths = [i[0] for i in data]
    # 增量更新
    for fake_image_path, image_info in image_info_dict.items():
        if fake_image_path not in cache_image_paths:
            cursor.execute(f'INSERT INTO {_TABLE_NAME} ({_KEY_FAKE_PATH}) VALUES ("{fake_image_path}")')
        cursor.execute(f'UPDATE {_TABLE_NAME} SET {_KEY_PATH} = "{image_info.path}" '
                       f'WHERE {_KEY_FAKE_PATH} = "{fake_image_path}"')
        cursor.execute(f'UPDATE {_TABLE_NAME} SET {_KEY_FILESIZE} = "{image_info.filesize}" '
                       f'WHERE {_KEY_FAKE_PATH} = "{fake_image_path}"')
        cursor.execute(f'UPDATE {_TABLE_NAME} SET {_KEY_COMIC_PATH} = "{image_info.comic_path}" '
                       f'WHERE {_KEY_FAKE_PATH} = "{fake_image_path}"')
        cursor.execute(f'UPDATE {_TABLE_NAME} SET {_KEY_TYPE} = "{image_info.type}" '
                       f'WHERE {_KEY_FAKE_PATH} = "{fake_image_path}"')
        # hash值特殊处理 按位数更新至对应列
        if isinstance(image_info.ahash, str) and len(image_info.ahash) > 16:
            cursor.execute(f'UPDATE {_TABLE_NAME} '
                           f'SET {_KEY_AHASH + str(len(image_info.ahash))} = "{image_info.ahash}" '
                           f'WHERE {_KEY_FAKE_PATH} = "{fake_image_path}"')
        if isinstance(image_info.phash, str) and len(image_info.phash) > 16:
            cursor.execute(f'UPDATE {_TABLE_NAME} '
                           f'SET {_KEY_PHASH + str(len(image_info.phash))} = "{image_info.phash}" '
                           f'WHERE {_KEY_FAKE_PATH} = "{fake_image_path}"')
        if isinstance(image_info.dhash, str) and len(image_info.dhash) > 16:
            cursor.execute(f'UPDATE {_TABLE_NAME} '
                           f'SET {_KEY_DHASH + str(len(image_info.dhash))} = "{image_info.dhash}" '
                           f'WHERE {_KEY_FAKE_PATH} = "{fake_image_path}"')

    cursor.close()
    conn.commit()
    conn.close()


def delete_useless_item():
    """删除数据库中无效的数据"""
    function_normal.print_function_info()
    conn = sqlite3.connect(_IMAGE_INFO_DB)
    cursor = conn.cursor()

    image_info_dict = read_db()  # 读取的数据库数据
    for _, image_info in image_info_dict.items():
        image_info: ImageInfo
        image_path = image_info.path
        filesize = image_info.filesize
        comic_path = image_info.comic_path
        comic_type = image_info.type
        if comic_type == 'folder':  # 漫画类型是文件夹时，直接检查本地文件
            if os.path.exists(image_path) and function_normal.get_size(image_path) == filesize:
                continue
        elif comic_type == 'archive':  # 漫画类型是压缩包时，检查压缩包是否存在和内部图片大小
            if os.path.exists(comic_path) and function_archive.get_image_size(comic_path, image_path) == filesize:
                continue
        # 路径外的引号必须使用“双引号，防止字符串自动转换引号导致出错（Windows文件名可以带'而不能带"）
        cursor.execute(f'''DELETE FROM {_TABLE_NAME} WHERE {_KEY_PATH}="{image_path}"''')

    cursor.close()
    conn.commit()
    conn.close()


def delete_item_by_comic(comic_path_deleted: str):
    """删除指定漫画路径对应的图片项数据"""
    function_normal.print_function_info()
    conn = sqlite3.connect(_IMAGE_INFO_DB)
    cursor = conn.cursor()
    # 路径外的引号必须使用“双引号，防止字符串自动转换引号导致出错（Windows文件名可以带'而不能带"）
    cursor.execute(f'''DELETE FROM {_TABLE_NAME} WHERE {_KEY_COMIC_PATH}="{comic_path_deleted}"''')

    cursor.close()
    conn.commit()
    conn.close()
