import os

from constant import _CACHE_DIRPATH, _PREVIEW_DIRPATH


def check_folder_exist():
    """检查默认文件夹是否存在"""
    if not os.path.exists(_CACHE_DIRPATH):
        os.mkdir(_CACHE_DIRPATH)
    if not os.path.exists(_PREVIEW_DIRPATH):
        os.mkdir(_PREVIEW_DIRPATH)
