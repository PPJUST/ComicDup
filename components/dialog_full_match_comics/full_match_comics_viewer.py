import lzytools_Qt
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QLabel

from components.dialog_full_match_comics.res.icon_base64 import ICON_RIGHT, ICON_WARNING, ICON_ERROR
from components.dialog_full_match_comics.res.ui_full_match_comics import Ui_Dialog


class FullMatchComicsViewer(QDialog):
    FullMatch = Signal(name='全量匹配')
    OpenMainComicPage = Signal(int, name='打开主漫画页面')
    OpenCompComicPage = Signal(int, name='打开次漫画页面')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.checkBox_show_diff_pages.setChecked(True)

        # 初始化表格控件
        self.ui.tableWidget_details_pages.setColumnCount(3)
        self.ui.tableWidget_details_pages.setHorizontalHeaderLabels(["主编号", "次编号", "比对情况"])
        self.ui.tableWidget_details_pages.resizeColumnsToContents()
        self.ui.tableWidget_details_pages.verticalHeader().setVisible(False)

        # 绑定信号
        self.ui.pushButton_match.clicked.connect(self.FullMatch.emit)
        self.ui.pushButton_quit.clicked.connect(self.close)
        self.ui.checkBox_show_diff_pages.stateChanged.connect(self._hide_right_match_group)

    def show_simple_result(self, result: str):
        """显示简单结果"""
        self.ui.textBrowser_simple_result.setText(result)

    def add_combobox_items(self, items: list[str]):
        """添加下拉框项目"""
        self.ui.comboBox_main_comic.addItems(items)
        self.ui.comboBox_comp_comic.addItems(items)

    def clear_combobox_items(self):
        """清空下拉框项目"""
        self.ui.comboBox_main_comic.clear()
        self.ui.comboBox_comp_comic.clear()

    def get_main_comic_index(self):
        """获取主漫画编号"""
        text = self.ui.comboBox_main_comic.currentText()
        return int(text.split(' - ')[0])

    def get_comp_comic_index(self):
        """获取对比漫画编号"""
        text = self.ui.comboBox_comp_comic.currentText()
        return int(text.split(' - ')[0])

    def add_index_button(self, main_index: int = None, comp_index: int = None):
        """添加页码按钮"""
        row = self.ui.tableWidget_details_pages.rowCount()
        self.ui.tableWidget_details_pages.insertRow(row)
        # 添加主漫画按钮
        if main_index is not None:
            main_button = QPushButton(str(main_index))
            self.ui.tableWidget_details_pages.setCellWidget(row, 0, main_button)
            main_button.clicked.connect(self._open_page_main_comic)
        # 添加次漫画按钮
        if comp_index is not None:
            comp_button = QPushButton(str(comp_index))
            self.ui.tableWidget_details_pages.setCellWidget(row, 1, comp_button)
            comp_button.clicked.connect(self._open_page_comp_comic)
        # 添加比对状态图标
        if main_index is not None and comp_index is not None:
            if main_index == comp_index:
                icon = lzytools_Qt.convert_base64_image_to_pixmap(ICON_RIGHT)
            else:
                icon = lzytools_Qt.convert_base64_image_to_pixmap(ICON_WARNING)
        else:
            icon = lzytools_Qt.convert_base64_image_to_pixmap(ICON_ERROR)
        label_icon = QLabel()
        label_icon.setPixmap(icon)
        label_icon.setAlignment(Qt.AlignCenter)
        self.ui.tableWidget_details_pages.setCellWidget(row, 2, label_icon)

    def clear_index_button(self):
        """清空页码按钮"""
        self.ui.tableWidget_details_pages.clearContents()
        self.ui.tableWidget_details_pages.setRowCount(0)

    def _open_page_main_comic(self):
        """打开主漫画页面"""
        button: QPushButton = self.sender()
        print(button)
        index = button.text()
        self.OpenMainComicPage.emit(int(index))

    def _open_page_comp_comic(self):
        """打开次漫画页面"""
        button: QPushButton = self.sender()
        index = button.text()
        self.OpenCompComicPage.emit(int(index))

    def _hide_right_match_group(self):
        """隐藏一一对应的页码组"""
        table = self.ui.tableWidget_details_pages
        if self.ui.checkBox_show_diff_pages.isChecked():
            for row in range(table.rowCount()):
                cell_main = table.cellWidget(row, 0)
                if cell_main:
                    page_main = cell_main.text()
                else:
                    page_main = None
                cell_comp = table.cellWidget(row, 1)
                if cell_comp:
                    page_comp = cell_comp.text()
                else:
                    page_comp = None
                if page_main == page_comp:
                    table.hideRow(row)
                else:
                    table.showRow(row)
        else:
            for row in range(table.rowCount()):
                table.showRow(row)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = FullMatchComicsViewer()
    program_ui.show()
    app_.exec()
