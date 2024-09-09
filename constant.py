# 常量

# 配置文件路径
_CONFIG_FILE = r'config.ini'

# 缓存路径
_CACHE_DIRPATH = 'cache/'
_PREVIEW_DIRPATH = _CACHE_DIRPATH + 'preview/'  # 存放预览图的文件夹
_COMICS_INFO_DB = _CACHE_DIRPATH + 'comic_info.pkl'  # 漫画信息数据库
_IMAGE_INFO_DB = _CACHE_DIRPATH + 'image_info.db'  # 图片信息数据库
_MATCH_RESULT = _CACHE_DIRPATH + 'match_result.pkl'  # 相似漫画匹配结果

# 图标
_ICON_DIRPATH = r'res/icon/'
# 程序图标
_ICON_APP = _ICON_DIRPATH + 'app.ico'
# 执行区
_ICON_INFORMATION = _ICON_DIRPATH + 'information.png'
_ICON_RELOAD = _ICON_DIRPATH + 'reload.png'
_ICON_START = _ICON_DIRPATH + 'start.png'
_ICON_STOP = _ICON_DIRPATH + 'stop.png'
# 结果筛选器
_ICON_REFRESH = _ICON_DIRPATH + 'refresh.png'
# 算法选项
_ICON_CACHE = _ICON_DIRPATH + 'cache.png'
# 搜索列表
_ICON_ADD = _ICON_DIRPATH + 'add.png'
_ICON_REMOVE = _ICON_DIRPATH + 'remove.png'
_ICON_CLEAR = _ICON_DIRPATH + 'clear.png'
_ICON_DELETE = _ICON_DIRPATH + 'delete.png'
# 预览控件
_ICON_COMPUTER = _ICON_DIRPATH + 'computer.png'
_ICON_RECYCLE_BIN = _ICON_DIRPATH + 'recycle_bin.png'
_ICON_VIEW = _ICON_DIRPATH + 'view.png'
_ICON_ARCHIVE = _ICON_DIRPATH + 'archive.png'
_ICON_FOLDER = _ICON_DIRPATH + 'folder.png'
_ICON_ERROR_IMAGE = _ICON_DIRPATH + 'error_image.png'
_ICON_LAST = _ICON_DIRPATH + 'last.png'
_ICON_LAST_LAST = _ICON_DIRPATH + 'last_last.png'
_ICON_NEXT = _ICON_DIRPATH + 'next.png'
_ICON_NEXT_NEXT = _ICON_DIRPATH + 'next_next.png'
_ICON_QUIT = _ICON_DIRPATH + 'quit.png'

# 相似算法默认参数
_SIMILARITY_THRESHOLD = 90
_HASH_ALGORITHM = ['ahash', 'phash', 'dhash']
_IMAGE_SIZE = ['8', '12', '16']
_EXTRACT_IMAGES_COUNT = 1
_THREADS_COUNT = 1
