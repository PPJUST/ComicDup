from common.class_comic import ComicInfo, FileType


class ComicInfoModel:
    """单个漫画信息模块的模型组件"""

    def __init__(self):
        self.comic_info: ComicInfo = None

    def refresh_info(self):
        """刷新信息"""
        comic_path = self.comic_info.filepath
        self.comic_info = ComicInfo(comic_path)

    def analyse_comic(self, comic_path: str):
        """分析漫画信息"""
        self.comic_info = ComicInfo(comic_path)

    def get_filepath(self) -> str:
        """获取文件路径"""
        return self.comic_info.filepath

    def get_filename(self) -> str:
        """获取文件名"""
        return self.comic_info.filename

    def get_filetitle(self) -> str:
        """获取文件标题"""
        return self.comic_info.filetitle

    def get_parent_dirpath(self) -> str:
        """获取文件父级路径"""
        return self.comic_info.parent_dirpath

    def get_filesize_bytes(self) -> int:
        """获取文件大小（字节）"""
        return self.comic_info.filesize_bytes

    def get_filesize_bytes_extracted(self) -> int:
        """获取文件真实大小（字节），文件类型为解压文件"""
        return self.comic_info.filesize_bytes_extracted

    def get_filetype(self) -> FileType:
        """获取文件类型"""
        return self.comic_info.filetype

    def get_modified_time(self) -> float:
        """获取文件修改时间"""
        return self.comic_info.modified_time

    def get_page_paths(self) -> tuple:
        """获取内部文件路径"""
        return self.comic_info.page_paths

    def get_page_count(self) -> int:
        """获取页数"""
        return self.comic_info.page_count

    def get_preview_path(self) -> str:
        """获取预览小图本地路径"""
        return self.comic_info.preview_path
