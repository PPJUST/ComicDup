from PySide6.QtWidgets import QApplication

from setting_algorithm_model import SettingAlgorithmModel
from setting_algorithm_presenter import SettingAlgorithmPresenter
from setting_algorithm_viewer import SettingAlgorithmViewer

app_ = QApplication()
viewer = SettingAlgorithmViewer()
model = SettingAlgorithmModel()
presenter = SettingAlgorithmPresenter(viewer, model)
viewer.show()
app_.exec()
