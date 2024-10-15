# 用于同时预览多本漫画的外部框架
import os.path

from PySide6.QtCore import QTimer, Signal
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from class_.class_comic_info import ComicInfo
from constant import _ICON_LAST, _ICON_LAST_LAST, _ICON_NEXT, _ICON_NEXT_NEXT, _ICON_QUIT, \
    _ICON_REFRESH
from module import function_config_size, function_normal
from ui.group_preview.widget_comic_view import WidgetComicView
from ui.src.ui_dialog_preview import Ui_Dialog


class DialogPreview(QDialog):
    """用于同时预览多本漫画的外部框架"""
    signal_deleted = Signal(str, name='预览控件中删除的漫画路径')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 初始化
        self._set_icon()
        width = function_config_size.preview_dialog_width.get()
        height = function_config_size.preview_dialog_height.get()
        self.resize(width, height)

        # 延迟响应控件大小事件的定时器
        self.timer_resize = QTimer(self)
        self.timer_resize.setInterval(500)  # 延迟0.5秒
        self.timer_resize.setSingleShot(True)  # 设置为单次定时器
        self.timer_resize.timeout.connect(self._update_preview_size)

        # 绑定槽函数
        self.ui.toolButton_last_5.clicked.connect(lambda: self._page_turning(-5))
        self.ui.toolButton_last.clicked.connect(lambda: self._page_turning(-1))
        self.ui.toolButton_next.clicked.connect(lambda: self._page_turning(1))
        self.ui.toolButton_next_5.clicked.connect(lambda: self._page_turning(5))
        self.ui.toolButton_refresh.clicked.connect(self._reset_page_index)
        self.ui.pushButton_quit.clicked.connect(self.accept)

    def add_item(self, comic_info: ComicInfo):
        """添加项目"""
        function_normal.print_function_info()
        if os.path.exists(comic_info.path):  # 不存在的漫画不进行预览
            widget_comic_view = WidgetComicView(comic_info, self)
            widget_comic_view.signal_deleted.connect(self._comic_deleted)
            self.ui.horizontalLayout_place.addWidget(widget_comic_view)

    def _page_turning(self, step: int):
        """翻页
        :param step: int，翻页页数，±号代表翻页方向"""
        layout = self.ui.horizontalLayout_place
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicView = item.widget()
            widget_comic_view.page_turning(step)

    def _reset_page_index(self):
        """重置页码"""
        layout = self.ui.horizontalLayout_place
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicView = item.widget()
            widget_comic_view.reset_page_index()

    def _comic_deleted(self, deleted_path: str):
        """删除漫画后，更新ui"""
        function_normal.print_function_info()
        widget_ = self.sender()
        widget_.deleteLater()
        self.signal_deleted.emit(deleted_path)

    def _update_preview_size(self):
        """大小变动后更新预览图片大小"""
        layout = self.ui.horizontalLayout_place
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicView = item.widget()
            widget_comic_view.update_preview_image_size()

        # 保存预览控件到配置文件
        function_config_size.preview_dialog_width.update(self.width())
        function_config_size.preview_dialog_height.update(self.height())

    def _set_icon(self):
        """设置图标"""
        self.ui.toolButton_last_5.setIcon(QIcon(_ICON_LAST_LAST))
        self.ui.toolButton_last.setIcon(QIcon(_ICON_LAST))
        self.ui.toolButton_next.setIcon(QIcon(_ICON_NEXT))
        self.ui.toolButton_next_5.setIcon(QIcon(_ICON_NEXT_NEXT))
        self.ui.toolButton_refresh.setIcon(QIcon(_ICON_REFRESH))
        self.ui.pushButton_quit.setIcon(QIcon(_ICON_QUIT))

    def resizeEvent(self, event):
        # 每次大小改变时重启计时器
        self.timer_resize.start()
        super().resizeEvent(event)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = DialogPreview()
    show_ui.show()
    app.exec()
