from PySide6.QtWidgets import QApplication

from setting_match_model import SettingMatchModel
from setting_match_presenter import SettingMatchPresenter
from setting_match_viewer import SettingMatchViewer

app_ = QApplication()
viewer = SettingMatchViewer()
model = SettingMatchModel()
presenter = SettingMatchPresenter(viewer, model)
viewer.show()
app_.exec()
