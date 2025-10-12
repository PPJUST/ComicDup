# 设置文件相关的自定义类

class SimilarAlgorithm:
    """相似算法"""

    class aHash:
        """平均Hash算法"""
        text = 'aHash'

    class pHash:
        """感知Hash算法"""
        text = 'pHash'

    class dHash:
        """差异Hash算法"""
        text = 'dHash'

    class SSIM:
        """结构相似性算法"""
        text = 'SSIM'

    class ORB:
        """ORB特征点算法"""
        text = 'ORB'


class HashLength:
    """Hash长度"""

    class _64:
        """64位（8*8）"""
        text = '64'
        value = 64

    class _144:
        """144位（12*12）"""
        text = '144'
        value = 144

    class _256:
        """256位（16*16）"""
        text = '256'
        value = 256


class FileType:
    """文件类型"""

    class File:
        """文件"""
        text = '文件'

    class Folder:
        """文件夹"""
        text = '文件夹'

    class Archive:
        """压缩文件"""
        text = '压缩文件'

    class Unknown:
        """未知类型"""
        text = '未知类型'

    class Error:
        """错误"""
        text = '错误'


TYPES_HASH_ALGORITHM = (SimilarAlgorithm.aHash, SimilarAlgorithm.pHash, SimilarAlgorithm.dHash)
TEXT_HASH_ALGORITHM = (SimilarAlgorithm.aHash.text, SimilarAlgorithm.pHash.text, SimilarAlgorithm.dHash.text)

TYPES_ENHANCE_ALGORITHM = (SimilarAlgorithm.SSIM, SimilarAlgorithm.ORB)
TEXT_ENHANCE_ALGORITHM = (SimilarAlgorithm.SSIM.text, SimilarAlgorithm.ORB.text)

TEXT_HASH_LENGTH = (HashLength._64.text, HashLength._144.text, HashLength._256.text)

FileTypes = (FileType.File, FileType.Folder, FileType.Archive, FileType.Unknown)
