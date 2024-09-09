# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_scrollArea_comic_groupspAeDP.ui'
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
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 398, 296))
        self.horizontalLayout_place = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_place.setSpacing(30)
        self.horizontalLayout_place.setObjectName(u"horizontalLayout_place")
        self.horizontalLayout_place.setContentsMargins(3, 3, 3, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout__scrollbar = QHBoxLayout()
        self.horizontalLayout__scrollbar.setSpacing(0)
        self.horizontalLayout__scrollbar.setObjectName(u"horizontalLayout__scrollbar")
        self.horizontalLayout__scrollbar.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addLayout(self.horizontalLayout__scrollbar)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

