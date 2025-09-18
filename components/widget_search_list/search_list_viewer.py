import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog

from components.widget_search_list.res.icon_base64 import ICON_CLEAR, ICON_ADD
from components.widget_search_list.res.table_widget_filelist import TableWidgetFilelist
from components.widget_search_list.res.ui_search_list import Ui_Form


class SearchListViewer(QWidget):
    """搜索列表模块的界面组件"""
    DropFiles = Signal(object, name="拖入文件")

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setAcceptDrops(True)

        # 添加自定义控件
        self.table_widget_filelist = TableWidgetFilelist(self)
        self.ui.layout_filelist.addWidget(self.table_widget_filelist)

        # 绑定信号
        self.ui.pushButton_add_files.clicked.connect(self._choose_files)
        self.ui.pushButton_add_folders.clicked.connect(self._choose_folder)
        self.ui.pushButton_delete_useless_path.clicked.connect(self.remove_useless_row)
        self.ui.pushButton_clear.clicked.connect(self.clear)

        # 添加图标
        self.ui.pushButton_add_files.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_ADD))
        self.ui.pushButton_add_folders.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_ADD))
        self.ui.pushButton_delete_useless_path.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_CLEAR))
        self.ui.pushButton_clear.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_CLEAR))

    def add_row(self, filepath: str):
        """添加新的文件行"""
        self.table_widget_filelist.add_row(filepath)

    def remove_useless_row(self):
        """删除无效行"""
        self.table_widget_filelist.remove_useless_row()

    def get_paths(self) -> list:
        """获取所有文件路径"""
        return self.table_widget_filelist.get_paths()

    def clear(self):
        """清空列表"""
        self.table_widget_filelist.clear()

    def _choose_files(self):
        """弹出文件选择框"""
        paths = QFileDialog.getOpenFileNames(self, "选择文件", "", "All Files (*)")[0]
        self.DropFiles.emit(paths)

    def _choose_folder(self):
        """弹出文件夹选择框"""
        paths = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
        self.DropFiles.emit(paths)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            paths = [url.toLocalFile() for url in urls]
            self.DropFiles.emit(paths)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SearchListViewer()
    program_ui.show()
    app_.exec()
