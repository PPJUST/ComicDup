# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'similar_group_previewKntLlU.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.toolButton_previous2 = QToolButton(Form)
        self.toolButton_previous2.setObjectName(u"toolButton_previous2")

        self.horizontalLayout.addWidget(self.toolButton_previous2)

        self.toolButton_previous = QToolButton(Form)
        self.toolButton_previous.setObjectName(u"toolButton_previous")

        self.horizontalLayout.addWidget(self.toolButton_previous)

        self.toolButton_next = QToolButton(Form)
        self.toolButton_next.setObjectName(u"toolButton_next")

        self.horizontalLayout.addWidget(self.toolButton_next)

        self.toolButton_next2 = QToolButton(Form)
        self.toolButton_next2.setObjectName(u"toolButton_next2")

        self.horizontalLayout.addWidget(self.toolButton_next2)

        self.toolButton_reset = QToolButton(Form)
        self.toolButton_reset.setObjectName(u"toolButton_reset")

        self.horizontalLayout.addWidget(self.toolButton_reset)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Raised)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.pushButton_quit = QPushButton(Form)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.horizontalLayout.addWidget(self.pushButton_quit)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Raised)
        self.line_2.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout.addWidget(self.line_2)

        self.checkBox_auto_calc_similar = QCheckBox(Form)
        self.checkBox_auto_calc_similar.setObjectName(u"checkBox_auto_calc_similar")

        self.horizontalLayout.addWidget(self.checkBox_auto_calc_similar)

        self.checkBox_auto_image_diff = QCheckBox(Form)
        self.checkBox_auto_image_diff.setObjectName(u"checkBox_auto_image_diff")

        self.horizontalLayout.addWidget(self.checkBox_auto_image_diff)

        self.pushButton_calc_diff_pages = QPushButton(Form)
        self.pushButton_calc_diff_pages.setObjectName(u"pushButton_calc_diff_pages")

        self.horizontalLayout.addWidget(self.pushButton_calc_diff_pages)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 792, 564))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_group = QHBoxLayout()
        self.horizontalLayout_group.setObjectName(u"horizontalLayout_group")

        self.horizontalLayout_2.addLayout(self.horizontalLayout_group)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5168\u5c40\u7ffb\u9875", None))
#if QT_CONFIG(tooltip)
        self.toolButton_previous2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4e0a5\u9875</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_previous2.setText(QCoreApplication.translate("Form", u"previous2", None))
#if QT_CONFIG(tooltip)
        self.toolButton_previous.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4e0a1\u9875</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_previous.setText(QCoreApplication.translate("Form", u"previous", None))
#if QT_CONFIG(tooltip)
        self.toolButton_next.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4e0b1\u9875</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_next.setText(QCoreApplication.translate("Form", u"next", None))
#if QT_CONFIG(tooltip)
        self.toolButton_next2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4e0b5\u9875</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_next2.setText(QCoreApplication.translate("Form", u"next2", None))
#if QT_CONFIG(tooltip)
        self.toolButton_reset.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u91cd\u7f6e\u9875\u7801</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_reset.setText(QCoreApplication.translate("Form", u"reset", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.checkBox_auto_calc_similar.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5b9e\u65f6\u663e\u793a\u9884\u89c8\u56fe\u7247\u9875\u4e4b\u95f4\u7684\u76f8\u4f3c\u5ea6\uff0c\u4ee5\u7b2c\u4e00\u4e2a\u9879\u76ee\u7684\u56fe\u7247\u4e3a\u57fa\u51c6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_auto_calc_similar.setText(QCoreApplication.translate("Form", u"\u5b9e\u65f6\u663e\u793a\u76f8\u4f3c\u5ea6", None))
        self.checkBox_auto_image_diff.setText(QCoreApplication.translate("Form", u"\u5b9e\u65f6\u663e\u793a\u56fe\u7247\u5dee\u5f02", None))
#if QT_CONFIG(tooltip)
        self.pushButton_calc_diff_pages.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5bf9\u4e24\u4e2a\u9879\u76ee\u8fdb\u884c\u5168\u90e8\u56fe\u7247\u7684\u76f8\u4f3c\u5339\u914d\uff0c\u5206\u6790\u4e24\u4e2a\u9879\u76ee\u4e4b\u95f4\u7684\u5dee\u5f02\u60c5\u51b5</p><p>\u6ce8\u610f\uff0c\u5373\u4f7f\u5168\u90e8\u6b63\u786e\u5339\u914d\uff0c\u4ecd\u53ef\u80fd\u662f\u4e0d\u540c\u7684\u6c49\u5316\u7ec4\u3001\u4e0d\u540c\u7684\u4fee\u6b63</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_calc_diff_pages.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5dee\u5f02\u9875\u9762", None))
    # retranslateUi

