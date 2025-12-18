# 数据库方法
import os
import sqlite3
from typing import List, Tuple

import lzytools

from common import function_file
from common.class_config import SimilarAlgorithm, TYPES_HASH_ALGORITHM, FileType
from common.class_image import ImageInfoBase, ImageInfoFolder, ImageInfoArchive

DB_FILEPATH = 'DBImageInfo.db3'
TABLE_NAME = 'ImageInfo'
KEY_FILEPATH = 'filepath'  # 图片路径
KEY_FAKE_PATH = 'fake_path'  # 虚拟路径，组合漫画路径与图片路径，用于处理压缩文件类漫画（主键）
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
KEY_BELONG_COMIC_PATH = 'belong_comic_path'  # 图片所属漫画的路径
KEY_BELONG_COMIC_FILETYPE = 'belong_comic_filetype'  # 图片所属漫画的文件类型
KEY_BELONG_COMIC_FINGERPRINT = 'belong_comic_fingerprint'  # 图片所属漫画的文件指纹


class DBImageInfo:
    """图片信息数据库
    主键为图片路径"""

    def __init__(self, db_file: str = DB_FILEPATH):
        self.db_filepath = db_file
        self.check_exist(db_file)
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
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
                           f'{KEY_BELONG_COMIC_PATH} TEXT,'  # 图片所属漫画的路径
                           f'{KEY_BELONG_COMIC_FILETYPE} TEXT,'  # 图片所属漫画的文件类型
                           f'{KEY_BELONG_COMIC_FINGERPRINT} TEXT'
                           f')')

            conn.commit()
            cursor.close()
            conn.close()

    def add(self, image_info: ImageInfoBase):
        """添加/更新记录"""
        # 组合漫画路径与图片路径，用于处理压缩文件类漫画
        image_path = os.path.normpath(image_info.image_path)
        comic_path = os.path.normpath(image_info.belong_comic_path)
        fake_path = os.path.normpath(os.path.join(comic_path, os.path.basename(image_path)))

        self.cursor.execute(f'INSERT OR IGNORE INTO {TABLE_NAME} ({KEY_FAKE_PATH}) VALUES ("{fake_path}")')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_FILEPATH} = "{image_path}" '
                            f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_FILESIZE_BYTES} = "{image_info.filesize}" '
                            f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        # 只更新存在的hash值
        ahash_64 = image_info.get_hash(SimilarAlgorithm.aHash(), 64)
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

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_BELONG_COMIC_PATH} = "{image_info.belong_comic_path}" '
                            f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        self.cursor.execute(
            f'UPDATE {TABLE_NAME} SET {KEY_BELONG_COMIC_FILETYPE} = "{image_info.belong_comic_filetype.text}" '
            f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        self.cursor.execute(
            f'UPDATE {TABLE_NAME} SET {KEY_BELONG_COMIC_FINGERPRINT} = "{image_info.belong_comic_fingerprint}" '
            f'WHERE {KEY_FAKE_PATH} = "{fake_path}"')

        self.conn.commit()

    def update_belong_comic_moved(self, comic_fingerprint: str, old_comic_path: str, new_comic_path: str):
        """更新数据库中已移动路径的漫画对应的图片路径，更新其最新路径"""
        # 先检查新的漫画路径是否已经存在且文件指纹不同，如果符合则删除
        db_fingerprints_new_path = self.get_belong_comic_fingerprint_by_belong_comic_path(new_comic_path)
        for fingerprint in db_fingerprints_new_path:
            if fingerprint != comic_fingerprint:
                # 路径外的引号必须使用“双引号，防止字符串自动转换引号导致出错（Windows文件名可以带'而不能带"）
                self.cursor.execute(f'''DELETE FROM {TABLE_NAME} 
                WHERE {KEY_BELONG_COMIC_PATH} = "{new_comic_path}" 
                AND {KEY_BELONG_COMIC_FINGERPRINT} = "{fingerprint}"''')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_BELONG_COMIC_PATH} = "{new_comic_path}" '
                            f'WHERE {KEY_BELONG_COMIC_PATH} = "{old_comic_path}" '
                            f'AND {KEY_BELONG_COMIC_FINGERPRINT} = "{comic_fingerprint}"')

        self.conn.commit()

    def delete(self, image_path: str, comic_path: str):
        """删除记录"""
        fake_path = os.path.normpath(os.path.join(comic_path, os.path.basename(image_path)))

        # 路径外的引号必须使用“双引号，防止字符串自动转换引号导致出错（Windows文件名可以带'而不能带"）
        self.cursor.execute(f'''DELETE FROM {TABLE_NAME} WHERE {KEY_FAKE_PATH} = "{fake_path}"''')

        self.conn.commit()

        self._vacuum()

    def delete_useless_items(self):
        """删除无效的项目"""
        # 提取所有图片路径以及对应的漫画路径、类型
        self.cursor.execute(
            f'SELECT {KEY_FILEPATH}, {KEY_BELONG_COMIC_PATH}, {KEY_BELONG_COMIC_FILETYPE} FROM {TABLE_NAME}')
        # 组合为一个字典
        image_infos = {path[0]: (path[1], path[2]) for path in self.cursor.fetchall()}
        for image_path, (comic_path, comic_filetype) in image_infos.items():
            if comic_filetype == FileType.Folder.text:
                if not os.path.exists(image_path):
                    self.delete(image_path, comic_path)
            elif comic_filetype == FileType.Archive.text:
                if not os.path.exists(comic_path):
                    self.delete(image_path, comic_path)

    def get_image_info_by_hash(self, hash_: str, hash_type: TYPES_HASH_ALGORITHM) -> List[ImageInfoBase]:
        """根据hash值获取图片信息类"""
        hash_length = len(hash_)
        if isinstance(hash_type, SimilarAlgorithm.aHash):
            key_hash = KEY_AHASH_64.replace('64', str(hash_length))
        elif isinstance(hash_type, SimilarAlgorithm.pHash):
            key_hash = KEY_PHASH_64.replace('64', str(hash_length))
        elif isinstance(hash_type, SimilarAlgorithm.dHash):
            key_hash = KEY_DHASH_64.replace('64', str(hash_length))
        else:
            raise Exception('未知的hash类型')

        self.cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE {key_hash} = "{hash_}"')

        # 获取列名
        columns = [desc[0] for desc in self.cursor.description]

        # 获取结果列表
        results = self.cursor.fetchall()

        # 转换为图片信息类
        results_image_info: List[ImageInfoBase] = []
        for result in results:
            result_dict = dict(zip(columns, result))  # 先转为键名-键值的字典格式

            #  提取图片所属漫画的类型，并生成漫画信息类实例
            belong_comic_filetype_str = result_dict[KEY_BELONG_COMIC_FILETYPE]
            if belong_comic_filetype_str == FileType.Folder.text:
                image_info = ImageInfoFolder(image_path=result_dict[KEY_FILEPATH])
            elif belong_comic_filetype_str == FileType.Archive.text:
                image_info = ImageInfoArchive(image_path=result_dict[KEY_FILEPATH])
            else:
                raise Exception('漫画文件类型错误')

            # 图片大小
            filesize = result_dict[KEY_FILESIZE_BYTES]
            image_info.update_filesize(filesize)

            # 图片所属
            belong_comic_path = result_dict[KEY_BELONG_COMIC_PATH]
            image_info.update_belong_comic_path(belong_comic_path)
            belong_comic_fingerprint = result_dict[KEY_BELONG_COMIC_FINGERPRINT]
            image_info.update_belong_comic_fingerprint(belong_comic_fingerprint)

            # hash值
            ahash_64 = result_dict[KEY_AHASH_64]
            if ahash_64:
                image_info.update_hash(ahash_64, SimilarAlgorithm.aHash, len(ahash_64))
            ahash_144 = result_dict[KEY_AHASH_144]
            if ahash_144:
                image_info.update_hash(ahash_144, SimilarAlgorithm.aHash, len(ahash_144))
            ahash_256 = result_dict[KEY_AHASH_256]
            if ahash_256:
                image_info.update_hash(ahash_256, SimilarAlgorithm.aHash, len(ahash_256))
            phash_64 = result_dict[KEY_PHASH_64]
            if phash_64:
                image_info.update_hash(phash_64, SimilarAlgorithm.pHash, len(phash_64))
            phash_144 = result_dict[KEY_PHASH_144]
            if phash_144:
                image_info.update_hash(phash_144, SimilarAlgorithm.pHash, len(phash_144))
            phash_256 = result_dict[KEY_PHASH_256]
            if phash_256:
                image_info.update_hash(phash_256, SimilarAlgorithm.pHash, len(phash_256))
            dhash_64 = result_dict[KEY_DHASH_64]
            if dhash_64:
                image_info.update_hash(dhash_64, SimilarAlgorithm.dHash, len(dhash_64))
            dhash_144 = result_dict[KEY_DHASH_144]
            if dhash_144:
                image_info.update_hash(dhash_144, SimilarAlgorithm.dHash, len(dhash_144))
            dhash_256 = result_dict[KEY_DHASH_256]
            if dhash_256:
                image_info.update_hash(dhash_256, SimilarAlgorithm.dHash, len(dhash_256))

            results_image_info.append(image_info)

        return results_image_info

    def get_fake_path_by_belong_comic(self, comic_path: str, comic_fingerprint: str):
        """根据所属漫画信息获取主键虚拟路径"""
        self.cursor.execute(f'SELECT {KEY_FAKE_PATH} FROM {TABLE_NAME} '
                            f'WHERE {KEY_BELONG_COMIC_PATH} = "{comic_path}" '
                            f'AND {KEY_BELONG_COMIC_FINGERPRINT} = "{comic_fingerprint}"')
        result = self.cursor.fetchall()
        paths = [item[0] for item in result]
        paths = list(set(paths))
        return paths

    def get_belong_comic_path_by_belong_comic_fingerprint(self, comic_fingerprint: str):
        """根据所属漫画的指纹获取数据库中对应的漫画路径"""
        self.cursor.execute(f'SELECT {KEY_BELONG_COMIC_PATH} FROM {TABLE_NAME} '
                            f'WHERE{KEY_BELONG_COMIC_FINGERPRINT} = "{comic_fingerprint}"')
        result = self.cursor.fetchall()
        paths = [item[0] for item in result]
        paths = list(set(paths))
        return paths

    def get_belong_comic_fingerprint_by_belong_comic_path(self, comic_path: str):
        """根据所属漫画的路径获取数据库中对应的指纹"""
        self.cursor.execute(f'SELECT {KEY_BELONG_COMIC_PATH} FROM {TABLE_NAME} '
                            f'WHERE {KEY_BELONG_COMIC_PATH} = "{comic_path}"')
        result = self.cursor.fetchall()
        fingerprints = [item[0] for item in result]
        fingerprints = list(set(fingerprints))
        return fingerprints

    def get_hashs(self, hash_algorithm: TYPES_HASH_ALGORITHM, hash_length: int) -> List[str]:
        """获取所有图片的hash值"""
        if isinstance(hash_algorithm, SimilarAlgorithm.aHash):
            key_hash = KEY_AHASH_64.replace('64', str(hash_length))
        elif isinstance(hash_algorithm, SimilarAlgorithm.pHash):
            key_hash = KEY_PHASH_64.replace('64', str(hash_length))
        elif isinstance(hash_algorithm, SimilarAlgorithm.dHash):
            key_hash = KEY_DHASH_64.replace('64', str(hash_length))
        else:
            raise Exception('未知的hash类型')

        self.cursor.execute(f'SELECT {KEY_BELONG_COMIC_PATH}, {key_hash} FROM {TABLE_NAME}')
        results: List[Tuple[str, str]] = self.cursor.fetchall()

        hashs = []
        for result in results:
            comic_path = result[0]
            hash_value = result[1]
            if os.path.exists(comic_path):  # 仅获取存在的漫画数据
                hashs.append(hash_value)
        return hashs

    def is_image_exist(self, image_path: str, comic_path: str):
        """检查漫画路径在数据库中是否已存在"""
        fake_path = os.path.normpath(os.path.join(comic_path, os.path.basename(image_path)))

        self.cursor.execute(f'SELECT 1 FROM {TABLE_NAME} WHERE {KEY_FAKE_PATH} = "{fake_path}"')
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False

    def get_info_item_count(self) -> int:
        """统计数据库中记录的图片数量"""
        self.cursor.execute(f'SELECT COUNT(*) FROM {TABLE_NAME}')
        result = self.cursor.fetchone()
        return result[0]

    def get_info_db_size(self) -> str:
        """获取数据库文件大小"""
        size_bytes = os.path.getsize(self.db_filepath)
        size = function_file.format_bytes_size(size_bytes)
        return size

    def get_info_update_time(self) -> str:
        """获取数据库文件最后修改时间"""
        modified_time = os.path.getmtime(self.db_filepath)
        modified_time_str = lzytools.time.convert_duration_to_date(modified_time)
        return modified_time_str

    def clear(self):
        """清空数据库"""
        print('清空数据库')
        self.cursor.execute(f"DELETE FROM {TABLE_NAME};")
        self.conn.commit()
        self._vacuum()

    def _vacuum(self):
        """手动清除空闲列表数据"""
        self.cursor.execute('VACUUM')
