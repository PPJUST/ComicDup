from PySide6.QtWidgets import QApplication

from similar_group_preview_model import SimilarGroupPreviewModel
from similar_group_preview_presenter import SimilarGroupPreviewPresenter
from similar_group_preview_viewer import SimilarGroupPreviewViewer

app_ = QApplication()
viewer = SimilarGroupPreviewViewer()
model = SimilarGroupPreviewModel()
presenter = SimilarGroupPreviewPresenter(viewer, model)
viewer.show()
app_.exec()
