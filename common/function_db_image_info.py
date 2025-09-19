# 数据库方法
import os
import sqlite3

from common.class_comic import ImageInfo
from common.class_config import SimilarAlgorithm

"""漫画信息数据库"""
DB_FILEPATH = 'DBImageInfo.db3'
KEY_FAKE_PATH = 'fake_path'  # 虚拟路径，组合漫画路径与图片路径，用于处理压缩文件类漫画
TABLE_NAME = 'ImageInfo'
KEY_FILEPATH = 'filepath'  # 图片路径
KEY_FILESIZE_BYTES = 'filesize_bytes'  # 文件大小（字节）
KEY_AHASH_64 = 'aHash_64'  # 均值哈希（64位）
KEY_AHASH_144 = 'aHash_144'  # 均值哈希（144位）
KEY_AHASH_256 = 'aHash_256'  # 均值哈希（256位）
KEY_PHASH_64 = 'pHash_64'  # 感知哈希（64位）
KEY_PHASH_144 = 'pHash_144'  # 感知哈希（144位）
KEY_PHASH_256 = 'pHash_256'  # 感知哈希（256位）
KEY_DHASH_64 = 'dHash_64'  # 差异哈希（64位）
KEY_DHASH_144 = 'dHash_144'  # 差异哈希（144位）
KEY_DHASH_256 = 'dHash_256'  # 差异哈希（256位）
KEY_COMIC_PATH_BELONG = 'comic_path_belong'  # 图片所属漫画的路径
KEY_COMIC_FILETYPE_BELONG = 'comic_filetype_belong'  # # 图片所属漫画的文件类型


class DBImageInfo:
    """图片信息数据库
    主键为图片路径"""

    def __init__(self, db_file: str = DB_FILEPATH):
        self.check_exist()

        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def check_exist(self, db_file: str = DB_FILEPATH):
        """检查初始数据库是否存在"""
        if not os.path.exists(db_file):
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '  # 表名
                           f'({KEY_FILEPATH} TEXT,'  # 图片路径
                           f'{KEY_FAKE_PATH} TEXT Primary KEY,'  # 虚拟路径，组合漫画路径与图片路径，用于处理压缩文件类漫画
                           f'{KEY_FILESIZE_BYTES} INTEGER,'  # 文件大小（字节）
                           f'{KEY_AHASH_64} TEXT,'  # 均值哈希（64位）
                           f'{KEY_AHASH_144} TEXT,'  # 均值哈希（144位）
                           f'{KEY_AHASH_256} TEXT,'  # 均值哈希（256位）
                           f'{KEY_PHASH_64} TEXT,'  # 感知哈希（64位）
                           f'{KEY_PHASH_144} TEXT,'  # 感知哈希（144位）
                           f'{KEY_PHASH_256} TEXT,'  # 感知哈希（256位）
                           f'{KEY_DHASH_64} TEXT,'  # 差异哈希（64位）
                           f'{KEY_DHASH_144} TEXT,'  # 差异哈希（144位）
                           f'{KEY_DHASH_256} TEXT,'  # 差异哈希（256位）
                           f'{KEY_COMIC_PATH_BELONG} TEXT,'  # 图片所属漫画的路径
                           f'{KEY_COMIC_FILETYPE_BELONG} TEXT,'  # 图片所属漫画的文件类型
                           f')')

            cursor.close()
            conn.close()

    def add(self, image_info: ImageInfo):
        """添加/更新记录"""
        # 组合漫画路径与图片路径，用于处理压缩文件类漫画
        image_path = os.path.normpath(image_info.image_path)
        comic_path = os.path.normpath(image_info.comic_path_belong)
        fake_path = os.path.normpath(os.path.join(comic_path, os.path.basename(image_path)))

        self.cursor.execute(f'INSERT OR IGNORE INTO {TABLE_NAME} ({KEY_FAKE_PATH}) VALUES ("{fake_path}")')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_FILEPATH} = "{image_path}" '
                            f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_FILESIZE_BYTES} = "{image_info.filesize}" '
                            f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        # 只更新存在的hash值
        ahash_64 = image_info.get_hash(SimilarAlgorithm.aHash, 64)
        if ahash_64:
            self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_AHASH_64} = "{ahash_64}" '
                                f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')
        ahash_144 = image_info.get_hash(SimilarAlgorithm.aHash, 144)
        if ahash_144:
            self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_AHASH_144} = "{ahash_144}" '
                                f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')
        ahash_256 = image_info.get_hash(SimilarAlgorithm.aHash, 256)
        if ahash_256:
            self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_AHASH_256} = "{ahash_256}" '
                                f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        phash_64 = image_info.get_hash(SimilarAlgorithm.pHash, 64)
        if phash_64:
            self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_PHASH_64} = "{phash_64}" '
                                f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')
        phash_144 = image_info.get_hash(SimilarAlgorithm.pHash, 144)
        if phash_144:
            self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_PHASH_144} = "{phash_144}" '
                                f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')
        phash_256 = image_info.get_hash(SimilarAlgorithm.pHash, 256)
        if phash_256:
            self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_PHASH_256} = "{phash_256}" '
                                f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        dhash_64 = image_info.get_hash(SimilarAlgorithm.dHash, 64)
        if dhash_64:
            self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_DHASH_64} = "{dhash_64}" '
                                f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')
        dhash_144 = image_info.get_hash(SimilarAlgorithm.dHash, 144)
        if dhash_144:
            self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_DHASH_144} = "{dhash_144}" '
                                f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')
        dhash_256 = image_info.get_hash(SimilarAlgorithm.dHash, 256)
        if dhash_256:
            self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_DHASH_256} = "{dhash_256}" '
                                f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_COMIC_PATH_BELONG} = "{image_info.comic_path_belong}" '
                            f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        self.cursor.execute(
            f'UPDATE {TABLE_NAME} SET {KEY_COMIC_FILETYPE_BELONG} = "{image_info.comic_filetype_belong}" '
            f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        self.conn.commit()

    def delete(self, image_path: str, comic_path: str):
        """删除记录"""
        fake_path = os.path.normpath(os.path.join(comic_path, os.path.basename(image_path)))

        # 路径外的引号必须使用“双引号，防止字符串自动转换引号导致出错（Windows文件名可以带'而不能带"）
        self.cursor.execute(f'''DELETE FROM {TABLE_NAME} WHERE {KEY_FAKE_PATH} = "{fake_path}"''')
        self.conn.commit()

    def get(self):
        """获取记录"""
        # 备忘录

    def is_image_exist(self, image_path: str, comic_path: str):
        """检查漫画路径在数据库中是否已存在"""
        fake_path = os.path.normpath(os.path.join(comic_path, os.path.basename(image_path)))

        self.cursor.execute(f'SELECT 1 FROM {TABLE_NAME} WHERE {KEY_FAKE_PATH} = "{fake_path}"')
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
