from PySide6.QtWidgets import QApplication

from similar_result_preview_model import SimilarResultPreviewModel
from similar_result_preview_presenter import SimilarResultPreviewPresenter
from similar_result_preview_viewer import SimilarResultPreviewViewer

app_ = QApplication()
viewer = SimilarResultPreviewViewer()
model = SimilarResultPreviewModel()
presenter = SimilarResultPreviewPresenter(viewer, model)
viewer.show()
app_.exec()
