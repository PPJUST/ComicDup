from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication

from class_ import class_image_info
from module import function_config_similar_option, function_config, function_config_size, function_config_folder_list
from ui.main_window import MainWindow


def check_default_setting():
    """检查默认设置"""
    # 检查文件夹是否存在
    function_config.check_folder_exist()
    # 检查配置文件中的设置项
    function_config_similar_option.check_section()
    function_config_size.check_section()
    function_config_folder_list.check_section()
    # 检查初始图片信息数据库
    class_image_info.create_default_sqlite()


def main():
    app = QApplication()
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)
    show_ui = MainWindow()
    width = function_config_size.main_width.get()
    height = function_config_size.main_height.get()
    show_ui.resize(width, height)
    show_ui.show()
    app.exec()


if __name__ == '__main__':
    check_default_setting()
    main()
