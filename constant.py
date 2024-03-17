# 常量设置

# 图标
ICON_DEL = 'icon/del.png'
ICON_ARCHIVE = 'icon/archive.png'
ICON_FOLDER = 'icon/folder.png'
ICON_PREVIOUS = 'icon/previous.png'
ICON_RECYCLE_BIN = 'icon/recycle_bin.png'
ICON_NEXT = 'icon/next.png'
ICON_REFRESH = 'icon/refresh.png'
ICON_NEXT_5P = 'icon/next_5p.png'
ICON_PREVIOUS_5P = 'icon/previous_5p.png'
OVERSIZE_IMAGE = 'icon/oversize_image.jpg'
ICON_START = 'icon/start.png'
ICON_STOP = 'icon/stop.png'
ICON_LOAD = 'icon/load.png'
ICON_CACHE = 'icon/cache.png'
ICON_INFORMATION = 'icon/information.png'
ICON_CHECK = 'icon/check.png'
ICON_RESET = 'icon/reset.png'
ICON_CLEAR = 'icon/clear.png'
INFO_MAIN = 'icon/info_main.png'
INFO_PREVIEW = 'icon/info_preview.png'
INFO_CACHE = 'icon/info_cache.png'

# 缓存文件相关
CACHE_FOLDER = 'cache'
HASH_CACHE_FILE = CACHE_FOLDER + '/hash_cache.db'  # 哈希值缓存
SIMILAR_GROUPS_PICKLE = CACHE_FOLDER + '/similar_groups.pickle'  # 相似组结果
COMICS_DATA_PICKLE = CACHE_FOLDER + '/comics_data.pickle'  # 所有漫画数据（自定义类，包含漫画各种基础信息）
CURRENT_COMICS_DATA_PICKLE = CACHE_FOLDER + '/current_comics_data.pickle'  # 当前任务的漫画数据
TEMP_IMAGE_FOLDER = CACHE_FOLDER + '/temp_image_folder'  # 解压后图片存放路径
EXTRACT_TEMP_IMAGE_FOLDER = TEMP_IMAGE_FOLDER + '/extract_archive'  # 临时解压路径
COMIC_FOLDERS = CACHE_FOLDER + '/comic_folders.pickle'  # 当前任务找到的漫画文件夹
ARCHIVES = CACHE_FOLDER + '/archives.pickle'  # 当前任务找到的压缩包
IMAGE_DATA_DICT = CACHE_FOLDER + '/image_data_dict.pickle'  # 图片对应漫画路径

# 配置文件相关
CONFIG_FILE = 'config.ini'

# 其他
MAX_EXTRACT_IMAGE_NUMBER = 3
RESIZE_IMAGE_ACCURACY = 16
RESIZE_IMAGE_HEIGHT = 300
