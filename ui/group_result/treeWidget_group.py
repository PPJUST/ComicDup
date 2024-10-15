# 用于显示相似组的外部框架

from PySide6.QtWidgets import *

from class_ import class_comic_info
from module import function_match_result, function_normal
from ui.group_result.scrollArea_comic_group import ScrollAreaComicGroup


class TreeWidgetGroup(QTreeWidget):
    """用于显示相似组的外部框架(Widget->ScrollArea->■TreeWidget)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHeaderHidden(True)

    def show_group(self):
        """显示所有组"""
        function_normal.print_function_info()
        # 清空
        self.clear()

        # 提取本地缓存
        similar_comic_group = function_match_result.read_result()
        comic_info_dict = class_comic_info.read_db()
        # 插入节点
        for index, comic_group in enumerate(similar_comic_group, start=1):
            print('显示相似组 ', index, comic_group)
            # 创建父节点
            item_parent = QTreeWidgetItem()
            item_parent.setText(0, f'■ 第{index}组 - {len(comic_group)}项')
            # item_parent.setBackground(0, QColor(248, 232, 137))
            self.addTopLevelItem(item_parent)
            # 创建子节点
            item_child = QTreeWidgetItem()
            item_parent.addChild(item_child)
            # 创建自定义控件
            child_widget = ScrollAreaComicGroup(comic_group, comic_info_dict=comic_info_dict)
            child_widget.signal_delete.connect(self._delete_emtpy_group)
            child_widget.signal_hide.connect(self._hide_group)
            # 将自定义控件设置为子节点的部件
            self.setItemWidget(item_child, 0, child_widget)

        # 打开所有父节点
        self.expandAll()

    def refresh_widget(self):
        """刷新子控件，重新显示所有漫画"""
        function_normal.print_function_info()
        for index in range(self.topLevelItemCount()):
            print('刷新节点 ', index)
            parent_item = self.topLevelItem(index)  # 父节点
            parent_item.setExpanded(True)
            for index_ in range(parent_item.childCount()):
                child_item = parent_item.child(index_)  # 子节点
                widget: ScrollAreaComicGroup = self.itemWidget(child_item, 0)  # 子节点控件
                widget.refresh_widget()

    def check_validity(self):
        """检查有效性，无效则删除"""
        function_normal.print_function_info()
        for index in range(self.topLevelItemCount()):
            print('刷新节点', index)
            parent_item = self.topLevelItem(index)  # 父节点
            for index_ in range(parent_item.childCount()):
                child_item = parent_item.child(index_)  # 子节点
                widget: ScrollAreaComicGroup = self.itemWidget(child_item, 0)  # 子节点控件
                widget.check_validity()

    def filter_same(self):
        """仅显示页数、大小相同项"""
        function_normal.print_function_info()
        for index in range(self.topLevelItemCount()):
            print('刷新节点', index)
            parent_item = self.topLevelItem(index)  # 父节点
            for index_ in range(parent_item.childCount()):
                child_item = parent_item.child(index_)  # 子节点
                widget: ScrollAreaComicGroup = self.itemWidget(child_item, 0)  # 子节点控件
                widget.filter_same()

    def filter_pages_diff(self):
        """剔除页数差异过大项"""
        function_normal.print_function_info()
        for index in range(self.topLevelItemCount()):
            print('刷新节点', index)
            parent_item = self.topLevelItem(index)  # 父节点
            for index_ in range(parent_item.childCount()):
                child_item = parent_item.child(index_)  # 子节点
                widget: ScrollAreaComicGroup = self.itemWidget(child_item, 0)  # 子节点控件
                widget.filter_pages_diff()

    def _delete_emtpy_group(self):
        """删除空节点"""
        widget_scroll_area = self.sender()
        child_item = self.itemAt(widget_scroll_area.pos())  # 获取子节点对象
        top_level_item = child_item.parent()  # 获取父节点对象
        for index in range(self.topLevelItemCount()):
            item = self.topLevelItem(index)
            if item == top_level_item:
                self.takeTopLevelItem(index)  # 删除父节点

    def _hide_group(self):
        """折叠对应的节点"""
        widget_scroll_area = self.sender()
        child_item = self.itemAt(widget_scroll_area.pos())  # 获取子节点对象
        if child_item:
            top_level_item = child_item.parent()  # 获取父节点对象
            if top_level_item:
                top_level_item.setExpanded(False)
