import os.path

import natsort
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from satic_function import icon_del


class DropLineEdit(QLineEdit):
    """自定义QLineEdit控件
    拖入【文件夹】/【文件】到QLineEdit中，将QLineEdit的文本设置为【拖入的文件夹路径】或【拖入的文件所属的文件夹路径】并发送信号"""

    signal_lineEdit_dropped = Signal(set)  # 发送获取的文件夹路径str信号

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)  # 设置可拖入
        self.setReadOnly(True)

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

            self.setText(dirpath_list[0])
            self.signal_lineEdit_dropped.emit(set(dirpath_list))


class WidgetFolderlist(QWidget):
    signal_checkbox_clicked = Signal(bool)
    signal_delbutton_clicked = Signal()
    signal_pathline_dropped = Signal(set)

    def __init__(self):
        super().__init__()
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setStretch(2, 1)

        self.checkBox_checked = QCheckBox()
        self.checkBox_checked.setTristate(False)
        self.horizontalLayout.addWidget(self.checkBox_checked)

        self.toolButton_del = QToolButton()
        self.toolButton_del.setIcon(QIcon(icon_del))
        self.horizontalLayout.addWidget(self.toolButton_del)

        self.lineEdit_dirpath = DropLineEdit()
        self.lineEdit_dirpath.setPlaceholderText('拖入文件夹到此处')
        self.horizontalLayout.addWidget(self.lineEdit_dirpath)

        """连接信号与槽函数"""
        self.checkBox_checked.stateChanged.connect(self.click_checkbox)
        self.toolButton_del.clicked.connect(self.click_del_button)
        self.lineEdit_dirpath.signal_lineEdit_dropped.connect(self.accept_signal_dropped)

    def set_checked(self, mode):
        self.checkBox_checked.setChecked(mode)

    def set_linetext(self, text):
        self.lineEdit_dirpath.setText(text)

    def accept_signal_dropped(self, dirpath_set):
        """接收文本框拖入信号"""
        self.set_checked(True)
        self.signal_pathline_dropped.emit(dirpath_set)

    def click_checkbox(self):
        self.signal_checkbox_clicked.emit(self.checkBox_checked.isChecked())

    def click_del_button(self):
        self.signal_delbutton_clicked.emit()


class ListWidgetFolderlist(QListWidget):
    signal_folder_dict = Signal(dict)

    def __init__(self):
        super().__init__()
        self.insert_item()  # 初始插入空白行
        self.dirpath_dict = dict()

    def insert_item(self, item_data: dict = None):
        """在末尾插入行项目"""
        end_index = self.count()
        item = QListWidgetItem()
        item_widget = WidgetFolderlist()
        # 连接信号
        item_widget.signal_pathline_dropped.connect(self.accept_item_dropped)
        item_widget.signal_checkbox_clicked.connect(self.accept_item_checked)
        item_widget.signal_delbutton_clicked.connect(self.del_item)
        if item_data:
            item_widget.set_checked(item_data['mode'])
            item_widget.set_linetext(item_data['path'])
        self.insertItem(end_index + 1, item)
        self.setItemWidget(item, item_widget)

    def refresh_item_widget(self):
        """刷新行项目（去重）和变量"""
        # 清空布局
        self.clear()
        # 重新插入行项目
        key_list = [key for key in self.dirpath_dict.keys()]
        for key in natsort.natsorted(key_list):
            value = self.dirpath_dict[key]
            if key != '':
                self.insert_item({'path': key, 'mode': value})
        # 结尾插入空行
        self.insert_item()
        # 发送变量信号
        self.signal_folder_dict.emit(self.dirpath_dict)

    def del_item(self):
        """删除行项目"""
        del_item_widget = self.sender()
        for i in range(self.count()):
            item = self.item(i)
            item_widget = self.itemWidget(item)
            dirpath = item_widget.lineEdit_dirpath.text()
            if del_item_widget is item_widget:
                self.dirpath_dict.pop(dirpath)
                break
        # 刷新控件
        self.refresh_item_widget()

    def accept_item_checked(self):
        """接收子控件的信号"""
        item_widget = self.sender()
        dirpath = item_widget.lineEdit_dirpath.text()
        checked = item_widget.checkBox_checked.isChecked()
        self.dirpath_dict[dirpath] = checked
        self.signal_folder_dict.emit(self.dirpath_dict)

    def accept_item_dropped(self, dirpath_set):
        """接收子控件的信号"""
        # 添加数据行
        for path in dirpath_set:
            self.dirpath_dict[path] = True
        # 更新变量
        self.refresh_item_widget()


def main():
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = ListWidgetFolderlist()
    show_ui.show()
    app.exec()


if __name__ == '__main__':
    main()
