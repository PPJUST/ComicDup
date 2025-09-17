import os
import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

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
    os.chdir(exe_parent)
    print(f'设置工作路径为{exe_parent}')


if __name__ == "__main__":
    set_working_directory_to_exe_path()
    load_app()
