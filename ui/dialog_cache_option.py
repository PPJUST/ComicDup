# 缓存选项
from PySide6.QtCore import Signal
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from class_ import class_comic_info, class_image_info
from constant import _ICON_REFRESH, _PREVIEW_DIRPATH, _COMICS_INFO_DB, _IMAGE_INFO_DB, _ICON_CLEAR, _ICON_QUIT, \
    _MATCH_RESULT
from module import function_normal, function_config
from ui.src.ui_dialog_cache_option import Ui_Dialog


class DialogCacheOption(QDialog):
    """缓存选项"""
    signal_update_cache = Signal(name='更新缓存数据')
    signal_match_cache = Signal(name='缓存内部查重')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 初始化
        self._set_icon()
        self._load_info()

        # 绑定槽函数
        self.ui.pushButton_check_dup_inside.clicked.connect(self.check_dup_inside)
        self.ui.pushButton_update_cache.clicked.connect(self.update_cache)
        self.ui.pushButton_delete_error_data.clicked.connect(self.delete_useless_cache)
        self.ui.pushButton_clear_cache.clicked.connect(self.clear_cache)
        self.ui.pushButton_quit.clicked.connect(self.accept)

    def check_dup_inside(self):
        """缓存内部查重"""
        function_normal.print_function_info()
        self.signal_match_cache.emit()
        self.accept()

    def update_cache(self):
        """更新缓存数据"""
        function_normal.print_function_info()
        self.signal_update_cache.emit()
        self.accept()

    def delete_useless_cache(self):
        """删除数据库中无效的数据"""
        function_normal.print_function_info()
        # 处理漫画信息数据库
        class_comic_info.delete_useless_item()
        # 处理预览图
        class_comic_info.delete_useless_preview()
        # 处理图片信息数据库
        class_image_info.delete_useless_item()
        # 更新显示数据
        self._load_info()

    def clear_cache(self):
        """清空缓存数据"""
        function_normal.print_function_info()
        function_normal.delete(_PREVIEW_DIRPATH)  # 删除预览图
        function_normal.delete(_COMICS_INFO_DB)  # 删除漫画信息数据库
        function_normal.delete(_IMAGE_INFO_DB)  # 删除图片信息数据库
        function_normal.delete(_MATCH_RESULT)  # 删除匹配结果

        # 删除后创建默认数据库
        function_config.check_folder_exist()
        class_image_info.create_default_sqlite()

        # 更新显示数据
        self._load_info()

    def _load_info(self):
        """加载设置信息"""
        function_normal.print_function_info()
        comic_count = len(class_comic_info.read_db())
        self.ui.label_comic_count.setText(str(comic_count))

        image_count = len(class_image_info.read_db())
        self.ui.label_image_count.setText(str(image_count))

        db_size_mb = round(
            (function_normal.get_size(_COMICS_INFO_DB)
             + function_normal.get_size(_IMAGE_INFO_DB)
             + function_normal.get_size(_MATCH_RESULT))
            / 1024 / 1024, 2)
        self.ui.label_db_filesize.setText(str(db_size_mb))

        preview_size_mb = round(function_normal.get_size(_PREVIEW_DIRPATH) / 1024 / 1024, 2)
        self.ui.label_preview_filesize.setText(str(preview_size_mb))

    def _set_icon(self):
        """设置图标"""
        self.ui.pushButton_check_dup_inside.setIcon(QIcon(_ICON_REFRESH))
        self.ui.pushButton_update_cache.setIcon(QIcon(_ICON_REFRESH))
        self.ui.pushButton_delete_error_data.setIcon(QIcon(_ICON_CLEAR))
        self.ui.pushButton_clear_cache.setIcon(QIcon(_ICON_CLEAR))
        self.ui.pushButton_quit.setIcon(QIcon(_ICON_QUIT))


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = DialogCacheOption()
    show_ui.show()
    app.exec()
