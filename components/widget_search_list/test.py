from PySide6.QtWidgets import QApplication

from search_list_model import SearchListModel
from search_list_presenter import SearchListPresenter
from search_list_viewer import SearchListViewer

app_ = QApplication()
viewer = SearchListViewer()
model = SearchListModel()
presenter = SearchListPresenter(viewer, model)
viewer.show()
app_.exec()
