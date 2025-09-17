from PySide6.QtCore import QObject

from components import widget_exec, widget_setting_algorithm, widget_setting_match, widget_setting_comic, \
    widget_search_list, widget_runtime_info, widget_similar_result_filter, widget_assembler_similar_result_preview
from components.window.window_model import WindowModel
from components.window.window_viewer import WindowViewer
from thread.thread_analyse_comic_info import ThreadAnalyseComicInfo
from thread.thread_analyse_image_info import ThreadAnalyseImageInfo
from thread.thread_compare_hash import ThreadCompareHash
from thread.thread_compare_ssim import ThreadCompareSSIM
from thread.thread_search_comic import ThreadSearchComic


class WindowPresenter(QObject):
    """主窗口的桥梁组件"""

    def __init__(self, viewer: WindowViewer, model: WindowModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        # 实例化控件
        self.widget_exec = widget_exec.get_presenter()
        self.widget_setting_algorithm = widget_setting_algorithm.get_presenter()
        self.widget_setting_match = widget_setting_match.get_presenter()
        self.widget_setting_comic = widget_setting_comic.get_presenter()
        self.widget_search_list = widget_search_list.get_presenter()
        self.widget_runtime_info = widget_runtime_info.get_presenter()
        self.widget_similar_result_filter = widget_similar_result_filter.get_presenter()
        self.similar_result_preview = widget_assembler_similar_result_preview.get_presenter()

        # 实例化子线程
        self.thread_search_comic = ThreadSearchComic()
        self.thread_analyse_comic_info = ThreadAnalyseComicInfo()
        self.thread_analyse_image_info = ThreadAnalyseImageInfo()
        self.thread_compare_hash = ThreadCompareHash()
        self.thread_compare_ssim = ThreadCompareSSIM()

        # 初始化viewer
        self._init_viewer()

        # 绑定控件信号
        self._bind_signal()

    def start(self):
        """执行查重"""
        # 获取设置选项
        # 备忘录
        # 获取需要检索的路径
        # 备忘录
        # 传参给子线程
        # 备忘录
        self.widget_exec.Start.emit()

    def set_thread_setting(self):
        """将设置选项传参给子线程"""
        # 基础hash算法
        hash_algorithm = self.widget_setting_algorithm.get_base_algorithm()
        self.thread_analyse_image_info.set_hash_type(hash_algorithm)
        # 是否使用增强算法
        is_enhance_algorithm = self.widget_setting_algorithm.get_is_enhance_algorithm()
        # 增强hash算法
        enhance_algorithm = self.widget_setting_algorithm.get_enhance_algorithm()
        # 相似度阈值
        similar_threshold = self.widget_setting_algorithm.get_similar_threshold()
        self.thread_compare_ssim.set_threshold(similar_threshold)
        # 汉明距离阈值
        hamming_distance = self.widget_setting_algorithm.get_hamming_distance()
        self.thread_compare_hash.set_hamming_distance(hamming_distance)
        # hash长度
        hash_length = self.widget_setting_algorithm.get_hash_length()
        self.thread_analyse_image_info.set_hash_length(hash_algorithm)

        # 每本漫画提取的页数
        extract_pages = self.widget_setting_match.get_extract_pages()
        # 是否匹配缓存
        is_match_cache = self.widget_setting_match.get_is_match_cache()
        # 是否仅匹配相似文件名
        is_match_similar_filename = self.widget_setting_match.get_is_match_similar_filename()
        # 线程数
        thread_count = self.widget_setting_match.get_thread_count()

        # 漫画页数下限
        pages_lower_limit = self.widget_setting_comic.get_pages_lower_limit()
        self.thread_search_comic.set_pages_lower_limit(pages_lower_limit)
        # 是否识别压缩文件
        is_analyze_archive = self.widget_setting_comic.get_is_analyze_archive()
        self.thread_search_comic.set_is_check_archive(is_analyze_archive)
        # 是否允许其他文件类型
        is_allow_other_filetypes = self.widget_setting_comic.get_is_allow_other_filetypes()
        self.thread_search_comic.set_is_allow_other_filetypes(is_allow_other_filetypes)

    def _init_viewer(self):
        """设置viewer"""
        self.viewer.add_viewer_exec(self.widget_exec.viewer)
        self.viewer.add_viewer_setting_1(self.widget_setting_algorithm.viewer)
        self.viewer.add_viewer_setting_2(self.widget_setting_match.viewer)
        self.viewer.add_viewer_setting_3(self.widget_setting_comic.viewer)
        self.viewer.add_viewer_search_list(self.widget_search_list.viewer)
        self.viewer.add_viewer_runtime_info(self.widget_runtime_info.viewer)
        self.viewer.add_viewer_result_filter(self.widget_similar_result_filter.viewer)
        self.viewer.add_viewer_result_preview(self.similar_result_preview.viewer)

    def _bind_signal(self):
        """绑定信号"""
        self.widget_exec.Start.connect(self.start)
        self.widget_exec.Stop.connect()
        self.widget_exec.LoadLastResult.connect()
        self.widget_exec.OpenAbout.connect()
