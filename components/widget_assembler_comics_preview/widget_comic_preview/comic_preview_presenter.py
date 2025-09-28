import os

import lzytools.file
from PySide6.QtCore import QObject

from common import function_file
from common.class_comic import ComicInfo, FileType
from components.widget_assembler_comics_preview.widget_comic_preview.comic_preview_model import ComicPreviewModel
from components.widget_assembler_comics_preview.widget_comic_preview.comic_preview_viewer import ComicPreviewViewer


class ComicPreviewPresenter(QObject):
    """漫画预览模块的桥梁组件"""

    def __init__(self, viewer: ComicPreviewViewer, model: ComicPreviewModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_info: ComicInfo = None
        self.page_paths = []  # 页面列表
        self.page_index = 1  # 当前页码（从1开始）

        # 绑定信号
        self._bind_signal()

    def set_comic(self, comic_info: ComicInfo):
        """设置需要显示的漫画"""
        self.comic_info = comic_info
        self.page_paths = self.comic_info.get_page_paths()
        self.page_index = 1

        # 显示漫画信息
        # 文件类型
        filetype = self.comic_info.filetype
        if isinstance(filetype, FileType.Folder) or filetype == FileType.Folder:
            self.viewer.set_icon_folder()
        elif isinstance(filetype, FileType.Archive) or filetype == FileType.Archive:
            self.viewer.set_icon_archive()
        # 文件大小
        filesize = self.comic_info.filesize_bytes_extracted
        filesize_str = function_file.format_bytes_size(filesize)
        self.viewer.set_filesize(filesize_str)
        # 文件名
        self.viewer.set_filename(self.comic_info.filename)
        # 父路径
        self.viewer.set_parent_dirpath(self.comic_info.parent_dirpath)
        # 总页数
        self.viewer.set_page_count(self.comic_info.page_count)
        # 当前页码
        self.viewer.set_current_page(1)
        # 显示第一页的图像
        self.show_page(self.page_index)

    def show_page(self, page_index: int):
        """显示指定页的图像
        :param page_index:从1开始计数的页码"""
        image_path = self.page_paths[page_index - 1]
        self.viewer.show_image(image_path)

    def turn_to_previous_page(self, page_count: int = 1):
        """向前翻页"""
        if self.page_index == 1:  # 在第一页时，如果需要切换到上一页，则切换到最后一页
            self.page_index = len(self.page_paths)
        else:  # 不在第一页时，按正常逻辑操作，但不能超过页码的下限1
            self.page_index -= page_count
            if self.page_index < 1:
                self.page_index = 1
        self.show_page(self.page_index)

    def turn_to_next_page(self, page_count: int = 1):
        """向后翻页"""
        if self.page_index == len(self.page_paths):  # 在最后一页时，如果需要切换到下一页，则切换到第一页
            self.page_index = 1
        else:  # 不在最后一页时，按正常逻辑操作，但不能超过页码的上限
            self.page_index += page_count
            if self.page_index > len(self.page_paths):
                self.page_index = len(self.page_paths)
        self.show_page(self.page_index)

    def open_path(self):
        """打开漫画文件"""
        path = self.comic_info.filepath
        os.startfile(path)

    def delete_comic(self):
        """删除漫画文件"""
        path = self.comic_info.filepath
        lzytools.file.delete(path, send_to_trash=True)

    def get_viewer(self):
        """获取viewer"""
        return self.viewer

    def _bind_signal(self):
        """绑定信号"""
        self.viewer.PreviousPage.connect(self.turn_to_previous_page)
        self.viewer.NextPage.connect(self.turn_to_next_page)
        self.viewer.OpenPath.connect(self.open_path)
        self.viewer.Delete.connect(self.delete_comic)
