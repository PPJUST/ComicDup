from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from common.class_order import ORDER_KEYS_TEXT, ORDER_DIRECTIONS_TEXT, ORDER_KEYS, ORDER_DIRECTIONS
from components.widget_similar_result_filter.res.ui_similar_result_filter import Ui_Form


class SimilarResultFilterViewer(QWidget):
    """相似结果筛选器模块的界面组件"""
    RefreshResult = Signal(name='重置匹配结果')
    FilterSameItems = Signal(name='筛选器 仅显示页数、文件大小相同项')
    FilterExcludeDiffPages = Signal(name='筛选器 剔除页数差异过大项')
    ReconfirmDelete = Signal(bool, name='删除前再次确认')
    ChangeSortKey = Signal(str, name='排序键值改变')
    ChangeSortDirection = Signal(str, name='排序方向改变')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化
        self._load_setting()

        # 绑定信号
        self.ui.pushButton_refresh_result.clicked.connect(self.RefreshResult.emit)
        self.ui.pushButton_filter_same_items.clicked.connect(self.FilterSameItems.emit)
        self.ui.pushButton_exclude_diff_pages.clicked.connect(self.FilterExcludeDiffPages.emit)
        self.ui.checkBox_reconfirm_before_delete.stateChanged.connect(self.ReconfirmDelete.emit)
        self.ui.comboBox_sort_key.currentTextChanged.connect(self.ChangeSortKey.emit)
        self.ui.comboBox_sort_direction.currentTextChanged.connect(self.ChangeSortDirection.emit)

        self.ui.pushButton_filter_same_items.setEnabled(False)  # todo
        self.ui.pushButton_exclude_diff_pages.setEnabled(False) # todo

    def _load_setting(self):
        """加载设置"""
        self.ui.comboBox_sort_key.addItems(ORDER_KEYS_TEXT)
        self.ui.comboBox_sort_direction.addItems(ORDER_DIRECTIONS_TEXT)

    def get_order_key(self):
        """获取排序键"""
        key = self.ui.comboBox_sort_key.currentText()
        for type_key in ORDER_KEYS:
            if type_key.text == key:
                return type_key

    def get_order_direction(self):
        """获取排序方向"""
        direction = self.ui.comboBox_sort_direction.currentText()
        for type_direction in ORDER_DIRECTIONS:
            if type_direction.text == direction:
                return type_direction


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SimilarResultFilterViewer()
    program_ui.show()
    app_.exec()
