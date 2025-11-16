import os
import sys

import lzytools.common
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMessageBox

from common import function_cache_preview, function_cache_result
from components import window


def load_app():
    app_ = QApplication()
    app_.setStyle('Fusion')
    # 设置白色背景色
    # palette = QPalette()
    # palette.setColor(QPalette.Window, QColor(255, 255, 255))
    # app_.setPalette(palette)

    # 设置全局字体
    font = QFont("Microsoft YaHei", 10)  # 字体名称和大小
    app_.setFont(font)

    presenter = window.get_presenter()
    viewer = presenter.viewer
    model = presenter.model
    viewer.show()
    app_.exec()


def set_working_directory_to_exe_path():
    """设置工作目录为程序所在目录，防止拖入文件/命令行启动时程序工作目录错误"""
    print('工作路径测试')
    print('sys.argv', sys.argv)
    print('sys.executable', sys.executable)
    print('__file__', __file__)
    print('工作路径测试完成')

    exe_path = sys.argv[0]
    exe_parent = os.path.dirname(__file__)
    if exe_parent:
        os.chdir(exe_parent)
        print(f'设置工作路径为{exe_parent}')


def check_cache_exist():
    """检查缓存文件夹是否存在"""
    function_cache_preview.check_cache_exist()
    function_cache_result.check_cache_exist()


def show_dup_info():
    app_ = QApplication([])
    messagebox = QMessageBox()
    messagebox.setText('OnlyUnzip已经运行了一个实例，请勿重复运行。')
    messagebox.exec()
    sys.exit(1)


if __name__ == "__main__":
    set_working_directory_to_exe_path()
    check_cache_exist()
    if not lzytools.common.check_mutex('ComicDup'):  # 互斥体检查（单个实例）
        load_app()
    else:
        show_dup_info()
