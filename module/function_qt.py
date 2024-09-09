from PySide6.QtGui import Qt
from PySide6.QtWidgets import QLabel


def update_label_long_text(label: QLabel):
    """文本长度超限时，尾部显示..."""
    # 获取字体度量
    font_metrics = label.fontMetrics()
    label_width = label.width()
    original_text = label.toolTip()  # .text()或.toolTip()

    # 判断文本是否超出label宽度，并处理
    if font_metrics.horizontalAdvance(original_text) > label_width:
        elided_text = font_metrics.elidedText(original_text, Qt.ElideRight, label_width)
        label.setText(elided_text)
