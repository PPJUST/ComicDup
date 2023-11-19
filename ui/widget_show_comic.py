import os

import send2trash
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class WidgetShowComic(QWidget):
    signal_del_file = Signal(str)  # 删除文件的路径信号
    signal_double_click = Signal(str)  # 左键双击预览图信号，附带路径str

    def __init__(self):
        super().__init__()
        """设置布局"""
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # 控件组 勾选框和文件名
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)

        self.checkBox = QCheckBox()
        self.horizontalLayout.addWidget(self.checkBox)

        self.label_filename = QLabel()
        self.label_filename.setText('文件名')
        self.label_filename.setWordWrap(True)
        self.horizontalLayout.addWidget(self.label_filename)

        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 控件组 文件夹
        self.label_dirpath = QLabel()
        self.label_dirpath.setText('文件路径')
        self.label_dirpath.setWordWrap(True)
        self.verticalLayout.addWidget(self.label_dirpath)

        # 控件组 图标和文件数
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)

        self.label_filetype_icon = QLabel()
        self.label_filetype_icon.setText('图标')
        self.label_filetype_icon.setFixedSize(15, 15)
        self.horizontalLayout_2.addWidget(self.label_filetype_icon)

        self.label_size_and_count = QLabel()
        self.label_size_and_count.setText('大小/文件数')
        self.horizontalLayout_2.addWidget(self.label_size_and_count)

        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # 控件组 预览图
        self.label_preview = QLabel()
        self.label_size_and_count.setText('显示图像')
        self.label_preview.setFrameShape(QFrame.Box)
        self.label_preview.setFixedSize(125, 175)
        self.label_preview.mouseDoubleClickEvent = self.label_double_clicked
        self.verticalLayout.addWidget(self.label_preview)

        self.verticalLayout.setStretch(3, 1)

        """初始化"""
        self.filepath = None
        self.set_label_menu()

    def label_double_clicked(self, event):
        if event.button() == Qt.LeftButton:
            if self.filepath:
                self.signal_double_click.emit(self.filepath)

    def set_label_menu(self):
        """设置label的右键菜单"""
        menu = QMenu()

        aciton_open_file = QAction('打开文件', menu)
        aciton_open_file.triggered.connect(self.open_file)
        menu.addAction(aciton_open_file)

        aciton_open_parentfolder = QAction('打开所在目录', menu)
        aciton_open_parentfolder.triggered.connect(self.open_parentfolder)
        menu.addAction(aciton_open_parentfolder)

        aciton_del_file = QAction('删除文件', menu)
        aciton_del_file.triggered.connect(self.del_file)
        menu.addAction(aciton_del_file)

        self.setContextMenuPolicy(Qt.CustomContextMenu)  # 设置右键菜单策略
        self.customContextMenuRequested.connect(lambda pos: menu.exec(self.mapToGlobal(pos)))  # 显示菜单

    def set_filepath(self, filepath):
        self.filepath = filepath

        dirpath, filename = os.path.split(filepath)
        self.label_dirpath.setText(dirpath)
        self.label_filename.setText(filename)

    def set_size_and_count(self, text):
        self.label_size_and_count.setText(text)

    def set_preview(self, image):
        self.label_preview.setAlignment(Qt.AlignCenter)
        # 设置图片对象
        pixmap = QPixmap(image)
        # 获取QLabel的大小
        label_size = self.label_preview.size()
        # 根据图片大小和QLabel大小来缩放图片并保持纵横比
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_preview.setPixmap(scaled_pixmap)

    def set_filetype_icon(self, image):
        self.label_filetype_icon.setAlignment(Qt.AlignCenter)
        # 设置图片对象
        pixmap = QPixmap(image)
        # 获取QLabel的大小
        label_size = self.label_filetype_icon.size()
        # 根据图片大小和QLabel大小来缩放图片并保持纵横比
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_filetype_icon.setPixmap(scaled_pixmap)

    def open_file(self):
        os.startfile(self.filepath)

    def open_parentfolder(self):
        os.startfile(os.path.split(self.filepath)[0])

    def del_file(self):
        send2trash.send2trash(self.filepath)
        self.signal_del_file.emit(self.filepath)


def main():
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetShowComic()
    show_ui.show()
    app.exec()


if __name__ == '__main__':
    main()
