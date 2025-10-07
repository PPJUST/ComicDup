import os

import lzytools._qt_pyside6
import lzytools.archive
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton, QHeaderView

from common.class_config import FileType
from components.widget_search_list.res.icon_base64 import ICON_ARCHIVE, ICON_FOLDER, ICON_WARNING


class TableWidgetFilelist(QTableWidget):
    """用于显示文件列表的表格控件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # 设置表格列数
        self.setColumnCount(4)
        # 设置列标题
        self.setHorizontalHeaderLabels(['', '类型', '文件名', '文件路径'])
        # 隐藏行号
        self.verticalHeader().setVisible(False)
        # 设置列宽
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)

    def get_paths(self):
        """获取所有文件路径"""
        paths = []
        for row in range(self.rowCount()):
            paths.append(self.item(row, 3).text())
        return paths

    def add_row(self, filepath):
        """添加一行数据"""
        # 插入到最后一行
        row = self.rowCount()
        self.insertRow(row)

        # 第一列：删除按钮
        button_delete = QPushButton("X")
        button_delete.setStyleSheet("""
            background-color: transparent;
            border: none; 
            color: red; 
            """)
        # 绑定删除按钮事件
        button_delete.clicked.connect(lambda checked, r=row: self.remove_row(r))
        # 添加到表格
        self.setCellWidget(row, 0, button_delete)

        # 第二列：文件类型图标
        item_icon = QTableWidgetItem()
        filetype = self.check_filetype(filepath)
        if isinstance(filetype, FileType.Archive):
            icon = lzytools._qt_pyside6.base64_to_pixmap(ICON_ARCHIVE)
        elif isinstance(filetype, FileType.Folder):
            icon = lzytools._qt_pyside6.base64_to_pixmap(ICON_FOLDER)
        else:
            icon = lzytools._qt_pyside6.base64_to_pixmap(ICON_WARNING)
        item_icon.setIcon(icon)
        item_icon.setFlags(item_icon.flags() & ~Qt.ItemIsEditable)  # 设置不可编辑
        self.setItem(row, 1, item_icon)

        # 第三列：文件标题
        item_filetitle = QTableWidgetItem()
        item_filetitle.setText(os.path.basename(filepath))
        item_filetitle.setFlags(item_filetitle.flags() & ~Qt.ItemIsEditable)  # 设置不可编辑
        item_filetitle.setToolTip(filepath)
        self.setItem(row, 2, item_filetitle)

        # 第四列：文件路径
        item_filepath = QTableWidgetItem()
        item_filepath.setText(filepath)
        item_filepath.setFlags(item_filepath.flags() & ~Qt.ItemIsEditable)  # 设置不可编辑
        item_filepath.setToolTip(filepath)
        self.setItem(row, 3, item_filepath)

    def remove_row(self, row):
        """删除指定行"""
        if 0 <= row < self.rowCount():
            self.removeRow(row)
            # 重新绑定所有删除按钮，因为删除一行后其他行的索引会变化
            self._rebind_delete_buttons()

    def remove_useless_row(self):
        """删除无效行"""
        for row in range(self.rowCount() - 1, -1, -1):  # 从最后一行检查到第一行，防止删除前一行后导致索引改变而row不变
            filepath = self.item(row, 3).text()
            if not os.path.exists(filepath):
                self.remove_row(row)

    def clear(self):
        """清空所有行"""
        self.setRowCount(0)

    def _rebind_delete_buttons(self):
        """重新绑定所有删除按钮"""
        for row in range(self.rowCount()):
            button_delete: QPushButton = self.cellWidget(row, 0)
            if button_delete:
                # 重新绑定事件
                button_delete.clicked.disconnect()
                button_delete.clicked.connect(lambda checked, r=row: self.remove_row(r))

    def check_filetype(self, filepath):
        """检查文件类型，仅识别文件夹/压缩文件"""
        if not os.path.exists(filepath):
            return FileType.Error()
        else:
            if os.path.isdir(filepath):
                return FileType.Folder()
            elif lzytools.archive.is_archive(filepath) or lzytools.archive.is_archive_by_filename(
                    os.path.basename(filepath)):
                return FileType.Archive()
            else:
                return FileType.Unknown()
