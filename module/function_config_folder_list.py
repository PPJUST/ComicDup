# 配置文件的方法（需搜索的文件夹列表）

import configparser
import os

from constant import _CONFIG_FILE

_SECTION_FOLDER_LIST = 'folder_list'
_OPTION_FOLDER_LIST = 'folder_list'
_DEFAULT_VALUE_FOLDER_LIST = ''


def check_section(config_file=_CONFIG_FILE):
    """检查配置中的设置项是否存在"""
    if not os.path.exists(config_file):
        with open(config_file, 'w', encoding='utf-8'):
            pass
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    if _SECTION_FOLDER_LIST not in config.sections():
        config.add_section(_SECTION_FOLDER_LIST)
        config.set(_SECTION_FOLDER_LIST, _OPTION_FOLDER_LIST, _DEFAULT_VALUE_FOLDER_LIST)
        config.write(open(config_file, 'w', encoding='utf-8'))


class folder_list:
    """设置项-需搜索的文件夹列表"""

    @staticmethod
    def get():
        lst = _get_value(_SECTION_FOLDER_LIST).split('|')
        lst = [i for i in lst if i]
        return lst

    @staticmethod
    def update(folder_list_: list):
        text = '|'.join(folder_list_)
        _update_value(_SECTION_FOLDER_LIST, text)


def _get_value(key, section=_SECTION_FOLDER_LIST, config_file=_CONFIG_FILE):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    value = config.get(section, key)
    return value


def _update_value(key, value, section=_SECTION_FOLDER_LIST, config_file=_CONFIG_FILE):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    config.set(section, key, str(value))
    config.write(open(config_file, 'w', encoding='utf-8'))
