# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'full_match_comicsnpzoAT.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(390, 401)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox_main_comic = QComboBox(Dialog)
        self.comboBox_main_comic.setObjectName(u"comboBox_main_comic")

        self.horizontalLayout_2.addWidget(self.comboBox_main_comic)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.comboBox_comp_comic = QComboBox(Dialog)
        self.comboBox_comp_comic.setObjectName(u"comboBox_comp_comic")

        self.horizontalLayout_3.addWidget(self.comboBox_comp_comic)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_match = QPushButton(Dialog)
        self.pushButton_match.setObjectName(u"pushButton_match")

        self.horizontalLayout.addWidget(self.pushButton_match)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_quit = QPushButton(Dialog)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.horizontalLayout.addWidget(self.pushButton_quit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.textBrowser_simple_result = QTextBrowser(Dialog)
        self.textBrowser_simple_result.setObjectName(u"textBrowser_simple_result")

        self.verticalLayout_2.addWidget(self.textBrowser_simple_result)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.checkBox_show_diff_pages = QCheckBox(Dialog)
        self.checkBox_show_diff_pages.setObjectName(u"checkBox_show_diff_pages")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_show_diff_pages.sizePolicy().hasHeightForWidth())
        self.checkBox_show_diff_pages.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.checkBox_show_diff_pages)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMaximumSize(QSize(160, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 158, 158))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_details_pages = QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_details_pages.setObjectName(u"tableWidget_details_pages")

        self.horizontalLayout_4.addWidget(self.tableWidget_details_pages)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalLayout_5.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5168\u91cf\u6bd4\u5bf9", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8bf4\u660e\uff1a\u9009\u62e9\u9700\u8981\u8fdb\u884c\u5168\u91cf\u6bd4\u5bf9\u7684\u4e24\u672c\u6f2b\u753b\uff0c\u8fdb\u884c\u6bd4\u5bf9\u5e76\u8fd4\u56de\u6bd4\u5bf9\u7ed3\u679c\u3002", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u610f\uff1a\u6bd4\u5bf9\u7ed3\u679c\u4ec5\u4f9b\u53c2\u8003\uff01\uff01\uff01", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u610f\uff1a\u672a\u505a\u591a\u7ebf\u7a0b\uff0c\u6240\u4ee5\u6bd4\u5bf9\u65f6UI\u4f1a\u5361\u4f4f\uff01\uff01\uff01", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u4e3b\u6f2b\u753b\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u6b21\u6f2b\u753b\uff1a", None))
        self.label_6.setText("")
        self.pushButton_match.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u6bd4\u5bf9", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u6bd4\u5bf9\u7ed3\u679c\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6bd4\u5bf9\u8be6\u60c5\uff1a", None))
        self.checkBox_show_diff_pages.setText(QCoreApplication.translate("Dialog", u"\u4ec5\u663e\u793a\u5dee\u5f02\u9875\u9762", None))
    # retranslateUi

