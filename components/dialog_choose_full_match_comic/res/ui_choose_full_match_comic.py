# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_full_match_comiczFZbwH.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(421, 403)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox_comic_1 = QSpinBox(Dialog)
        self.spinBox_comic_1.setObjectName(u"spinBox_comic_1")
        self.spinBox_comic_1.setMinimum(1)

        self.horizontalLayout.addWidget(self.spinBox_comic_1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.spinBox_comic_2 = QSpinBox(Dialog)
        self.spinBox_comic_2.setObjectName(u"spinBox_comic_2")
        self.spinBox_comic_2.setMinimum(2)

        self.horizontalLayout_2.addWidget(self.spinBox_comic_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_exec = QPushButton(Dialog)
        self.pushButton_exec.setObjectName(u"pushButton_exec")

        self.horizontalLayout_3.addWidget(self.pushButton_exec)

        self.pushButton_quit = QPushButton(Dialog)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.horizontalLayout_3.addWidget(self.pushButton_quit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.textBrowser_match_result = QTextBrowser(Dialog)
        self.textBrowser_match_result.setObjectName(u"textBrowser_match_result")

        self.verticalLayout.addWidget(self.textBrowser_match_result)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5168\u91cf\u5339\u914d", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u9700\u8981\u8fdb\u884c\u5168\u91cf\u5339\u914d\u7684\u4e24\u672c\u6f2b\u753b\u7684\u7f16\u53f7\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u610f\uff1a\u672c\u529f\u80fd\u4ec5\u4e3a\u5c1d\u9c9c\u4f7f\u7528\uff0c\u4ecd\u5728\u8c03\u8bd5\u9636\u6bb5\u3002", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u610f\uff1a\u6267\u884c\u540e\u4f1a\u5361\u987f\uff0c\u8fd9\u662f\u6b63\u5e38\u73b0\u8c61\u3002", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6f2b\u753b1\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6f2b\u753b2\uff1a", None))
        self.pushButton_exec.setText(QCoreApplication.translate("Dialog", u"\u6267\u884c", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5339\u914d\u7ed3\u679c\uff1a", None))
    # retranslateUi

