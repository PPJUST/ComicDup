class TypeRuntimeInfo:
    """运行信息分类"""

    class StepInfo:
        """步骤运行信息（开始、结束等）"""
        text = 'StepInfo: '

    class RateInfo:
        """进度信息（具体的执行进度信息）"""
        text = 'RateInfo: '

    class Warning:
        """错误信息（处理失败等））"""
        text = 'Warning: '


TYPE_RUNTIME_INFO = (TypeRuntimeInfo.StepInfo, TypeRuntimeInfo.RateInfo, TypeRuntimeInfo.Warning)
