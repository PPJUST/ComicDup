from PySide6.QtWidgets import QApplication

from comic_info_model import ComicInfoModel
from comic_info_presenter import ComicInfoPresenter
from comic_info_viewer import ComicInfoViewer

app_ = QApplication()
viewer = ComicInfoViewer()
model = ComicInfoModel()
presenter = ComicInfoPresenter(viewer, model)
viewer.show()
app_.exec()
