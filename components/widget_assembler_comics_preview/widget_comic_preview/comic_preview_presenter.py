import base64
import os

import lzytools
import lzytools_archive
import lzytools_image
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

from common import function_file, function_image
from common.class_comic import ComicInfoBase
from common.class_config import FileType
from components.widget_assembler_comics_preview.widget_comic_preview.comic_preview_model import ComicPreviewModel
from components.widget_assembler_comics_preview.widget_comic_preview.comic_preview_viewer import ComicPreviewViewer
from components.widget_assembler_comics_preview.widget_comic_preview.res.icon_base64 import ICON_READ_FAILED


class ComicPreviewPresenter(QObject):
    """漫画预览模块的桥梁组件"""
    ComicDeleted = Signal(name='删除漫画')
    TurnPaged = Signal(name='翻页')

    def __init__(self, viewer: ComicPreviewViewer, model: ComicPreviewModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_info: ComicInfoBase = None
        self.page_paths = []  # 页面列表
        self.page_index = 1  # 当前页码（从1开始）
        self.is_reconfirm_before_delete = True  # 删除前是否需要再次确认

        # 绑定信号
        self._bind_signal()

    def set_is_reconfirm_before_delete(self, is_reconfirm: bool):
        """设置是否删除前再次确认"""
        self.is_reconfirm_before_delete = is_reconfirm

    def set_comic(self, comic_info: ComicInfoBase):
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
        filesize = self.comic_info.filesize_bytes
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
        try:
            # 文件夹类漫画
            if isinstance(self.comic_info.filetype, FileType.Folder) or self.comic_info.filetype == FileType.Folder:
                image_path = self.page_paths[page_index - 1]
                if not os.path.exists(image_path):
                    raise Exception('read failed')
                self.viewer.show_image(image_path)
            # 压缩文件类漫画
            elif isinstance(self.comic_info.filetype, FileType.Archive) or self.comic_info.filetype == FileType.Archive:
                archive_path = self.comic_info.filepath
                inside_image_path = self.page_paths[page_index - 1]
                image_bytes = lzytools_archive.read_image(archive_path, inside_image_path)
                if not image_bytes:
                    raise Exception('read failed')
                self.viewer.show_bytes_image(image_bytes, inside_image_path)
        except:  # 读取失败时
            image_base64 = ICON_READ_FAILED
            image_bytes = base64.b64decode(image_base64)
            self.viewer.show_bytes_image(image_bytes)

    def calc_current_image_hash(self):
        """计算当前显示的图片的hash值"""
        # 简单计算12*12的dhash
        comic_type = self.comic_info.filetype
        if isinstance(comic_type, FileType.Folder) or comic_type == FileType.Folder:
            image_path = self.page_paths[self.page_index - 1]
            hash_ = function_image.calc_image_hash(image_path, 'dhash', 144)
        elif isinstance(comic_type, FileType.Archive) or comic_type == FileType.Archive:
            archive_path = self.comic_info.filepath
            inside_image_path = self.page_paths[self.page_index - 1]
            hash_ = function_image.calc_archive_image_hash(archive_path, inside_image_path, 'dhash', 144)
        else:
            hash_ = ''

        return hash_

    def compare_current_image_hash(self, compare_hash: str):
        """计算当前图片的hash值，并于提供的hash值进行对比，计算相似度，并显示在ui上"""
        try:
            # 计算相似度
            self_hash = self.calc_current_image_hash()
            similar = lzytools_image.calc_hash_similar(self_hash, compare_hash)
            similar_str = f'{int(similar * 100)}%'
            # 显示在ui的左上角
            self.viewer.show_similar(similar_str)
        except:  # 无法正常计算相似度时
            self.viewer.show_similar('计算失败')

    def show_similar_info(self, info: str):
        """显示相似度信息"""
        self.viewer.show_similar(info)

    def clear_similar_info(self):
        """清除相似度信息"""
        self.viewer.show_similar('')

    def turn_to_previous_page(self, page_count: int = 1):
        """向前翻页"""
        if self.page_index == 1:  # 在第一页时，如果需要切换到上一页，则切换到最后一页
            self.page_index = len(self.page_paths)
        else:  # 不在第一页时，按正常逻辑操作，但不能超过页码的下限1
            self.page_index -= page_count
            if self.page_index < 1:
                self.page_index = 1
        self.show_page(self.page_index)
        self.viewer.set_current_page(self.page_index)
        self.TurnPaged.emit()

    def turn_to_next_page(self, page_count: int = 1):
        """向后翻页"""
        if self.page_index == len(self.page_paths):  # 在最后一页时，如果需要切换到下一页，则切换到第一页
            self.page_index = 1
        else:  # 不在最后一页时，按正常逻辑操作，但不能超过页码的上限
            self.page_index += page_count
            if self.page_index > len(self.page_paths):
                self.page_index = len(self.page_paths)
        self.show_page(self.page_index)
        self.viewer.set_current_page(self.page_index)
        self.TurnPaged.emit()

    def reset_page(self):
        """重置页码"""
        self.page_index = 1
        self.show_page(self.page_index)
        self.viewer.set_current_page(self.page_index)
        self.TurnPaged.emit()

    def resize_image_size(self, width: int, height: int):
        """设置图片尺寸"""
        self.viewer.resize_image_size(width, height)

    def open_path(self):
        """打开漫画文件"""
        path = self.comic_info.filepath
        os.startfile(path)

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
            self.ComicDeleted.emit()

    def get_viewer(self):
        """获取viewer"""
        return self.viewer

    def _bind_signal(self):
        """绑定信号"""
        self.viewer.PreviousPage.connect(self.turn_to_previous_page)
        self.viewer.NextPage.connect(self.turn_to_next_page)
        self.viewer.OpenPath.connect(self.open_path)
        self.viewer.Delete.connect(self.delete_comic)
