# 数据库方法
import os
import sqlite3
from typing import Union

from common.class_comic import ComicInfo

"""漫画信息数据库"""
DB_FILEPATH = 'DBComicInfo.db3'
TABLE_NAME = 'ComicInfo'
KEY_FILEPATH = 'filepath'  # 文件路径
KEY_FILENAME = 'filename'  # 文件名（含扩展名）
KEY_FILETITLE = 'filetitle'  # 文件标题（不含扩展名）
KEY_PARENT_DIRPATH = 'parent_dirpath'  # 文件父级路径
KEY_FILESIZE_BYTES = 'filesize_bytes'  # 文件大小（字节）
KEY_FILESIZE_BYTES_EXTRACTED = 'filesize_bytes_extracted'  # 文件真实大小（字节）
KEY_FILETYPE = 'filetype'  # 文件类型
KEY_MODIFIED_TIME = 'modified_time'  # 文件修改时间（自纪元以来的秒数）
KEY_PAGE_PATHS = 'page_paths'  # 内部文件路径
KEY_PAGE_COUNT = 'page_count'  # 页数
KEY_PREVIEW_PATH = 'preview_path'  # 预览小图本地路径

CONVERT_KEY = '|'  # 用于列表与字符串相互转换的分隔符


def convert_list_to_str(lst: Union[list, tuple]):
    """将列表转换为字符串"""
    return CONVERT_KEY.join(lst)


def convert_str_to_list(str_: str):
    """将字符串还原为列表"""
    return str_.split(CONVERT_KEY)


class DBComicInfo:
    """漫画信息数据库
    主键为漫画路径"""

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
                           f'({KEY_FILEPATH} TEXT Primary KEY, '  # 文件路径
                           f'{KEY_FILENAME} TEXT,'  # 文件名（含扩展名）
                           f'{KEY_FILETITLE} TEXT,'  # 文件标题（不含扩展名）
                           f'{KEY_PARENT_DIRPATH} TEXT,'  # 文件父级路径
                           f'{KEY_FILESIZE_BYTES} INTEGER,'  # 文件大小（字节）
                           f'{KEY_FILESIZE_BYTES_EXTRACTED} INTEGER,'  # 文件真实大小（字节）
                           f'{KEY_FILETYPE} TEXT,'  # 文件类型
                           f'{KEY_MODIFIED_TIME} REAL,'  # 文件修改时间（自纪元以来的秒数）
                           f'{KEY_PAGE_PATHS} TEXT,'  # 内部文件路径
                           f'{KEY_PAGE_COUNT} INTEGER,'  # 页数
                           f'{KEY_PREVIEW_PATH} TEXT,'  # 预览小图本地路径
                           f')')

            cursor.close()
            conn.close()

    def add(self, comic_info: ComicInfo):
        """添加/更新记录"""
        comic_path = os.path.normpath(comic_info.filepath)

        self.cursor.execute(f'INSERT OR IGNORE INTO {TABLE_NAME} ({KEY_FILEPATH}) VALUES ("{comic_path}")')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_FILENAME} = "{comic_info.filename}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_FILETITLE} = "{comic_info.filetitle}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_PARENT_DIRPATH} = "{comic_info.parent_dirpath}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_FILESIZE_BYTES} = "{comic_info.filesize_bytes}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        self.cursor.execute(
            f'UPDATE {TABLE_NAME} SET {KEY_FILESIZE_BYTES_EXTRACTED} = "{comic_info.filesize_bytes_extracted}" '
            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        filetype = comic_info.filetype
        filetype_str = filetype.text
        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_FILETYPE} = "{filetype_str}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_MODIFIED_TIME} = "{comic_info.modified_time}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        # 内部文件路径进行特殊处理
        paths = comic_info.page_paths
        str_paths = convert_list_to_str(paths)
        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_PAGE_PATHS} = "{str_paths}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_PAGE_COUNT} = "{comic_info.page_count}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_PREVIEW_PATH} = "{comic_info.preview_path}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        self.conn.commit()

    def delete(self, comic_path: str):
        """删除记录"""
        comic_path = os.path.normpath(comic_path)

        # 路径外的引号必须使用“双引号，防止字符串自动转换引号导致出错（Windows文件名可以带'而不能带"）
        self.cursor.execute(f'''DELETE FROM {TABLE_NAME} WHERE {KEY_FILEPATH} = "{comic_path}"''')
        self.conn.commit()

    def get(self):
        """获取记录"""
        # 备忘录

    def is_comic_exist(self, comic_path: str):
        """检查漫画路径在数据库中是否已存在"""
        self.cursor.execute(f'SELECT 1 FROM {TABLE_NAME} WHERE {KEY_FILEPATH} = "{comic_path}"')
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
