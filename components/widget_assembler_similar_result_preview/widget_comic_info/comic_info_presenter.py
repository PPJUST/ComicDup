import os

from PySide6.QtCore import QObject

from common import function_file
from common.class_comic import FileType
from components.widget_assembler_similar_result_preview.widget_comic_info.comic_info_model import ComicInfoModel
from components.widget_assembler_similar_result_preview.widget_comic_info.comic_info_viewer import ComicInfoViewer
from components.widget_search_list.res.icon_base64 import ICON_FOLDER, ICON_ARCHIVE


class ComicInfoPresenter(QObject):
    """单个漫画信息模块的桥梁组件"""

    def __init__(self, viewer: ComicInfoViewer, model: ComicInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_showed = None  # 显示的漫画的路径

        # 绑定信号
        self.viewer.OpenPath.connect(self.open_path)
        self.viewer.RefreshInfo.connect(self.refresh_info)
        self.viewer.Delete.connect(self.delete_comic)

    def set_comic(self, comic_path: str):
        """设置需要显示的漫画"""
        self.comic_showed = comic_path
        self.model.analyse_comic(comic_path)
        self._set_comic_info()

    def open_path(self):
        """打开路径"""
        os.startfile(self.model.get_filepath())

    def refresh_info(self):
        """刷新信息"""
        self.model.refresh_info()
        self._set_comic_info()

    def delete_comic(self):
        """删除漫画"""
        # 备忘录

    def _set_comic_info(self):
        """在viewer上显示漫画信息"""
        filetype = self.model.get_filetype()

        self.viewer.set_filetitle(self.model.get_filetitle())
        self.viewer.set_parent_dirpath(self.model.get_parent_dirpath())
        self.viewer.set_page_count(self.model.get_page_count())
        self.viewer.set_preview(self.model.get_preview_path())
        # 按文件类型显示icon
        if isinstance(filetype, FileType.Folder):
            icon_base64 = ICON_FOLDER
        elif isinstance(filetype, FileType.Archive):
            icon_base64 = ICON_ARCHIVE
        else:
            icon_base64 = ''
        self.viewer.set_icon(icon_base64)
        # 按文件类型显示文件大小
        if isinstance(filetype, FileType.Folder):
            bytes_size = self.model.get_filesize_bytes()
        elif isinstance(filetype, FileType.Archive):
            bytes_size = self.model.get_filesize_bytes_extracted()
        else:
            bytes_size = 0
        size_str = function_file.format_bytes_size(bytes_size)
        self.viewer.set_filesize(size_str)

    def get_viewer(self) -> ComicInfoViewer:
        """获取viewer"""
        return self.viewer