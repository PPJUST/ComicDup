from PySide6.QtCore import QObject

from common.class_comic import ComicInfo
from components.widget_assembler_comics_preview import widget_comic_preview
from components.widget_assembler_comics_preview.widget_similar_group_preview.similar_group_preview_model import \
    SimilarGroupPreviewModel
from components.widget_assembler_comics_preview.widget_similar_group_preview.similar_group_preview_viewer import \
    SimilarGroupPreviewViewer


class SimilarGroupPreviewPresenter(QObject):
    """相似组预览框架模块的桥梁组件"""

    def __init__(self, viewer: SimilarGroupPreviewViewer, model: SimilarGroupPreviewModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.widgets_comic = []  # 显示的漫画控件列表

        # 绑定信号
        self._bind_signal()

    def add_comic(self, comic_info: ComicInfo):
        """显示漫画"""
        self.widget_comic_preview = widget_comic_preview.get_presenter()
        self.widget_comic_preview.set_comic(comic_info)
        self.widgets_comic.append(self.widget_comic_preview)
        self.viewer.add_widget(self.widget_comic_preview.get_viewer())

    def turn_to_previous_page(self, page_count: int = 1):
        """全局翻页-转到上一页"""
        pass

    def turn_to_next_page(self, page_count: int = 1):
        """全局翻页-转到下一页"""
        pass

    def reset_page_number(self):
        """重置页码"""
        pass

    def quit(self):
        """退出"""
        pass

    def clear(self):
        """清空页面"""
        pass

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
