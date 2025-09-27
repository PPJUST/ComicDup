# 预览相似组内漫画控件的组装器，用于整合各个子部件
# 单个漫画预览控件A>显示在漫画组预览器B
# 控件的添加在模块内部实现，assembler仅提供访问接口
from .assembler import AssemblerDialogComicsPreview


def get_assembler() -> AssemblerDialogComicsPreview:
    _assembler = AssemblerDialogComicsPreview()
    return _assembler
