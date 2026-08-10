import lzytools_Qt
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, Qt, QAction
from PySide6.QtWidgets import QApplication, QFrame, QMenu

from components.widget_assembler_similar_result_preview.widget_comic_info.res.icon_base64 import ICON_JUMP_TO, \
    ICON_REFRESH, ICON_DELETE
from components.widget_assembler_similar_result_preview.widget_comic_info.res.ui_comic_info import Ui_Form


class ComicInfoViewer(QFrame):
    """单个漫画信息模块的界面组件"""
    OpenPath = Signal(name='打开文件')
    OpenDir = Signal(name='打开文件所在路径')
    RefreshInfo = Signal(name='刷新漫画信息')
    Delete = Signal(name='删除漫画')
    Rename = Signal(name='重命名漫画')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 绑定信号
        self.ui.toolButton_open_path.clicked.connect(self.OpenPath)
        self.ui.toolButton_refresh.clicked.connect(self.RefreshInfo)
        self.ui.toolButton_delete.clicked.connect(self.Delete)

        # 设置图标
        self._set_icon()

        # 设置ui
        self.ui.label_preview.setFixedSize(250, 128)
        self.ui.label_preview.setAlignment(Qt.AlignCenter)
        self.setMinimumWidth(250)
        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Plain)
        self.setLineWidth(1)
        self.ui.label_filetitle.setStyleSheet("font-weight: bold")

        # 添加右键菜单
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._context_menu)

        # 添加tips提示
        self.ui.toolButton_open_path.setToolTip("打开文件所在路径")
        self.ui.toolButton_refresh.setToolTip("刷新漫画信息")
        self.ui.toolButton_delete.setToolTip("删除漫画")

    def set_filetype_icon(self, icon_base64: str):
        """设置漫画的文件类型图标"""
        pixmap = lzytools_Qt.convert_base64_image_to_pixmap(icon_base64)
        self.ui.label_icon.setPixmap(pixmap)

    def set_filetitle(self, filetitle: str):
        """设置漫画标题"""
        self.ui.label_filetitle.setText(filetitle)

    def set_parent_dirpath(self, parent_dirpath: str):
        """设置漫画的父级路径"""
        self.ui.label_parent_dirpath.setText(parent_dirpath)

    def set_page_count(self, page_count: int):
        """设置漫画的页数"""
        self.ui.label_page_count.setText(str(page_count))

    def set_filesize(self, filesize: str):
        """设置漫画的文件大小"""
        self.ui.label_filesize.setText(filesize)

    def set_preview(self, preview_path: str):
        """设置漫画的预览图片"""
        self.ui.label_preview.setPixmap(QPixmap(preview_path))

    def set_similarity(self, similarity: str):
        """设置相似度（百分比）
        :param similarity:百分比数字文本，例如90%"""
        self.ui.label_similarity.setText(str(similarity))
        # 相似度>90%，绿色文本，相似度>80%，蓝色文本，否则为黑色文本
        if float(similarity.replace('%', '')) >= 90:
            self.ui.label_similarity.setStyleSheet("color: green")
        elif float(similarity.replace('%', '')) >= 80:
            self.ui.label_similarity.setStyleSheet("color: blue")
        else:
            self.ui.label_similarity.setStyleSheet("color: black")

    def set_color(self, color: str):
        """为漫画项的文本添加颜色"""
        self.ui.label_filetitle.setStyleSheet(f"color: {color}")
        self.ui.label_page_count.setStyleSheet(f"color: {color}")
        self.ui.label_ye.setStyleSheet(f"color: {color}")
        self.ui.label_filesize.setStyleSheet(f"color: {color}")

    def highlight_filesize(self):
        """高亮显示文件大小"""
        self.ui.label_filesize.setStyleSheet("color: green")

    def highlight_pages(self):
        """高亮显示页数"""
        self.ui.label_page_count.setStyleSheet("color: green")
        self.ui.label_ye.setStyleSheet("color: green")

    def highlight_file_time(self):
        """高亮显示文件时间"""
        pass

    def highlight_filename(self):
        """高亮显示文件名"""
        self.ui.label_filetitle.setStyleSheet("color: green")

    def _context_menu(self, pos):
        """添加右键菜单"""
        menu = QMenu()
        menu.adjustSize()

        action_open_file = QAction('打开文件', menu)
        action_open_file.triggered.connect(self.OpenPath.emit)
        menu.addAction(action_open_file)

        action_open_dir = QAction('打开目录', menu)
        action_open_dir.triggered.connect(self.OpenDir.emit)
        menu.addAction(action_open_dir)

        action_refresh = QAction('刷新信息', menu)
        action_refresh.triggered.connect(self.RefreshInfo.emit)
        menu.addAction(action_refresh)

        action_rename = QAction('重命名', menu)
        action_rename.triggered.connect(self.Rename.emit)
        menu.addAction(action_rename)

        action_delete = QAction('删除', menu)
        action_delete.triggered.connect(self.Delete.emit)
        menu.addAction(action_delete)

        menu.exec(self.mapToGlobal(pos))

    def _set_icon(self):
        """设置图标"""
        self.ui.toolButton_open_path.setIcon(lzytools_Qt.convert_base64_image_to_pixmap(ICON_JUMP_TO))
        self.ui.toolButton_refresh.setIcon(lzytools_Qt.convert_base64_image_to_pixmap(ICON_REFRESH))
        self.ui.toolButton_delete.setIcon(lzytools_Qt.convert_base64_image_to_pixmap(ICON_DELETE))


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = ComicInfoViewer()
    program_ui.show()
    app_.exec()
