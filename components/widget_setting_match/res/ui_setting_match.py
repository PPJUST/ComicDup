# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_matchjtIDsW.ui'
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
        Form.resize(175, 125)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.spinBox_extract_pages = QSpinBox(Form)
        self.spinBox_extract_pages.setObjectName(u"spinBox_extract_pages")

        self.horizontalLayout.addWidget(self.spinBox_extract_pages)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.checkBox_match_cache = QCheckBox(Form)
        self.checkBox_match_cache.setObjectName(u"checkBox_match_cache")

        self.verticalLayout.addWidget(self.checkBox_match_cache)

        self.checkBox_match_similar_filename = QCheckBox(Form)
        self.checkBox_match_similar_filename.setObjectName(u"checkBox_match_similar_filename")

        self.verticalLayout.addWidget(self.checkBox_match_similar_filename)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_same_parent_folder = QCheckBox(Form)
        self.checkBox_same_parent_folder.setObjectName(u"checkBox_same_parent_folder")

        self.horizontalLayout_2.addWidget(self.checkBox_same_parent_folder)

        self.spinBox_same_parent_folder = QSpinBox(Form)
        self.spinBox_same_parent_folder.setObjectName(u"spinBox_same_parent_folder")

        self.horizontalLayout_2.addWidget(self.spinBox_same_parent_folder)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_thread_count = QSpinBox(Form)
        self.spinBox_thread_count.setObjectName(u"spinBox_thread_count")

        self.horizontalLayout_3.addWidget(self.spinBox_thread_count)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4ece\u6bcf\u672c\u6f2b\u753b\u4e2d\u63d0\u53d6\u7684\u56fe\u7247\u6570\u91cf\uff0c\u7528\u4e8e\u76f8\u4f3c\u5339\u914d\uff0c\u63d0\u53d6\u9875\u6570\u8d8a\u591a\u8ba1\u7b97\u91cf\u8d8a\u5927\uff08\u6307\u6570\u7ea7\u589e\u957f\uff09</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"\u63d0\u53d6\u6f2b\u753b\u9875\u6570", None))
#if QT_CONFIG(tooltip)
        self.spinBox_extract_pages.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4ece\u6bcf\u672c\u6f2b\u753b\u4e2d\u63d0\u53d6\u7684\u56fe\u7247\u6570\u91cf\uff0c\u7528\u4e8e\u76f8\u4f3c\u5339\u914d\uff0c\u63d0\u53d6\u9875\u6570\u8d8a\u591a\u8ba1\u7b97\u91cf\u8d8a\u5927\uff08\u6307\u6570\u7ea7\u589e\u957f\uff09</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_match_cache.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5728\u5339\u914d\u76f8\u4f3c\u6f2b\u753b\u65f6\uff0c\u662f\u5426\u989d\u5916\u5339\u914d\u6570\u636e\u5e93\u4e2d\u5df2\u7ecf\u7f13\u5b58\u7684\u6f2b\u753b\u6570\u636e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_match_cache.setText(QCoreApplication.translate("Form", u"\u5339\u914d\u7f13\u5b58\u6570\u636e", None))
        self.checkBox_match_similar_filename.setText(QCoreApplication.translate("Form", u"\u4ec5\u5339\u914d\u76f8\u4f3c\u6587\u4ef6\u540d", None))
#if QT_CONFIG(tooltip)
        self.checkBox_same_parent_folder.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5728\u5339\u914d\u76f8\u4f3c\u6f2b\u753b\u65f6\uff0c\u4ec5\u5339\u914d\u5728\u540cn\u5c42\u7ea7\u7236\u6587\u4ef6\u5939\u4e0b\u7684\u6f2b\u753b</p><p>\u5982\u679c\u6f2b\u753b\u662f\u6309\u4f5c\u8005\u6574\u7406\u4e14\u90fd\u5728\u540c\u4e00\u76ee\u5f55\u4e0b\uff0c\u5219\u63a8\u8350\u5339\u914d\u5c42\u7ea7\u4e3a 1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_same_parent_folder.setText(QCoreApplication.translate("Form", u"\u4ec5\u5339\u914d\u540c", None))
#if QT_CONFIG(tooltip)
        self.spinBox_same_parent_folder.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5728\u5339\u914d\u76f8\u4f3c\u6f2b\u753b\u65f6\uff0c\u4ec5\u5339\u914d\u5728\u540cn\u5c42\u7ea7\u7236\u6587\u4ef6\u5939\u4e0b\u7684\u6f2b\u753b</p><p>\u5982\u679c\u6f2b\u753b\u662f\u6309\u4f5c\u8005\u6574\u7406\u4e14\u90fd\u5728\u540c\u4e00\u76ee\u5f55\u4e0b\uff0c\u5219\u63a8\u8350\u5339\u914d\u5c42\u7ea7\u4e3a 1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"\u5c42\u7236\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u591a\u7ebf\u7a0b\u4f7f\u7528\u7684\u7ebf\u7a0b\u6570\u91cf\uff0c\u7ebf\u7a0b\u6570\u8d8a\u591a\u8ba1\u7b97\u8d8a\u5feb</p><p>\u4e0d\u80fd\u8d85\u8fc7CPU\u7ebf\u7a0b\u6570\u4e0a\u9650</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7ebf\u7a0b\u6570", None))
#if QT_CONFIG(tooltip)
        self.spinBox_thread_count.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u591a\u7ebf\u7a0b\u4f7f\u7528\u7684\u7ebf\u7a0b\u6570\u91cf\uff0c\u7ebf\u7a0b\u6570\u8d8a\u591a\u8ba1\u7b97\u8d8a\u5feb</p><p>\u4e0d\u80fd\u8d85\u8fc7CPU\u7ebf\u7a0b\u6570\u4e0a\u9650</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

