from PySide6.QtCore import QObject, Signal


class ObjectEmittingStream(QObject):
    """自定义输出流，用于替代 sys.stdout 和 sys.stderr
    当有内容写入时，通过信号将文本发送出去
    """
    _instance = None
    _is_init = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    TextWritten = Signal(str)

    def write(self, text):
        """print 语句最终会调用这个方法"""
        if text and text.strip():
            self.TextWritten.emit(text)

    def flush(self):
        """必须实现，但可以为空"""
        pass
