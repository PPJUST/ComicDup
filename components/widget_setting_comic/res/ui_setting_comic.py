# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_comicHDoIGB.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(209, 73)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_pages_lower_limit = QSpinBox(Form)
        self.spinBox_pages_lower_limit.setObjectName(u"spinBox_pages_lower_limit")

        self.horizontalLayout_3.addWidget(self.spinBox_pages_lower_limit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.checkBox_analyze_archive = QCheckBox(Form)
        self.checkBox_analyze_archive.setObjectName(u"checkBox_analyze_archive")

        self.verticalLayout.addWidget(self.checkBox_analyze_archive)

        self.checkBox_allow_other_filetypes = QCheckBox(Form)
        self.checkBox_allow_other_filetypes.setObjectName(u"checkBox_allow_other_filetypes")

        self.verticalLayout.addWidget(self.checkBox_allow_other_filetypes)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4e00\u4e2a\u6587\u4ef6\u5939/\u538b\u7f29\u6587\u4ef6\u4e2d\u5b58\u5728n\u5f20\u56fe\u7247\u53ca\u4ee5\u4e0a\u65f6\uff0c\u624d\u4f1a\u88ab\u8bc6\u522b\u4e3a\u6f2b\u753b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9875\u6570\u4e0b\u9650", None))
#if QT_CONFIG(tooltip)
        self.spinBox_pages_lower_limit.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4e00\u4e2a\u6587\u4ef6\u5939/\u538b\u7f29\u6587\u4ef6\u4e2d\u5b58\u5728n\u5f20\u56fe\u7247\u53ca\u4ee5\u4e0a\u65f6\uff0c\u624d\u4f1a\u88ab\u8bc6\u522b\u4e3a\u6f2b\u753b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_analyze_archive.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8bc6\u522b\u6f2b\u753b\u65f6\uff0c\u662f\u5426\u68c0\u67e5\u538b\u7f29\u6587\u4ef6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_analyze_archive.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b\u538b\u7f29\u6587\u4ef6\u7c7b\u6f2b\u753b", None))
#if QT_CONFIG(tooltip)
        self.checkBox_allow_other_filetypes.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5728\u8bc6\u522b\u6f2b\u753b\u65f6\uff0c\u662f\u5426\u5141\u8bb8\u6587\u4ef6\u5939/\u538b\u7f29\u6587\u4ef6\u5185\u5305\u542b\u9664\u56fe\u7247\u4ee5\u5916\u7684\u6587\u4ef6\u7c7b\u578b</p><p>\uff08\u6ce8\u610f\uff0c\u5982\u679c\u6587\u4ef6\u5939\u4e2d\u5305\u542b\u5b50\u6587\u4ef6\u5939\uff0c\u5219\u8be5\u6587\u4ef6\u5939\u4e0d\u4f1a\u88ab\u8bc6\u522b\u4e3a\u6f2b\u753b\uff09</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_allow_other_filetypes.setText(QCoreApplication.translate("Form", u"\u5141\u8bb8\u5305\u542b\u9664\u56fe\u7247\u5916\u7684\u5176\u4ed6\u7c7b\u578b\u6587\u4ef6", None))
    # retranslateUi

