# 说明
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap, Qt
from PySide6.QtWidgets import *

from constant import _ICON_NEXT, _ICON_LAST, _PAGE_MAIN, _PAGE_PREVIEW, _PAGE_CACHE, _PAGE_EXAMPLE_GRAYS_AND_COLOR, \
    _PAGE_EXAMPLE_DIFF_COMIC, _PAGE_EXAMPLE_COVER_MISSING
from ui.src.ui_dialog_information import Ui_dialog


class DialogInformation(QDialog):
    """说明"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.setFixedSize(900, 600)

        # 插页
        self._add_image_page(_PAGE_MAIN)
        self._add_image_page(_PAGE_PREVIEW)
        self._add_image_page(_PAGE_CACHE)
        self._add_image_page(_PAGE_EXAMPLE_GRAYS_AND_COLOR)
        self._add_image_page(_PAGE_EXAMPLE_DIFF_COMIC)
        self._add_image_page(_PAGE_EXAMPLE_COVER_MISSING)

        # 初始化
        self.ui.toolButton_next.setIcon(QIcon(_ICON_NEXT))
        self.ui.toolButton_last.setIcon(QIcon(_ICON_LAST))
        self.ui.textBrowser.setOpenExternalLinks(True)  # 设置允许打开外部链接
        self.ui.label_max_page.setText(str(self.ui.stackedWidget_show.count()))

        # 设置槽函数
        self.ui.toolButton_next.clicked.connect(lambda: self.page_turning(1))
        self.ui.toolButton_last.clicked.connect(lambda: self.page_turning(-1))

    def page_turning(self, step: int):
        """翻页"""
        page_index = self.ui.stackedWidget_show.currentIndex() + step
        max_page = self.ui.stackedWidget_show.count()
        if page_index >= max_page:
            page_index = 0
        if page_index < 0:
            page_index = max_page - 1

        self.ui.stackedWidget_show.setCurrentIndex(page_index)
        self.ui.label_current_page.setText(str(page_index + 1))

    def _add_image_page(self, image_file):
        """插入图片页"""
        new_page = QWidget()
        layout = QVBoxLayout()

        label = QLabel()
        pixmap = QPixmap(image_file)
        # 重设预览Label的大小
        pixmap_height = pixmap.height()
        pixmap_width = pixmap.width()
        label_height = self.height() - self.ui.label_max_page.height() - 10 * 4
        resize_width = int(pixmap_width * label_height / pixmap_height)
        label_size = QSize(resize_width, label_height)
        label.resize(label_size)
        # 缩放图片并保持纵横比
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # 显示图片
        label.setPixmap(scaled_pixmap)

        layout.addWidget(label)
        new_page.setLayout(layout)

        self.ui.stackedWidget_show.addWidget(new_page)
