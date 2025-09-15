from PySide6.QtWidgets import QApplication

from similar_group_info_model import SimilarGroupInfoModel
from similar_group_info_presenter import SimilarGroupInfoPresenter
from similar_group_info_viewer import SimilarGroupInfoViewer

app_ = QApplication()
viewer = SimilarGroupInfoViewer()
model = SimilarGroupInfoModel()
presenter = SimilarGroupInfoPresenter(viewer, model)
viewer.show()
app_.exec()
