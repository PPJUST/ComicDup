# 漫画预览控件
import os.path

import natsort
import send2trash
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import constant
from constant import OVERSIZE_IMAGE
from module import function_config
from module import function_normal


class DialogComicsPreview(QDialog):
    """用于对比多本漫画差异的Dialog控件"""
    signal_del_file = Signal(str)
    signal_resized = Signal()

    def __init__(self):
        super().__init__()
        """设置ui"""
        self.verticalLayout = QVBoxLayout(self)
        width, height = function_config.get_preview_widget_wh()
        self.resize(width, height)

        # 控件组 同步滚动
        self.horizontalLayout = QHBoxLayout()

        self.label_sync_scroll = QLabel()
        self.label_sync_scroll.setText('同步滚动')
        self.horizontalLayout.addWidget(self.label_sync_scroll)

        self.toolButton_previous_5p_image = QToolButton()
        self.toolButton_previous_5p_image.setIcon(QIcon(constant.ICON_PREVIOUS_5P))
        self.horizontalLayout.addWidget(self.toolButton_previous_5p_image)

        self.toolButton_previous_image = QToolButton()
        self.toolButton_previous_image.setIcon(QIcon(constant.ICON_PREVIOUS))
        self.horizontalLayout.addWidget(self.toolButton_previous_image)

        self.toolButton_next_image = QToolButton()
        self.toolButton_next_image.setIcon(QIcon(constant.ICON_NEXT))
        self.horizontalLayout.addWidget(self.toolButton_next_image)

        self.toolButton_next_5p_image = QToolButton()
        self.toolButton_next_5p_image.setIcon(QIcon(constant.ICON_NEXT_5P))
        self.horizontalLayout.addWidget(self.toolButton_next_5p_image)

        self.toolButton_refresh = QToolButton()
        self.toolButton_refresh.setIcon(QIcon(constant.ICON_REFRESH))
        self.horizontalLayout.addWidget(self.toolButton_refresh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # 控件组 预览
        self.scrollArea = QScrollArea()
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.layout_comic_widget = QHBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        """设置初始变量"""
        self.show_path_list = None
        self.sync_scroll_index = 0  # 同步滚动索引

        """设置定时器，用于延迟改变预览图控件大小"""
        self.resize_timer = QTimer()
        self.resize_timer.setSingleShot(True)  # 设置单次触发
        self.resize_timer.timeout.connect(self.resize_preview_size)

        """连接槽函数"""
        self.toolButton_next_image.clicked.connect(lambda: self.sync_show_next_image(step=1))
        self.toolButton_previous_image.clicked.connect(lambda: self.sync_show_previous_image(step=1))
        self.toolButton_next_5p_image.clicked.connect(lambda: self.sync_show_next_image(step=5))
        self.toolButton_previous_5p_image.clicked.connect(lambda: self.sync_show_previous_image(step=5))
        self.toolButton_refresh.clicked.connect(self.refresh_index)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize_timer.start(300)  # 延迟x毫秒

    def resize_preview_size(self):
        height = self.size().height() - 200
        layout = self.layout_comic_widget.layout()
        function_config.reset_preview_widget_wh(self.size().width(), self.size().height())

        for i in range(layout.count()):
            item = layout.itemAt(i)
            show_comic_widget = item.widget()
            show_comic_widget.reset_height(height)

    def set_show_path_list(self, path_list):
        """设置需要显示的文件的列表"""
        self.show_path_list = path_list
        self.show_path()

    def show_path(self):
        """将列表中的文件显示在ui上"""
        for path in self.show_path_list:
            if os.path.exists(path) and os.path.isdir(path):
                show_comic_widget = WidgetSingleComicPreview()
                self.layout_comic_widget.addWidget(show_comic_widget)
                show_comic_widget.set_path(path)
                show_comic_widget.signal_del_file.connect(self.accept_signal_del_file)

    def sync_show_next_image(self, step: int = 1):
        """全局滚动，索引+1"""
        layout = self.layout_comic_widget.layout()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            show_comic_widget = item.widget()
            show_comic_widget.show_next_image(step)

    def sync_show_previous_image(self, step: int = 1):
        """全局滚动，索引-1"""
        layout = self.layout_comic_widget.layout()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            show_comic_widget = item.widget()
            show_comic_widget.show_previous_image(step)

    def refresh_index(self):
        """重置索引"""
        layout = self.layout_comic_widget.layout()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            show_comic_widget = item.widget()
            show_comic_widget.reset_index()

    def accept_signal_del_file(self, path):
        """接收子控件删除文件的信号，并再次发送信号"""
        self.signal_del_file.emit(path)


class WidgetSingleComicPreview(QWidget):
    """单本漫画预览控件，附带一些小功能"""
    signal_del_file = Signal(str)

    def __init__(self):
        super().__init__()
        """设置ui"""
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setAlignment(Qt.AlignCenter)

        # 控件组 预览图
        self.label_preview = QLabel()
        self.label_preview.setText('显示图像')
        self.label_preview.setScaledContents(True)
        self.label_preview.setAlignment(Qt.AlignCenter)
        self.label_preview.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.label_preview.setStyleSheet('border: 2px solid red')
        self.verticalLayout.addWidget(self.label_preview)

        # 控件组 文件信息
        self.horizontalLayout_2 = QHBoxLayout()

        self.label_filetype_icon = QLabel()
        self.label_filetype_icon.setText('图标')
        self.label_filetype_icon.setFixedSize(15, 15)
        self.horizontalLayout_2.addWidget(self.label_filetype_icon)

        self.label_size_and_count = QLabel()
        self.label_size_and_count.setText('大小')
        self.horizontalLayout_2.addWidget(self.label_size_and_count)

        self.label_filepath = QLabel()
        self.label_filepath.setText('文件路径')
        self.label_filepath.setWordWrap(True)
        self.horizontalLayout_2.addWidget(self.label_filepath)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # 控件组 操作按钮
        self.horizontalLayout = QHBoxLayout()

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_previous_image = QToolButton()
        self.toolButton_previous_image.setIcon(QIcon(constant.ICON_PREVIOUS))
        self.horizontalLayout.addWidget(self.toolButton_previous_image)

        self.toolButton_next_image = QToolButton()
        self.toolButton_next_image.setIcon(QIcon(constant.ICON_NEXT))
        self.horizontalLayout.addWidget(self.toolButton_next_image)

        self.label_index = QLabel()
        self.label_index.setText('显示索引')
        self.horizontalLayout.addWidget(self.label_index)

        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Plain)
        self.horizontalLayout.addWidget(self.line)

        self.toolButton_recycle_bin = QToolButton()
        self.toolButton_recycle_bin.setIcon(QIcon(constant.ICON_RECYCLE_BIN))
        self.horizontalLayout.addWidget(self.toolButton_recycle_bin)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)

        """设置初始变量"""
        self.path = None
        self.image_list = []
        self.image_index = 0
        self.resize_height = self.sizeHint().height()  # 重设预览图控件的高度

        """连接槽函数"""
        self.toolButton_recycle_bin.clicked.connect(self.delete_file)
        self.toolButton_next_image.clicked.connect(lambda: self.show_next_image(step=1))
        self.toolButton_previous_image.clicked.connect(lambda: self.show_previous_image(step=1))

    def set_path(self, path):
        """设置需要显示的路径"""
        self.path = path

        for i in natsort.natsorted(os.listdir(path)):
            fullpath = os.path.join(path, i)
            if function_normal.check_filetype(fullpath) == 'image':
                self.image_list.append(fullpath)

        self.set_filetype_icon(constant.ICON_FOLDER)
        self.set_filesize_text()
        self.label_filepath.setText(path)
        self.show_preview()

    def set_index(self, step: int):
        """增减索引"""
        self.image_index += step
        self.show_preview()

    def reset_index(self):
        """重置索引"""
        self.image_index = 0
        self.show_preview()

    def reset_height(self, height: int):
        """重设预览图控件的高度"""
        self.resize_height = height
        self.show_preview()

    def show_preview(self):
        """显示预览图"""
        self.show_index()
        # 设置图片对象
        pixmap = QPixmap(self.image_list[self.image_index])
        if pixmap.isNull():  # 处理超过限制的图片对象，替换为裂图图标
            pixmap = QPixmap(OVERSIZE_IMAGE)
        pixmap_height = pixmap.height()
        pixmap_width = pixmap.width()
        # 重设预览QLabel的大小
        resize_width = int(pixmap_width * self.resize_height / pixmap_height)
        label_size = QSize(resize_width, self.resize_height)
        self.label_preview.resize(label_size)
        # 缩放图片并保持纵横比
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # 设置显示图片
        self.label_preview.setPixmap(scaled_pixmap)

    def delete_file(self):
        """删除文件"""
        if os.path.exists(self.path):
            send2trash.send2trash(self.path)
        self.signal_del_file.emit(self.path)
        self.deleteLater()

    def show_next_image(self, step: int = 1):
        """显示下一张图片"""
        max_index = len(self.image_list) - 1
        if self.image_index == max_index:
            self.image_index = 0
        else:
            if self.image_index + step >= max_index:
                self.image_index = max_index
            else:
                self.image_index += step

        self.show_preview()

    def show_previous_image(self, step: int = 1):
        """显示上一张图片"""
        max_index = len(self.image_list) - 1

        if self.image_index == 0:
            self.image_index = max_index
        else:
            if self.image_index - step <= 0:
                self.image_index = 0
            else:
                self.image_index -= step

        self.show_preview()

    def show_index(self):
        """显示当前进度"""
        max_index = len(self.image_list)
        if self.image_index >= 0:
            index = self.image_index + 1
        else:
            index = max_index + self.image_index + 1
        self.label_index.setText(f' {index} / {max_index} ')

    def set_filetype_icon(self, image):
        self.label_filetype_icon.setAlignment(Qt.AlignCenter)
        # 设置图片对象
        pixmap = QPixmap(image)
        # 获取QLabel的大小
        label_size = self.label_filetype_icon.size()
        # 根据图片大小和QLabel大小来缩放图片并保持纵横比
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_filetype_icon.setPixmap(scaled_pixmap)

    def set_filesize_text(self):
        """设置大小文本"""
        size_mb = round(function_normal.get_size(self.path) / 1024 / 1024, 2)
        self.label_size_and_count.setText(f'| {size_mb}MB |')
