from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.widget_similar_result_filter.res.ui_similar_result_filter import Ui_Form


class SimilarResultFilterViewer(QWidget):
    """相似结果筛选器模块的界面组件"""
    RefreshResult = Signal(name='重置匹配结果')
    FilterSameItems = Signal(name='筛选器 仅显示页数、文件大小相同项')
    FilterExcludeDiffPages = Signal(name='筛选器 剔除页数差异过大项')
    ReconfirmDelete = Signal(bool, name='删除前再次确认')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 绑定信号
        self.ui.pushButton_refresh_result.clicked.connect(self.RefreshResult.emit)
        self.ui.pushButton_filter_same_items.clicked.connect(self.FilterSameItems.emit)
        self.ui.pushButton_exclude_diff_pages.clicked.connect(self.FilterExcludeDiffPages.emit)
        self.ui.checkBox_reconfirm_before_delete.stateChanged.connect(self.ReconfirmDelete.emit)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SimilarResultFilterViewer()
    program_ui.show()
    app_.exec()
