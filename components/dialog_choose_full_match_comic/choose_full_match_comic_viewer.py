from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QDialog

from common.class_match_page_result import MatchResult
from components.dialog_choose_full_match_comic.res.ui_choose_full_match_comic import Ui_Dialog


class ChooseFullMatchComicViewer(QDialog):
    ChooseFullMatchComicsIndex = Signal(int, int, name='选择的漫画索引')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_exec.clicked.connect(self.emit_signal)
        self.ui.pushButton_quit.clicked.connect(self.close)

    def emit_signal(self):
        """发送信号"""
        comic_index_1 = self.ui.spinBox_comic_1.value()
        comic_index_2 = self.ui.spinBox_comic_2.value()
        self.ChooseFullMatchComicsIndex.emit(comic_index_1, comic_index_2)

    def show_result(self, result_state):
        """显示结果"""
        self.ui.textBrowser_match_result.clear()
        self.ui.textBrowser_match_result.append('即使页面匹配，也可能是不同的汉化组或修正')
        if isinstance(result_state, str):
            self.ui.textBrowser_match_result.setText(result_state)
        elif isinstance(result_state, MatchResult.OneToOne):
            self.ui.textBrowser_match_result.setText(result_state.text)
        else:
            self.ui.textBrowser_match_result.append(result_state.text)
            self.ui.textBrowser_match_result.append("\n漫画1问题页码如下：")
            # 传入参数的页码是从0开始计数的，所以显示时需要+1
            self.ui.textBrowser_match_result.append(', '.join(str(i + 1) for i in result_state.wrong_pages_comic_1))
            self.ui.textBrowser_match_result.append("\n漫画2问题页码如下：")
            self.ui.textBrowser_match_result.append(', '.join(str(i + 1) for i in result_state.wrong_pages_comic_2))


if __name__ == "__main__":
    app_ = QApplication()
    program_ui = ChooseFullMatchComicViewer()
    program_ui.show()
    app_.exec()
