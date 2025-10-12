from typing import Union

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from components.widget_setting_match.res.ui_setting_match import Ui_Form


class SettingMatchViewer(QWidget):
    """设置模块（匹配设置项）的界面组件"""
    ChangeExtractPages = Signal(int, name="修改漫画提取页数")
    ChangeIsMatchCache = Signal(bool, name="修改是否匹配缓存")
    ChangeIsMatchSimilarFilename = Signal(bool, name="修改是否仅匹配相似文件名")
    ChangeThreadCount = Signal(int, name="修改线程数")

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 加载初始设置
        self._load_setting()

        # 绑定信号
        self._bind_signal()

        self.ui.checkBox_match_cache.setEnabled(False)  # 备忘录
        self.ui.checkBox_match_similar_filename.setEnabled(False)  # 备忘录

    def set_extract_pages(self, count: int):
        """设置提取页数"""
        self.ui.spinBox_extract_pages.setValue(count)

    def set_is_match_cache(self, is_enable: bool):
        """设置是否匹配缓存"""
        self.ui.checkBox_match_cache.setChecked(is_enable)

    def set_is_match_similar_filename(self, is_enable: bool):
        """设置是否仅匹配相似文件名"""
        self.ui.checkBox_match_similar_filename.setChecked(is_enable)

    def set_thread_count(self, count: Union[str, int]):
        """设置线程数"""
        self.ui.spinBox_thread_count.setValue(int(count))

    def _load_setting(self):
        """加载初始设置"""
        pass

    def _bind_signal(self):
        """绑定信号"""
        self.ui.spinBox_extract_pages.valueChanged.connect(self.ChangeExtractPages.emit)
        self.ui.checkBox_match_cache.stateChanged.connect(self.ChangeIsMatchCache.emit)
        self.ui.checkBox_match_similar_filename.stateChanged.connect(self.ChangeIsMatchSimilarFilename.emit)
        self.ui.spinBox_thread_count.valueChanged.connect(self.ChangeThreadCount.emit)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SettingMatchViewer()
    program_ui.show()
    app_.exec()
