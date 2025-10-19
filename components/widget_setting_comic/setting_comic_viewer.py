from PySide6.QtCore import Signal, QEvent
from PySide6.QtWidgets import QWidget, QApplication, QComboBox, QSpinBox

from components.widget_setting_comic.res.ui_setting_comic import Ui_Form


class SettingComicViewer(QWidget):
    """设置模块（漫画设置项）的界面组件"""
    ChangePagesLowerLimit = Signal(int, name="修改识别为漫画的页数下限")
    ChangeIsAnalyzeArchive = Signal(bool, name="修改是否识别压缩文件")
    ChangeIsAllowOtherFiletypes = Signal(bool, name="修改是否允许漫画包含其他类型文件")

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 设置数值类选项的上下限
        self.ui.spinBox_pages_lower_limit.setRange(1, 100)

        # 加载初始设置
        self._load_setting()

        # 绑定信号
        self._bind_signal()

        # 安装事件过滤器，禁用滚轮动作
        self.ui.spinBox_pages_lower_limit.installEventFilter(self)

    def set_pages_lower_limit(self, count: int):
        """设置识别为漫画的页数下限"""
        self.ui.spinBox_pages_lower_limit.setValue(count)

    def set_is_analyze_archive(self, is_enable: bool):
        """设置是否识别压缩文件"""
        self.ui.checkBox_analyze_archive.setChecked(is_enable)

    def set_is_allow_other_filetypes(self, is_enable: bool):
        """设置是否允许漫画包含其他类型文件"""
        self.ui.checkBox_allow_other_filetypes.setChecked(is_enable)

    def _load_setting(self):
        """加载初始设置"""
        pass

    def _bind_signal(self):
        """绑定信号"""
        self.ui.spinBox_pages_lower_limit.valueChanged.connect(self.ChangePagesLowerLimit.emit)
        self.ui.checkBox_analyze_archive.stateChanged.connect(self.ChangeIsAnalyzeArchive.emit)
        self.ui.checkBox_allow_other_filetypes.stateChanged.connect(self.ChangeIsAllowOtherFiletypes.emit)

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
    program_ui = SettingComicViewer()
    program_ui.show()
    app_.exec()
