# 预览单本漫画的控件
import os

import send2trash
from PySide6.QtCore import Signal, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from class_.class_comic_info import ComicInfo
from constant import _ICON_FOLDER, _ICON_ARCHIVE, _ICON_COMPUTER, _ICON_LAST, _ICON_NEXT, _ICON_RECYCLE_BIN, \
    _ICON_ERROR_IMAGE
from module import function_archive
from ui.src.ui_widget_comic_view import Ui_Form
from ui.tableWidget_filename import TabelWidgetFilename


class WidgetComicView(QWidget):
    """预览单本漫画的控件"""
    signal_deleted = Signal(str, name='预览控件中删除的漫画路径')

    def __init__(self, comic_info: ComicInfo, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 添加文件名控件
        self.tableWidget_filename = TabelWidgetFilename(self)
        self.ui.horizontalLayout_filename.addWidget(self.tableWidget_filename)
        # 初始化
        self._comic_info = comic_info
        self._page_index = 1  # 页码
        self._update_info()
        self._set_icon()
        self.ui.label_preview.setAlignment(Qt.AlignCenter)

        # 绑定槽函数
        self.ui.toolButton_open_file.clicked.connect(self._open_file)
        self.ui.toolButton_last.clicked.connect(lambda: self.page_turning(-1))
        self.ui.toolButton_next.clicked.connect(lambda: self.page_turning(1))
        self.ui.toolButton_delete.clicked.connect(self._delete_file)

    def page_turning(self, step: int):
        """翻页
        :param step: int，翻页页数，±号代表翻页方向"""
        new_page_index = self._page_index + step
        image_count = self._comic_info.image_count

        # 向后翻页超限时，分情况处理
        if new_page_index > image_count:
            if self._page_index == image_count:  # 在最后一页翻页时，切换到第一页
                new_page_index = 1
            else:  # 否则切换到最后一页
                new_page_index = image_count

        # 向前翻页超限时，分情况处理
        if new_page_index < 1:
            if self._page_index == 1:  # 在第一页翻页时，切换到最后一页
                new_page_index = image_count
            else:  # 否则切换到第一页
                new_page_index = 1

        # 更新页码参数
        self._page_index = new_page_index
        self._show_page()

    def reset_page_index(self):
        """重置页码"""
        self._page_index = 1
        self._show_page()

    def update_preview_image_size(self):
        """更新预览图片大小"""
        self._show_page()

    def _update_info(self):
        """更新漫画信息"""
        # 漫画类别
        comic_type = self._comic_info.filetype
        if comic_type == 'folder':
            self.ui.label_comic_type.setPixmap(QPixmap(_ICON_FOLDER))
        elif comic_type == 'archive':
            self.ui.label_comic_type.setPixmap(QPixmap(_ICON_ARCHIVE))

        # 文件名
        filename = os.path.basename(self._comic_info.path)
        self.tableWidget_filename.set_filename(filename, self._comic_info.path)

        # 文件大小
        filesize = self._comic_info.filesize  # 字节
        filesize_mb = round(filesize / 1024 / 1024, 2)
        self.ui.label_filesize.setText(f'{filesize_mb}MB')

        # 图片计数
        image_count = self._comic_info.image_count
        self.ui.label_page_count.setText(f'{image_count}')

        # 设置索引
        self.ui.label_page_index.setText(str(self._page_index))

        # 显示预览图
        self._show_page()

    def _show_page(self):
        """显示对应页码的图片"""
        self.ui.label_page_index.setText(str(self._page_index))
        # 设置图片对象
        index = self._page_index - 1  # 页码转为索引
        image_path = self._comic_info.images[index]
        if self._comic_info.filetype == 'folder':
            pixmap = QPixmap(image_path)
        else:
            img_bytes = function_archive.read_image(self._comic_info.path, image_path)
            pixmap = QPixmap()
            pixmap.loadFromData(img_bytes)
        if pixmap.isNull():  # 处理超过限制的图片对象，替换为裂图图标
            pixmap = QPixmap(_ICON_ERROR_IMAGE)

        # 重设预览QLabel的大小
        pixmap_height = pixmap.height()
        pixmap_width = pixmap.width()
        label_height = (self.parent().parent().height()
                        - self.ui.label_comic_type.height()
                        - self.ui.toolButton_open_file.height()
                        - 4 * 6)  # 框架的高-内部其他控件的高-控件之间的间隔
        resize_width = int(pixmap_width * label_height / pixmap_height)
        label_size = QSize(resize_width, label_height)
        self.ui.label_preview.resize(label_size)
        # 缩放图片并保持纵横比
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 显示图片
        self.ui.label_preview.setPixmap(scaled_pixmap)

    def _delete_file(self):
        """删除文件"""
        comic_path = self._comic_info.path
        send2trash.send2trash(comic_path)
        self.signal_deleted.emit(comic_path)

    def _open_file(self):
        """打开文件"""
        comic_path = self._comic_info.path
        os.startfile(comic_path)

    def _set_icon(self):
        """设置图标"""
        self.ui.toolButton_open_file.setIcon(QIcon(_ICON_COMPUTER))
        self.ui.toolButton_last.setIcon(QIcon(_ICON_LAST))
        self.ui.toolButton_next.setIcon(QIcon(_ICON_NEXT))
        self.ui.toolButton_delete.setIcon(QIcon(_ICON_RECYCLE_BIN))
