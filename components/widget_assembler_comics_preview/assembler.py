from PySide6.QtCore import Signal, QTimer
from PySide6.QtWidgets import QDialog, QVBoxLayout

from common.class_comic import ComicInfoBase
from common.function_config import SettingPreviewDialogSize, CONFIG_FILE
from components.widget_assembler_comics_preview import widget_similar_group_preview


class AssemblerDialogComicsPreview(QDialog):
    """预览相似组内漫画的dialog组装器"""
    ComicDeleted = Signal(object, name='删除漫画对应的漫画信息类')

    def __init__(self):
        super().__init__()
        self.setWindowTitle('漫画预览器')
        self.setModal(True)
        self.resize(800, 600)

        # 添加控件实例到dialog中
        self.presenter = widget_similar_group_preview.get_presenter()
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.presenter.get_viewer())

        # 初始化ui
        self._init_viewer()

        # 定时器，用于延迟保存窗口尺寸
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self._save_size)

        # 绑定信号
        self.presenter.Quit.connect(self.close)
        self.presenter.ComicDeleted.connect(self.ComicDeleted.emit)

    def get_presenter(self):
        """获取presenter"""
        return self.presenter

    def get_viewer(self):
        """获取viewer"""
        return self.presenter.get_viewer()

    def add_comic(self, comic_info: ComicInfoBase):
        """添加漫画"""
        self.presenter.add_comic(comic_info)

    def set_is_reconfirm_before_delete(self, is_reconfirm: bool):
        """设置是否删除前再次确认"""
        self.presenter.set_is_reconfirm_before_delete(is_reconfirm)

    def clear(self):
        """清空结果"""
        self.presenter.clear()

    def _init_viewer(self):
        """初始化ui"""
        config = SettingPreviewDialogSize(CONFIG_FILE)
        width, height = config.read()
        self.presenter.get_viewer().resize(width, height)

    def _save_size(self):
        """保存窗口大小"""
        width = self.presenter.get_viewer().width()
        height = self.presenter.get_viewer().height()
        size = (width, height)
        config = SettingPreviewDialogSize(CONFIG_FILE)
        config.set(size)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # 改变内部图片label大小
        self.presenter.resize_image_size(self.width(), self.height())
        # 延迟保存窗口大小
        self.timer.start()
