# 子线程-分析图片信息
import os
from typing import Dict, List

from common.class_comic import ComicInfoBase
from common.class_config import SimilarAlgorithm, TYPES_HASH_ALGORITHM, FileType
from common.class_image import ImageInfoBase, ImageInfoFolder, ImageInfoArchive
from common.class_runtime import TypeRuntimeInfo
from thread.thread_pattern import ThreadPattern


class ThreadAnalyseImageInfo(ThreadPattern):
    """子线程-分析图片信息"""

    def __init__(self):
        super().__init__()
        self.step_index = 3
        self.step_info = '计算图片hash'

        # 漫画信息类列表，用于提取相关数据
        self.comic_info_list: List[ComicInfoBase] = []
        # 图片hash字典
        self.image_info_dict: Dict[str, ImageInfoBase] = dict()
        # 每本漫画提取的图片数
        self.extract_pages = 2

        # 计算的图片hash类型
        self.hash_type = SimilarAlgorithm.dHash()
        # 图片hash长度
        self.hash_length = 64

    def get_image_info_dict(self):
        """获取图片信息字典"""
        image_info_dict = self.image_info_dict
        self.clear()
        return image_info_dict

    def set_comic_info_list(self, comic_info_list: list):
        """设置图片所在的漫画信息类列表"""
        self.comic_info_list = comic_info_list

    def set_hash_type(self, hash_type: TYPES_HASH_ALGORITHM):
        """设置需要计算的图片hash类型"""
        self.hash_type = hash_type

    def set_hash_length(self, length: int):
        """设置需要计算的图片hash类型"""
        self.hash_length = length

    def set_extract_pages(self, extract_pages: int):
        """设置需要提取的图片数"""
        self.extract_pages = extract_pages

    def clear(self):
        """清空数据"""
        self.comic_info_list = []
        self.image_info_dict = dict()

    def get_corr_comic_info(self, image_path: str):
        """获取图片对应的漫画信息类"""
        image_path = os.path.normpath(image_path)
        for comic_info in self.comic_info_list:
            image_list = comic_info.get_page_paths()
            if image_path in image_list:
                return comic_info
        return None

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始分析图片信息')
        print('启动子线程 分析图片信息')
        _count = 0
        for index, comic_info in enumerate(self.comic_info_list, start=1):
            if self._is_stop:
                break
            self.SignalRate.emit(f'{index}/{len(self.comic_info_list)}')
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'开始分析漫画中的图片信息：{comic_info.filepath}')
            # 根据不同的漫画类型，实例化不同的图片信息类
            comic_filetype = comic_info.filetype
            images_inside = comic_info.get_page_paths()
            images_extract = images_inside[:self.extract_pages]
            for image in images_extract:
                _count += 1
                if isinstance(comic_filetype, FileType.Folder):
                    image_info = ImageInfoFolder(image)
                elif isinstance(comic_filetype, FileType.Archive):
                    image_info = ImageInfoArchive(image)
                else:
                    raise Exception('未知的漫画类型')
                # 将图片对应的漫画信息类传递给图片信息类，更新部分数据
                image_info.update_info_by_comic_info(comic_info)
                image_info.calc_hash(self.hash_type, self.hash_length)  # 计算指定hash值
                # 保存到变量时，使用虚拟路径，防止压缩文件的相对文件名导致的重复值
                faker_path = image_info.faker_path
                self.image_info_dict[faker_path] = image_info
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'完成分析漫画中的图片信息：{comic_info.filepath}')

        # 结束后发送信号
        print('提取的图片信息', self.image_info_dict)
        print('结束子线程 分析图片信息')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '全部图片信息完成分析')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'共完成分析{_count}张图片')
        self.finished()
