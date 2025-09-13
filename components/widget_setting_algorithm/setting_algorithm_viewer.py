from typing import Union

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from common.class_config import ITEMS_HASH_ALGORITHM, ITEMS_HASH_LENGTH, ITEMS_ENHANCE_ALGORITHM
from components.widget_setting_algorithm.res.ui_setting_algorithm import Ui_Form


class SettingAlgorithmViewer(QWidget):
    """设置模块（相似算法设置项）的界面组件"""
    ChangeBasicAlgorithm = Signal(str, name="修改基础算法")
    ChangeIsEnhanceAlgorithm = Signal(bool, name="修改是否启用增强算法")
    ChangeEnhanceAlgorithm = Signal(str, name="修改增强算法")
    ChangeHashLength = Signal(str, name="修改Hash长度")
    ChangeSimilarThreshold = Signal(int, name="修改相似度阈值")

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 加载初始设置
        self._load_setting()

        # 绑定信号
        self._bind_signal()

    def set_basic_algorithm(self, algorithm: str):
        """设置基础算法"""
        self.ui.comboBox_basic_algorithm.setCurrentText(algorithm)

    def set_is_enhance_algorithm(self, is_enable: bool):
        """设置是否启用增强算法"""
        self.ui.checkBox_enhance_algorithm.setChecked(is_enable)

    def set_enhance_algorithm(self, algorithm: str):
        """设置增强算法"""
        self.ui.comboBox_enhance_algorithm.setCurrentText(algorithm)

    def set_hash_length(self, length: Union[str, int]):
        """设置Hash长度"""
        self.ui.comboBox_hash_length.setCurrentText(str(length))

    def set_similar_threshold(self, threshold: Union[str, int]):
        """设置相似度阈值"""
        self.ui.spinBox_similarity_threshold.setValue(int(threshold))

    def _load_setting(self):
        """加载初始设置"""
        # 基础算法
        self.ui.comboBox_basic_algorithm.addItems(ITEMS_HASH_ALGORITHM)
        # 增强算法
        self.ui.comboBox_enhance_algorithm.addItems(ITEMS_ENHANCE_ALGORITHM)
        # 相似度阈值
        pass
        # Hash长度
        self.ui.comboBox_hash_length.addItems(ITEMS_HASH_LENGTH)

    def _bind_signal(self):
        """绑定信号"""
        self.ui.comboBox_basic_algorithm.currentTextChanged.connect(self.ChangeBasicAlgorithm.emit)
        self.ui.checkBox_enhance_algorithm.stateChanged.connect(self.ChangeIsEnhanceAlgorithm.emit)
        self.ui.comboBox_enhance_algorithm.currentTextChanged.connect(self.ChangeEnhanceAlgorithm.emit)
        self.ui.spinBox_similarity_threshold.valueChanged.connect(self.ChangeSimilarThreshold.emit)
        self.ui.comboBox_hash_length.currentTextChanged.connect(self.ChangeHashLength.emit)


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = SettingAlgorithmViewer()
    program_ui.show()
    app_.exec()
