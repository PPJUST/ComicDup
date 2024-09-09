# 算法选项
import os

from PySide6.QtCore import Signal
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from constant import _ICON_CACHE, _SIMILARITY_THRESHOLD, _HASH_ALGORITHM, _EXTRACT_IMAGES_COUNT, _IMAGE_SIZE, \
    _THREADS_COUNT
from module import function_config_similar_option as option
from ui.dialog_cache_option import DialogCacheOption
from ui.src.ui_widget_option import Ui_Form


class WidgetOption(QWidget):
    signal_update_cache = Signal(name='更新缓存数据')
    signal_match_cache = Signal(name='缓存内部查重')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化
        self._set_icon()
        self.ui.spinBox_similarity_threshold.setValue(_SIMILARITY_THRESHOLD)
        self.ui.spinBox_similarity_threshold.setMinimum(70)
        self.ui.spinBox_similarity_threshold.setMaximum(100)
        self.ui.comboBox_hash_algorithm.addItems(_HASH_ALGORITHM)
        self.ui.spinBox_extract_images.setValue(_EXTRACT_IMAGES_COUNT)
        self.ui.spinBox_extract_images.setMinimum(1)
        self.ui.spinBox_extract_images.setMaximum(5)
        self.ui.comboBox_image_size.addItems(_IMAGE_SIZE)
        self.ui.spinBox_threads.setValue(_THREADS_COUNT)
        self.ui.spinBox_threads.setMinimum(1)
        self.ui.spinBox_threads.setMaximum(os.cpu_count())

        # 加载设置
        self._load_option()

        # 添加缓存dialog
        self._dialog_cache = DialogCacheOption(self)
        self._dialog_cache.signal_match_cache.connect(self.signal_match_cache.emit)
        self._dialog_cache.signal_update_cache.connect(self.signal_update_cache.emit)

        # 绑定槽函数
        self.ui.spinBox_similarity_threshold.valueChanged.connect(self.update_option_threshold)
        self.ui.comboBox_hash_algorithm.currentTextChanged.connect(self.update_option_hash)
        self.ui.checkBox_ssim.stateChanged.connect(self.update_option_ssim)
        self.ui.checkBox_match_cache.stateChanged.connect(self.update_option_cache)
        self.ui.pushButton_cache_option.clicked.connect(self._open_cache_option)
        self.ui.spinBox_extract_images.valueChanged.connect(self.update_option_images)
        self.ui.comboBox_image_size.currentTextChanged.connect(self.update_option_size)
        self.ui.spinBox_threads.valueChanged.connect(self.update_option_threads)

    def set_enable(self, is_enable: bool):
        """是否启用"""
        self.setEnabled(is_enable)

    def _open_cache_option(self):
        """打开缓存设置"""
        self._dialog_cache.exec()

    def _set_icon(self):
        """设置图标"""
        self.ui.pushButton_cache_option.setIcon(QIcon(_ICON_CACHE))

    def _load_option(self):
        """加载设置"""
        self.ui.spinBox_similarity_threshold.setValue(option.similarity_threshold.get())
        self.ui.comboBox_hash_algorithm.setCurrentText(option.hash_algorithm.get())
        self.ui.checkBox_ssim.setChecked(option.ssim.get())
        self.ui.checkBox_match_cache.setChecked(option.cache.get())
        self.ui.spinBox_extract_images.setValue(option.extract_images.get())
        self.ui.comboBox_image_size.setCurrentText(str(option.image_size.get()))
        self.ui.spinBox_threads.setValue(option.threads.get())

    def update_option_threshold(self):
        option.similarity_threshold.update(self.ui.spinBox_similarity_threshold.value())

    def update_option_hash(self):
        option.hash_algorithm.update(self.ui.comboBox_hash_algorithm.currentText())

    def update_option_ssim(self):
        option.ssim.update(self.ui.checkBox_ssim.isChecked())

    def update_option_cache(self):
        option.cache.update(self.ui.checkBox_match_cache.isChecked())

    def update_option_images(self):
        option.extract_images.update(self.ui.spinBox_extract_images.value())

    def update_option_size(self):
        option.image_size.update(self.ui.comboBox_image_size.currentText())

    def update_option_threads(self):
        option.threads.update(self.ui.spinBox_threads.value())


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = WidgetOption()
    show_ui.show()
    app.exec()
