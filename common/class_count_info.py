class CountInfo:
    """信息统计类"""

    def __init__(self):
        self.item_count: int = 0  # 项目数统计
        self.size_count: str = ''  # 大小统计
        self.update_time: str = ''  # 更新时间

    def set_item_count(self, item_count: int):
        """设置项目数"""
        self.item_count = item_count

    def set_size_count(self, size_count: str):
        """设置大小"""
        self.size_count = size_count

    def set_update_time(self, update_time: str):
        """设置更新时间"""
        self.update_time = update_time

    def get_item_count(self) -> int:
        """获取项目数"""
        return self.item_count

    def get_size_count(self) -> str:
        """获取大小"""
        return self.size_count

    def get_update_time(self) -> str:
        """获取更新时间"""
        return self.update_time
