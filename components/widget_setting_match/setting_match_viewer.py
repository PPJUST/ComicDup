import os
from typing import Union

from PySide6.QtCore import Signal, QEvent
from PySide6.QtWidgets import QWidget, QApplication, QComboBox, QSpinBox

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

        # 设置数值类选项的上下限
        self.ui.spinBox_extract_pages.setRange(1, 100)
        self.ui.spinBox_same_parent_folder.setRange(1, 10)
        self.ui.spinBox_thread_count.setRange(1, os.cpu_count())  # 上限为cpu逻辑核心数

        # 加载初始设置
        self._load_setting()

        # 绑定信号
        self._bind_signal()

        # 安装事件过滤器，禁用滚轮动作
        self.ui.spinBox_thread_count.installEventFilter(self)
        self.ui.spinBox_extract_pages.installEventFilter(self)
        self.ui.spinBox_same_parent_folder.installEventFilter(self)

        self.ui.checkBox_match_similar_filename.setEnabled(False)  # todo
        self.ui.checkBox_same_parent_folder.setEnabled(False)  # todo 仅匹配同一目录下的漫画（设置目录层级，往上几级）
        self.ui.spinBox_same_parent_folder.setEnabled(False)  # todo

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

    def set_options_state(self, is_enable: bool):
        """设置选项启用/禁用"""
        self.ui.spinBox_extract_pages.setEnabled(is_enable)
        self.ui.checkBox_match_cache.setEnabled(is_enable)
        self.ui.checkBox_match_similar_filename.setEnabled(is_enable)
        self.ui.checkBox_same_parent_folder.setEnabled(is_enable)
        self.ui.spinBox_same_parent_folder.setEnabled(is_enable)
        self.ui.spinBox_thread_count.setEnabled(is_enable)

    def _load_setting(self):
        """加载初始设置"""
        pass

    def _bind_signal(self):
        """绑定信号"""
        self.ui.spinBox_extract_pages.valueChanged.connect(self.ChangeExtractPages.emit)
        self.ui.checkBox_match_cache.stateChanged.connect(self.ChangeIsMatchCache.emit)
        self.ui.checkBox_match_similar_filename.stateChanged.connect(self.ChangeIsMatchSimilarFilename.emit)
        self.ui.spinBox_thread_count.valueChanged.connect(self.ChangeThreadCount.emit)

    def eventFilter(self, obj, event):
        # 拦截控件的滚轮动作
        if isinstance(obj, QComboBox) and event.type() == QEvent.Wheel:
            return True
        elif isinstance(obj, QSpinBox) and event.type() == QEvent.Wheel:
            return True
        # 其他事件正常传递
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SettingMatchViewer()
    program_ui.show()
    app_.exec()
