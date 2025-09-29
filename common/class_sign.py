class SignStatus:
    """操作状态标识"""

    class Pending:
        """待处理"""
        text = 'Pending'

    class Completed:
        """已完成全部处理"""
        text = 'Completed'

    class Partial:
        """已部分处理"""
        text = 'Partial'


TYPE_SIGN_STATUS = (SignStatus.Pending, SignStatus.Completed, SignStatus.Partial)
