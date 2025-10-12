import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtGui import QMouseEvent, Qt
from PySide6.QtWidgets import QWidget, QApplication

from common.class_sign import TYPE_SIGN_STATUS
from components.widget_assembler_similar_result_preview.widget_similar_group_info.res.icon_base64 import ICON_ZOOM_IN
from components.widget_assembler_similar_result_preview.widget_similar_group_info.res.ui_similar_group_info import \
    Ui_Form


class SimilarGroupInfoViewer(QWidget):
    """单个相似组信息模块的界面组件"""
    Preview = Signal(name='预览相似组')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 设置图标
        self.ui.toolButton_preview.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_ZOOM_IN))
        self.ui.toolButton_preview.clicked.connect(self.Preview.emit)

    def set_group_index(self, index: int):
        """设置当前组的编号"""
        self.ui.label_index.setText(str(index))

    def set_item_count(self, count: int):
        """设置当前组内部项目的总数"""
        self.ui.label_item_count.setText(str(count))

    def set_item_size(self, size: str):
        """设置当前组内部项目的文件大小统计"""
        self.ui.label_size_count.setText(size)

    def set_group_sign(self, sign: TYPE_SIGN_STATUS):
        """设置当前组的标记"""
        sign_str = sign.text
        self.ui.label_sign.setText(sign_str)

    def add_widget(self, widget: QWidget):
        """添加漫画项控件"""
        layout = self.ui.scrollAreaWidgetContents_similar_group.layout()
        layout.addWidget(widget)

    def remove_widget(self, widget: QWidget):
        """删除漫画项控件"""
        layout = self.ui.scrollAreaWidgetContents_similar_group.layout()
        layout.removeWidget(widget)
        widget.deleteLater()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.Preview.emit()
            event.accept()
        else:
            super().mouseDoubleClickEvent(event)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SimilarGroupInfoViewer()
    program_ui.show()
    app_.exec()
