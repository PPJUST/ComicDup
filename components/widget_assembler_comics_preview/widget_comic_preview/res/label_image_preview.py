import os.path

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class LabelImagePreview(QLabel):
    """预览图片的label"""

    def __init__(self, parent=None, image_path: str = None):
        """:param image_path: str，图片路径"""
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.pixmap_original = None
        self.image_filename = None
        if image_path:
            self.pixmap_original = QPixmap(image_path)
            self.image_filename = os.path.split(image_path)[1]

    def set_image(self, image_path: str = None):
        """设置图片"""
        self.pixmap_original = QPixmap(image_path)
        self.image_filename = os.path.split(image_path)[1]
        self.resize_image_size(self.width(), self.height())

    def set_bytes_image(self, data: bytes, filename: str = None):
        """设置bytes图片"""
        self.pixmap_original = QPixmap()
        self.pixmap_original.loadFromData(data, format=None)
        self.resize_image_size(self.width(), self.height())
        if filename:
            self.image_filename = os.path.split(filename)[1]

    def resize_image_size(self, width: int, height: int):
        """设置图片尺寸"""
        size = QSize(width, height)
        if self.pixmap_original and not self.pixmap_original.isNull():
            scaled_pixmap = self.pixmap_original.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)
