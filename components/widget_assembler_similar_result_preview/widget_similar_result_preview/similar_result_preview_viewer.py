from PySide6.QtCore import Signal, QSize
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem

from components.widget_assembler_similar_result_preview.widget_similar_result_preview.res.ui_similar_result_preview import \
    Ui_Form


class SimilarResultPreviewViewer(QWidget):
    """相似匹配结果模块的界面组件"""
    PreviousPage = Signal(name='上一页')
    NextPage = Signal(name='下一页')
    ChangeShowGroupCount = Signal(str, name='改变每页显示的组数')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 绑定信号
        self.ui.pushButton_previous_page.clicked.connect(self.PreviousPage.emit)
        self.ui.pushButton_next_page.clicked.connect(self.NextPage.emit)
        self.ui.comboBox_show_group_count.currentTextChanged.connect(self.ChangeShowGroupCount.emit)

    def add_similar_group(self, similar_group_widget: QWidget):
        """添加相似匹配结果组"""
        # 创建列表项
        list_item = QListWidgetItem()
        # 将widget设置到列表项
        self.ui.listWidget_group.addItem(list_item)
        self.ui.listWidget_group.setItemWidget(list_item, similar_group_widget)
        # 设置列表项的高度，以适应自定义widget
        size_hint = similar_group_widget.sizeHint()
        size_hint.setHeight(size_hint.height() + 45)
        list_item.setSizeHint(size_hint)

    def clear(self):
        """清空内容"""
        self.ui.listWidget_group.clear()

    def get_show_group_count(self) -> int:
        """获取每页显示的组数"""
        return self.ui.comboBox_show_group_count.currentText()

    def set_current_page(self, current_page: int):
        """设置当前页数"""
        self.ui.label_current_page.setText(str(current_page))
        self._auto_set_previous_next_button_enabled()

    def set_total_page(self, total_page: int):
        """设置总页数"""
        self.ui.label_total_page.setText(str(total_page))
        self._auto_set_previous_next_button_enabled()

    def set_group_count(self, group_count: int):
        """设置组数统计"""
        self.ui.label_group_count.setText(str(group_count))

    def set_item_count(self, comic_count: int):
        """设置项目数统计"""
        self.ui.label_comic_count.setText(str(comic_count))

    def set_filesize_count(self, filesize_count: str):
        """设置文件大小统计"""
        self.ui.label_size_count.setText(str(filesize_count))

    def _auto_set_previous_next_button_enabled(self):
        """自动设置上一页下一页按钮是否可用"""
        current_page = int(self.ui.label_current_page.text())
        total_page = int(self.ui.label_total_page.text())
        if total_page == 1:
            self.ui.pushButton_previous_page.setEnabled(False)
            self.ui.pushButton_next_page.setEnabled(False)
        else:
            if current_page == 1:
                self.ui.pushButton_previous_page.setEnabled(False)
                self.ui.pushButton_next_page.setEnabled(True)
            elif current_page == total_page:
                self.ui.pushButton_previous_page.setEnabled(True)
                self.ui.pushButton_next_page.setEnabled(False)
            else:
                self.ui.pushButton_previous_page.setEnabled(True)
                self.ui.pushButton_next_page.setEnabled(True)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SimilarResultPreviewViewer()
    program_ui.show()
    app_.exec()
