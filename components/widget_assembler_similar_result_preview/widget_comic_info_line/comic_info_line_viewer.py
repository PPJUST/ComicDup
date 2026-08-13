import lzytools_Qt
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, Qt, QAction
from PySide6.QtWidgets import QApplication, QFrame, QMenu

from components.widget_assembler_similar_result_preview.widget_comic_info_line.res.icon_base64 import ICON_JUMP_TO, \
    ICON_REFRESH, ICON_DELETE
from components.widget_assembler_similar_result_preview.widget_comic_info_line.res.ui_comic_info_line import Ui_Form


class ComicInfoLineViewer(QFrame):
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
        self.ui.label_filepath.setStyleSheet("font-weight: bold")

        # 添加右键菜单
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._context_menu)

        # 添加tips提示
        self.ui.toolButton_open_path.setToolTip("打开文件所在路径")
        self.ui.toolButton_refresh.setToolTip("刷新漫画信息")
        self.ui.toolButton_delete.setToolTip("删除漫画")

    def set_filepath(self, filepath: str):
        """设置漫画路径"""
        self.ui.label_filepath.setText(filepath)

    def set_filetype_icon(self, icon_base64: str):
        """设置漫画的文件类型图标"""
        pixmap = lzytools_Qt.convert_base64_image_to_pixmap(icon_base64)
        self.ui.label_icon.setPixmap(pixmap)

    def set_filesize(self, filesize: str):
        """设置漫画的文件大小"""
        self.ui.label_filesize.setText(filesize)

    def set_page_count(self, page_count: int):
        """设置漫画的页数"""
        self.ui.label_page_count.setText(str(page_count))

    def set_file_time(self, file_time: str):
        """设置文件的创建时间"""
        self.ui.label_file_time.setText(file_time)

    def set_preview(self, preview_path: str):
        """设置漫画的预览图片"""
        self.ui.label_preview.setPixmap(QPixmap(preview_path))

    def set_attribute_circle_name(self, circle_name: list):
        """设置社团名称"""
        self.ui.label_circle_name.setText(' | '.join(circle_name))

    def set_attribute_artist_name(self, artist_name: list):
        """设置作者名称"""
        self.ui.label_artist_name.setText(' | '.join(artist_name))

    def set_attribute_language(self, language: list):
        """设置语言"""
        self.ui.label_language.setText(' | '.join(language))

    def set_attribute_translator(self, translator_name: list):
        """设置译者名称"""
        self.ui.label_translator.setText(' | '.join(translator_name))

    def set_attribute_special_indicators(self, special_indicators: list):
        """设置特别标示"""
        self.ui.label_special_indicators.setText(' | '.join(special_indicators))

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

    def highlight_filesize(self):
        """高亮显示文件大小"""
        self.ui.label_filesize.setStyleSheet("color: green")

    def highlight_pages(self):
        """高亮显示页数"""
        self.ui.label_page_count.setStyleSheet("color: green")
        self.ui.label_ye.setStyleSheet("color: green")

    def highlight_file_time(self):
        """高亮显示文件时间"""
        self.ui.label_file_time.setStyleSheet("color: green")

    def highlight_filename(self):
        """高亮显示文件名"""
        self.ui.label_filepath.setStyleSheet("color: green")

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
    program_ui = ComicInfoLineViewer()
    program_ui.show()
    app_.exec()
