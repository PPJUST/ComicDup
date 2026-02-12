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
import os.path
from typing import List

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

from common.class_comic import ComicInfoBase
from common.class_image import ImageInfoBase
from common.class_runtime import TYPE_RUNTIME_INFO, TypeRuntimeInfo
from components import widget_exec, widget_setting_algorithm, widget_setting_match, widget_setting_comic, \
    widget_search_list, widget_runtime_info, widget_similar_result_filter, widget_assembler_similar_result_preview, \
    dialog_match_result_cache, widget_cache_manager
from components.window.window_model import WindowModel
from components.window.window_viewer import WindowViewer
from thread.thread_analyse_comic_info import ThreadAnalyseComicInfo
from thread.thread_analyse_image_info import ThreadAnalyseImageInfo
from thread.thread_compare_comic import ThreadCompareComic
from thread.thread_refresh_comic_db import ThreadRefreshComicDB
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
        self.thread_compare_comic = ThreadCompareComic()
        self.thread_save_comic = ThreadSaveComic()
        self.thread_save_image = ThreadSaveImage()
        self.thread_refresh_comic_db = ThreadRefreshComicDB()

        # 将设置项传递给子线程
        self._set_thread_setting()
        self.thread_save_comic.set_db_comic_info(self.model.get_comic_db())
        self.thread_save_comic.set_db_image_info(self.model.get_image_db())
        self.thread_save_image.set_db_image_info(self.model.get_image_db())

        # 初始化viewer
        self._init_viewer()

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
        # 由于历史记录中可能存在已经被删除的项目，所以需要进行一次存在校验
        match_result_filter = []
        for group in match_result:
            group_filter = []
            for comic_info in group:
                comic_path = comic_info.filepath
                if os.path.exists(comic_path):
                    group_filter.append(comic_info)
            match_result_filter.append(group_filter)
        self.show_similar_result(match_result_filter)
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '完成加载历史匹配结果')

    def open_about(self):
        """打开程序说明"""
        pass  # todo
        QMessageBox.information(self.viewer, "提示", "编写中...")

    def start(self):
        """执行查重"""
        # 开始计时
        self.widget_runtime_info.start_time()
        self.widget_runtime_info.update_step_count(4)

        # 禁用相关设置选项
        self._set_options_state(False)

        # 获取需要检索的路径
        search_paths = self.widget_search_list.get_paths()
        if not search_paths:
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '未选择需要检索的目录')
            self.stop()
            return

        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '执行查找重复项')

        # 切换到运行信息页
        self.viewer.turn_page_running_info()

        # 将设置项重新传递给子线程
        self._set_thread_setting()

        # 子线程启动
        self.is_stop = False
        self.start_search_comic()

    def stop(self):
        """停止查重"""
        self.is_stop = True
        self._set_options_state(True)
        self.widget_runtime_info.stop_time()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '当前匹配任务已结束')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '-' * 200)
        self.thread_search_comic.set_stop()
        self.thread_analyse_comic_info.set_stop()
        self.thread_analyse_image_info.set_stop()
        self.thread_compare_comic.set_stop()

    """子线程方法"""

    def start_search_comic(self):
        """启动子线程-搜索漫画"""
        print('启动子线程-搜索漫画')
        if not self.is_stop:
            self.thread_search_comic.start()
        else:
            self.stop()

    def thread_search_comic_finished(self):
        """子线程-搜索漫画执行完毕"""
        print('子线程-搜索漫画执行完毕')
        if not self.is_stop:
            # 提取漫画路径列表
            comics_path = self.thread_search_comic.get_comics_path()
            print('提取到的漫画数量', len(comics_path))
            if not comics_path:
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '未找到任何漫画')
                self.stop()
                return
            self._comic_paths_search = comics_path  # 赋值给变量，用于后续使用
            # 传递给 子线程-分析漫画信息
            self.start_thread_analyse_comic_info(comics_path)
        else:
            self.stop()

    def start_thread_analyse_comic_info(self, comics_path: list):
        """启动子线程-分析漫画信息"""
        print('启动子线程-分析漫画信息')
        if not self.is_stop:
            self.thread_analyse_comic_info.set_comics(comics_path)
            self.thread_analyse_comic_info.start()
        else:
            self.stop()

    def thread_analyse_comic_info_finished(self):
        """子线程-分析漫画信息执行完毕"""
        print('子线程-分析漫画信息执行完毕')
        if not self.is_stop:
            # 提取漫画信息类字典
            comic_info_dict = self.thread_analyse_comic_info.get_comic_info_dict()
            comic_info_list = list(comic_info_dict.values())
            print('分析完毕的漫画数量', len(comic_info_list))
            if not comic_info_list:
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '未找到任何漫画')
                self.stop()
                return
            # 保存到本地数据库中
            self.start_save_comic_info(comic_info_list)
        else:
            self.stop()

    def start_save_comic_info(self, comic_info_list: List[ComicInfoBase]):
        """启动子线程-保存漫画信息到数据库"""
        print('启动子线程-保存漫画信息到数据库')
        if not self.is_stop:
            self.thread_save_comic.set_comic_info_list(comic_info_list)
            self.thread_save_comic.start()
        else:
            self.stop()

    def thread_save_comic_info_finished(self):
        """子线程-保存漫画信息到数据库执行完毕"""
        print('子线程-保存漫画信息到数据库执行完毕')
        if not self.is_stop:
            comic_info_list = self.thread_save_comic.get_comic_info_list()
            self.start_analyse_image_info(comic_info_list)
        else:
            self.stop()

    def start_analyse_image_info(self, comic_info_list: list):
        """启动子线程-分析图片信息"""
        print('启动子线程-分析图片信息')
        print('需分析图片的漫画数量', len(comic_info_list))
        if not self.is_stop:
            self.thread_analyse_image_info.set_comic_info_list(comic_info_list)
            self.thread_analyse_image_info.start()
        else:
            self.stop()

    def thread_analyse_image_info_finished(self):
        """子线程-分析图片信息执行完毕"""
        print('子线程-分析图片信息执行完毕')
        if not self.is_stop:
            # 提取图片信息字典
            image_info_dict = self.thread_analyse_image_info.get_image_info_dict()
            print('分析完成的图片数量', len(image_info_dict))
            if not image_info_dict:
                self.stop()
                self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, '未找到任何图片')
                return
            # 保存到本地数据库中
            self.start_save_image_info(image_info_dict.values())
        else:
            self.stop()

    def start_save_image_info(self, image_info_list: List[ImageInfoBase]):
        """启动子线程-保存图片信息到数据库"""
        print('启动子线程-保存图片信息到数据库')
        if not self.is_stop:
            self.thread_save_image.set_image_info_list(image_info_list)
            self.thread_save_image.start()
        else:
            self.stop()

    def thread_save_image_info_finished(self):
        """子线程-保存图片信息到数据库执行完毕"""
        print('子线程-保存图片信息到数据库执行完毕')
        if not self.is_stop:
            # 提取漫画信息类列表
            comic_info_dict = self.thread_analyse_comic_info.get_comic_info_dict()
            comic_info_list = list(comic_info_dict.values())
            # 将提取的漫画信息类列表传递给子线程
            self.start_thread_compare_comic(comic_info_list)
        else:
            self.stop()

    def start_thread_compare_comic(self, comic_info_list: list[ComicInfoBase]):
        """启动子线程-对比漫画信息"""
        print('启动子线程-对比漫画信息')
        if not self.is_stop:
            # 传递参数
            is_match_cache = self.widget_setting_match.get_is_match_cache()  # 是否匹配缓存
            if is_match_cache:
                cache_comic_info_list = self.model.get_comic_infos()  # 缓存中的漫画信息类列表
                self.thread_compare_comic.set_cache_comic_info_list(cache_comic_info_list)
            image_hash_dict = self.model.get_hashs_all_type()  # 哈希值字典，键为虚拟图片路径，值为3种图片hash*3种长度的字典
            self.thread_compare_comic.set_image_hash_dict(image_hash_dict)

            self.thread_compare_comic.set_comic_info_list(comic_info_list)
            self.thread_compare_comic.start()
        else:
            self.stop()

    def thread_compare_comic_finished(self):
        """子线程-对比漫画信息执行完毕"""
        print('子线程-对比漫画信息执行完毕')
        if not self.is_stop:
            similar_groups = self.thread_compare_comic.get_similar_groups()
            # 生成组中漫画的预览图并保存到数据库中
            self.model.save_comic_preview(similar_groups)
            # 保存相似匹配结果到本地缓存
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '正在保存相似匹配结果到本地缓存')
            self.presenter_match_result_cache.save_match_result(similar_groups)
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, '完成保存相似匹配结果到本地缓存')
            # 更新缓存统计信息
            self._update_cache_info()
            # 显示匹配结果
            self.show_similar_result(similar_groups)
        else:
            self.stop()

    def show_similar_result(self, comic_info_groups: List[List[ComicInfoBase]]):
        """显示相似匹配结果"""
        if not self.is_stop:
            self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '显示相似匹配结果')
            self.assembler_similar_result_preview.clear()
            self.assembler_similar_result_preview.set_groups(comic_info_groups)
            self.assembler_similar_result_preview.show_similar_result()
            self.order_similar_result()  # 手动进行一次排序
            self.viewer.turn_page_match_result()

        self.stop()

    """缓存管理相关方法"""

    def _prepare_before_cache_thread(self):
        """缓存管理相关子线程启动前的准备操作"""
        # 开始计时
        self.widget_runtime_info.start_time()
        # 禁用相关设置选项
        self._set_options_state(False)
        # 切换到运行信息页
        self.viewer.turn_page_running_info()
        # 将设置项重新传递给子线程
        self._set_thread_setting()
        self.is_stop = False

    def refresh_cache(self):
        """刷新缓存"""
        self._prepare_before_cache_thread()
        # 刷新漫画数据库项目
        # 获取存储的漫画路径列表
        comics_path_list = self.model.get_comic_paths()
        # 传递参数
        self.thread_refresh_comic_db.set_comics_path(comics_path_list)
        self.thread_refresh_comic_db.set_comic_db(self.model.get_comic_db())
        # 重新分析漫画信息并刷新漫画数据库
        self.thread_refresh_comic_db.start()

        # note 不刷新图片数据库项目

    def thread_refresh_comic_db_finished(self):
        """子线程-刷新缓存数据执行完毕"""
        print('子线程-刷新缓存数据执行完毕')
        self.stop()

    def delete_useless_cache(self):
        """删除无用缓存"""
        self.model.delete_useless_cache()

    def clear_cache(self):
        """清空缓存"""
        self.model.clear_cache()
        self._update_cache_info()  # 更新统计信息

    def match_cache_data_self(self):
        """漫画数据库项目自我匹配"""
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始数据库内部匹配')
        # 跳步启动子线程
        self._prepare_before_cache_thread()
        cache_comic_info_list = self.model.get_comic_infos()  # 缓存中的漫画信息类列表
        image_hash_dict = self.model.get_hashs_all_type()  # 哈希值字典，键为虚拟图片路径，值为3种图片hash*3种长度的字典
        self.thread_compare_comic.set_image_hash_dict(image_hash_dict)
        self.thread_compare_comic.set_comic_info_list(cache_comic_info_list)
        self.thread_compare_comic.set_cache_comic_info_list(
            cache_comic_info_list)  # note 缓存变量也要赋值，防止同时勾选匹配缓存选项时缓存变量没有值的问题
        self.thread_compare_comic.start()

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
        # 子线程-搜索漫画
        self.thread_search_comic.initialize()
        thread_count = self.widget_setting_match.get_thread_count()  # 线程数
        self.thread_search_comic.set_max_workers(thread_count)
        search_paths = self.widget_search_list.get_paths()  # 搜索路径
        self.thread_search_comic.set_search_list(search_paths)
        pages_lower_limit = self.widget_setting_comic.get_pages_lower_limit()  # 漫画页数下限
        self.thread_search_comic.set_pages_lower_limit(pages_lower_limit)
        is_analyze_archive = self.widget_setting_comic.get_is_analyze_archive()  # 是否识别压缩文件
        self.thread_search_comic.set_is_check_archive(is_analyze_archive)
        is_allow_other_filetypes = self.widget_setting_comic.get_is_allow_other_filetypes()  # 是否允许其他文件类型
        self.thread_search_comic.set_is_allow_other_filetypes(is_allow_other_filetypes)

        # 子线程-分析漫画信息
        self.thread_analyse_comic_info.initialize()
        self.thread_analyse_comic_info.set_max_workers(thread_count)

        # 子线程-保存漫画信息到数据库
        self.thread_save_comic.initialize()
        self.thread_save_comic.set_max_workers(thread_count)

        # 子线程-分析图片信息
        self.thread_analyse_image_info.initialize()
        self.thread_analyse_image_info.set_max_workers(thread_count)
        extract_pages = self.widget_setting_match.get_extract_pages()  # 每本漫画提取的页数
        self.thread_analyse_image_info.set_extract_pages(extract_pages)
        hash_algorithm = self.widget_setting_algorithm.get_base_algorithm()  # hash算法
        self.thread_analyse_image_info.set_hash_type(hash_algorithm)
        hash_length = self.widget_setting_algorithm.get_hash_length()  # hash长度
        self.thread_analyse_image_info.set_hash_length(hash_length)

        # 线程-保存图片信息到数据库
        self.thread_save_image.initialize()
        self.thread_save_image.set_max_workers(thread_count)

        # 子线程-对比漫画信息
        self.thread_compare_comic.initialize()
        self.thread_compare_comic.set_max_workers(thread_count)
        is_match_cache = self.widget_setting_match.get_is_match_cache()  # 是否匹配缓存
        self.thread_compare_comic.set_is_match_cache(is_match_cache)
        self.thread_compare_comic.set_extract_pages(extract_pages)
        self.thread_compare_comic.set_hash_type(hash_algorithm)
        self.thread_compare_comic.set_hash_length(hash_length)
        hamming_distance = self.widget_setting_algorithm.get_hamming_distance()  # 汉明距离阈值
        self.thread_compare_comic.set_hamming_distance(hamming_distance)
        is_match_same_parent_dir = self.widget_setting_match.get_is_match_same_parent_folder()  # 是否仅匹配相同父目录
        self.thread_compare_comic.set_is_match_same_parent_dir(is_match_same_parent_dir)
        parent_dir_level = self.widget_setting_match.get_match_parent_folder_level()  # 父目录层级
        self.thread_compare_comic.set_parent_dir_level(parent_dir_level)
        is_enhance_algorithm = self.widget_setting_algorithm.get_is_enhance_algorithm()  # 是否使用增强算法
        self.thread_compare_comic.set_is_enhance_algorithm(is_enhance_algorithm)
        enhance_algorithm = self.widget_setting_algorithm.get_enhance_algorithm()  # 增强hash算法类型
        self.thread_compare_comic.set_enhance_algorithm(enhance_algorithm)

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

    def _set_options_state(self, is_enable: bool):
        """设置选项启用/禁用"""
        if is_enable:
            self.widget_exec.set_button_state_end()
        else:
            self.widget_exec.set_button_state_start()
        self.widget_setting_algorithm.set_options_state(is_enable)
        self.widget_setting_match.set_options_state(is_enable)
        self.widget_setting_comic.set_options_state(is_enable)
        self.widget_cache_manager.set_options_state(is_enable)

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
        self.widget_similar_result_filter.FilterSameItems.connect(
            self.assembler_similar_result_preview.show_same_item_in_group)
        self.widget_similar_result_filter.FilterSameFilesizeItems.connect(
            self.assembler_similar_result_preview.show_same_filesize_item_in_group)
        self.widget_similar_result_filter.FilterExcludeDiffPages.connect(
            self.assembler_similar_result_preview.show_similar_pages_item_in_group)
        self.widget_similar_result_filter.ChangeSortKey.connect(self.order_similar_result)
        self.widget_similar_result_filter.ChangeSortDirection.connect(self.order_similar_result)

        self.widget_cache_manager.CacheRefresh.connect(self.refresh_cache)
        self.widget_cache_manager.CacheDeleteUseless.connect(self.delete_useless_cache)
        self.widget_cache_manager.CacheMatch.connect(self.match_cache_data_self)
        self.widget_cache_manager.CacheClear.connect(self.clear_cache)

        self.assembler_similar_result_preview.UpdateComicInfo.connect(
            self.thread_save_comic.save_comic_info_without_infotips)

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

        # self.thread_compare_comic.SignalStart.connect()
        self.thread_compare_comic.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_compare_comic.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_compare_comic.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_compare_comic.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        self.thread_compare_comic.SignalFinished.connect(self.thread_compare_comic_finished)
        # self.thread_compare_comic.SignalStopped.connect()

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

        # self.thread_refresh_comic_db.SignalStart.connect()
        self.thread_refresh_comic_db.SignalIndex.connect(self.update_runtime_info_index)
        self.thread_refresh_comic_db.SignalInfo.connect(self.update_runtime_info_title)
        self.thread_refresh_comic_db.SignalRate.connect(self.update_runtime_info_rate)
        self.thread_refresh_comic_db.SignalRuntimeInfo.connect(self.update_runtime_info_textline)
        self.thread_refresh_comic_db.SignalFinished.connect(self.thread_refresh_comic_db_finished)
        # self.thread_refresh_comic_db.SignalStopped.connect()
