# 进行相似比较的子线程组

from thread.thread_analyse_comics_data import ThreadAnalyseComicsData
from thread.thread_calc_hash import ThreadCalcHash
from thread.thread_check_folder import ThreadCheckFolder
from thread.thread_compare_hash import ThreadCompareHash
from thread.thread_model import ThreadModel


class ThreadCompareManager(ThreadModel):
    """进行相似比较的子线程组"""

    def __init__(self):
        super().__init__()
        # 子线程-检查文件夹
        self.child_thread_check = ThreadCheckFolder()
        self.child_thread_check.signal_step.connect(self.emit_signal_step)
        self.child_thread_check.signal_rate.connect(self.emit_signal_rate)
        self.child_thread_check.signal_finished.connect(lambda: self.child_thread_analyse.start())
        self.child_thread_check.signal_stopped.connect(self.emit_signal_stopped)

        # 子线程-提取漫画数据
        self.child_thread_analyse = ThreadAnalyseComicsData()
        self.child_thread_analyse.signal_step.connect(self.emit_signal_step)
        self.child_thread_analyse.signal_rate.connect(self.emit_signal_rate)
        self.child_thread_analyse.signal_finished.connect(lambda: self.child_thread_calc.start())
        self.child_thread_analyse.signal_stopped.connect(self.emit_signal_stopped)

        # 子线程-计算Hash
        self.child_thread_calc = ThreadCalcHash()
        self.child_thread_calc.signal_step.connect(self.emit_signal_step)
        self.child_thread_calc.signal_rate.connect(self.emit_signal_rate)
        self.child_thread_calc.signal_finished.connect(lambda: self.child_thread_compare.start())
        self.child_thread_calc.signal_stopped.connect(self.emit_signal_stopped)

        # 子线程-相似匹配
        self.child_thread_compare = ThreadCompareHash()
        self.child_thread_compare.signal_step.connect(self.emit_signal_step)
        self.child_thread_compare.signal_rate.connect(self.emit_signal_rate)
        self.child_thread_compare.signal_finished.connect(self.emit_signal_finished)
        self.child_thread_compare.signal_stopped.connect(self.emit_signal_stopped)

    def reset_stop_code(self):
        super().reset_stop_code()
        self.child_thread_check.reset_stop_code()
        self.child_thread_analyse.reset_stop_code()
        self.child_thread_calc.reset_stop_code()
        self.child_thread_compare.reset_stop_code()

    def run(self):
        super().run()
        self.child_thread_check.start()
