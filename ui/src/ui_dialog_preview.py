# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_previewxBATpJ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.toolButton_last_5 = QToolButton(Dialog)
        self.toolButton_last_5.setObjectName(u"toolButton_last_5")

        self.horizontalLayout.addWidget(self.toolButton_last_5)

        self.toolButton_last = QToolButton(Dialog)
        self.toolButton_last.setObjectName(u"toolButton_last")

        self.horizontalLayout.addWidget(self.toolButton_last)

        self.toolButton_next = QToolButton(Dialog)
        self.toolButton_next.setObjectName(u"toolButton_next")

        self.horizontalLayout.addWidget(self.toolButton_next)

        self.toolButton_next_5 = QToolButton(Dialog)
        self.toolButton_next_5.setObjectName(u"toolButton_next_5")

        self.horizontalLayout.addWidget(self.toolButton_next_5)

        self.toolButton_refresh = QToolButton(Dialog)
        self.toolButton_refresh.setObjectName(u"toolButton_refresh")

        self.horizontalLayout.addWidget(self.toolButton_refresh)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.pushButton_quit = QPushButton(Dialog)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.horizontalLayout_2.addWidget(self.pushButton_quit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 392, 263))
        self.horizontalLayout_place = QHBoxLayout(self.scrollAreaWidget)
        self.horizontalLayout_place.setSpacing(3)
        self.horizontalLayout_place.setObjectName(u"horizontalLayout_place")
        self.horizontalLayout_place.setContentsMargins(3, 3, 3, 3)
        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u9884\u89c8", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u540c\u6b65\u7ffb\u9875", None))
        self.toolButton_last_5.setText(QCoreApplication.translate("Dialog", u"<<", None))
        self.toolButton_last.setText(QCoreApplication.translate("Dialog", u"<", None))
        self.toolButton_next.setText(QCoreApplication.translate("Dialog", u">", None))
        self.toolButton_next_5.setText(QCoreApplication.translate("Dialog", u">>", None))
        self.toolButton_refresh.setText(QCoreApplication.translate("Dialog", u"refresh", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
    # retranslateUi

