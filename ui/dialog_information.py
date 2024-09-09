# 说明

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import *

from constant import _ICON_NEXT, _ICON_LAST
from ui.src.ui_dialog_information import Ui_dialog


class DialogInformation(QDialog):
    """说明"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        # 插页
        # 备忘录 插入图片页

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
        label.setPixmap(pixmap)

        layout.addWidget(label)
        new_page.setLayout(layout)

        self.ui.stackedWidget_show.addWidget(new_page)
