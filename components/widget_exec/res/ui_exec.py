# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'area_execbqscVa.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(179, 70)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.gridLayout.addWidget(self.pushButton_start, 0, 0, 1, 1)

        self.pushButton_stop = QPushButton(Form)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.gridLayout.addWidget(self.pushButton_stop, 0, 1, 1, 1)

        self.pushButton_load_last_result = QPushButton(Form)
        self.pushButton_load_last_result.setObjectName(u"pushButton_load_last_result")

        self.gridLayout.addWidget(self.pushButton_load_last_result, 1, 0, 1, 1)

        self.pushButton_info = QPushButton(Form)
        self.pushButton_info.setObjectName(u"pushButton_info")

        self.gridLayout.addWidget(self.pushButton_info, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u67e5\u91cd", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u67e5\u91cd", None))
        self.pushButton_load_last_result.setText(QCoreApplication.translate("Form", u"\u52a0\u8f7d\u4e0a\u6b21\u7ed3\u679c", None))
        self.pushButton_info.setText(QCoreApplication.translate("Form", u"\u7a0b\u5e8f\u8bf4\u660e", None))
    # retranslateUi

