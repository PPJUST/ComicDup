from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QVBoxLayout

from common.class_comic import ComicInfoBase
from components.widget_assembler_comics_preview import widget_similar_group_preview


class AssemblerDialogComicsPreview(QDialog):
    """预览相似组内漫画的dialog组装器"""
    ComicDeleted = Signal(object, name='删除漫画对应的漫画信息类')

    def __init__(self):
        super().__init__()
        self.setWindowTitle('漫画预览器')
        self.setModal(True)

        # 添加控件实例到dialog中
        self.presenter = widget_similar_group_preview.get_presenter()
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.presenter.get_viewer())

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
