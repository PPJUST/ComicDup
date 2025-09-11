# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'area_result_filterdFSlhT.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(265, 72)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_refresh_result = QPushButton(Form)
        self.pushButton_refresh_result.setObjectName(u"pushButton_refresh_result")

        self.horizontalLayout.addWidget(self.pushButton_refresh_result)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_filter_same_items = QPushButton(Form)
        self.pushButton_filter_same_items.setObjectName(u"pushButton_filter_same_items")

        self.verticalLayout.addWidget(self.pushButton_filter_same_items)

        self.pushButton_exclude_diff_pages = QPushButton(Form)
        self.pushButton_exclude_diff_pages.setObjectName(u"pushButton_exclude_diff_pages")

        self.verticalLayout.addWidget(self.pushButton_exclude_diff_pages)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_refresh_result.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e\u7ed3\u679c", None))
        self.pushButton_filter_same_items.setText(QCoreApplication.translate("Form", u"\u4ec5\u663e\u793a\u9875\u6570\u3001\u6587\u4ef6\u5927\u5c0f\u76f8\u540c\u9879", None))
        self.pushButton_exclude_diff_pages.setText(QCoreApplication.translate("Form", u"\u5254\u9664\u9875\u6570\u5dee\u5f02\u8fc7\u5927\u9879", None))
    # retranslateUi

