import os

import DoujinTools
import lzytools
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

from common import function_file
from common.class_comic import ComicInfoBase
from common.class_config import FileType
from components.widget_assembler_similar_result_preview.widget_comic_info_line.comic_info_line_model import \
    ComicInfoLineModel
from components.widget_assembler_similar_result_preview.widget_comic_info_line.comic_info_line_viewer import \
    ComicInfoLineViewer
from components.widget_search_list.res.icon_base64 import ICON_FOLDER, ICON_ARCHIVE


class ComicInfoLinePresenter(QObject):
    """单个漫画信息模块的桥梁组件"""
    ComicDeleted = Signal(name='删除漫画')
    UpdateComicInfo = Signal(ComicInfoBase, name='更新数据库中的漫画信息')

    def __init__(self, viewer: ComicInfoLineViewer, model: ComicInfoLineModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_info: ComicInfoBase = None  # 显示的漫画的漫画信息类
        self.is_reconfirm_before_delete = True  # 删除前是否需要再次确认

        # 绑定信号
        self.viewer.OpenPath.connect(self.open_path)
        self.viewer.OpenDir.connect(self.open_dir)
        self.viewer.RefreshInfo.connect(self.refresh_info)
        self.viewer.Delete.connect(self.delete_comic)
        self.viewer.Rename.connect(self.rename_comic)

    def get_comic_path(self):
        """获取漫画路径"""
        return self.comic_info.filepath

    def get_comic_info(self):
        """获取漫画信息类"""
        return self.comic_info

    def set_is_reconfirm_before_delete(self, is_reconfirm: bool):
        """设置是否删除前再次确认"""
        self.is_reconfirm_before_delete = is_reconfirm

    def set_comic_info(self, comic_info: ComicInfoBase):
        """设置需要显示的漫画的漫画信息类"""
        self.comic_info = comic_info
        self._show_comic_info()

    def open_path(self):
        """打开路径"""
        os.startfile(self.comic_info.filepath)

    def open_dir(self):
        """打开路径所在目录"""
        os.startfile(os.path.dirname(self.comic_info.filepath))

    def refresh_info(self):
        """刷新信息"""
        # 调用内部方法更新信息
        self.comic_info.refresh()
        self.comic_info.save_preview_image()

        # 更新本地数据库
        self.UpdateComicInfo.emit(self.comic_info)

        # 重新显示
        self.set_comic_info(self.comic_info)

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

    def rename_comic(self):
        """重命名文件"""
        pass  # todo

    def set_similarity(self, similarity: str):
        """设置相似度（百分比）
        :param similarity:百分比数字文本，例如90%"""
        self.viewer.set_similarity(similarity)

    def highlight_filesize(self):
        """高亮显示文件大小"""
        self.viewer.highlight_filesize()

    def highlight_pages(self):
        """高亮显示页数"""
        self.viewer.highlight_pages()

    def highlight_file_time(self):
        """高亮显示文件时间"""
        self.viewer.highlight_file_time()

    def highlight_filename(self):
        """高亮显示文件名"""
        self.viewer.highlight_filename()

    def _show_comic_info(self):
        """在viewer上显示漫画信息"""
        filetype = self.comic_info.filetype

        self.viewer.set_filepath(self.comic_info.filepath)
        if not os.path.exists(self.comic_info.preview_path):
            self.comic_info.fix_preview_path()
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

        self.viewer.set_page_count(self.comic_info.page_count)
        # 最后修改时间
        modified_time = self.comic_info.modified_time
        modified_time_str = lzytools.time.convert_duration_to_date(modified_time, _format="%Y-%m-%d")
        self.viewer.set_file_time(modified_time_str)

        self._analyse_filetitle()

    def _analyse_filetitle(self):
        """分析漫画名，识别字段"""
        filetitle = self.comic_info.filetitle
        doujin_name = DoujinTools.name.DoujinshiName(filetitle)

        circle_names = doujin_name.circle_names.get_value()
        self.viewer.set_attribute_circle_name(circle_names)

        artist_names = doujin_name.artist_names.get_value()
        self.viewer.set_attribute_artist_name(artist_names)

        language = doujin_name.language.get_value()
        self.viewer.set_attribute_language(language)

        translators = doujin_name.translators.get_value()
        self.viewer.set_attribute_translator(translators)

        special_indicators = doujin_name.special_indicators.get_value()
        self.viewer.set_attribute_special_indicators(special_indicators)

    def get_viewer(self) -> ComicInfoLineViewer:
        """获取viewer"""
        return self.viewer
