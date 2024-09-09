# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_filter_resultAgrEIq.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(164, 96)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_refresh = QPushButton(self.groupBox)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.horizontalLayout_2.addWidget(self.pushButton_refresh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkBox_filter_same_items = QCheckBox(self.groupBox)
        self.checkBox_filter_same_items.setObjectName(u"checkBox_filter_same_items")

        self.verticalLayout.addWidget(self.checkBox_filter_same_items)

        self.checkBox_filter_pages_diff_items = QCheckBox(self.groupBox)
        self.checkBox_filter_pages_diff_items.setObjectName(u"checkBox_filter_pages_diff_items")

        self.verticalLayout.addWidget(self.checkBox_filter_pages_diff_items)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5339\u914d\u7ed3\u679c\u5904\u7406", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("Form", u"\u5237\u65b0\u7ed3\u679c", None))
        self.checkBox_filter_same_items.setText(QCoreApplication.translate("Form", u"\u7b5b\u9009 - \u9875\u6570\u3001\u5927\u5c0f\u76f8\u540c\u9879", None))
        self.checkBox_filter_pages_diff_items.setText(QCoreApplication.translate("Form", u"\u5254\u9664 - \u9875\u6570\u5dee\u5f02\u8fc7\u5927\u9879", None))
    # retranslateUi

