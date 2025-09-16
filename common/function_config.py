# 配置文件的方法
import configparser
import os

from common.class_config import TYPES_HASH_ALGORITHM, SimilarAlgorithm, TYPES_ENHANCE_ALGORITHM

CONFIG_FILE = 'setting.ini'


def check_config_exists():
    """检查配置文件是否存在"""
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w', encoding='utf-8'):
            pass


class _ModuleChildSetting:
    """抽象类：设置项"""

    def __init__(self, config_file: str):
        """:param config_file: 配置文件的ConfigParser对象"""
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(config_file, encoding='utf-8')

    def _read_key(self, section: str, key: str, default_value):
        """读取对应设置项的值，如果失败则返回默认值"""
        return self.config.get(section, key, fallback=default_value)

    def _set_value(self, section: str, key: str, value: str):
        """设置设置项"""
        # 由于设置模块分为了3个子模块，更新配置文件时需要重新读取最新的配置文件
        self._reload()

        if section not in self.config:
            self.config.add_section(section)
        self.config.set(section, key, str(value))
        self.config.write(open(CONFIG_FILE, 'w', encoding='utf-8'))

    def _reload(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file, encoding='utf-8')


class _ModuleChildSettingSingleEnable(_ModuleChildSetting):
    """抽象类：设置项，仅是否启用的选项模版"""

    def __init__(self, config_file, section: str, key: str, default_value: bool):
        super().__init__(config_file)
        self.section = section
        self.key = key
        self._default_value = default_value

    def read(self) -> bool:
        """读取设置项"""
        value = self._read_key(self.section, self.key, self._default_value)
        if isinstance(value, bool):
            return value
        elif value == 'True':
            return True
        elif value == 'False':
            return False
        else:
            raise ValueError(self.section, self.key, '无效的设置项值')

    def set(self, value: bool):
        """设置设置项"""
        self._set_value(self.section, self.key, str(value))


class _ModuleChildSettingSingleText(_ModuleChildSetting):
    """抽象类：设置项，纯文本项的选项模版"""

    def __init__(self, config_file, section: str, key: str, default_value: str):
        super().__init__(config_file)
        self.section = section
        self.key = key
        self._default_value = default_value

    def read(self) -> str:
        """读取设置项"""
        return self._read_key(self.section, self.key, self._default_value)

    def set(self, value: str):
        """设置设置项"""
        self._set_value(self.section, self.key, str(value))


class SettingBasicAlgorithm(_ModuleChildSetting):
    """相似算法：相似度基础算法"""

    def __init__(self, config_file):
        super().__init__(config_file)
        self.section = 'BasicAlgorithm'
        self.key = 'algorithm'
        self._default_value: TYPES_HASH_ALGORITHM = SimilarAlgorithm.dHash()

    def read(self) -> TYPES_HASH_ALGORITHM:
        """读取设置项"""
        value = self._read_key(self.section, self.key, self._default_value)
        # 将读取的文本值转换为对应的自定义类
        if isinstance(value, TYPES_HASH_ALGORITHM):
            return value
        elif value == SimilarAlgorithm.aHash.text:
            return SimilarAlgorithm.aHash()
        elif value == SimilarAlgorithm.pHash.text:
            return SimilarAlgorithm.pHash()
        elif value == SimilarAlgorithm.dHash.text:
            return SimilarAlgorithm.dHash()
        else:
            raise ValueError(self.section, self.key, '无效的设置项值')

    def set(self, value: TYPES_HASH_ALGORITHM):
        """设置设置项"""
        if isinstance(value, str):
            value_str = value
        elif isinstance(value, TYPES_HASH_ALGORITHM):
            value_str = value.text
        else:
            raise ValueError(value, '传参错误')
        self._set_value(self.section, self.key, value_str)


class SettingIsEnhanceAlgorithm(_ModuleChildSettingSingleEnable):
    """相似算法：是否启用相似度增强算法"""

    def __init__(self, config_file):
        super().__init__(config_file, section='IsEnhanceAlgorithm', key='is_enable', default_value=False)


class SettingEnhanceAlgorithm(_ModuleChildSetting):
    """相似算法：相似度增强算法"""

    def __init__(self, config_file):
        super().__init__(config_file)
        self.section = 'EnhanceAlgorithm'
        self.key = 'algorithm'
        self._default_value: TYPES_ENHANCE_ALGORITHM = SimilarAlgorithm.SSIM()

    def read(self) -> TYPES_ENHANCE_ALGORITHM:
        """读取设置项"""
        value = self._read_key(self.section, self.key, self._default_value)
        # 将读取的文本值转换为对应的自定义类
        if isinstance(value, TYPES_ENHANCE_ALGORITHM):
            return value
        elif value == SimilarAlgorithm.SSIM.text:
            return SimilarAlgorithm.SSIM()
        elif value == SimilarAlgorithm.ORB.text:
            return SimilarAlgorithm.ORB()
        else:
            raise ValueError(self.section, self.key, '无效的设置项值')

    def set(self, value: TYPES_ENHANCE_ALGORITHM):
        """设置设置项"""
        if isinstance(value, str):
            value_str = value
        elif isinstance(value, TYPES_ENHANCE_ALGORITHM):
            value_str = value.text
        else:
            raise ValueError(value, '传参错误')
        self._set_value(self.section, self.key, value_str)


class SettingSimilarThreshold(_ModuleChildSetting):
    """相似算法：相似度阈值"""

    def __init__(self, config_file):
        super().__init__(config_file)
        self.section = 'SimilarThreshold'
        self.key = 'threshold'
        self._default_value: int = 90

    def read(self) -> int:
        """读取设置项"""
        value = self._read_key(self.section, self.key, self._default_value)
        # 将读取的文本值转换为数值
        if isinstance(value, str):
            return int(value)
        elif isinstance(value, int):
            return value
        else:
            raise ValueError(self.section, self.key, '无效的设置项值')

    def set(self, value: int):
        """设置设置项"""
        value_str = str(value)
        self._set_value(self.section, self.key, value_str)


class SettingHashLength(_ModuleChildSetting):
    """相似算法：Hash值长度"""

    def __init__(self, config_file):
        super().__init__(config_file)
        self.section = 'HashLength'
        self.key = 'length'
        self._default_value: int = 64

    def read(self) -> int:
        """读取设置项"""
        value = self._read_key(self.section, self.key, self._default_value)
        # 将读取的文本值转换为数值
        if isinstance(value, str):
            return int(value)
        elif isinstance(value, int):
            return value
        else:
            raise ValueError(self.section, self.key, '无效的设置项值')

    def set(self, value: int):
        """设置设置项"""
        value_str = str(value)
        self._set_value(self.section, self.key, value_str)


class SettingExtractPages(_ModuleChildSetting):
    """匹配选项：提取漫画页数"""

    def __init__(self, config_file):
        super().__init__(config_file)
        self.section = 'ExtractPages'
        self.key = 'count'
        self._default_value: int = 2

    def read(self) -> int:
        """读取设置项"""
        value = self._read_key(self.section, self.key, self._default_value)
        # 将读取的文本值转换为数值
        if isinstance(value, str):
            return int(value)
        elif isinstance(value, int):
            return value
        else:
            raise ValueError(self.section, self.key, '无效的设置项值')

    def set(self, value: int):
        """设置设置项"""
        value_str = str(value)
        self._set_value(self.section, self.key, value_str)


class SettingIsMatchCache(_ModuleChildSettingSingleEnable):
    """匹配选项：是否匹配缓存"""

    def __init__(self, config_file):
        super().__init__(config_file, section='IsMatchCache', key='is_enable', default_value=False)


class SettingIsMatchSimilarFilename(_ModuleChildSettingSingleEnable):
    """匹配选项：是否仅匹配相似文件名"""

    def __init__(self, config_file):
        super().__init__(config_file, section='IsMatchSimilarFilename', key='is_enable', default_value=False)


class SettingThreadCount(_ModuleChildSetting):
    """匹配选项：线程数"""

    def __init__(self, config_file):
        super().__init__(config_file)
        self.section = 'ThreadCount'
        self.key = 'count'
        self._default_value: int = 2

    def read(self) -> int:
        """读取设置项"""
        value = self._read_key(self.section, self.key, self._default_value)
        # 将读取的文本值转换为数值
        if isinstance(value, str):
            return int(value)
        elif isinstance(value, int):
            return value
        else:
            raise ValueError(self.section, self.key, '无效的设置项值')

    def set(self, value: int):
        """设置设置项"""
        value_str = str(value)
        self._set_value(self.section, self.key, value_str)


class SettingComicPagesLowerLimit(_ModuleChildSetting):
    """漫画选项：识别为漫画的页数下限"""

    def __init__(self, config_file):
        super().__init__(config_file)
        self.section = 'ComicPagesLowerLimit'
        self.key = 'limit'
        self._default_value: int = 4

    def read(self) -> int:
        """读取设置项"""
        value = self._read_key(self.section, self.key, self._default_value)
        # 将读取的文本值转换为数值
        if isinstance(value, str):
            return int(value)
        elif isinstance(value, int):
            return value
        else:
            raise ValueError(self.section, self.key, '无效的设置项值')

    def set(self, value: int):
        """设置设置项"""
        value_str = str(value)
        self._set_value(self.section, self.key, value_str)


class SettingIsAnalyzeArchive(_ModuleChildSettingSingleEnable):
    """漫画选项：是否识别压缩文件"""

    def __init__(self, config_file):
        super().__init__(config_file, section='IsAnalyzeArchive', key='is_enable', default_value=False)


class SettingIsAllowOtherFiletypesInComic(_ModuleChildSettingSingleEnable):
    """漫画选项：是否允许漫画包含其他类型文件"""

    def __init__(self, config_file):
        super().__init__(config_file, section='IsAllowOtherFiletypesInComic', key='is_enable', default_value=False)
