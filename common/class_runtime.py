class TypeRuntimeInfo:
    """运行信息分类"""

    class StepInfo:
        """步骤运行信息（开始、结束等）"""
        text = 'StepInfo: '
        color = 'ForestGreen'
        font_size = 16

    class RateInfo:
        """进度信息（具体的执行进度信息）"""
        text = 'RateInfo: '
        color = 'Black'
        font_size = 12

    class Notice:
        """重要提示信息（匹配成功等））"""
        text = 'Notice: '
        color = 'RoyalBlue'
        font_size = 14

    class Warning:
        """错误信息（处理失败等））"""
        text = 'Warning: '
        color = 'DarkRed'
        font_size = 14


TYPE_RUNTIME_INFO = (TypeRuntimeInfo.StepInfo, TypeRuntimeInfo.RateInfo, TypeRuntimeInfo.Warning,
                     TypeRuntimeInfo.Notice)
