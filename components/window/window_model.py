import os
from pathlib import Path
from typing import List

import lzytools
import natsort
from PySide6.QtCore import Signal, QObject

from common import function_cache_preview, function_file
from common.class_comic import ComicInfoBase
from common.class_config import TYPES_HASH_ALGORITHM
from common.class_count_info import CountInfo
from common.class_image import ImageInfoBase
from common.class_runtime import TypeRuntimeInfo
from common.function_config import SettingWindowSize, CONFIG_FILE
from common.function_db_comic_info import DBComicInfo
from common.function_db_image_info import DBImageInfo


class WindowModel(QObject):
    """主窗口的模型组件"""
    SignalRuntimeInfo = Signal(object, str, name='运行信息')

    def __init__(self, ):
        super().__init__()
        # 连接数据库
        self.db_comic_info = DBComicInfo()
        self.db_image_info = DBImageInfo()

    def get_comic_db(self):
        return self.db_comic_info

    def get_image_db(self):
        return self.db_image_info

    def get_hash_list_from_image_infos(self, image_infos: List[ImageInfoBase], hash_type: TYPES_HASH_ALGORITHM,
                                       hash_length: int):
        """从图片信息类列表中读取图片hash值列表"""
        hash_list = []
        for image_info in image_infos:
            hash_ = image_info.get_hash(hash_type, hash_length)
            hash_list.append(hash_)

        return hash_list

    def get_hashs(self, hash_algorithm: TYPES_HASH_ALGORITHM, hash_length: int) -> List[str]:
        """获取数据库中所有图片的hash值"""
        return self.db_image_info.get_hashs(hash_algorithm, hash_length)

    def get_hash_from_image_info(self, image_info: ImageInfoBase, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        """从图片信息类中读取图片hash值"""
        hash_ = image_info.get_hash(hash_type, hash_length)
        return hash_

    def get_image_info_by_hash(self, hash_: str, hash_type: TYPES_HASH_ALGORITHM):
        """根据hash值获取对应的图片信息类（列表）"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '将图片hash值转换为对应的图片路径')
        # 由于一个hash值可能对应多个图片，因此返回一个列表
        image_infos = self.db_image_info.get_image_info_by_hash(hash_, hash_type)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'需要转换的hash值：{hash_}')
        for _image_info in image_infos:
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'转换的图片路径：{_image_info.image_path}')
        print('将hash值转换为对应的图片')
        print('hash值', hash_)
        return image_infos

    def get_comic_info_by_image_info(self, image_info: ImageInfoBase):
        """根据图片信息类获取对应的漫画信息类"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '将图片路径转换为对应的漫画路径')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'需要转换的图片路径：{image_info.image_path}')
        comic_path = image_info.belong_comic_path
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'转换的漫画路径：{comic_path}')
        return self.get_comic_info_by_comic_path(comic_path)

    def get_comic_info_by_comic_path(self, comic_path: str):
        """根据漫画路径获取对于的漫画信息类"""
        comic_info = self.db_comic_info.get_comic_info_by_comic_path(comic_path)
        return comic_info

    def get_comic_paths(self) -> List[str]:
        """获取数据库中所有的漫画路径"""
        comics_path_list = self.db_comic_info.get_comic_paths()
        return comics_path_list

    def convert_hash_group_to_comic_info_group(self,
                                               hash_group: List[List[str]],
                                               hash_type: TYPES_HASH_ALGORITHM) -> List[List[ComicInfoBase]]:
        """将hash值组列表转换为对应的漫画组列表"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '将hash值相似组转换为对应的漫画路径组')
        # hash组格式：[[hash1, hash2, hash3], [hash4, hash5, hash6]]
        # 先转换为漫画路径格式
        comic_path_group = []
        for h_group in hash_group:
            p_group = set()
            for hash_ in h_group:
                image_infos = self.get_image_info_by_hash(hash_, hash_type)
                for image_info in image_infos:
                    comic_path = image_info.belong_comic_path
                    p_group.add(comic_path)
            if len(p_group) >= 2:
                comic_path_group.append(list(p_group))
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'共完成{len(comic_path_group)}组的转换')
        #  然后合并有交集的项目（用于整合组间相似项）
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'合并有交集的相似组')
        comic_path_group = lzytools.common.merge_intersection_item(comic_path_group)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'合并为{len(comic_path_group)}组')
        # 最后转换为漫画信息类格式
        comic_info_group = []
        for cp_group in comic_path_group:
            ci_group = []
            for comic_path in cp_group:
                comic_info = self.get_comic_info_by_comic_path(comic_path)
                if comic_info:
                    ci_group.append(comic_info)
            comic_info_group.append(ci_group)

        return comic_info_group

    def filter_comic_info_group_is_exist(self, comic_info_group: List[List[ComicInfoBase]]):
        """筛选漫画信息类列表，剔除已经不存在的项目"""
        # 漫画组格式：[[ComicInfo1,ComicInfo2,ComicInfo3], [ComicInfo4,ComicInfo5,ComicInfo6]]
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'对相似组进行有效性筛选')
        comic_info_group_filter = []
        for group in comic_info_group:
            group: List[ComicInfoBase]
            group_filter = []
            for comic_info in group:
                path = comic_info.filepath
                if os.path.exists(path):
                    group_filter.append(comic_info)
            if len(group_filter) >= 2:
                group_filter = natsort.os_sorted(group_filter)  # 进行一次路径排序，便于后续显示
                comic_info_group_filter.append(group_filter)

        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'完成相似组有效性筛选')
        return comic_info_group_filter

    def filter_comic_info_group_is_in_search_list(self, comic_info_group: List[List[ComicInfoBase]],
                                                  comic_path_search_list: List[str]):
        """筛选漫画信息类列表，剔除不在搜索列表中的项目"""
        # 漫画组格式：[[ComicInfo1,ComicInfo2,ComicInfo3], [ComicInfo4,ComicInfo5,ComicInfo6]]
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'对相似组进行相关性筛选')
        comic_info_group_filter = []
        for group in comic_info_group:
            group: List[ComicInfoBase]
            group_filter = []
            for comic_info in group:
                path = comic_info.filepath
                if path in comic_path_search_list:
                    group_filter.append(comic_info)
            if len(group_filter) >= 2:
                comic_info_group_filter.append(group_filter)

        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'完成相似组相关性筛选')
        return comic_info_group_filter

    def filter_comic_info_group_is_in_same_parent_folder(self, comic_info_group: List[List[ComicInfoBase]],
                                                         level: int):
        """筛选漫画信息类列表，剔除不在相同n层父目录下的项目"""
        print('相同父目录匹配')
        # 漫画组格式：[[ComicInfo1,ComicInfo2,ComicInfo3], [ComicInfo4,ComicInfo5,ComicInfo6]]
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'对相似组进行相关性筛选')
        comic_info_group_filter = []
        for group in comic_info_group:
            group: List[ComicInfoBase]
            group_filter = []
            # 先提取组中所有项目的文件路径
            filepaths = [i.filepath for i in group]
            # 然后提取出文件路径列表中的上n层父目录路径
            parent_folders = []
            for i in filepaths:
                path = Path(i)
                max_index = len(path.parents) - 1
                if level > max_index:
                    p_path = path.parents[max_index]  # 超限返回根目录
                else:
                    p_path = path.parents[level - 1]
                parent_folders.append(str(p_path))
            # 然后提取出父目录路径列表中存在父子关系、相同项的项
            parent_folders_filter = set()
            for p_1 in parent_folders:
                if parent_folders.count(p_1) >= 2:  # 相同项
                    parent_folders_filter.add(p_1)
                for p_2 in parent_folders:  # 父子关系
                    if p_2 == p_1:
                        continue
                    if p_2 in p_1:
                        parent_folders_filter.add(p_1)
                        parent_folders_filter.add(p_2)
            print('共同父目录', parent_folders_filter)
            # 最后逐个匹配文件路径，如果在父目录列表下，则添加进相似组中
            for comic_info in group:
                path = comic_info.filepath
                for parent in parent_folders_filter:
                    if parent in path:
                        print('是子目录，添加进相似组', path)
                        group_filter.append(comic_info)
                        break

            if len(group_filter) >= 2:
                comic_info_group_filter.append(group_filter)

        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, f'完成相似组相关性筛选')
        return comic_info_group_filter

    def write_hash_to_comic_info(self, comic_info_group: List[List[ComicInfoBase]],
                                 hash_algorithm: TYPES_HASH_ALGORITHM, hash_length: int):
        """将ComicInfo对应的图片hash值写入ComicInfo中"""
        for group in comic_info_group:
            for comic_info in group:
                fingerprint = comic_info.fingerprint
                hashs = self.db_image_info.get_hashs_by_belong_comic_fingerprint(fingerprint, hash_algorithm,
                                                                                 hash_length)
                comic_info.set_db_hashs(hashs)

        return comic_info_group

    def delete_useless_cache(self):
        """删除无用缓存"""
        # 删除无效的漫画数据库项目
        self.db_comic_info.delete_useless_items()
        # 删除无效的图片数据库项目
        self.db_image_info.delete_useless_items()
        # 删除无效的预览图
        preview_paths_in_db = self.db_comic_info.get_preview_paths()
        preview_paths_in_local = function_cache_preview.get_preview_image_paths()
        for preview_path in preview_paths_in_local:
            print('检查预览图是否存在于数据库', preview_path)
            if preview_path not in preview_paths_in_db:
                print('不存在，删除')
                lzytools.file.delete(preview_path, send_to_trash=True)  # note 调试阶段，仅删除到回收站而不是直接删除

    def clear_cache(self):
        """清空缓存"""
        # 清空漫画数据库
        self.db_comic_info.clear()
        # 清空图片数据库
        self.db_image_info.clear()
        # 清空预览图
        function_cache_preview.clear_cache()

    def get_comic_db_count_info(self) -> CountInfo:
        """获取漫画数据库统计信息"""
        item_count = self.db_comic_info.get_info_item_count()
        filesize = self.db_comic_info.get_info_db_size()
        update_time = self.db_comic_info.get_info_update_time()

        info_count = CountInfo()
        info_count.set_item_count(item_count)
        info_count.set_size_count(filesize)
        info_count.set_update_time(update_time)

        return info_count

    def get_image_db_count_info(self) -> CountInfo:
        """获取图片数据库统计信息"""
        item_count = self.db_image_info.get_info_item_count()
        filesize = self.db_image_info.get_info_db_size()
        update_time = self.db_image_info.get_info_update_time()

        info_count = CountInfo()
        info_count.set_item_count(item_count)
        info_count.set_size_count(filesize)
        info_count.set_update_time(update_time)

        return info_count

    def get_preview_image_count_info(self) -> CountInfo:
        """获取预览图缓存的统计信息"""
        item_count = function_cache_preview.get_preview_image_count()
        filesize_bytes = function_cache_preview.get_preview_size()
        filesize_str = function_file.format_bytes_size(filesize_bytes)

        info_count = CountInfo()
        info_count.set_item_count(item_count)
        info_count.set_size_count(filesize_str)

        return info_count

    def get_window_size_db(self):
        """获取数据库中的窗口尺寸"""
        config = SettingWindowSize(CONFIG_FILE)
        width, height = config.read()
        return width, height

    def set_window_size_db(self, width: int, height: int):
        """设置数据库中的窗口尺寸"""
        config = SettingWindowSize(CONFIG_FILE)
        size = (width, height)
        config.set(size)
