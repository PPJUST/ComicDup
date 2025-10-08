import lzytools._qt_pyside6
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.widget_assembler_comics_preview.widget_similar_group_preview.res.icon_base64 import ICON_LEFT_ARROW_1, \
    ICON_LEFT_ARROW_3, ICON_RIGHT_ARROW_1, ICON_RIGHT_ARROW_3, ICON_QUIT, ICON_REFRESH
from components.widget_assembler_comics_preview.widget_similar_group_preview.res.ui_similar_group_preview import Ui_Form


class SimilarGroupPreviewViewer(QWidget):
    """相似组预览框架模块的界面组件"""
    PreviousPage = Signal(name='上一页')
    PreviousPage2 = Signal(name='上一页2')
    NextPage = Signal(name='下一页')
    NextPage2 = Signal(name='下一页2')
    Reset = Signal(name='重置页码')
    Quit = Signal(name='退出')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 设置图标
        self._set_icon()

        # 绑定信号
        self._bind_signal()

    def add_widget(self, widget: QWidget):
        """显示一个控件"""
        self.ui.horizontalLayout_group.addWidget(widget)

    def remove_widget(self, widget: QWidget):
        """删除漫画项控件"""
        layout = self.ui.horizontalLayout_group.layout()
        layout.removeWidget(widget)
        widget.deleteLater()

    def clear(self):
        """清空界面"""
        layout = self.ui.horizontalLayout_group

        for i in reversed(range(layout.count())):
            # 获取布局项目
            item = layout.itemAt(i)

            # 从项目中获取控件
            widget = item.widget()

            if widget:  # 确保它是一个控件，而不是另一个布局

                # 从布局中移除控件
                layout.removeWidget(widget)

                # 从内存中删除
                widget.deleteLater()

    def _set_icon(self):
        """设置图标"""
        self.ui.toolButton_previous2.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_LEFT_ARROW_3))
        self.ui.toolButton_previous.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_LEFT_ARROW_1))
        self.ui.toolButton_next.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_RIGHT_ARROW_1))
        self.ui.toolButton_next2.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_RIGHT_ARROW_3))
        self.ui.toolButton_reset.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_REFRESH))
        self.ui.pushButton_quit.setIcon(lzytools._qt_pyside6.base64_to_pixmap(ICON_QUIT))

    def _bind_signal(self):
        """绑定信号"""
        self.ui.toolButton_previous.clicked.connect(self.PreviousPage.emit)
        self.ui.toolButton_previous2.clicked.connect(self.PreviousPage2.emit)
        self.ui.toolButton_next.clicked.connect(self.NextPage.emit)
        self.ui.toolButton_next2.clicked.connect(self.NextPage2.emit)
        self.ui.toolButton_reset.clicked.connect(self.Reset.emit)
        self.ui.pushButton_quit.clicked.connect(self.Quit.emit)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SimilarGroupPreviewViewer()
    program_ui.show()
    app_.exec()
