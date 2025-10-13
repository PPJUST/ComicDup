import lzytools.file
from PySide6.QtCore import QObject

from common import function_cache_preview
from common.class_count_info import CountInfo
from common.function_db_comic_info import DBComicInfo
from common.function_db_image_info import DBImageInfo
from components.widget_cache_manager.cache_manager_model import CacheManagerModel
from components.widget_cache_manager.cache_manager_viewer import CacheManagerViewer
from thread.thread_refresh_comic_db import ThreadRefreshComicDB


class CacheManagerPresenter(QObject):
    """缓存管理器模块的桥梁组件"""

    def __init__(self, viewer: CacheManagerViewer, model: CacheManagerModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 漫画数据库对象
        self.comic_db: DBComicInfo = None

        # 图片数据库对象
        self.image_db: DBImageInfo = None

        # 绑定信号
        self._bind_signal()

    def set_comic_db(self, db_comic_info: DBComicInfo):
        """设置漫画数据库对象"""
        self.comic_db = db_comic_info

    def set_image_db(self, db_image_info: DBImageInfo):
        """设置图片数据库对象"""
        self.image_db = db_image_info

    def set_comic_cache_count_info(self, count_info: CountInfo):
        """设置漫画数据库信息"""
        self.viewer.set_comic_cache_count_info(count_info)

    def set_image_cache_count_info(self, count_info: CountInfo):
        """设置图片数据库信息"""
        self.viewer.set_image_cache_count_info(count_info)

    def set_preview_cache_count_info(self, count_info: CountInfo):
        """设置预览图信息"""
        self.viewer.set_preview_cache_count_info(count_info)

    def clear_cache(self):
        """清空缓存"""
        # 清空漫画数据库
        self.comic_db.clear()
        # 清空图片数据库
        self.image_db.clear()
        # 清空预览图
        function_cache_preview.clear_cache()

    def delete_useless_cache(self):
        """删除无用缓存"""
        # 删除无效的漫画数据库项目
        self.comic_db.delete_useless_items()
        # 删除无效的图片数据库项目
        self.image_db.delete_useless_items()
        # 删除无效的预览图
        preview_paths_in_db = self.comic_db.get_preview_paths()
        preview_paths_in_local = function_cache_preview.get_preview_image_paths()
        for preview_path in preview_paths_in_local:
            print('检查预览图是否存在于数据库', preview_path)
            if preview_path not in preview_paths_in_db:
                print('不存在，删除')
                lzytools.file.delete(preview_path, send_to_trash=True)  # 备忘录 调试阶段，仅删除到回收站而不是直接删除

    def refresh_cache(self):
        """刷新缓存"""
        # 刷新漫画数据库项目
        # 获取存储的漫画路径列表
        comics_path_list = self.comic_db.get_comic_paths()
        # 实例化更新子线程
        self.thread_refresh_comic_db = ThreadRefreshComicDB()
        # 传递参数
        self.thread_refresh_comic_db.set_comics_path(comics_path_list)
        self.thread_refresh_comic_db.set_comic_db(self.comic_db)
        # 重新分析漫画信息并刷新漫画数据库
        self.thread_refresh_comic_db.start()

        # 刷新图片数据库项目
        # 备忘录 图片数据库暂时不做更新方法

    def match_cache(self):
        """缓存内部匹配"""
        # 备忘录

    def _bind_signal(self):
        """绑定信号"""
        self.viewer.RefreshCache.connect(self.refresh_cache)
        self.viewer.MatchCache.connect(self.match_cache)
        self.viewer.DeleteUselessCache.connect(self.delete_useless_cache)
        self.viewer.ClearCache.connect(self.clear_cache)
