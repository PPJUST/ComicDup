# 配置文件的方法（界面大小）

import configparser
import os

from constant import _CONFIG_FILE

_SECTION_SIZE = 'size'
_OPTION_MAIN_WIDTH = 'main_width'
_DEFAULT_VALUE_MAIN_WIDTH = '900'
_OPTION_MAIN_HEIGHT = 'main_height'
_DEFAULT_VALUE_MAIN_HEIGHT = '600'
_OPTION_PREVIEW_DIALOG_WIDTH = 'preview_dialog_width'
_DEFAULT_VALUE_PREVIEW_DIALOG_WIDTH = '600'
_OPTION_PREVIEW_DIALOG_HEIGHT = 'preview_dialog_height'
_DEFAULT_VALUE_PREVIEW_DIALOG_HEIGHT = '400'


def check_section(config_file=_CONFIG_FILE):
    """检查配置中的设置项是否存在"""
    if not os.path.exists(config_file):
        with open(config_file, 'w', encoding='utf-8'):
            pass
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    if _SECTION_SIZE not in config.sections():
        config.add_section(_SECTION_SIZE)
        config.set(_SECTION_SIZE, _OPTION_MAIN_WIDTH, _DEFAULT_VALUE_MAIN_WIDTH)
        config.set(_SECTION_SIZE, _OPTION_MAIN_HEIGHT, _DEFAULT_VALUE_MAIN_HEIGHT)
        config.set(_SECTION_SIZE, _OPTION_PREVIEW_DIALOG_WIDTH, _DEFAULT_VALUE_PREVIEW_DIALOG_WIDTH)
        config.set(_SECTION_SIZE, _OPTION_PREVIEW_DIALOG_HEIGHT, _DEFAULT_VALUE_PREVIEW_DIALOG_HEIGHT)
        config.write(open(config_file, 'w', encoding='utf-8'))


class main_width:
    """设置项-主界面宽度"""

    @staticmethod
    def get():
        return int(_get_value(_OPTION_MAIN_WIDTH))

    @staticmethod
    def update(width: int):
        _update_value(_OPTION_MAIN_WIDTH, width)


class main_height:
    """设置项-主界面高度"""

    @staticmethod
    def get():
        return int(_get_value(_OPTION_MAIN_HEIGHT))

    @staticmethod
    def update(height: int):
        _update_value(_OPTION_MAIN_HEIGHT, height)


class preview_dialog_width:
    """设置项-预览dialog宽度"""

    @staticmethod
    def get():
        return int(_get_value(_OPTION_PREVIEW_DIALOG_WIDTH))

    @staticmethod
    def update(width: int):
        _update_value(_OPTION_PREVIEW_DIALOG_WIDTH, width)


class preview_dialog_height:
    """设置项-预览dialog高度"""

    @staticmethod
    def get():
        return int(_get_value(_OPTION_PREVIEW_DIALOG_HEIGHT))

    @staticmethod
    def update(height: int):
        _update_value(_OPTION_PREVIEW_DIALOG_HEIGHT, height)


def _get_value(key, section=_SECTION_SIZE, config_file=_CONFIG_FILE):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    value = config.get(section, key)
    return value


def _update_value(key, value, section=_SECTION_SIZE, config_file=_CONFIG_FILE):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    config.set(section, key, str(value))
    config.write(open(config_file, 'w', encoding='utf-8'))
