import configparser
import os.path
import pickle

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


def save_data_pickle(similar_group_list, comic_data_dict):
    """存储原始数据"""
    with open("similar_group_list.pickle", "wb") as sp:
        pickle.dump(similar_group_list, sp)

    with open("comic_data_dict.pickle", "wb") as cp:
        pickle.dump(comic_data_dict, cp)


def get_data_pickle():
    """读取保存的原始数据"""
    if os.path.exists("similar_group_list.pickle"):
        with open("similar_group_list.pickle", "rb") as sp:
            similar_group_list = pickle.load(sp)
    else:
        similar_group_list = []

    if os.path.exists("comic_data_dict.pickle"):
        with open("comic_data_dict.pickle", "rb") as cp:
            comic_data_dict = pickle.load(cp)
    else:
        comic_data_dict = {}

    return similar_group_list, comic_data_dict
