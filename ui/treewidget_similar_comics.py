# 显示漫画相似组的控件
import os

import send2trash
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import ICON_FOLDER, ICON_ARCHIVE, OVERSIZE_IMAGE
from module import function_cache_comicdata
from module import function_cache_similargroup
from ui.dialog_comics_preview import DialogComicsPreview


class TreeWidgetSimilarComics(QTreeWidget):
    """显示漫画相似组的控件"""

    def __init__(self):
        super().__init__()
        self.setHeaderHidden(True)

    def show_comics(self, filter_type:str = None):
        """显示所有相似漫画
        :param filter_type: str格式，筛选类型（用于显示经过筛选后的结果）"""
        self.clear()

        if filter_type:
            similar_groups = function_cache_similargroup.read_similar_groups_pickle_filter(filter_type)
        else:
            similar_groups = function_cache_similargroup.read_similar_groups_pickle()
        comics_data = function_cache_comicdata.read_comics_data_pickle()

        for index, similar_group in enumerate(similar_groups, start=1):
            # 创建父节点
            top_item = QTreeWidgetItem()
            top_item.setText(0, f'■ 相似组 {index} - {len(similar_group)}项')
            top_item.setBackground(0, QColor(248, 232, 137))
            self.addTopLevelItem(top_item)

            # 创建子节点
            child_item = QTreeWidgetItem()
            top_item.addChild(child_item)

            # 创建自定义控件组
            comics_item = ScrollAreaComicsData(similar_group, comics_data)
            comics_item.signal_empty_group.connect(self.hidden_emtpy_group)

            # 将控件组设置为子节点的单元格部件
            self.setItemWidget(child_item, 0, comics_item)

        # 打开所有父节点
        self.expandAll()

    def hidden_emtpy_group(self):
        """折叠空节点"""
        comics_item = self.sender()  # 获取发送信号的控件
        child_item = self.itemAt(comics_item.pos())  # 获取子节点对象
        top_level_item = child_item.parent()  # 获取父节点对象
        self.collapseItem(top_level_item)  # 折叠父节点


class ScrollAreaComicsData(QScrollArea):
    """显示一组漫画数据的控件，用于treeWidget节点下的item控件
    (ScrollArea->Widget->ComicWidget)"""
    signal_empty_group = Signal()

    def __init__(self, similar_group: set, comics_data: dict):
        super().__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        # 漫画数据用传参的方法，而不用读取本地数据库的方法，避免多次重复读取数据库
        self.similar_group = similar_group  # 相似组集合，内部元素为漫画路径str
        self.set_widgets(comics_data)

    def set_widgets(self, comics_data: dict):
        """添加漫画控件
        :param comics_data: 漫画数据，key为漫画路径str，value为自定义漫画数据class
        """
        # 清空
        item_widget = self.takeWidget()
        if item_widget:
            item_widget.deleteLater()

        # 创建用于存放单本漫画控件的Widget
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(30)

        # 向Widget中添加单本漫画控件
        for comic_path in self.similar_group:
            if os.path.exists(comic_path) and comic_path in comics_data:
                # 提取数据
                comic_class = comics_data[comic_path]
                filesize_mb = round(comic_class.filesize / 1024 / 1024, 2)
                image_count = comic_class.image_count
                preview_file = comic_class.preview_file
                filetype = comic_class.filetype
                # 添加自定义控件
                widget_comic = WidgetSingleComicData()
                widget_comic.signal_del_file.connect(self.delete_comic)
                widget_comic.signal_double_click.connect(self.show_dialog_comics_preview)
                widget_comic.setStyleSheet('{border: 1px solid gray;')
                widget_comic.set_filepath(comic_path)
                widget_comic.set_size_and_count(f'{filesize_mb}MB/{image_count}图')
                widget_comic.set_preview(preview_file)
                if filetype == 'folder':
                    widget_comic.set_filetype_icon(ICON_FOLDER)
                elif filetype == 'archive':
                    widget_comic.set_filetype_icon(ICON_ARCHIVE)
                layout.addWidget(widget_comic)

        widget.setLayout(layout)
        self.setWidget(widget)

    def delete_comic(self, path_delete):
        """删除单本漫画，并刷新ui"""
        self.similar_group.remove(path_delete)
        comics_data = function_cache_comicdata.read_comics_data_pickle()

        self.set_widgets(comics_data)

        if not self.similar_group:
            self.signal_empty_group.emit()

    def show_dialog_comics_preview(self):
        """预览选中的相似组"""
        dialog = DialogComicsPreview()
        dialog.set_show_path_list(self.similar_group)
        dialog.signal_del_file.connect(self.delete_comic)
        dialog.exec()


class WidgetSingleComicData(QWidget):
    """显示单本漫画基本信息的控件，包括预览图、页数、大小等"""
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
        if event.button() == Qt.LeftButton and self.filepath:
            self.signal_double_click.emit(self.filepath)

    def set_label_menu(self):
        """设置label的右键菜单"""
        menu = QMenu()

        action_open_file = QAction('打开文件', menu)
        action_open_file.triggered.connect(self.open_file)
        menu.addAction(action_open_file)

        action_open_parentfolder = QAction('打开所在目录', menu)
        action_open_parentfolder.triggered.connect(self.open_parentfolder)
        menu.addAction(action_open_parentfolder)

        action_del_file = QAction('删除文件', menu)
        action_del_file.triggered.connect(self.del_file)
        menu.addAction(action_del_file)

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
        if pixmap.isNull():  # 处理超过限制的图片对象，替换为裂图图标
            pixmap = QPixmap(OVERSIZE_IMAGE)
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
