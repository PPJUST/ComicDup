# 作为文件名控件的tableWidget，利用文本单元格自动隐藏长文本的特性
from PySide6.QtGui import Qt
from PySide6.QtWidgets import *


class TabelWidgetFilename(QTableWidget):
    """作为文件名控件的tableWidget，利用文本单元格自动隐藏长文本的特性"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.NoFrame)
        # 设置列宽度为自动适应控件大小
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # 隐藏行列
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        # 设置为单行单列
        self.setColumnCount(1)
        self.insertRow(0)
        # 固定控件高度、单元格行高
        self.setFixedHeight(18)
        self.setRowHeight(0, 16)
        # 设置文本单元格
        self.item_filename = QTableWidgetItem('')
        self.setItem(0, 0, self.item_filename)
        # 禁止编辑单元格
        self.item_filename.setFlags(self.item_filename.flags() & ~Qt.ItemIsEditable)

    def set_filename(self, filename: str, tool_tip: str = None):
        """设置文件名"""
        if not tool_tip:
            tool_tip = filename
        else:
            tool_tip = filename + r'\n' + tool_tip
        self.item_filename.setText(filename)
        self.item_filename.setToolTip(tool_tip)
