# 对缓存数据进行相似比较的子线程组

from module import function_cache_hash, function_cache_thread
from thread.thread_compare_hash import ThreadCompareHash
from thread.thread_model import ThreadModel


class ThreadCompareCacheManager(ThreadModel):
    """对缓存数据进行相似比较的子线程组"""

    def __init__(self):
        super().__init__()
        self.child_thread = ThreadCompareHash()
        self.child_thread.signal_step.connect(self.emit_signal_step)
        self.child_thread.signal_rate.connect(self.emit_signal_rate)
        self.child_thread.signal_finished.connect(self.emit_signal_finished)
        self.child_thread.signal_stopped.connect(self.emit_signal_stopped)

    def run(self):
        super().run()
        # 读将当前任务计算的图片数据字典替换为缓存图片数据字典
        cache_image_data_dict = function_cache_hash.read_hash_cache()
        function_cache_thread.save_current_image_data_dict(cache_image_data_dict)
        # 启动子线程
        self.child_thread.start()

    def reset_stop_code(self):
        super().reset_stop_code()
        self.child_thread.reset_stop_code()
