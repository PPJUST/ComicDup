# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cache_managerysfLjv.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(175, 281)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_refresh = QPushButton(Form)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.verticalLayout.addWidget(self.pushButton_refresh)

        self.pushButton_cache_match = QPushButton(Form)
        self.pushButton_cache_match.setObjectName(u"pushButton_cache_match")

        self.verticalLayout.addWidget(self.pushButton_cache_match)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_delete_useless = QPushButton(Form)
        self.pushButton_delete_useless.setObjectName(u"pushButton_delete_useless")

        self.verticalLayout_2.addWidget(self.pushButton_delete_useless)

        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.verticalLayout_2.addWidget(self.pushButton_clear)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(3)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_comic_count = QLabel(Form)
        self.label_comic_count.setObjectName(u"label_comic_count")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_comic_count)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_comic_size = QLabel(Form)
        self.label_comic_size.setObjectName(u"label_comic_size")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_comic_size)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_comic_update = QLabel(Form)
        self.label_comic_update.setObjectName(u"label_comic_update")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_comic_update)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(3)
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.label_image_count = QLabel(Form)
        self.label_image_count.setObjectName(u"label_image_count")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_image_count)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.label_image_size = QLabel(Form)
        self.label_image_size.setObjectName(u"label_image_size")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_image_size)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.label_image_update = QLabel(Form)
        self.label_image_update.setObjectName(u"label_image_update")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_image_update)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(3)
        self.formLayout_3.setVerticalSpacing(3)
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.label_preview_count = QLabel(Form)
        self.label_preview_count.setObjectName(u"label_preview_count")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.label_preview_count)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.label_preview_size = QLabel(Form)
        self.label_preview_size.setObjectName(u"label_preview_size")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.label_preview_size)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_9)


        self.verticalLayout_3.addLayout(self.formLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("Form", u"\u5237\u65b0\u7f13\u5b58\u6570\u636e", None))
        self.pushButton_cache_match.setText(QCoreApplication.translate("Form", u"\u7f13\u5b58\u5185\u90e8\u67e5\u91cd", None))
        self.pushButton_delete_useless.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u65e0\u6548\u6570\u636e", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u7f13\u5b58", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"  \u5b58\u50a8\u9879\u76ee\u6570\uff1a", None))
        self.label_comic_count.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"  \u6570\u636e\u5e93\u5927\u5c0f\uff1a", None))
        self.label_comic_size.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"  \u66f4\u65b0\u65f6\u95f4\uff1a", None))
        self.label_comic_update.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6f2b\u753b\u6570\u636e\u5e93", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u6570\u636e\u5e93", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"  \u5b58\u50a8\u9879\u76ee\u6570\uff1a", None))
        self.label_image_count.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"  \u6570\u636e\u5e93\u5927\u5c0f\uff1a", None))
        self.label_image_size.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"  \u66f4\u65b0\u65f6\u95f4\uff1a", None))
        self.label_image_update.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"  \u7f13\u5b58\u56fe\u7247\u6570\uff1a", None))
        self.label_preview_count.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"  \u7f13\u5b58\u5927\u5c0f\uff1a", None))
        self.label_preview_size.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u9884\u89c8\u56fe\u7f13\u5b58", None))
    # retranslateUi

