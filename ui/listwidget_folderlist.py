# 文件夹列表显示控件，用于收集拖入的文件夹
import os.path

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import ICON_DEL
from module import function_normal


class ListWidgetFolderlist(QListWidget):
    """拖入文件夹列表显示控件，附带一些基本功能"""
    signal_folderlist = Signal(list)

    def __init__(self):
        super().__init__()
        self.dirpath_list = []

        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSpacing(3)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        dirpath_list = []
        if urls:
            for index in range(len(urls)):
                path = urls[index].toLocalFile()  # 获取路径
                if os.path.isdir(path):
                    dirpath = path
                else:
                    dirpath = os.path.split(path)[0]
                dirpath_list.append(dirpath)

        self.add_item(dirpath_list)

    def add_item(self, path_list: list):
        """新增行项目"""
        for path in path_list:
            if path not in self.dirpath_list:
                self.dirpath_list.append(path)

        self.refresh_list()

    def refresh_list(self):
        """刷新列表项目"""
        self.clear()
        for path in self.dirpath_list:
            end_index = self.count()
            item = QListWidgetItem()
            item_widget = WidgetFolderline()
            item_widget.set_dirpath(path)
            item_widget.signal_del.connect(self.del_item)

            self.insertItem(end_index + 1, item)
            self.setItemWidget(item, item_widget)

        self.signal_folderlist.emit(self.dirpath_list)

    def del_item(self):
        """删除行项目"""
        del_item_widget = self.sender()
        # 删除全局变量中的对应数据
        for i in range(self.count()):
            item = self.item(i)
            item_widget = self.itemWidget(item)
            dirpath = item_widget.label_dirpath.toolTip()
            if del_item_widget is item_widget:
                self.dirpath_list.remove(dirpath)
                break

        self.refresh_list()


class WidgetFolderline(QWidget):
    """单行路径控件，用于插入至主控件中"""
    signal_del = Signal()

    def __init__(self):
        super().__init__()
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setStretch(1, 1)

        self.toolButton_del = QToolButton()
        self.toolButton_del.setIcon(QIcon(ICON_DEL))
        self.toolButton_del.setStyleSheet("background-color: white; border: none;")
        self.horizontalLayout.addWidget(self.toolButton_del)

        self.label_dirpath = QLabel()
        self.label_dirpath.setText('显示文件夹路径')
        self.horizontalLayout.addWidget(self.label_dirpath)

        """连接信号与槽函数"""
        self.toolButton_del.clicked.connect(self.click_del_button)

    def set_dirpath(self, path):
        """设置文本"""
        self.label_dirpath.setText(function_normal.reverse_path(path))
        self.label_dirpath.setToolTip(path)

    def click_del_button(self):
        self.signal_del.emit()
