# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'area_setting_comicHcnsxj.ui'
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
        Form.resize(221, 91)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_pages_lower_limit = QSpinBox(Form)
        self.spinBox_pages_lower_limit.setObjectName(u"spinBox_pages_lower_limit")

        self.horizontalLayout_3.addWidget(self.spinBox_pages_lower_limit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.checkBox_analyze_archive = QCheckBox(Form)
        self.checkBox_analyze_archive.setObjectName(u"checkBox_analyze_archive")

        self.verticalLayout.addWidget(self.checkBox_analyze_archive)

        self.checkBox_allow_other_filetypes = QCheckBox(Form)
        self.checkBox_allow_other_filetypes.setObjectName(u"checkBox_allow_other_filetypes")

        self.verticalLayout.addWidget(self.checkBox_allow_other_filetypes)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9875\u6570\u4e0b\u9650", None))
        self.checkBox_analyze_archive.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b\u538b\u7f29\u6587\u4ef6\u7c7b\u6f2b\u753b", None))
        self.checkBox_allow_other_filetypes.setText(QCoreApplication.translate("Form", u"\u5141\u8bb8\u5305\u542b\u9664\u56fe\u7247\u5916\u7684\u5176\u4ed6\u7c7b\u578b\u6587\u4ef6", None))
    # retranslateUi

