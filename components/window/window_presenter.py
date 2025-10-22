# 主窗口
"""
子线程运行顺序：
1.主程序读取需要检索的目录，传递给 子线程-搜索漫画
2.子线程-搜索漫画 执行后得到一个漫画路径列表，将该列表传递给 子线程-分析漫画信息
3.子线程-分析漫画信息 执行后得到一个漫画信息类列表，将其保存到本地数据库中
4.分析得到的漫画信息类列表，提取其中每本漫画的N张图片路径，传递给 子线程-分析图片信息
5.子线程-分析图片信息 执行后得到一个图片信息类列表，将其保存到本地数据库中
6.分析得到的图片信息类列表，提取其中的图片hash值，传递给 子线程-对比图片hash值
7.子线程-对比图片hash值 执行后得到一个漫画相似组列表，该列表为初步筛选结果
8.如果需要使用增强算法，则将得到的漫画相似组列表传递给对应的子线程并执行，得到一个经过二次筛选的漫画相似组列表
9.提取该漫画相似组列表，并显示在UI中
"""
from typing import List

from PySide6.QtCore import QObject, Signal

from common.class_comic import ComicInfoBase
from common.class_config import SimilarAlgorithm
from common.class_image import ImageInfoBase
from common.class_runtime import TYPE_RUNTIME_INFO, TypeRuntimeInfo
from components import widget_exec, widget_setting_algorithm, widget_setting_match, widget_setting_comic, \
    widget_search_list, widget_runtime_info, widget_similar_result_filter, widget_assembler_similar_result_preview, \
    dialog_match_result_cache, widget_cache_manager
from components.window.window_model import WindowModel
from components.window.window_viewer import WindowViewer
from thread.thread_analyse_comic_info import ThreadAnalyseComicInfo
from thread.thread_analyse_image_info import ThreadAnalyseImageInfo
from thread.thread_compare_hash import ThreadCompareHash
from thread.thread_compare_ssim import ThreadCompareSSIM
from thread.thread_convert_hash_to_comic_info import ThreadConvertHashToComicInfo
from thread.thread_save_comic import ThreadSaveComic
from thread.thread_save_image import ThreadSaveImage
from thread.thread_search_comic import ThreadSearchComic


class WindowPresenter(QObject):
    """主窗口的桥梁组件"""
    SignalRuntimeInfo = Signal(object, str, name='运行信息')

    def __init__(self, viewer: WindowViewer, model: WindowModel):
        super().__init__()
        self.viewer = viewer
        self.model = model

        self.is_stop = False  # 是否停止
        self._comic_paths_search = []  # 检索漫画列表

        # 实例化控件
        self.widget_exec = widget_exec.get_presenter()
        self.widget_setting_algorithm = widget_setting_algorithm.get_presenter()
        self.widget_setting_match = widget_setting_match.get_presenter()
        self.widget_setting_comic = widget_setting_comic.get_presenter()
        self.widget_search_list = widget_search_list.get_presenter()
        self.widget_runtime_info = widget_runtime_info.get_presenter()
        self.widget_similar_result_filter = widget_similar_result_filter.get_presenter()
        self.assembler_similar_result_preview = widget_assembler_similar_result_preview.get_assembler()
        self.similar_result_preview = self.assembler_similar_result_preview.get_presenter()
        self.presenter_match_result_cache = dialog_match_result_cache.get_presenter()
        self.dialog_match_result_cache = self.presenter_match_result_cache.get_viewer()
        self.widget_cache_manager = widget_cache_manager.get_presenter()

        # 实例化子线程
        self.thread_search_comic = ThreadSearchComic()
        self.thread_analyse_comic_info = ThreadAnalyseComicInfo()
        self.thread_analyse_image_info = ThreadAnalyseImageInfo()
        self.thread_compare_hash = ThreadCompareHash()
        self.thread_compare_ssim = ThreadCompareSSIM()
        self.thread_save_comic = ThreadSaveComic()
        self.thread_save_image = ThreadSaveImage()
        self.thread_convert_hash_to_comic_info = ThreadConvertHashToComicInfo()

        # 将设置项传递给子线程
        self._set_thread_setting()
        self.thread_save_comic.set_db_comic_info(self.model.get_comic_db())
        self.thread_save_comic.set_db_image_info(self.model.get_image_db())
        self.thread_save_image.set_db_image_info(self.model.get_image_db())
        self.thread_convert_hash_to_comic_info.set_db_comic_info(self.model.get_comic_db())
        self.thread_convert_hash_to_comic_info.set_db_image_info(self.model.get_image_db())

        # 初始化viewer
        self._init_viewer()

        # 初始化子控件
        self._init_widget()

        # 更新缓存统计信息
        self._update_cache_info()

        # 绑定控件信号
        self._bind_signal()
        # 绑定子线程信号
        self._bind_thread_signal()
        # 绑定model信号
        self.model.SignalRuntimeInfo.connect(self.update_runtime_info_textline)

    def open_dialog_match_result_cache(self):
        """打开历史记录dialog"""
        self.dialog_match_result_cache.exec()

    def load_last_result(self, match_result: List[List[ComicInfoBase]]):
        """加载匹配结果"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '正在加载历史匹配结果')
        self.show_similar_result(match_result)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '完成加载历史匹配结果')

    def open_about(self):
        """打开程序说明"""
        pass  # 备忘录

    def start(self):
        """执行查重"""
        # 开始计时
        self.widget_runtime_info.start_time()
        self.widget_runtime_info.update_step_count(4)

        # 获取需要检索的路径
        search_paths = self.widget_search_list.get_paths()
        if not search_paths:
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '未选择需要检索的目录')
            self.widget_runtime_info.stop_time()
            return

        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '执行查找重复项')

        # 切换到运行信息页
        self.viewer.turn_page_running_info()

        # 将设置项重新传递给子线程
        self._set_thread_setting()

        # 传参给子线程，并启动
        self.is_stop = False
        self.start_search_comic(search_paths)

    def stop(self):
        """停止查重"""
        self.is_stop = True
        self.widget_runtime_info.stop_time()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '停止查找重复项')
        self.thread_search_comic.set_stop()
        self.thread_analyse_comic_info.set_stop()
        self.thread_analyse_image_info.set_stop()
        self.thread_compare_hash.set_stop()
        self.thread_compare_ssim.set_stop()

    """子线程方法"""

    def start_search_comic(self, search_paths: list):
        """启动子线程-搜索漫画"""
        if not self.is_stop:
            self.thread_search_comic.set_search_list(search_paths)
            self.thread_search_comic.start()
        else:
            self.widget_runtime_info.stop_time()

    def thread_search_comic_finished(self):
        """子线程-搜索漫画执行完毕"""
        if not self.is_stop:
            # 提取漫画路径列表
            comics_path = self.thread_search_comic.get_comics_path()
            if not comics_path:
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '未找到任何漫画')
                self.widget_runtime_info.stop_time()
                return
            self._comic_paths_search = comics_path  # 赋值给变量，用于后续使用
            # 传递给 子线程-分析漫画信息
            self.start_thread_analyse_comic_info(comics_path)
        else:
            self.widget_runtime_info.stop_time()

    def start_thread_analyse_comic_info(self, comics_path: list):
        """启动子线程-分析漫画信息"""
        if not self.is_stop:
            self.thread_analyse_comic_info.set_comics(comics_path)
            self.thread_analyse_comic_info.start()
        else:
            self.widget_runtime_info.stop_time()

    def thread_analyse_comic_info_finished(self):
        """子线程-分析漫画信息执行完毕"""
        if not self.is_stop:
            # 提取漫画信息类字典
            comic_info_dict = self.thread_analyse_comic_info.get_comic_info_dict()
            comic_info_list = list(comic_info_dict.values())
            if not comic_info_list:
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '未找到任何漫画')
                self.widget_runtime_info.stop_time()
                return
            # 保存到本地数据库中
            self.start_save_comic_info(comic_info_list)
        else:
            self.widget_runtime_info.stop_time()

    def start_save_comic_info(self, comic_info_list: List[ComicInfoBase]):
        """启动子线程-保存漫画信息到数据库"""
        if not self.is_stop:
            self.thread_save_comic.set_comic_info_list(comic_info_list)
            self.thread_save_comic.start()
        else:
            self.widget_runtime_info.stop_time()

    def thread_save_comic_info_finished(self):
        """子线程-保存漫画信息到数据库执行完毕"""
        if not self.is_stop:
            comic_info_list = self.thread_save_comic.get_comic_info_list()
            self.start_analyse_image_info(comic_info_list)
        else:
            self.widget_runtime_info.stop_time()

    def start_analyse_image_info(self, comic_info_list: list):
        """启动子线程-分析图片信息"""
        if not self.is_stop:
            self.thread_analyse_image_info.set_comic_info_list(comic_info_list)
            self.thread_analyse_image_info.start()
        else:
            self.widget_runtime_info.stop_time()

    def thread_analyse_image_info_finished(self):
        """子线程-分析图片信息执行完毕"""
        if not self.is_stop:
            # 提取图片信息字典
            image_info_dict = self.thread_analyse_image_info.get_image_info_dict()
            if not image_info_dict:
                self.widget_runtime_info.stop_time()
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '未找到任何图片')
                return
            # 保存到本地数据库中
            self.start_save_image_info(image_info_dict.values())
        else:
            self.widget_runtime_info.stop_time()

    def start_save_image_info(self, image_info_list: List[ImageInfoBase]):
        """启动子线程-保存图片信息到数据库"""
        if not self.is_stop:
            self.thread_save_image.set_image_info_list(image_info_list)
            self.thread_save_image.start()
        else:
            self.widget_runtime_info.stop_time()

    def thread_save_image_info_finished(self):
        """子线程-保存图片信息到数据库执行完毕"""
        if not self.is_stop:
            image_info_list = self.thread_save_image.get_image_info_list()
            # 提取图片信息中的hash值
            hash_algorithm = self.widget_setting_algorithm.get_base_algorithm()  # hash算法
            hash_length = self.widget_setting_algorithm.get_hash_length()  # hash长度
            # 检查匹配选项-是否匹配缓存数据
            is_match_cache = self.widget_setting_match.get_is_match_cache()
            if is_match_cache:  # 如果选中了匹配缓存数据，则从漫画信息数据库中提取出所有的项目并以此进行相似匹配（不会计算缺失的hash值）
                hash_list = self.model.get_hashs(hash_algorithm, hash_length)
            else:  # 否则仅匹配本次提取到的图片信息
                hash_list = self.model.get_hash_list_from_image_infos(image_info_list, hash_algorithm, hash_length)
            # 将提取的hash值列表传递给 子线程-对比图片hash
            self.start_thread_compare_hash(hash_list)
        else:
            self.widget_runtime_info.stop_time()

    def start_thread_compare_hash(self, hash_list: list):
        """启动子线程-对比图片hash"""
        if not self.is_stop:
            self.thread_compare_hash.set_hash_list(hash_list)
            self.thread_compare_hash.start()
        else:
            self.widget_runtime_info.stop_time()

    def thread_compare_hash_finished(self):
        """子线程-对比图片hash执行完毕"""
        if not self.is_stop:
            # 提取相似hash组列表
            similar_hash_groups = self.thread_compare_hash.get_similar_hash_group()
            if not similar_hash_groups:
                self.widget_runtime_info.stop_time()
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '未找到任何相似图片')
                return
            # 将hash列表转换为对应的漫画信息类列表
            self.start_convert_hash_to_comic_info(similar_hash_groups)
        else:
            self.widget_runtime_info.stop_time()

    def start_convert_hash_to_comic_info(self, similar_hash_groups: list[list[str]]):
        """启动子线程-转换hash值为漫画信息类"""
        if not self.is_stop:
            hash_type = self.widget_setting_algorithm.get_base_algorithm()  # 提取的hash类型
            self.thread_convert_hash_to_comic_info.set_hash_group(similar_hash_groups)
            self.thread_convert_hash_to_comic_info.set_hash_type(hash_type)
            self.thread_convert_hash_to_comic_info.start()
        else:
            self.widget_runtime_info.stop_time()

    def thread_convert_hash_to_comic_info_finished(self):
        """子线程-转换hash值为漫画信息类执行完毕"""
        if not self.is_stop:
            # 对转换的漫画信息类列表进行处理
            comic_info_groups = self.thread_convert_hash_to_comic_info.get_comic_info_group()
            # 检查漫画是否存在，剔除已经不存在的项目
            comic_info_groups_filter = self.model.filter_comic_info_group_is_exist(comic_info_groups)
            # 检查匹配选项-是否匹配缓存数据
            is_match_cache = self.widget_setting_match.get_is_match_cache()
            if not is_match_cache:  # 如果未选择匹配缓存数据，则剔除相似组中不在本次搜索目录中的漫画项目（由于hash转换是根据数据库数据，可能存在多余的路径）
                comic_info_groups_filter = self.model.filter_comic_info_group_is_in_search_list(comic_info_groups,
                                                                                                comic_path_search_list=self._comic_paths_search)
            # 保存到缓存
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '正在保存相似匹配结果到本地缓存')
            self.presenter_match_result_cache.save_match_result(comic_info_groups_filter)
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '完成保存相似匹配结果到本地缓存')
            # 更新缓存统计信息
            self._update_cache_info()
            # 显示匹配结果
            self.show_similar_result(comic_info_groups_filter)

            # 检查设置项，是否需要使用增强算法
            is_enhance_algorithm = self.widget_setting_algorithm.get_is_enhance_algorithm()
            enhance_algorithm = self.widget_setting_algorithm.get_enhance_algorithm()
            if is_enhance_algorithm:
                if isinstance(enhance_algorithm, SimilarAlgorithm.SSIM):
                    pass  # 备忘录
                elif isinstance(enhance_algorithm, SimilarAlgorithm.ORB):
                    pass  # 备忘录

        else:
            self.widget_runtime_info.stop_time()

    def start_thread_compare_ssim(self, image_group: list):
        """启动子线程-对比图片ssim"""
        if not self.is_stop:
            self.thread_compare_ssim.set_image_group(image_group)
            self.thread_compare_ssim.start()
        else:
            self.widget_runtime_info.stop_time()

    def show_similar_result(self, comic_info_groups: List[List[ComicInfoBase]]):
        """显示相似匹配结果"""
        if not self.is_stop:
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '显示相似匹配结果')
            self.assembler_similar_result_preview.clear()
            self.assembler_similar_result_preview.set_groups(comic_info_groups)
            self.assembler_similar_result_preview.show_similar_result()
            self.viewer.turn_page_match_result()

        self.widget_runtime_info.stop_time()

    """缓存内部匹配方法"""

    def self_match_comic_db(self):
        """漫画数据库项目自我匹配"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始漫画数据库内部匹配')
        # 手动勾选匹配选项-匹配缓存数据
        self.widget_setting_match.set_is_match_cache(True)
        # 提取图片信息中的hash值
        hash_algorithm = self.widget_setting_algorithm.get_base_algorithm()  # hash算法
        hash_length = self.widget_setting_algorithm.get_hash_length()  # hash长度
        hash_list = self.model.get_hashs(hash_algorithm, hash_length)
        # 启动子线程-对比图片hash
        self.start_thread_compare_hash(hash_list)

    """运行信息方法"""

    def update_runtime_info_index(self, index: int):
        """更新运行信息-步骤索引"""
        self.widget_runtime_info.update_step_index(index)

    def update_runtime_info_title(self, title: str):
        """更新运行信息-步骤标题"""
        self.widget_runtime_info.update_step_title(title)

    def update_runtime_info_rate(self, rate: str):
        """更新运行信息-步骤内部进度"""
        self.widget_runtime_info.update_progress_current(rate)

    def update_runtime_info_textline(self, info_type: TYPE_RUNTIME_INFO, text_info: str):
        """更新运行信息-文本行信息"""
        self.widget_runtime_info.update_textline(info_type, text_info)

    def order_similar_result(self):
        """排序相似匹配结果"""
        order_key = self.widget_similar_result_filter.get_order_key()
        order_direction = self.widget_similar_result_filter.get_order_direction()
        self.assembler_similar_result_preview.sort_groups_item(order_key, order_direction)

    def _set_thread_setting(self):
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
        self.thread_analyse_image_info.set_hash_length(hash_length)

        # 每本漫画提取的页数
        extract_pages = self.widget_setting_match.get_extract_pages()
        self.thread_analyse_image_info.set_extract_pages(extract_pages)
        # 是否匹配缓存
        is_match_cache = self.widget_setting_match.get_is_match_cache()
        # 是否仅匹配相似文件名
        is_match_similar_filename = self.widget_setting_match.get_is_match_similar_filename()
        # 线程数
        thread_count = self.widget_setting_match.get_thread_count()
        self.thread_analyse_comic_info.set_max_workers(thread_count)
        self.thread_analyse_image_info.set_max_workers(thread_count)
        self.thread_compare_hash.set_max_workers(thread_count)
        self.thread_compare_ssim.set_max_workers(thread_count)
        self.thread_search_comic.set_max_workers(thread_count)

        # 漫画页数下限
        pages_lower_limit = self.widget_setting_comic.get_pages_lower_limit()
        self.thread_search_comic.set_pages_lower_limit(pages_lower_limit)
        # 是否识别压缩文件
        is_analyze_archive = self.widget_setting_comic.get_is_analyze_archive()
        self.thread_search_comic.set_is_check_archive(is_analyze_archive)
        # 是否允许其他文件类型
        is_allow_other_filetypes = self.widget_setting_comic.get_is_allow_other_filetypes()
        self.thread_search_comic.set_is_allow_other_filetypes(is_allow_other_filetypes)

    def _update_cache_info(self):
        """更新缓存统计信息"""
        comic_count_info = self.model.get_comic_db_count_info()
        image_count_info = self.model.get_image_db_count_info()
        preview_image_info = self.model.get_preview_image_count_info()

        self.widget_cache_manager.set_comic_cache_count_info(comic_count_info)
        self.widget_cache_manager.set_image_cache_count_info(image_count_info)
        self.widget_cache_manager.set_preview_cache_count_info(preview_image_info)

    def _save_size(self):
        """保存窗口大小"""
        width = self.viewer.width()
        height = self.viewer.height()
        self.model.set_window_size_db(width, height)

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
        self.viewer.add_viewer_cache_manager(self.widget_cache_manager.viewer)

        # 读取配置文件中的窗口尺寸
        width, height = self.model.get_window_size_db()
        self.viewer.resize(width, height)

    def _init_widget(self):
        """初始化子控件"""
        self.widget_cache_manager.set_comic_db(self.model.db_comic_info)
        self.widget_cache_manager.set_image_db(self.model.db_image_info)

    def _bind_signal(self):
        """绑定信号"""
        self.viewer.Resized.connect(self._save_size)

        self.widget_exec.Start.connect(self.start)
        self.widget_exec.Stop.connect(self.stop)
        self.widget_exec.LoadLastResult.connect(self.open_dialog_match_result_cache)
        self.widget_exec.OpenAbout.connect(self.open_about)

        self.SignalRuntimeInfo.connect(self.update_runtime_info_textline)

        self.presenter_match_result_cache.Restore.connect(self.load_last_result)

        self.widget_similar_result_filter.ReconfirmDelete.connect(
            self.assembler_similar_result_preview.set_is_reconfirm_before_delete)
        self.widget_similar_result_filter.RefreshResult.connect(self.assembler_similar_result_preview.reload)
        self.widget_similar_result_filter.ChangeSortKey.connect(self.order_similar_result)
        self.widget_similar_result_filter.ChangeSortDirection.connect(self.order_similar_result)

        self.widget_cache_manager.MatchCache.connect(self.self_match_comic_db)

    def _bind_thread_signal(self):
        """绑定子线程信号"""
        # self.thread_search_comic.SignalStart.connect()
        self.thread_search_comic.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_search_comic.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_search_comic.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_search_comic.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        self.thread_search_comic.SignalFinished.connect(self.thread_search_comic_finished)
        # self.thread_search_comic.SignalStopped.connect()

        # self.thread_analyse_comic_info.SignalStart.connect()
        self.thread_analyse_comic_info.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_analyse_comic_info.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_analyse_comic_info.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_analyse_comic_info.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        self.thread_analyse_comic_info.SignalFinished.connect(self.thread_analyse_comic_info_finished)
        # self.thread_analyse_comic_info.SignalStopped.connect()

        # self.thread_analyse_image_info.SignalStart.connect()
        self.thread_analyse_image_info.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_analyse_image_info.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_analyse_image_info.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_analyse_image_info.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        self.thread_analyse_image_info.SignalFinished.connect(self.thread_analyse_image_info_finished)
        # self.thread_analyse_image_info.SignalStopped.connect()

        # self.thread_compare_hash.SignalStart.connect()
        self.thread_compare_hash.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_compare_hash.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_compare_hash.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_compare_hash.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        self.thread_compare_hash.SignalFinished.connect(self.thread_compare_hash_finished)
        # self.thread_compare_hash.SignalStopped.connect()

        # self.thread_compare_ssim.SignalStart.connect()
        self.thread_compare_ssim.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_compare_ssim.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_compare_ssim.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_compare_ssim.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        # self.thread_compare_ssim.SignalFinished.connect()
        # self.thread_compare_ssim.SignalStopped.connect()

        # self.thread_save_comic.SignalStart.connect()
        self.thread_save_comic.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_save_comic.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_save_comic.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_save_comic.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        self.thread_save_comic.SignalFinished.connect(self.thread_save_comic_info_finished)
        # self.thread_save_comic.SignalStopped.connect()

        # self.thread_save_image.SignalStart.connect()
        self.thread_save_image.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_save_image.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_save_image.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_save_image.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        self.thread_save_image.SignalFinished.connect(self.thread_save_image_info_finished)
        # self.thread_save_image.SignalStopped.connect()

        # self.thread_convert_hash_to_comic_info.SignalStart.connect()
        self.thread_convert_hash_to_comic_info.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_convert_hash_to_comic_info.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_convert_hash_to_comic_info.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_convert_hash_to_comic_info.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        self.thread_convert_hash_to_comic_info.SignalFinished.connect(self.thread_convert_hash_to_comic_info_finished)
        # self.thread_convert_hash_to_comic_info.SignalStopped.connect()
