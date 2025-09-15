from PySide6.QtCore import QObject

from components import widget_exec, widget_setting_algorithm, widget_setting_match, widget_setting_comic, \
    widget_search_list, widget_runtime_info, widget_similar_result_filter, widget_assembler_similar_result_preview
from components.window.window_model import WindowModel
from components.window.window_viewer import WindowViewer


class WindowPresenter(QObject):
    """主窗口的桥梁组件"""

    def __init__(self, viewer: WindowViewer, model:WindowModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 实例化控件
        self.widget_exec = widget_exec.get_presenter()
        self.widget_setting_algorithm = widget_setting_algorithm.get_presenter()
        self.widget_setting_match= widget_setting_match.get_presenter()
        self.widget_setting_comic= widget_setting_comic.get_presenter()
        self.widget_search_list= widget_search_list.get_presenter()
        self.widget_runtime_info= widget_runtime_info.get_presenter()
        self.widget_similar_result_filter= widget_similar_result_filter.get_presenter()
        self.similar_result_preview= widget_assembler_similar_result_preview.get_presenter()

        self.init_viewer()

    def init_viewer(self):
        """设置viewer"""
        self.viewer.add_viewer_exec(self.widget_exec.viewer)
        self.viewer.add_viewer_setting_1(self.widget_setting_algorithm.viewer)
        self.viewer.add_viewer_setting_2(self.widget_setting_match.viewer)
        self.viewer.add_viewer_setting_3(self.widget_setting_comic.viewer)
        self.viewer.add_viewer_search_list(self.widget_search_list.viewer)
        self.viewer.add_viewer_runtime_info(self.widget_runtime_info.viewer)
        self.viewer.add_viewer_result_filter(self.widget_similar_result_filter.viewer)
        self.viewer.add_viewer_result_preview(self.similar_result_preview.viewer)
