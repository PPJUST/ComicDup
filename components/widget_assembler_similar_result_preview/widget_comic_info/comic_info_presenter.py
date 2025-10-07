import os

import lzytools.file
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox

from common import function_file
from common.class_comic import ComicInfoBase
from common.class_config import FileType
from components.widget_assembler_similar_result_preview.widget_comic_info.comic_info_model import ComicInfoModel
from components.widget_assembler_similar_result_preview.widget_comic_info.comic_info_viewer import ComicInfoViewer
from components.widget_search_list.res.icon_base64 import ICON_FOLDER, ICON_ARCHIVE


class ComicInfoPresenter(QObject):
    """单个漫画信息模块的桥梁组件"""

    def __init__(self, viewer: ComicInfoViewer, model: ComicInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_info: ComicInfoBase = None  # 显示的漫画的漫画信息类
        self.is_reconfirm_before_delete = True  # 删除前是否需要再次确认

        # 绑定信号
        self.viewer.OpenPath.connect(self.open_path)
        self.viewer.RefreshInfo.connect(self.refresh_info)
        self.viewer.Delete.connect(self.delete_comic)

    def is_reconfirm_before_delete(self, is_reconfirm: bool):
        """设置是否删除前再次确认"""
        self.is_reconfirm_before_delete = is_reconfirm

    def set_comic_info(self, comic_info: ComicInfoBase):
        """设置需要显示的漫画的漫画信息类"""
        self.comic_info = comic_info
        self._show_comic_info()

    def open_path(self):
        """打开路径"""
        os.startfile(self.comic_info.filepath)

    def refresh_info(self, comic_info: ComicInfoBase):
        """刷新信息"""
        self.set_comic_info(comic_info)

    def delete_comic(self):
        """删除文件"""
        is_delete = True
        if self.is_reconfirm_before_delete:
            reply = QMessageBox.question(
                self.viewer,
                '确认删除',
                '是否删除本地漫画（到回收站）',
                QMessageBox.Yes | QMessageBox.No,  # 提供“是”和“否”两个按钮
                QMessageBox.No  # 默认聚焦在“否”按钮上
            )

            if reply == QMessageBox.No:
                is_delete = False

        if is_delete:
            path = self.comic_info.filepath
            lzytools.file.delete(path, send_to_trash=True)

        # 备忘录 删除后更新信息和变量

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
            bytes_size = self.comic_info.filesize_bytes
        else:
            bytes_size = 0
        size_str = function_file.format_bytes_size(bytes_size)
        self.viewer.set_filesize(size_str)

    def get_viewer(self) -> ComicInfoViewer:
        """获取viewer"""
        return self.viewer
