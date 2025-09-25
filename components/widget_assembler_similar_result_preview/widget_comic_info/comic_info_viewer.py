import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QApplication

from components.widget_assembler_similar_result_preview.widget_comic_info.res.icon_base64 import ICON_JUMP_TO, \
    ICON_REFRESH, ICON_DELETE
from components.widget_assembler_similar_result_preview.widget_comic_info.res.ui_comic_info import Ui_Form


class ComicInfoViewer(QWidget):
    """单个漫画信息模块的界面组件"""
    OpenPath = Signal(name='打开文件路径')
    RefreshInfo = Signal(name='刷新漫画信息')
    Delete = Signal(name='删除漫画')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 绑定信号
        self.ui.toolButton_open_path.clicked.connect(self.OpenPath)
        self.ui.toolButton_refresh.clicked.connect(self.RefreshInfo)
        self.ui.toolButton_delete.clicked.connect(self.Delete)

        # 设置图标
        self._set_icon()

    def set_filetype_icon(self, icon_base64: str):
        """设置漫画的文件类型图标"""
        pixmap = lzytools._qt_pyside6.base64_to_pixmap(icon_base64)
        self.ui.label_icon.setPixmap(pixmap)

    def set_filetitle(self, filetitle: str):
        """设置漫画标题"""
        self.ui.label_filetitle.setText(filetitle)

    def set_parent_dirpath(self, parent_dirpath: str):
        """设置漫画的父级路径"""
        self.ui.label_parent_dirpath.setText(parent_dirpath)

    def set_page_count(self, page_count: int):
        """设置漫画的页数"""
        self.ui.label_page_count.setText(str(page_count))

    def set_filesize(self, filesize: str):
        """设置漫画的文件大小"""
        self.ui.label_filesize.setText(filesize)

    def set_preview(self, preview_path: str):
        """设置漫画的预览图片"""
        self.ui.label_preview.setPixmap(QPixmap(preview_path))

    def _set_icon(self):
        """设置图标"""
        self.ui.toolButton_open_path.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_JUMP_TO))
        self.ui.toolButton_refresh.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_REFRESH))
        self.ui.toolButton_delete.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_DELETE))


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = ComicInfoViewer()
    program_ui.show()
    app_.exec()
