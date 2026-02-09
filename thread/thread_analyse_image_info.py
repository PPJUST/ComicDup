# 子线程-分析图片信息
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
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

        # 需要提取图片信息的漫画信息类列表
        self.comic_info_list: List[ComicInfoBase] = []
        # 提取得到的图片信息类
        self.image_info_dict: Dict[str, ImageInfoBase] = dict()
        # 每本漫画需要提取的图片数
        self.extract_pages = 2

        # 计算的图片hash类型
        self.hash_type = SimilarAlgorithm.dHash()
        # 计算的图片hash长度
        self.hash_length = 64

    def initialize(self):
        """初始化"""
        super().initialize()
        self.comic_info_list = []
        self.image_info_dict = dict()
        self.extract_pages = 2
        self.hash_type = SimilarAlgorithm.dHash()
        self.hash_length = 64

    def get_image_info_dict(self):
        """获取图片信息字典"""
        image_info_dict = self.image_info_dict
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
        print(f'启动线程池 分析图片信息，线程数量：{self.max_workers}')

        total_comics = len(self.comic_info_list)
        if total_comics == 0:
            self._finish_analyse(0)
            return

        # 使用线程池进行并发处理
        completed_count = 0
        total_images = 0
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有漫画的图片分析任务
            futures = {executor.submit(self._analyse, comic_info): comic_info for comic_info in
                       self.comic_info_list}

            # 处理完成的任务
            for future in as_completed(futures):
                if self._is_stop:
                    executor.shutdown(wait=False, cancel_futures=True)
                    break

                comic_info = futures[future]
                try:
                    # 获取该漫画分析出的图片信息
                    image_info_list = future.result()
                    total_images += len(image_info_list)
                    # 加入到结果字典
                    for image_info in image_info_list:
                        # 保存到字典时，使用虚拟路径，防止压缩文件的相对文件名导致的重复值
                        faker_path = image_info.faker_path
                        self.image_info_dict[faker_path] = image_info

                    completed_count += 1
                    self.SignalRate.emit(f'{completed_count}/{total_comics}')
                except Exception as e:
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning,
                                                f'分析漫画{comic_info.filepath}的图片失败：{str(e)}')

            self._finish_analyse(total_images)

    def _finish_analyse(self, total_images: int):
        """完成分析后的处理"""
        print('结束线程池 分析图片信息')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '全部图片信息完成分析')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'共完成分析{total_images}张图片')
        self.finished()

    def _analyse(self, comic_info: ComicInfoBase):
        """分析单本漫画中的图片信息（供线程池调用）"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.RateInfo, f'开始分析漫画中的图片信息：{comic_info.filepath}')

        image_info_list = []
        comic_filetype = comic_info.filetype
        images_inside = comic_info.get_page_paths()
        images_extract = images_inside[:self.extract_pages]

        for image in images_extract:
            # 根据漫画类型实例化对应的图片信息类
            if isinstance(comic_filetype, FileType.Folder):
                image_info = ImageInfoFolder(image)
            elif isinstance(comic_filetype, FileType.Archive):
                image_info = ImageInfoArchive(image)
            else:
                raise Exception(f'未知的漫画类型：{type(comic_filetype)}')

            # 更新图片信息并计算hash
            image_info.update_info_by_comic_info(comic_info)
            image_info.calc_hash(self.hash_type, self.hash_length)
            image_info_list.append(image_info)

        return image_info_list
