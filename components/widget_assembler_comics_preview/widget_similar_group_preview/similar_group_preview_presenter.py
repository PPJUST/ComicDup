from PySide6.QtCore import QObject, Signal

from common.class_comic import ComicInfoBase
from components.widget_assembler_comics_preview import widget_comic_preview
from components.widget_assembler_comics_preview.widget_comic_preview import ComicPreviewPresenter
from components.widget_assembler_comics_preview.widget_similar_group_preview.similar_group_preview_model import \
    SimilarGroupPreviewModel
from components.widget_assembler_comics_preview.widget_similar_group_preview.similar_group_preview_viewer import \
    SimilarGroupPreviewViewer


class SimilarGroupPreviewPresenter(QObject):
    """相似组预览框架模块的桥梁组件"""
    Quit = Signal(name='退出')
    ComicDeleted = Signal(object, name='删除漫画对应的漫画信息类')

    def __init__(self, viewer: SimilarGroupPreviewViewer, model: SimilarGroupPreviewModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.widgets_comic = []  # 显示的漫画控件列表
        self.is_reconfirm_before_delete = True  # 删除前是否需要再次确认（在此模块单独存储一次，用于创建子模块时进行赋值）
        self.is_show_similar = True  # 是否显示相似度

        # 绑定信号
        self._bind_signal()

    def add_comic(self, comic_info: ComicInfoBase):
        """显示漫画"""
        self.widget_comic_preview = widget_comic_preview.get_presenter()
        self.widget_comic_preview.set_comic(comic_info)
        self.widget_comic_preview.set_is_reconfirm_before_delete(self.is_reconfirm_before_delete)
        self.widget_comic_preview.ComicDeleted.connect(self.comic_deleted)
        self.widgets_comic.append(self.widget_comic_preview)
        self.viewer.add_widget(self.widget_comic_preview.get_viewer())

        if self.is_show_similar:
            self.show_current_page_similar()

    def turn_to_previous_page(self, page_count: int = 1):
        """全局翻页-向前翻页"""
        for widget in self.widgets_comic:
            widget: ComicPreviewPresenter
            widget.turn_to_previous_page(page_count)

        if self.is_show_similar:
            self.show_current_page_similar()

    def turn_to_next_page(self, page_count: int = 1):
        """全局翻页-向后翻页"""
        for widget in self.widgets_comic:
            widget: ComicPreviewPresenter
            widget.turn_to_next_page(page_count)

        if self.is_show_similar:
            self.show_current_page_similar()

    def set_is_reconfirm_before_delete(self, is_reconfirm: bool):
        """设置是否删除前再次确认"""
        self.is_reconfirm_before_delete = is_reconfirm

        for widget in self.widgets_comic:
            widget: ComicPreviewPresenter
            widget.set_is_reconfirm_before_delete(is_reconfirm)

    def reset_page_number(self):
        """重置页码"""
        for widget in self.widgets_comic:
            widget: ComicPreviewPresenter
            widget.reset_page()

        if self.is_show_similar:
            self.show_current_page_similar()

    def comic_deleted(self):
        """漫画被删除后的操作"""
        widget_presenter: ComicPreviewPresenter = self.sender()
        deleted_comic_info = widget_presenter.comic_info
        # 删除ui中显示的viewer
        viewer = widget_presenter.get_viewer()
        self.viewer.remove_widget(viewer)
        # 删除存储的presenter
        self.widgets_comic.remove(widget_presenter)
        widget_presenter.deleteLater()
        # 发送信号
        self.ComicDeleted.emit(deleted_comic_info)

        if self.is_show_similar:
            self.show_current_page_similar()

    def show_current_page_similar(self):
        """显示不同漫画当前页码的图片之间的相似度"""
        # 以第一本漫画作为基准
        # 计算第一本漫画当前页图片的hash值
        base_hash_ = self.widgets_comic[0].calc_current_image_hash()
        # 显示同组漫画当前页图片的相似度
        for widget in self.widgets_comic:
            widget: ComicPreviewPresenter
            widget.compare_current_image_hash(base_hash_)

    def quit(self):
        """退出"""
        self.clear()
        self.Quit.emit()

    def clear(self):
        """清空页面"""
        self.widgets_comic.clear()
        self.viewer.clear()

    def get_viewer(self):
        """获取viewer"""
        return self.viewer

    def _bind_signal(self):
        """绑定信号"""
        self.viewer.PreviousPage.connect(self.turn_to_previous_page)
        self.viewer.PreviousPage2.connect(lambda: self.turn_to_previous_page(5))
        self.viewer.NextPage.connect(self.turn_to_next_page)
        self.viewer.NextPage2.connect(lambda: self.turn_to_next_page(5))
        self.viewer.Reset.connect(self.reset_page_number)
        self.viewer.Quit.connect(self.quit)
