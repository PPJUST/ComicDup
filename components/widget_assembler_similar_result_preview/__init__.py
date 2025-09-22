# 相似组匹配结果控件的组装器，用于整合各个子部件
# 相似结果模块A->A内部显示相似组模块B->B内部显示漫画信息模块C
# 控件的添加在模块内部实现，assembler仅提供访问接口
from .assembler import AssemblerSimilarResultPreview
from .widget_similar_result_preview import SimilarResultPreviewPresenter


def get_assembler() -> AssemblerSimilarResultPreview:
    _assembler = AssemblerSimilarResultPreview()
    return _assembler
