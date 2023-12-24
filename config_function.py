import configparser
import os.path

config_file = 'config.ini'


def check_config():
    if not os.path.exists(config_file):
        with open(config_file, 'w', encoding='utf-8') as cw:
            pass
        config = configparser.ConfigParser()
        config.read(config_file, encoding='utf-8')
        config.add_section('preview_widget_wh')
        config.set('preview_widget_wh', 'width', '900')
        config.set('preview_widget_wh', 'height', '600')
        config.write(open(config_file, 'w', encoding='utf-8'))


def get_preview_widget_wh():
    """获取预览控件宽高"""
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    width = int(config.get('preview_widget_wh', 'width'))
    height = int(config.get('preview_widget_wh', 'height'))

    return width, height
