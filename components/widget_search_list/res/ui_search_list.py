# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'area_search_listOubXqP.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(494, 356)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_add_files = QPushButton(Form)
        self.pushButton_add_files.setObjectName(u"pushButton_add_files")

        self.horizontalLayout.addWidget(self.pushButton_add_files)

        self.pushButton_add_folders = QPushButton(Form)
        self.pushButton_add_folders.setObjectName(u"pushButton_add_folders")

        self.horizontalLayout.addWidget(self.pushButton_add_folders)

        self.pushButton_delete_useless_path = QPushButton(Form)
        self.pushButton_delete_useless_path.setObjectName(u"pushButton_delete_useless_path")

        self.horizontalLayout.addWidget(self.pushButton_delete_useless_path)

        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout.addWidget(self.pushButton_clear)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_add_files.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.pushButton_add_folders.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6587\u4ef6\u5939", None))
        self.pushButton_delete_useless_path.setText(QCoreApplication.translate("Form", u"\u79fb\u9664\u5931\u6548\u8def\u5f84", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
    # retranslateUi

