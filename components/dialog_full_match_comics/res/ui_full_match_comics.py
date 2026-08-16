# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'full_match_comicsRwVjyr.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(390, 515)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox_comic_main = QComboBox(Dialog)
        self.comboBox_comic_main.setObjectName(u"comboBox_comic_main")

        self.horizontalLayout_2.addWidget(self.comboBox_comic_main)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.comboBox_comic_comp = QComboBox(Dialog)
        self.comboBox_comic_comp.setObjectName(u"comboBox_comic_comp")

        self.horizontalLayout_3.addWidget(self.comboBox_comic_comp)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_simple_result = QLabel(Dialog)
        self.label_simple_result.setObjectName(u"label_simple_result")

        self.horizontalLayout_5.addWidget(self.label_simple_result)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton_show_details = QToolButton(Dialog)
        self.toolButton_show_details.setObjectName(u"toolButton_show_details")

        self.horizontalLayout_4.addWidget(self.toolButton_show_details)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.checkBox_show_diff_pages = QCheckBox(Dialog)
        self.checkBox_show_diff_pages.setObjectName(u"checkBox_show_diff_pages")

        self.verticalLayout.addWidget(self.checkBox_show_diff_pages)

        self.tableWidget_details_pages = QTableWidget(Dialog)
        self.tableWidget_details_pages.setObjectName(u"tableWidget_details_pages")

        self.verticalLayout.addWidget(self.tableWidget_details_pages)

        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5168\u91cf\u6bd4\u5bf9", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8bf4\u660e\uff1a\u9009\u62e9\u9700\u8981\u8fdb\u884c\u5168\u91cf\u6bd4\u5bf9\u7684\u4e24\u672c\u6f2b\u753b\uff0c\u8fdb\u884c\u6bd4\u5bf9\u5e76\u8fd4\u56de\u6bd4\u5bf9\u7ed3\u679c\u3002", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u610f\uff1a\u6bd4\u5bf9\u7ed3\u679c\u4ec5\u4f9b\u53c2\u8003\uff01\uff01\uff01", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u4e3b\u6f2b\u753b\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u6b21\u6f2b\u753b\uff1a", None))
        self.label_6.setText("")
        self.pushButton_match.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u6bd4\u5bf9", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u7b80\u6613\u6bd4\u5bf9\u7ed3\u679c\uff1a", None))
        self.label_simple_result.setText(QCoreApplication.translate("Dialog", u"\u6bd4\u5bf9\u7ed3\u679c", None))
        self.label_11.setText("")
        self.toolButton_show_details.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u6bd4\u5bf9\u8be6\u60c5\uff1a", None))
        self.checkBox_show_diff_pages.setText(QCoreApplication.translate("Dialog", u"\u4ec5\u663e\u793a\u5dee\u5f02\u9875", None))
    # retranslateUi

