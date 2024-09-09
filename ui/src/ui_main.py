# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainHdNsDt.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 69, 598))
        self.verticalLayout_functional_area = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_functional_area.setSpacing(3)
        self.verticalLayout_functional_area.setObjectName(u"verticalLayout_functional_area")
        self.verticalLayout_functional_area.setContentsMargins(3, 3, 3, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_result_area = QVBoxLayout(self.groupBox)
        self.verticalLayout_result_area.setSpacing(0)
        self.verticalLayout_result_area.setObjectName(u"verticalLayout_result_area")
        self.verticalLayout_result_area.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ComicDup", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u7ed3\u679c", None))
    # retranslateUi

