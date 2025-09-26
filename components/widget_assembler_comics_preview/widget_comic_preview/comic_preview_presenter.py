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

    def set_comic(self, comic_info: ComicInfo):
        """设置需要显示的漫画"""
        self.comic_info = comic_info
        self.page_paths = self.comic_info.get_page_paths()

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
        self.viewer.show_image(self.page_paths[0])

    def get_viewer(self):
        """获取viewer"""
        return self.viewer
