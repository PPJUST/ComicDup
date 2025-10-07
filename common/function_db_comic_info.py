# 数据库方法
import os
import sqlite3
from typing import Union

from common.class_comic import ComicInfo
from common.class_config import FileType

DB_FILEPATH = 'DBComicInfo.db3'
TABLE_NAME = 'ComicInfo'
KEY_FILEPATH = 'filepath'  # 文件路径（主键）
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
KEY_FINGERPRINT = 'fingerprint'  # 文件指纹（格式为文件大小bytes+内部文件路径，以|间隔）

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

    @staticmethod
    def check_exist(db_file: str = DB_FILEPATH):
        """检查初始数据库是否存在"""
        if not os.path.exists(db_file):
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '  # 表名
                           f'({KEY_FILEPATH} TEXT Primary KEY,'  # 文件路径
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
                           f'{KEY_FINGERPRINT} TEXT'  # 文件指纹 
                           f')')

            conn.commit()
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

        self.cursor.execute(f'UPDATE {TABLE_NAME} SET {KEY_FINGERPRINT} = "{comic_info.fingerprint}" '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}"')

        self.conn.commit()

    def update_comic_moved(self, comic_info: ComicInfo):
        """更新数据库中已移动路径的漫画，更新其最新路径（仅更新数据库中的第一个匹配项）"""
        # 提取漫画数据库中文件指纹对应的路径
        comic_paths_db = self.get_comic_paths_by_fingerprint(comic_info.fingerprint)
        # 更新首个不存在路径的数据，并删除该失效项
        comic_path_deleted = ''  # 被删除的漫画路径
        for path in comic_paths_db:
            if not os.path.exists(path):
                comic_path_deleted = path
                self.delete(path)
                self.add(comic_info)
                break
        return comic_path_deleted

    def delete(self, comic_path: str):
        """删除记录"""
        comic_path = os.path.normpath(comic_path)

        # 路径外的引号必须使用“双引号，防止字符串自动转换引号导致出错（Windows文件名可以带'而不能带"）
        self.cursor.execute(f'''DELETE FROM {TABLE_NAME} WHERE {KEY_FILEPATH} = "{comic_path}"''')
        self.conn.commit()

    def get_comic_info_by_comic_path(self, comic_path: str):
        """根据漫画文件路径获取漫画信息类"""
        comic_path = os.path.normpath(comic_path)

        self.cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE {KEY_FILEPATH} = "{comic_path}"')

        # 获取列名
        columns = [desc[0] for desc in self.cursor.description]

        # 获取结果列表
        result = self.cursor.fetchone()

        # 转换为漫画信息类
        result_dict = dict(zip(columns, result))  # 先转为键名-键值的字典格式
        comic_info = ComicInfo(comic_path, db_model=True)
        # 文件大小
        filesize_bytes = result_dict[KEY_FILESIZE_BYTES]
        filesize_bytes_extracted = result_dict[KEY_FILESIZE_BYTES_EXTRACTED]
        comic_info.update_filesize(filesize_bytes)
        comic_info.update_filesize_extracted(filesize_bytes_extracted)
        # 文件类型
        filetype_str = result_dict[KEY_FILETYPE]
        if filetype_str == FileType.Folder.text:
            filetype_class = FileType.Folder()
        elif filetype_str == FileType.Archive.text:
            filetype_class = FileType.Archive()
        elif filetype_str == FileType.File.text:
            filetype_class = FileType.File()
        else:
            raise Exception('漫画文件类型错误')
        comic_info.update_filetype(filetype_class)
        # 文件修改时间
        modified_time = result_dict[KEY_MODIFIED_TIME]
        comic_info.update_modified_time(modified_time)
        # 漫画页路径列表
        page_paths = convert_str_to_list(result_dict[KEY_PAGE_PATHS])
        comic_info.update_page_paths(page_paths)
        # 漫画预览小图路径
        preview_path = result_dict[KEY_PREVIEW_PATH]
        comic_info.update_preview_path(preview_path)
        # 文件指纹
        fingerprint = result_dict[KEY_FINGERPRINT]
        comic_info.update_fingerprint(fingerprint)

        return comic_info

    def get_comic_paths_by_fingerprint(self, fingerprint: str):
        """根据文件指纹获取所有漫画路径"""
        self.cursor.execute(f'SELECT {KEY_FILEPATH} FROM {TABLE_NAME} WHERE {KEY_FINGERPRINT} = "{fingerprint}"')
        result = self.cursor.fetchall()
        paths = [item[0] for item in result]
        paths = list(set(paths))
        return paths

    def is_comic_exist(self, comic_path: str, comic_fingerprint: str):
        """检查漫画在数据库中是否已存在
        同时使用路径和文件指纹判断"""
        comic_path = os.path.normpath(comic_path)
        self.cursor.execute(f'SELECT 1 FROM {TABLE_NAME} WHERE {KEY_FILEPATH} = "{comic_path}"')
        self.cursor.execute(f'SELECT 1 FROM {TABLE_NAME} '
                            f'WHERE {KEY_FILEPATH} = "{comic_path}" '
                            f'AND {KEY_FINGERPRINT} = "{comic_fingerprint}"')
        result = self.cursor.fetchone()
        print('检查漫画在数据库中是否已存在', comic_path, result)
        if result:
            return True
        else:
            return False

    def is_comic_moved(self, comic_fingerprint: str, comic_path: str):
        """检查已存在的漫画指纹，其对应的漫画路径是否已移动
        根据传入的漫画路径进行判断"""
        comic_path = os.path.normpath(comic_path)
        # 获取数据库中指纹对应的漫画路径列表
        comic_paths_in_db = self.get_comic_paths_by_fingerprint(comic_fingerprint)
        # 与传入路径匹配
        is_path_exist = not comic_path in comic_paths_in_db

        print('检查已存在的漫画指纹，其对应的漫画路径是否已移动', comic_path, is_path_exist)
        return is_path_exist

    def is_comic_path_exist(self, comic_path: str):
        """检查漫画路径在数据库中是否已存在"""
        comic_path = os.path.normpath(comic_path)
        self.cursor.execute(f'SELECT 1 FROM {TABLE_NAME} WHERE {KEY_FILEPATH} = "{comic_path}"')
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False

    def is_comic_exist_by_fingerprint(self, comic_fingerprint: str):
        """检查漫画指纹在数据库中是否已存在"""
        self.cursor.execute(f'SELECT 1 FROM {TABLE_NAME} WHERE {KEY_FINGERPRINT} = "{comic_fingerprint}"')
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
