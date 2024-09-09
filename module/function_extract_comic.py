# 提取符合规则的漫画文件夹/压缩包的方法
import os

from module import function_normal

_MIN_IMAGE_COUNT = 4


def extract_comics(dirpath: str) -> set:
    """提取一个文件夹内符合规则的漫画文件夹/压缩包
    :return: set，漫画路径集合，包含文件夹和压缩包"""
    if not os.path.exists(dirpath) or not os.path.isdir(dirpath):
        return set()

    # 提取漫画路径列表
    folder_structure = _FolderStructure(dirpath)
    comics_folder = folder_structure.comics_folder
    comics_archive = folder_structure.comics_archive

    # 合并
    comics = set()
    comics.update(comics_folder)
    comics.update(comics_archive)

    return comics


class _FolderStructure(dict):
    """文件夹内部结构，以及内部的所有符合规则的文件夹/压缩包漫画
    例：{文件夹路径:{'folder':(...), 'image':(...), 'archive':(...)}, ...}"""

    def __init__(self, dirpath):
        super().__init__()
        self._arg_folder = 'folder'
        self._arg_image = 'image'
        self._arg_archive = 'archive'
        self._archives = set()  # 内部所有的压缩包路径，不在该类中使用，用于在外部调用

        self.comics_folder = set()  # 符合规则的文件夹类型的漫画
        self.comics_archive = set()  # 符合规则的压缩包类型的漫画

        # 提取内部结构
        self.analyze_structure(dirpath)
        # 识别漫画
        self.extract_comics()

    def extract_comics(self):
        """提取符合规则的漫画文件夹/压缩包"""
        # 检查文件夹
        for dirpath_ in self:
            is_comic_folder = self._is_comic_folder(dirpath_)
            if is_comic_folder:
                self.comics_folder.add(dirpath_)
        # 检查压缩包
        for archive_path in self._archives:
            is_comic_archive = self._is_comic_archive(archive_path)
            if is_comic_archive:
                self.comics_archive.add(archive_path)

    def analyze_structure(self, dirpath):
        """分析文件夹内部结构，区分出每个子文件夹内的文件夹/图片/压缩包数量"""
        for dirpath_, dirnames, filenames in os.walk(dirpath):
            # 提取内部所有文件夹，写入字典
            for dirname in dirnames:
                dirpath_joined = os.path.normpath(os.path.join(dirpath_, dirname))
                # 向字典中添加当前文件夹作为key，并添加空的value
                if dirpath_joined not in self:
                    self._add_empty_value(dirpath_joined)
                # 向字典中添加当前文件夹的父目录作为key，并将当前文件夹作为arg添加
                parent_folder = os.path.dirname(dirpath_joined)
                if parent_folder not in self:
                    self._add_empty_value(parent_folder)
                    self._add_value_arg_folder(parent_folder, dirpath_joined)

            # 提取内部所有文件，写入字典
            for filename in filenames:
                filepath_join = os.path.normpath(os.path.join(dirpath_, filename))
                parent_folder = os.path.dirname(filepath_join)
                # 向字典中添加当前文件夹的父目录作为key
                if parent_folder not in self:
                    self._add_empty_value(parent_folder)
                # 根据文件类型写入不同的value
                filetype_ = function_normal.guess_filetype(filepath_join)
                if filetype_ == 'image':
                    self._add_value_arg_image(parent_folder, filepath_join)
                elif filetype_ == 'archive':
                    self._add_value_arg_archive(parent_folder, filepath_join)
                    self._archives.add(filepath_join)

    def _is_comic_folder(self, dirpath):
        """检查文件夹是否为符合规则的漫画文件夹（内部图片数>=指定数，无子文件夹，同级文件中无压缩包）"""
        if dirpath in self:
            structure = self[dirpath]
            arg_folder = structure[self._arg_folder]
            arg_image = structure[self._arg_image]
            arg_archive = structure[self._arg_archive]

            if arg_archive:  # 同级文件中无压缩包
                return False
            elif arg_folder:  # 无子文件夹
                return False
            elif len(arg_image) >= _MIN_IMAGE_COUNT:  # 内部图片数>=指定数
                return True
            else:
                return False

    @staticmethod
    def _is_comic_archive(archive_path: str):
        """检查压缩包是否为符合规则的漫画压缩包（内部图片数>=指定数，所有图片都在同一级）"""
        images = function_normal.get_images_from_archive(archive_path)
        # 判断是否都为同级文件
        parents = [os.path.dirname(i) for i in images]
        if len(set(parents)) != 1:
            return False
        elif len(images) >= _MIN_IMAGE_COUNT:
            return True
        else:
            return False

    def _add_empty_value(self, dirpath):
        """添加空的内部参数"""
        self[dirpath] = {self._arg_folder: set(), self._arg_image: set(), self._arg_archive: set()}

    def _add_value_arg_folder(self, dirpath, arg):
        """添加内部参数"""
        self[dirpath][self._arg_folder].add(arg)

    def _add_value_arg_image(self, dirpath, arg):
        """添加内部参数"""
        self[dirpath][self._arg_image].add(arg)

    def _add_value_arg_archive(self, dirpath, arg):
        """添加内部参数"""
        self[dirpath][self._arg_archive].add(arg)
