from typing import List

from common.class_comic import ComicInfo, ImageInfo
from common.class_config import TYPES_HASH_ALGORITHM
from common.function_db_comic_info import DBComicInfo


class WindowModel:
    """主窗口的模型组件"""

    def __init__(self, ):
        super().__init__()
        # 连接数据库
        self.db_comic_info = DBComicInfo()

    def save_comic_info_to_db(self, comic_infos: List[ComicInfo]):
        """保存漫画信息到本地数据库中"""
        for comic_info in comic_infos:
            self.db_comic_info.add(comic_info)

    def get_images_from_comic_infos(self, comic_infos: List[ComicInfo], extract_image_count: int):
        """提取漫画信息类列表中指定数量的内部图片路径"""
        images_inside = []
        for comic_info in comic_infos:
            images_inside.extend(self.get_images_from_comic_info(comic_info, extract_image_count))

        return images_inside

    def get_images_from_comic_info(self, comic_info: ComicInfo, extract_image_count: int):
        """提取漫画信息类中指定数量的内部图片路径"""
        images_inside = comic_info.get_page_paths()
        return images_inside[:extract_image_count]

    def save_image_info_to_db(self, image_infos: List[ImageInfo]):
        """保存图片信息到本地数据库中"""
        # 备忘录

    def get_hash_from_image_info(self, image_info: ImageInfo, hash_type: TYPES_HASH_ALGORITHM, hash_length: int):
        """从图片信息类中读取图片hash值"""
        hash_ = image_info.get_hash(hash_type, hash_length)
        return hash_
