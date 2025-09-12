from PySide6.QtWidgets import QApplication

from setting_comic_model import SettingComicModel
from setting_comic_presenter import SettingComicPresenter
from setting_comic_viewer import SettingComicViewer

app_ = QApplication()
viewer = SettingComicViewer()
model = SettingComicModel()
presenter = SettingComicPresenter(viewer, model)
viewer.show()
app_.exec()
