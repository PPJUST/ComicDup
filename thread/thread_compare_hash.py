# 子线程-对比图片hash
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

import lzytools_image

from common.class_runtime import TypeRuntimeInfo
from thread.thread_pattern import ThreadPattern


class ThreadCompareHash(ThreadPattern):
    """子线程-对比图片hash"""

    def __init__(self):
        super().__init__()
        self.step_index = 4
        self.step_info = '对比图片hash'

        # 需要匹配的hash值列表
        self.hash_list: List[str] = []
        # 相似hash组列表
        self.similar_hash_group: List[List[str]] = []

        # 用于匹配的缓存hash数据
        self.is_match_cache = False  # 是否匹配缓存数据
        self.cache_hash_list: List[str] = []

        # 判断为相似的汉明距离上限
        self.hamming_distance = 10

    def get_similar_hash_group(self):
        """获取相似hash组列表"""
        similar_hash_group = self.similar_hash_group
        self.clear()
        return similar_hash_group

    def set_hash_list(self, hash_list: list):
        """设置需要匹配的hash值列表"""
        hash_list = self.sort_hash(hash_list)
        self.hash_list = hash_list

    def set_is_match_cache(self, is_match_cache: bool):
        """设置是否匹配缓存数据"""
        self.is_match_cache = is_match_cache

    def get_is_match_cache(self):
        """获取是否匹配缓存数据"""
        return self.is_match_cache

    def set_cache_hash_list(self, cache_hash_list: List[str]):
        """设置用于匹配的缓存hash数据"""
        self.cache_hash_list = cache_hash_list

    def set_hamming_distance(self, hamming_distance: int):
        """设置最大汉明距离"""
        self.hamming_distance = hamming_distance

    def clear(self):
        """清空数据"""
        self.hash_list = []
        self.similar_hash_group = []

    def run(self):
        super().run()
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '开始对比图片相似度')
        print(f'启动线程池 对比图片hash，线程数量：{self.max_workers}')

        total = len(self.hash_list)
        print('hash总数', total)
        if total == 0:
            self._finish_compare()
            return

        # 使用线程池进行并发处理
        completed_count = 0

        # 生成用于匹配的hash值列表
        match_hash_list = self.hash_list.copy()
        # 如果需要匹配缓存hash值，则写入匹配列表中
        if self.is_match_cache:
            match_hash_list.extend(self.cache_hash_list)

        # 重新排序
        match_hash_list = self.sort_hash(match_hash_list)
        print('用于匹配的hash列表总数', len(match_hash_list))
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有任务
            # note 线程公用匹配列表，请勿在匹配方法中修改该列表
            futures = {executor.submit(self._compare, hash_, match_hash_list.copy()): hash_ for hash_ in self.hash_list}

            # 处理完成的任务
            for future in as_completed(futures):
                if self._is_stop:
                    executor.shutdown(wait=False, cancel_futures=True)
                    break

                hash_ = futures[future]
                try:
                    similar_group = future.result()
                    print('显示匹配结果', similar_group)
                    # 即使只有其自身，仍旧写入相似组，因为可能存在漫画的复制品，导致hash值相同，但是跳过空值（纯色页）
                    if similar_group:
                        self.similar_hash_group.append(similar_group)
                    completed_count += 1
                    self.SignalRate.emit(f'{completed_count}/{total}')
                except Exception as e:
                    self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Warning, f'对比{hash_}失败：{str(e)}')

            self._finish_compare()

    @staticmethod
    def sort_hash(hash_list: list):
        """排序hash列表"""
        # 按hash值中0的个数对其进行排序，在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，两个hash值的汉明距离不可能再低于阈值
        return sorted(hash_list, key=lambda x: x.count('0'))

    def _finish_compare(self):
        """完成对比后的处理"""
        print('结束线程池 对比图片hash')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.StepInfo, '全部图片对比完成')
        self.SignalRuntimeInfo.emit(TypeRuntimeInfo.Notice, f'共匹配到{len(self.similar_hash_group)}组相似组')
        self.finished()

    def _compare(self, hash_: str, match_hash_list: List[str]):
        """对比单个hash值与其他hash值的相似度"""
        # 统计需匹配的hash中0和1的个数，如果占比大于90%，则判断为纯色图片，不进行后续匹配
        zero_count = hash_.count('0')
        if zero_count / len(hash_) > 0.8 or zero_count / len(hash_) < 0.2:
            return None

        print(f'匹配hash 主hash【{hash_}】')
        # 去重对比列表以及剔除自身
        filter_list = []
        if match_hash_list.count(hash_) == 1:  # 如果计数为1，则说明自身为匹配列表中的唯一元素，则直接剔除并去重即可
            for i in match_hash_list:
                if i != hash_ and i not in filter_list:
                    filter_list.append(i)
        else:  # 否则，说明该hash对应的图片存在重复项目，直接去重即可
            for i in match_hash_list:
                if i not in filter_list:
                    filter_list.append(i)
        match_hash_list = filter_list

        # 最终的相似hash值列表
        similar_group = set()

        # 从匹配列表中提取出有效的hash值
        # 在计算两个hash值的汉明距离时，如果其0的计数差异大于阈值的1/2时，两个hash值的汉明距离不可能再低于阈值
        # 匹配列表在匹配前已经进行过排序操作，所以只需要提取出中间段的hash值
        min_zero_count = int(zero_count / 2)
        max_zero_count = int(zero_count * 1.5)
        # 找列表切片索引
        start = 0
        end = len(match_hash_list)
        for index, i in enumerate(match_hash_list):
            _c = i.count('0')
            if not start and _c >= min_zero_count:
                start = index
            if _c >= max_zero_count:
                end = index
                break

        match_hash_list_filter = match_hash_list[start:end]
        print('对比hash列表', len(match_hash_list_filter))

        # 执行匹配
        for hash_compare in match_hash_list_filter:
            distance = lzytools_image.calc_hash_hamming_distance(hash_, hash_compare)
            if distance <= self.hamming_distance:
                similar_group.add(hash_compare)

        # 手动清空变量
        match_hash_list.clear()
        match_hash_list_filter.clear()

        # 存在相似项时才返回数据，否则返回空
        if len(similar_group) > 0:
            similar_group.add(hash_)
            print(f'返回匹配结果{similar_group}')
            return list(similar_group)
        else:
            print(f'返回匹配结果[]')
            return []
