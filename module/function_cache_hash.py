# 图像hash缓存的方法
"""
hash缓存数据库说明：
数据库使用sqlite3，主键为图片文件路径path，列名为filesize，图片文件大小int，comic_path，漫画路径str，ahash等，哈希值str
"""
import os
import sqlite3

from constant import HASH_CACHE_FILE
from module import function_normal


def check_hash_cache_exist():
    """检查哈希值缓存数据库是否存在"""
    function_normal.print_function_info()
    if not os.path.exists(HASH_CACHE_FILE):
        conn = sqlite3.connect(HASH_CACHE_FILE)
        cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS hash (path TEXT Primary KEY, filesize INTEGER, comic_path TEXT, ahash TEXT, phash TEXT, dhash TEXT)')


def read_hash_cache():
    """读取hash缓存
    :return: 哈希值dict,key为图片路径，value为图片数据dict"""
    function_normal.print_function_info()
    conn = sqlite3.connect(HASH_CACHE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hash')
    data = cursor.fetchall()
    columns_name = [i[0] for i in cursor.description]
    data_origin = [dict(zip(columns_name, row)) for row in data]

    image_data_dict = {}
    for item_dict in data_origin:
        for key, value in item_dict.items():  # 处理hash值为None的文本的情况
            if value == 'None':
                item_dict[key] = None

        path = item_dict['path']
        image_data_dict[path] = item_dict

    return image_data_dict


def update_hash_cache(image_hash_dict: dict):
    """更新hash缓存"""
    function_normal.print_function_info()
    # 读取
    conn = sqlite3.connect(HASH_CACHE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT path FROM hash")
    data = cursor.fetchall()
    cache_image_paths = [item[0] for item in data]

    # 更新
    for image, data_dict in image_hash_dict.items():
        if image not in cache_image_paths:
            cursor.execute(f'INSERT INTO hash (path) VALUES ("{image}")')
        for column, value in data_dict.items():
            cursor.execute(f'UPDATE hash SET {column} = "{str(value)}" WHERE path = "{image}"')

    cursor.close()
    conn.commit()
    conn.close()


def delete_hash_cache():
    """删除hash缓存"""
    function_normal.print_function_info()
    conn = sqlite3.connect(HASH_CACHE_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hash")
    cursor.close()
    conn.commit()
    conn.close()


def clear_unuseful_cache():
    """删除hash缓存中的无效项"""
    function_normal.print_function_info()
    conn = sqlite3.connect(HASH_CACHE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT path, filesize FROM hash')
    datas = cursor.fetchall()
    for data in datas:
        image_path = data[0]
        filesize = data[1]
        if not os.path.exists(image_path) or function_normal.get_size(image_path) != filesize:
            cursor.execute(f'''DELETE FROM hash WHERE path="{image_path}"''')  # 路径外的引号必须使用“双引号（Windows文件名可以带'而不能带"）
    cursor.close()
    conn.commit()
    conn.close()
