import lzytools_Qt
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QDialog

from components.dialog_full_match_comics.res.icon_base64 import ICON_ARROW_UP, ICON_ARROW_DOWN
from components.dialog_full_match_comics.res.ui_full_match_comics import Ui_Dialog


class FullMatchComicsViewer(QDialog):
    FullMatch = Signal(name='全量匹配')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 隐藏下拉内容
        self.ui.checkBox_show_diff_pages.hide()
        self.ui.tableWidget_details_pages.hide()

        # 绑定信号
        self.ui.pushButton_match.clicked.connect(self.FullMatch.emit)
        self.ui.pushButton_quit.clicked.connect(self.close)

    def show_simple_result(self, result: str):
        """显示简单结果"""
        self.ui.label_simple_result.setText(result)

    def add_combobox_items(self, items: list[str]):
        """添加下拉框项目"""
        self.ui.comboBox_comic_main.addItems(items)
        self.ui.comboBox_comic_comp.addItems(items)

    def clear_combobox_items(self):
        """清空下拉框项目"""
        self.ui.comboBox_comic_main.clear()
        self.ui.comboBox_comic_comp.clear()

    def get_comic_index_1(self):
        """获取主漫画编号"""
        text = self.ui.comboBox_comic_main.currentText()
        return int(text.split(' - ')[0])

    def get_comic_index_2(self):
        """获取对比漫画编号"""
        text = self.ui.comboBox_comic_comp.currentText()
        return int(text.split(' - ')[0])

    def set_arrow_button_icon_up(self):
        self.ui.toolButton_show_details.setIcon(lzytools_Qt.convert_base64_image_to_pixmap(ICON_ARROW_UP))

    def set_arrow_button_icon_down(self):
        self.ui.toolButton_show_details.setIcon(lzytools_Qt.convert_base64_image_to_pixmap(ICON_ARROW_DOWN))


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = FullMatchComicsViewer()
    program_ui.show()
    app_.exec()
