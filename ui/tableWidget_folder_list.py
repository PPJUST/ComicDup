# 文件夹列表显示控件

import os
from typing import Union

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import _ICON_DELETE
from module import function_config_folder_list

_TITLE_BUTTON = ''
_TITLE_DIRNAME = '文件夹名称'
_TITLE_PATH = '文件夹路径'
_TITLE_LINE = [_TITLE_BUTTON, _TITLE_DIRNAME, _TITLE_PATH]

_BUTTON_STYLE = 'background-color: white; border: none;'
_ROW_HEIGHT = 20  # 行项目高度


class TableWidgetFolderList(QTableWidget):
    """文件夹列表显示控件"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragDropMode(self.DragDropMode.InternalMove)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)  # 选择模式为整行
        self.verticalHeader().setVisible(False)  # 不显示行号
        self.setVerticalScrollMode(QTableWidget.ScrollPerPixel)  # 平滑滚动
        self.setHorizontalScrollMode(QTableWidget.ScrollPerPixel)  # 平滑滚动
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # 手动调整列宽
        self.setMinimumHeight(200)

        # 设置标题行
        self.setColumnCount(len(_TITLE_LINE))
        self.setHorizontalHeaderLabels(_TITLE_LINE)
        self.setColumnWidth(_TITLE_LINE.index(_TITLE_BUTTON), _ROW_HEIGHT)
        self.setColumnWidth(_TITLE_LINE.index(_TITLE_PATH), 150)

        # 加载配置
        folder_list = function_config_folder_list.folder_list.get()
        if folder_list:
            self.insert_item(folder_list)

    def get_paths_showed(self):
        """获取当前显示的所有行项目的路径"""
        paths_showed = []
        for row in range(self.rowCount()):
            path = self.item(row, _TITLE_LINE.index(_TITLE_PATH)).text()
            paths_showed.append(path)

        return paths_showed

    def insert_item(self, paths: Union[list, str]):
        """插入行项目"""
        if isinstance(paths, str):
            paths = [paths]

        for path in paths:
            if os.path.isdir(path):
                path_insert = path
            else:
                path_insert = os.path.dirname(path)

            path_insert = os.path.normpath(path_insert)
            if path_insert not in self.get_paths_showed():
                # 插入行项目
                row_position = self.rowCount()
                self.insertRow(row_position)
                # 设置删除按钮
                button_del = QToolButton()
                button_del.clicked.connect(self.remove_item_by_button)
                button_del.setIcon(QIcon(_ICON_DELETE))
                button_del.setStyleSheet(_BUTTON_STYLE)
                self.setCellWidget(row_position, _TITLE_LINE.index(_TITLE_BUTTON), button_del)
                # 插入文件夹名称
                _title = os.path.basename(path_insert)
                item_title = QTableWidgetItem(_title)
                item_title.setToolTip(_title)
                self.setItem(row_position, _TITLE_LINE.index(_TITLE_DIRNAME), item_title)
                self.item(row_position, _TITLE_LINE.index(_TITLE_DIRNAME)).setToolTip(_title)
                self.setRowHeight(row_position, _ROW_HEIGHT)
                # 插入文件夹路径
                item_path = QTableWidgetItem(path_insert)
                item_path.setToolTip(path_insert)
                self.setItem(row_position, _TITLE_LINE.index(_TITLE_PATH), item_path)
                self.item(row_position, _TITLE_LINE.index(_TITLE_PATH)).setToolTip(path_insert)
                # 设置禁止编辑单元格
                for column in range(self.columnCount()):
                    item = self.item(row_position, column)
                    try:
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 禁用单元格编辑
                    except AttributeError:
                        pass

        # 保存至配置文件
        function_config_folder_list.folder_list.update(self.get_paths_showed())

    def remove_item(self):
        """删除行项目"""
        for item in self.selectedItems():
            try:
                row = item.row()
                self.removeRow(row)
            except RuntimeError:
                # 由于默认选中整行，selectedItems()会返回该行的所有单元格，从而导致在删除该行的其他单元格时重复删除整行而报错
                pass

        # 保存至配置文件
        function_config_folder_list.folder_list.update(self.get_paths_showed())

    def remove_item_by_button(self):
        """删除行项目（点击行项目中的删除按钮）"""
        button = self.sender()
        for row in range(self.rowCount()):
            if self.cellWidget(row, _TITLE_LINE.index('')) == button:
                self.removeRow(row)
                break

        # 保存至配置文件
        function_config_folder_list.folder_list.update(self.get_paths_showed())

    def clear_items(self):
        """清空所有行项目"""
        while self.rowCount():
            self.removeRow(0)

        # 保存至配置文件
        function_config_folder_list.folder_list.update(self.get_paths_showed())

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        paths = []
        if urls:
            for index in range(len(urls)):
                path = urls[index].toLocalFile()  # 获取路径
                path = os.path.normpath(path)
                if os.path.exists(path):
                    paths.append(path)
                else:
                    continue

        self.insert_item(paths)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = TableWidgetFolderList()
    show_ui.show()
    app.exec()
