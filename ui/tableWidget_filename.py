# 作为文件名控件的tableWidget，支持文本自动换行显示
from PySide6.QtGui import Qt
from PySide6.QtWidgets import *


class TabelWidgetFilename(QTableWidget):
    """作为文件名控件的tableWidget，支持文本自动换行显示"""

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
        # 设置控件高度自适应内容
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # 设置文本单元格
        self.item_filename = QTableWidgetItem('')
        self.item_filename.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setItem(0, 0, self.item_filename)
        # 启用自动换行
        self.setWordWrap(True)
        # 禁止编辑单元格
        self.item_filename.setFlags(self.item_filename.flags() & ~Qt.ItemIsEditable)

    def set_filename(self, filename: str, tool_tip: str = None):
        """设置文件名"""
        if not tool_tip:
            tool_tip = filename
        else:
            tool_tip = f'{filename}\n\n{tool_tip}'
        self.item_filename.setText(filename)
        self.item_filename.setToolTip(tool_tip)
