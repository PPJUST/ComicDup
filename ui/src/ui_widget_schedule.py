# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_schedulenjNLJd.ui'
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
        Form.resize(189, 97)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_runtime_total = QLabel(self.groupBox)
        self.label_runtime_total.setObjectName(u"label_runtime_total")

        self.gridLayout.addWidget(self.label_runtime_total, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_schedule_total = QLabel(self.groupBox)
        self.label_schedule_total.setObjectName(u"label_schedule_total")

        self.gridLayout.addWidget(self.label_schedule_total, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_runtime_step = QLabel(self.groupBox)
        self.label_runtime_step.setObjectName(u"label_runtime_step")

        self.gridLayout.addWidget(self.label_runtime_step, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_schedule_step = QLabel(self.groupBox)
        self.label_schedule_step.setObjectName(u"label_schedule_step")

        self.gridLayout.addWidget(self.label_schedule_step, 3, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8fd0\u884c\u8fdb\u5ea6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u603b\u7528\u65f6\uff1a", None))
        self.label_runtime_total.setText(QCoreApplication.translate("Form", u"0:00:00", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u603b\u8fdb\u5ea6\uff1a", None))
        self.label_schedule_total.setText(QCoreApplication.translate("Form", u"-/-", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u7528\u65f6\uff1a", None))
        self.label_runtime_step.setText(QCoreApplication.translate("Form", u"0:00:00", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8fdb\u5ea6\uff1a", None))
        self.label_schedule_step.setText(QCoreApplication.translate("Form", u"-/-", None))
    # retranslateUi

