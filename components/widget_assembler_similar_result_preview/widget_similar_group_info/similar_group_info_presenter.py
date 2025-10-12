from typing import List

from PySide6.QtCore import QObject

from common import function_file
from common.class_comic import ComicInfoBase
from common.class_sign import SignStatus, TYPE_SIGN_STATUS
from components import widget_assembler_comics_preview
from components.widget_assembler_comics_preview import AssemblerDialogComicsPreview
from components.widget_assembler_similar_result_preview import widget_comic_info
from components.widget_assembler_similar_result_preview.widget_comic_info import ComicInfoPresenter
from components.widget_assembler_similar_result_preview.widget_similar_group_info.similar_group_info_model import \
    SimilarGroupInfoModel
from components.widget_assembler_similar_result_preview.widget_similar_group_info.similar_group_info_viewer import \
    SimilarGroupInfoViewer


class SimilarGroupInfoPresenter(QObject):
    """单个相似组信息模块的桥梁组件"""

    def __init__(self, viewer: SimilarGroupInfoViewer, model: SimilarGroupInfoModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.comic_info_list: List[ComicInfoBase] = []  # 内部漫画项的漫画信息类列表
        self.comics_presenter: List[ComicInfoPresenter] = []  # 内部漫画项的桥梁组件
        self.dialog_comics_preview: AssemblerDialogComicsPreview = widget_assembler_comics_preview.get_assembler()  # 预览漫画的dialog

        # 绑定信号
        self.viewer.Preview.connect(self.preview)
        self.dialog_comics_preview.ComicDeleted.connect(self.dialog_comic_deleted)

    def set_group_index(self, index: int):
        """设置当前组的编号"""
        self.viewer.set_group_index(index)

    def set_item_count(self):
        """设置当前组内部项目的总数"""
        self.viewer.set_item_count(len(self.comic_info_list))

    def set_item_size(self):
        """设置当前组内部项目的文件大小统计"""
        size_bytes = 0
        for comic_info in self.comic_info_list:
            size_bytes += comic_info.filesize_bytes
        size = function_file.format_bytes_size(size_bytes)
        self.viewer.set_item_size(size)

    def set_group_sign(self, sign: TYPE_SIGN_STATUS):
        """设置当前组的标记"""
        self.viewer.set_group_sign(sign)

    def add_comics(self, comic_info_list: List[ComicInfoBase]):
        """批量添加内部漫画信息项"""
        for comic_info in comic_info_list:
            self.add_comic(comic_info)

        self.set_item_count()
        self.set_item_size()
        self.highlight_comic_pages()
        self.highlight_comic_filesize()
        self.set_group_sign(SignStatus.Pending)

    def add_comic(self, comic_info: ComicInfoBase):
        """添加内部漫画信息项"""
        self.comic_info_list.append(comic_info)

        comic_info_presenter = widget_comic_info.get_presenter()
        comic_info_presenter.set_comic_info(comic_info)
        comic_info_presenter.ComicDeleted.connect(self.comic_deleted)
        self.comics_presenter.append(comic_info_presenter)

        widget = comic_info_presenter.get_viewer()
        self.viewer.add_widget(widget)

    def preview(self):
        """预览当前组内的所有漫画"""
        for comic_info in self.comic_info_list:
            self.dialog_comics_preview.add_comic(comic_info)

        self.dialog_comics_preview.exec()
        self.dialog_comics_preview.clear()

    def set_is_reconfirm_before_delete(self, is_reconfirm: bool):
        """设置是否删除前再次确认"""
        for widget in self.comics_presenter:
            widget: ComicInfoPresenter
            widget.set_is_reconfirm_before_delete(is_reconfirm)

        self.dialog_comics_preview.set_is_reconfirm_before_delete(is_reconfirm)

    def comic_deleted(self):
        """漫画被删除后的操作"""
        widget_presenter: ComicInfoPresenter = self.sender()
        # 删除存储的漫画信息类
        deleted_comic_info = widget_presenter.get_comic_info()
        self.comic_info_list.remove(deleted_comic_info)
        # 删除ui中显示的viewer
        viewer = widget_presenter.get_viewer()
        self.viewer.remove_widget(viewer)
        # 删除存储的presenter
        self.comics_presenter.remove(widget_presenter)
        widget_presenter.deleteLater()
        # 更新标记
        self._update_group_sign()

    def dialog_comic_deleted(self, deleted_comic_info: ComicInfoBase):
        """预览器中的漫画被删除后的操作"""
        # 检索控件，找到漫画信息类对应的控件
        widget_presenter_delete = None
        for presenter in self.comics_presenter:
            if presenter.get_comic_info() == deleted_comic_info:
                widget_presenter_delete = presenter
                break
        if widget_presenter_delete:
            # 删除存储的漫画信息类
            deleted_comic_info = widget_presenter_delete.get_comic_info()
            self.comic_info_list.remove(deleted_comic_info)
            # 删除ui中显示的viewer
            viewer = widget_presenter_delete.get_viewer()
            self.viewer.remove_widget(viewer)
            # 删除存储的presenter
            self.comics_presenter.remove(widget_presenter_delete)
            widget_presenter_delete.deleteLater()
            # 更新标记
            self._update_group_sign()
        else:
            raise RuntimeError('未找到对应的控件')

    def highlight_comic_pages(self):
        """高亮页数最多的漫画的文本"""
        max_pages = 0
        # 获取最大页数
        for widget_presenter in self.comics_presenter:
            comic_info = widget_presenter.get_comic_info()
            pages = comic_info.page_count
            if pages > max_pages:
                max_pages = pages
        # 高亮最大页数
        for widget_presenter in self.comics_presenter:
            comic_info = widget_presenter.get_comic_info()
            pages = comic_info.page_count
            if pages == max_pages:
                widget_presenter.highlight_pages()

    def highlight_comic_filesize(self):
        """高亮文件大小最大的漫画的文本"""
        max_filesize = 0
        # 获取最大文件大小
        for widget_presenter in self.comics_presenter:
            comic_info = widget_presenter.get_comic_info()
            filesize = comic_info.filesize_bytes
            if filesize > max_filesize:
                max_filesize = filesize
        # 高亮最大文件大小
        for widget_presenter in self.comics_presenter:
            comic_info = widget_presenter.get_comic_info()
            filesize = comic_info.filesize_bytes
            if filesize == max_filesize:
                widget_presenter.highlight_filesize()

    def _update_group_sign(self):
        """更新当前组的标记"""
        item_count = len(self.comic_info_list)
        if item_count <= 1:
            self.set_group_sign(SignStatus.Completed)
        else:
            self.set_group_sign(SignStatus.Partial)

    def get_viewer(self):
        """获取模块的Viewer"""
        return self.viewer
