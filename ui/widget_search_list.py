# 搜索列表

from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import _ICON_ADD, _ICON_CLEAR, _ICON_REMOVE
from ui.src.ui_widget_search_list import Ui_Form
from ui.tableWidget_folder_list import TableWidgetFolderList


class WidgetSearchList(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化
        self._set_icon()

        # 添加自定义控件
        self.tableWidget_folder_list = TableWidgetFolderList()
        self.ui.verticalLayout_folder_list.addWidget(self.tableWidget_folder_list)

        # 绑定槽函数
        self.ui.toolButton_add.clicked.connect(self.add_item)
        self.ui.toolButton_del.clicked.connect(self.remove_item)
        self.ui.toolButton_clear.clicked.connect(self.clear_items)

    def get_paths_showed(self):
        paths_showed = self.tableWidget_folder_list.get_paths_showed()
        return paths_showed

    def set_enable(self, is_enable: bool):
        """是否启用"""
        self.setEnabled(is_enable)

    def _set_icon(self):
        """设置图标"""
        self.ui.toolButton_add.setIcon(QIcon(_ICON_ADD))
        self.ui.toolButton_del.setIcon(QIcon(_ICON_REMOVE))
        self.ui.toolButton_clear.setIcon(QIcon(_ICON_CLEAR))

    def add_item(self):
        """插入行项目"""
        options = QFileDialog.Options()
        folder_paths = QFileDialog.getExistingDirectory(self, "选择文件夹", "", options=options)

        if folder_paths:
            self.tableWidget_folder_list.insert_item(folder_paths)

    def remove_item(self):
        """删除行项目"""
        self.tableWidget_folder_list.remove_item()

    def clear_items(self):
        """清空行项目"""
        self.tableWidget_folder_list.clear_items()


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = WidgetSearchList()
    show_ui.show()
    app.exec()
