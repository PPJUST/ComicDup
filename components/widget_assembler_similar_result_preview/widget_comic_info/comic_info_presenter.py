import os

from PySide6.QtCore import QObject

from common import function_file
from common.class_comic import FileType, ComicInfo
from components.widget_assembler_similar_result_preview.widget_comic_info.comic_info_model import ComicInfoModel
from components.widget_assembler_similar_result_preview.widget_comic_info.comic_info_viewer import ComicInfoViewer
from components.widget_search_list.res.icon_base64 import ICON_FOLDER, ICON_ARCHIVE


class ComicInfoPresenter(QObject):
    """单个漫画信息模块的桥梁组件"""

    def __init__(self, viewer: ComicInfoViewer, model: ComicInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_info: ComicInfo = None  # 显示的漫画的漫画信息类

        # 绑定信号
        self.viewer.OpenPath.connect(self.open_path)
        self.viewer.RefreshInfo.connect(self.refresh_info)
        self.viewer.Delete.connect(self.delete_comic)

    def set_comic_info(self, comic_info: ComicInfo):
        """设置需要显示的漫画的漫画信息类"""
        self.comic_info = comic_info
        self._show_comic_info()

    def open_path(self):
        """打开路径"""
        os.startfile(self.comic_info.filepath)

    def refresh_info(self, comic_info: ComicInfo):
        """刷新信息"""
        self.set_comic_info(comic_info)

    def delete_comic(self):
        """删除漫画"""
        # 备忘录

    def _show_comic_info(self):
        """在viewer上显示漫画信息"""
        filetype = self.comic_info.filetype

        self.viewer.set_filetitle(self.comic_info.filetitle)
        self.viewer.set_parent_dirpath(self.comic_info.parent_dirpath)
        self.viewer.set_page_count(self.comic_info.page_count)
        self.viewer.set_preview(self.comic_info.preview_path)
        # 按文件类型显示icon
        if isinstance(filetype, FileType.Folder):
            icon_base64 = ICON_FOLDER
        elif isinstance(filetype, FileType.Archive):
            icon_base64 = ICON_ARCHIVE
        else:
            icon_base64 = ''
        self.viewer.set_filetype_icon(icon_base64)
        # 按文件类型显示文件大小
        if isinstance(filetype, FileType.Folder):
            bytes_size = self.comic_info.filesize_bytes
        elif isinstance(filetype, FileType.Archive):
            bytes_size = self.comic_info.filesize_bytes_extracted
        else:
            bytes_size = 0
        size_str = function_file.format_bytes_size(bytes_size)
        self.viewer.set_filesize(size_str)

    def get_viewer(self) -> ComicInfoViewer:
        """获取viewer"""
        return self.viewer
