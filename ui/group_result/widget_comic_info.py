# 显示单本漫画基本信息，预览图、页数、文件大小等
import os
from typing import Union

import send2trash
from PySide6.QtCore import Signal
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from class_.class_comic_info import ComicInfo
from constant import _ICON_ERROR_IMAGE
from constant import _ICON_VIEW, _ICON_COMPUTER, _ICON_RECYCLE_BIN, _ICON_FOLDER, _ICON_ARCHIVE
from module import function_normal
from ui.src.ui_widget_comic_info import Ui_Form
from ui.tableWidget_filename import TabelWidgetFilename


class WidgetComicInfo(QWidget):
    """显示单本漫画基本信息，预览图、页数、文件大小等(■Widget->ScrollArea->TreeWidget)"""
    signal_view = Signal()
    signal_delete = Signal()

    def __init__(self, comic_info: ComicInfo, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # ui设置
        self.setFixedSize(150, 290)
        self.ui.label_preview.setFixedSize(140, 200)  # 设置固定高度200，宽度为高度*0.7
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self._set_context_menu()
        self.ui.label_preview.setAlignment(Qt.AlignCenter)
        self._set_icon()

        # 添加文件名控件
        self.tableWidget_filename = TabelWidgetFilename(self)
        self.ui.horizontalLayout_filename.addWidget(self.tableWidget_filename)

        # 初始化
        self._comic_info = comic_info
        self._update_info()

        # 绑定预览图label双击事件
        self.ui.label_preview.mouseDoubleClickEvent = self._double_click_preview

        # 绑定槽函数
        self.ui.toolButton_view.clicked.connect(self.signal_view.emit)
        self.ui.toolButton_open_file.clicked.connect(self._open_file)
        self.ui.toolButton_delete.clicked.connect(self._delete_file)

    def get_comic_info(self):
        """获取对应的漫画信息类"""
        return self._comic_info

    def get_comic_path(self):
        """获取对应的漫画路径"""
        return self._comic_info.path

    def check_validity(self):
        """检查有效性，无效则删除该项（路径存在，大小一致）"""
        comic_path = self._comic_info.path
        filesize = self._comic_info.filesize
        if not os.path.exists(comic_path) or not function_normal.get_size(comic_path) == filesize:
            self.signal_delete.emit()
            return comic_path

    def get_size_and_count(self):
        """获取漫画大小和页数"""
        path = self._comic_info.path
        filesize = self._comic_info.real_filesize
        image_count = self._comic_info.image_count
        info = {'filesize': filesize, 'image_count': image_count}
        return path, info

    def delete_if_in_list(self, paths: Union[list, str]):
        """删除在传入参数list中存在的项"""
        if isinstance(paths, str):
            paths = [paths]

        path = self._comic_info.path
        if path in paths:
            self.signal_delete.emit()

    def _update_info(self):
        """更新漫画信息"""
        # 漫画类别
        comic_type = self._comic_info.filetype
        if comic_type == 'folder':
            self.ui.label_type.setPixmap(QPixmap(_ICON_FOLDER))
        elif comic_type == 'archive':
            self.ui.label_type.setPixmap(QPixmap(_ICON_ARCHIVE))

        # 文件名
        filename = os.path.basename(self._comic_info.path)
        self.tableWidget_filename.set_filename(filename)

        # 文件大小
        filesize = self._comic_info.filesize  # 字节
        filesize_mb = round(filesize / 1024 / 1024, 2)
        self.ui.label_filesize.setText(f'{filesize_mb}MB')

        # 图片计数
        image_count = self._comic_info.image_count
        self.ui.label_image_count.setText(f'{image_count}图')

        # 显示预览图
        self._set_preview()

    def _open_file(self):
        """打开文件"""
        comic_path = self._comic_info.path
        os.startfile(comic_path)

    def _open_parent_folder(self):
        """打开所在目录"""
        comic_path = self._comic_info.path
        os.startfile(os.path.dirname(comic_path))

    def _delete_file(self):
        """删除文件"""
        comic_path = self._comic_info.path
        if os.path.exists(comic_path):
            send2trash.send2trash(comic_path)
        self.signal_delete.emit()

    def _set_preview(self):
        """显示预览图"""
        review_image_path = self._comic_info.preview_path
        pixmap = QPixmap(review_image_path)
        if not pixmap or pixmap.isNull():  # 处理超过限制的图片对象，替换为裂图图标
            pixmap = QPixmap(_ICON_ERROR_IMAGE)
        # 获取QLabel的大小
        label_size = self.ui.label_preview.size()
        # 根据图片大小和QLabel大小来缩放图片并保持纵横比
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.label_preview.setPixmap(scaled_pixmap)

    def _set_icon(self):
        """设置图标"""
        self.ui.toolButton_view.setIcon(QIcon(_ICON_VIEW))
        self.ui.toolButton_open_file.setIcon(QIcon(_ICON_COMPUTER))
        self.ui.toolButton_delete.setIcon(QIcon(_ICON_RECYCLE_BIN))

    def _set_context_menu(self):
        """设置右键菜单"""
        menu = QMenu(self)

        action_view = QAction('预览', menu)
        action_view.triggered.connect(self.signal_view.emit)
        menu.addAction(action_view)

        action_open_file = QAction('打开文件', menu)
        action_open_file.triggered.connect(self._open_file)
        menu.addAction(action_open_file)

        action_open_parent_folder = QAction('打开所在目录', menu)
        action_open_parent_folder.triggered.connect(self._open_parent_folder)
        menu.addAction(action_open_parent_folder)

        action_delete = QAction('删除文件', menu)
        action_delete.triggered.connect(self._delete_file)
        menu.addAction(action_delete)

        self.customContextMenuRequested.connect(lambda pos: menu.exec(self.mapToGlobal(pos)))  # 显示菜单

    def _double_click_preview(self, event):
        """预览图label双击事件"""
        if event.button() == Qt.LeftButton:
            self.signal_view.emit()
