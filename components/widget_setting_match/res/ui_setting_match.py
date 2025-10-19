# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_matchvyIAYD.ui'
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
        self.label_3.setText(QCoreApplication.translate("Form", u"\u63d0\u53d6\u6f2b\u753b\u9875\u6570", None))
        self.checkBox_match_cache.setText(QCoreApplication.translate("Form", u"\u5339\u914d\u7f13\u5b58\u6570\u636e", None))
        self.checkBox_match_similar_filename.setText(QCoreApplication.translate("Form", u"\u4ec5\u5339\u914d\u76f8\u4f3c\u6587\u4ef6\u540d", None))
        self.checkBox_same_parent_folder.setText(QCoreApplication.translate("Form", u"\u4ec5\u5339\u914d\u540c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5c42\u7236\u76ee\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7ebf\u7a0b\u6570", None))
    # retranslateUi

