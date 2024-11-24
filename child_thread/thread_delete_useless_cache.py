# 子线程-删除数据库中的无效项目

from child_thread.thread_pattern import ThreadPattern
from class_ import class_comic_info, class_image_info


class ThreadDeleteUselessCache(ThreadPattern):
    """删除数据库中的无效项目"""

    def __init__(self):
        super().__init__()

    def run(self):
        # 处理漫画信息数据库
        class_comic_info.delete_useless_item()
        # 处理预览图
        class_comic_info.delete_useless_preview()
        # 处理图片信息数据库
        class_image_info.delete_useless_item()

        self.signal_finished.emit('')
