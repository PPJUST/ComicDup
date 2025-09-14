from PySide6.QtCore import Signal, QSize
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem

from components.widget_similar_result_preview.res.ui_similar_result_preview import Ui_Form


class SimilarResultPreviewViewer(QWidget):
    """相似匹配结果模块的界面组件"""
    PreviousPage = Signal(name='上一页')
    NextPage = Signal(name='下一页')
    ChangeShowGroupCount = Signal(int, name='改变每页显示的组数')

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
        # 设置列表项的高度，以适应自定义widget
        list_item.setSizeHint(QSize(0, 80))
        # 将widget设置到列表项
        self.ui.listWidget_group.addItem(list_item)
        self.ui.listWidget_group.setItemWidget(list_item, similar_group_widget)

    def clear(self):
        """清空内容"""
        self.ui.listWidget_group.clear()

    def get_show_group_count(self) -> int:
        """获取每页显示的组数"""
        return self.ui.comboBox_show_group_count.currentText()

if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SimilarResultPreviewViewer()
    program_ui.show()
    app_.exec()
