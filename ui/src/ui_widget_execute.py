# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_executePVHLzy.ui'
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
        Form.resize(161, 75)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.pushButton_start = QPushButton(self.groupBox)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.gridLayout.addWidget(self.pushButton_start, 0, 0, 1, 1)

        self.pushButton_stop = QPushButton(self.groupBox)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.gridLayout.addWidget(self.pushButton_stop, 0, 1, 1, 1)

        self.pushButton_load_last_result = QPushButton(self.groupBox)
        self.pushButton_load_last_result.setObjectName(u"pushButton_load_last_result")

        self.gridLayout.addWidget(self.pushButton_load_last_result, 1, 0, 1, 1)

        self.pushButton_information = QPushButton(self.groupBox)
        self.pushButton_information.setObjectName(u"pushButton_information")

        self.gridLayout.addWidget(self.pushButton_information, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u6267\u884c", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.pushButton_load_last_result.setText(QCoreApplication.translate("Form", u"\u52a0\u8f7d\u7ed3\u679c", None))
        self.pushButton_information.setText(QCoreApplication.translate("Form", u"\u8bf4\u660e", None))
    # retranslateUi

