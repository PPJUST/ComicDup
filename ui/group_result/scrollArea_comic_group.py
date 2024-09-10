# 显示一组相似漫画的框架
import natsort
from PySide6.QtCore import Signal
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from class_ import class_comic_info
from ui.group_preview.dialog_preview import DialogPreview
from ui.group_result.widget_comic_info import WidgetComicInfo
from ui.src.ui_scrollArea_comic_group import Ui_Form


class ScrollAreaComicGroup(QWidget):
    """显示一组相似漫画的框架(Widget->■ScrollArea->TreeWidget)
    :param similar_group: set，漫画相似组，内部元素为漫画路径"""
    signal_delete = Signal(name='删除该控件')

    def __init__(self, similar_group: set, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化
        # self.ui.scrollArea.setStyleSheet('border: 1px solid red')  # 调试使用
        self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.scrollArea.setWidgetResizable(True)

        self._similar_group = similar_group
        self._add_child_widget()

        # 移动scrollArea的横向滚动条到另外的控件中
        # 如果直接使用原版的横向滚动条，在出现横向滚动条时控件内部的显示高度会改变，
        # 导致内部的子控件高度超限，控件会出现纵向滚动条，所以需要将其放置在scrollArea外
        self.ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollbar = self.ui.scrollArea.horizontalScrollBar()
        self.ui.horizontalLayout__scrollbar.addWidget(self.scrollbar)

    def refresh_widget(self):
        """刷新子控件，重新显示所有漫画"""
        layout = self.ui.horizontalLayout_place
        if layout.count() != len(self._similar_group):  # 存在筛选器时，清空布局后重新添加
            self._add_child_widget()

    def check_validity(self):
        """检查有效性，无效则删除"""
        layout = self.ui.horizontalLayout_place
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicInfo = item.widget()
            useless_comic = widget_comic_view.check_validity()
            if useless_comic:
                self._similar_group.remove(useless_comic)  # 删除已失效的漫画，防止重置筛选器后重新出现

    def filter_same(self):
        """仅显示页数、大小相同项"""
        # 先清除之前的筛选器结果
        self.refresh_widget()

        # 收集子控件的漫画信息类
        info_dict = {}
        layout = self.ui.horizontalLayout_place
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicInfo = item.widget()
            path, info = widget_comic_view.get_size_and_count()
            size_count_joined = ' - '.join([str(i) for i in info.values()])
            info_dict[path] = size_count_joined
        # 找出需要删除的项目（无重复的页数和大小的项）
        delete_paths = []
        for path, info_ in info_dict.items():
            if list(info_dict.values()).count(info_) < 2:
                delete_paths.append(path)
        # 删除对应项目
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicInfo = item.widget()
            widget_comic_view.delete_if_in_list(delete_paths)

    def filter_pages_diff(self):
        """剔除页数差异过大项"""
        # 先清除之前的筛选器结果
        self.refresh_widget()

        # 收集子控件的漫画信息类
        info_dict = {}
        layout = self.ui.horizontalLayout_place
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicInfo = item.widget()
            path, info = widget_comic_view.get_size_and_count()
            info_dict[path] = info['image_count']
        # 以最小页数的150%为上限，确认需删除的项目
        min_page = natsort.natsorted(info_dict.values())[0] * 1.5
        delete_paths = []
        for path, page_count in info_dict.items():
            if page_count > min_page:
                delete_paths.append(path)
        # 删除对应项目
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicInfo = item.widget()
            widget_comic_view.delete_if_in_list(delete_paths)

    def _add_child_widget(self):
        """添加子控件（单本漫画预览控件）"""
        # 先清空
        layout = self.ui.horizontalLayout_place
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # 添加子控件
        for comic_path in self._similar_group:
            comic_info = class_comic_info.get_comic_info(comic_path)
            child_widget = WidgetComicInfo(comic_info)
            child_widget.signal_view.connect(self._view_comics)
            child_widget.signal_delete.connect(self._comic_deleted)
            layout.addWidget(child_widget)

    def _view_comics(self):
        """预览相似组中的漫画"""
        dialog_preview = DialogPreview(self)
        dialog_preview.signal_deleted.connect(self._remove_widget_in_path)
        layout = self.ui.horizontalLayout_place
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicInfo = item.widget()
            comic_info = widget_comic_view.get_comic_info()
            dialog_preview.add_item(comic_info)
        dialog_preview.exec()

    def _comic_deleted(self):
        """删除单本漫画后，更新ui"""
        # 由于deleteLater方法只会在下一次事件循环时删除控件，不会立即从内存中删除
        # 所以在剩余控件数为1且正确删除无报错时，即可发送删除信号
        is_delete = False
        if self.ui.horizontalLayout_place.count() == 1:
            is_delete = True

        widget_ = self.sender()
        widget_.deleteLater()

        # 如果删除子控件后，layout中无其余控件，则删除发生信号删除自身
        if is_delete:
            self.signal_delete.emit()

    def _remove_widget_in_path(self, deleted_path):
        """在预览控件中删除漫画时，同步删除主页面的中的漫画控件"""
        layout = self.ui.horizontalLayout_place
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget_comic_view: WidgetComicInfo = item.widget()
            widget_comic_view.delete_if_in_list(deleted_path)
