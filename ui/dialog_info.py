# 说明、教程的dialog控件

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import *

from constant import ICON_NEXT, ICON_PREVIOUS, INFO_MAIN, \
    INFO_PREVIEW, INFO_CACHE
from ui.ui_info_dialog import Ui_dialog


class DialogInfo(QDialog):
    """说明、教程的dialog控件"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        # 插页
        self._add_image_page(INFO_MAIN)
        self._add_image_page(INFO_PREVIEW)
        self._add_image_page(INFO_CACHE)
        # 初始化
        self.ui.toolButton_next.setIcon(QIcon(ICON_NEXT))
        self.ui.toolButton_previous.setIcon(QIcon(ICON_PREVIOUS))
        self.ui.label_max_page.setText(str(self.ui.stackedWidget_show.count()))
        self.ui.textBrowser.setOpenExternalLinks(True)  # 设置允许打开外部链接
        # 设置槽函数
        self.ui.toolButton_next.clicked.connect(lambda: self.to_page(1))
        self.ui.toolButton_previous.clicked.connect(lambda: self.to_page(-1))

    def to_page(self, index):
        """切页"""
        page_index = self.ui.stackedWidget_show.currentIndex() + index
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
        label.setPixmap(pixmap)

        layout.addWidget(label)
        new_page.setLayout(layout)

        self.ui.stackedWidget_show.addWidget(new_page)
