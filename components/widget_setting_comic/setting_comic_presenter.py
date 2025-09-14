from PySide6.QtCore import QObject

from components.widget_setting_comic.setting_comic_model import SettingComicModel
from components.widget_setting_comic.setting_comic_viewer import SettingComicViewer


class SettingComicPresenter(QObject):
    """设置模块（漫画设置项）的桥梁组件"""

    def __init__(self, viewer: SettingComicViewer, model:SettingComicModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 加载初始设置
        self._load_setting()

        # 绑定信号
        self._bind_signal()

    def _load_setting(self):
        """加载初始设置"""
        pages_lower_limit = self.model.get_pages_lower_limit()
        self.viewer.set_pages_lower_limit(pages_lower_limit)

        is_analyze_archive = self.model.get_is_analyze_archive()
        self.viewer.set_is_analyze_archive(is_analyze_archive)

        is_allow_other_filetypes = self.model.get_is_allow_other_filetypes()
        self.viewer.set_is_allow_other_filetypes(is_allow_other_filetypes)

    def _bind_signal(self):
        """绑定信号"""
        self.viewer.ChangePagesLowerLimit.connect(self.model.set_pages_lower_limit)
        self.viewer.ChangeIsAnalyzeArchive.connect(self.model.set_is_analyze_archive)
        self.viewer.ChangeIsAllowOtherFiletypes.connect(self.model.set_is_allow_other_filetypes)
