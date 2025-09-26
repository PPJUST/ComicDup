from PySide6.QtWidgets import QApplication

from comic_preview_model import ComicPreviewModel
from comic_preview_presenter import ComicPreviewPresenter
from comic_preview_viewer import ComicPreviewViewer

app_ = QApplication()
viewer = ComicPreviewViewer()
model = ComicPreviewModel()
presenter = ComicPreviewPresenter(viewer, model)
viewer.show()
app_.exec()
