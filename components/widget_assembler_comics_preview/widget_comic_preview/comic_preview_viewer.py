import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.widget_assembler_comics_preview.widget_comic_preview.res.icon_base64 import ICON_ARCHIVE, ICON_FOLDER, \
    ICON_LEFT_ARROW, ICON_RIGHT_ARROW, ICON_JUMP_TO, ICON_DELETE
from components.widget_assembler_comics_preview.widget_comic_preview.res.ui_comic_preview import Ui_Form


class ComicPreviewViewer(QWidget):
    """漫画预览模块的界面组件"""
    PreviousPage = Signal(name='上一页')
    NextPage = Signal(name='下一页')
    OpenPath = Signal(name='打开文件路径')
    Delete = Signal(name='删除漫画')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 添加自定义图像显示控件
        self.label_image_preview = lzytools._qt_pyside6.LabelImageAutoSize()
        self.ui.verticalLayout_preview.addWidget(self.label_image_preview)

        # 绑定信号
        self._bind_signal()

        # 设置图标
        self._set_icon()

    def show_image(self, preview_path: str):
        """显示图像"""
        self.label_image_preview.set_image(preview_path)

    def set_icon_archive(self):
        """设置文件类型图片为压缩文件"""
        self.ui.label_icon.setPixmap(lzytools._qt_pyside6.base64_to_pixmap(ICON_ARCHIVE))

    def set_icon_folder(self):
        """设置文件类型图片为文件夹"""
        self.ui.label_icon.setPixmap(lzytools._qt_pyside6.base64_to_pixmap(ICON_FOLDER))

    def set_filesize(self, filesize: str):
        """设置文件大小"""
        self.ui.label_filesize.setText(filesize)

    def set_filename(self, filename: str):
        """设置文件名"""
        self.ui.label_filename.setText(filename)

    def set_parent_dirpath(self, parent_dirpath: str):
        """设置父级路径"""
        self.ui.label_parent_dirpath.setText(parent_dirpath)

    def set_current_page(self, current_page: int):
        """设置当前页码"""
        self.ui.label_current_page.setText(str(current_page))

    def set_page_count(self, page_count: int):
        """设置页数"""
        self.ui.label_page_count.setText(str(page_count))

    def _bind_signal(self):
        """绑定信号"""
        self.ui.toolButton_previous.clicked.connect(self.PreviousPage.emit)
        self.ui.toolButton_next.clicked.connect(self.NextPage.emit)
        self.ui.toolButton_open.clicked.connect(self.OpenPath.emit)
        self.ui.toolButton_delete.clicked.connect(self.Delete.emit)

    def _set_icon(self):
        """设置图标"""
        self.ui.toolButton_previous.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_LEFT_ARROW))
        self.ui.toolButton_next.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_RIGHT_ARROW))
        self.ui.toolButton_open.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_JUMP_TO))
        self.ui.toolButton_delete.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_DELETE))


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = ComicPreviewViewer()
    program_ui.show()
    app_.exec()
