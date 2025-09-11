# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'area_similar_result_previewnUnNbF.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTreeView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(359, 240)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_previous_page = QPushButton(Form)
        self.pushButton_previous_page.setObjectName(u"pushButton_previous_page")

        self.horizontalLayout.addWidget(self.pushButton_previous_page)

        self.pushButton_next_page = QPushButton(Form)
        self.pushButton_next_page.setObjectName(u"pushButton_next_page")

        self.horizontalLayout.addWidget(self.pushButton_next_page)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_show_group_count = QComboBox(Form)
        self.comboBox_show_group_count.setObjectName(u"comboBox_show_group_count")

        self.horizontalLayout.addWidget(self.comboBox_show_group_count)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.treeView_group = QTreeView(Form)
        self.treeView_group.setObjectName(u"treeView_group")

        self.verticalLayout.addWidget(self.treeView_group)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_previous_page.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u9875", None))
        self.pushButton_next_page.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u9875", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6bcf\u9875\u663e\u793a\u7ec4\u6570", None))
    # retranslateUi

