# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_search_listyxkutX.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(273, 250)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_add = QToolButton(self.groupBox)
        self.toolButton_add.setObjectName(u"toolButton_add")

        self.horizontalLayout.addWidget(self.toolButton_add)

        self.toolButton_del = QToolButton(self.groupBox)
        self.toolButton_del.setObjectName(u"toolButton_del")

        self.horizontalLayout.addWidget(self.toolButton_del)

        self.toolButton_clear = QToolButton(self.groupBox)
        self.toolButton_clear.setObjectName(u"toolButton_clear")

        self.horizontalLayout.addWidget(self.toolButton_clear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_folder_list = QVBoxLayout()
        self.verticalLayout_folder_list.setObjectName(u"verticalLayout_folder_list")

        self.verticalLayout.addLayout(self.verticalLayout_folder_list)

        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u641c\u7d22\u6587\u4ef6\u5939", None))
        self.toolButton_add.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_del.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_clear.setText(QCoreApplication.translate("Form", u"...", None))
    # retranslateUi

