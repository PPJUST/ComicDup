from PySide6.QtWidgets import QApplication

from comic_info_line_model import ComicInfoLineModel
from comic_info_line_presenter import ComicInfoLinePresenter
from comic_info_line_viewer import ComicInfoLineViewer

app_ = QApplication()
viewer = ComicInfoLineViewer()
model = ComicInfoLineModel()
presenter = ComicInfoLinePresenter(viewer, model)
viewer.show()
app_.exec()
