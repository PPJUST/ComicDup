from PySide6.QtWidgets import QDialog, QVBoxLayout

from common.class_comic import ComicInfo
from components.widget_assembler_comics_preview import widget_similar_group_preview


class AssemblerDialogComicsPreview(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('漫画预览器')
        self.setModal(True)

        # 添加控件实例到dialog中
        self.presenter = widget_similar_group_preview.get_presenter()
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.presenter.get_viewer())

    def get_presenter(self):
        """获取presenter"""
        return self.presenter

    def get_viewer(self):
        """获取viewer"""
        return self.presenter.get_viewer()

    def add_comic(self, comic_info: ComicInfo):
        """添加漫画"""
        self.presenter.add_comic(comic_info)

    def clear(self):
        """清空结果"""
        self.presenter.clear()
