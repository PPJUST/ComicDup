# 漫画页面全量匹配的结果的类


class MatchResult:
    """漫画页面全量匹配的结果的类"""

    class OneToOne:
        """完全正确匹配"""
        text = '完全正确匹配'

    class SameCountButWrongPageNumber:
        """全部页面都被匹配，但是页面顺序错误"""
        text = '全部页面都被匹配，但是页面顺序错误'
        wrong_pages_comic_1 = []
        wrong_pages_comic_2 = []

    class SameCountButWrongPage:
        """有页面未匹配"""
        text = '有页面未匹配'
        wrong_pages_comic_1 = []
        wrong_pages_comic_2 = []

    class LossPageComic1:
        """漫画1有缺页，即漫画2有多余页"""
        text = '漫画1有缺页，即漫画2有多余页'
        wrong_pages_comic_1 = []
        wrong_pages_comic_2 = []

    class LossPageComic2:
        """漫画2有缺页，即漫画1有多余页"""
        text = '漫画2有缺页，即漫画1有多余页'
        wrong_pages_comic_1 = []
        wrong_pages_comic_2 = []

    class Unknown:
        """未知"""
        text = '未知错误'
        wrong_pages_comic_1 = []
        wrong_pages_comic_2 = []


MatchResults = [MatchResult.OneToOne, MatchResult.SameCountButWrongPageNumber, MatchResult.SameCountButWrongPage,
                MatchResult.LossPageComic1, MatchResult.LossPageComic2, MatchResult.Unknown]
