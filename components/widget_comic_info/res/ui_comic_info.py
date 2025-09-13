# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comic_infoDkAlqT.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 240)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_icon = QLabel(Form)
        self.label_icon.setObjectName(u"label_icon")

        self.horizontalLayout.addWidget(self.label_icon)

        self.label_filetitle = QLabel(Form)
        self.label_filetitle.setObjectName(u"label_filetitle")

        self.horizontalLayout.addWidget(self.label_filetitle)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_parent_dirpath = QLabel(Form)
        self.label_parent_dirpath.setObjectName(u"label_parent_dirpath")

        self.verticalLayout.addWidget(self.label_parent_dirpath)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_page_count = QLabel(Form)
        self.label_page_count.setObjectName(u"label_page_count")

        self.horizontalLayout_2.addWidget(self.label_page_count)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_filesize = QLabel(Form)
        self.label_filesize.setObjectName(u"label_filesize")

        self.horizontalLayout_3.addWidget(self.label_filesize)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_preview = QLabel(Form)
        self.label_preview.setObjectName(u"label_preview")

        self.verticalLayout.addWidget(self.label_preview)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton_open_path = QToolButton(Form)
        self.toolButton_open_path.setObjectName(u"toolButton_open_path")

        self.horizontalLayout_4.addWidget(self.toolButton_open_path)

        self.toolButton_refresh = QToolButton(Form)
        self.toolButton_refresh.setObjectName(u"toolButton_refresh")

        self.horizontalLayout_4.addWidget(self.toolButton_refresh)

        self.toolButton_delete = QToolButton(Form)
        self.toolButton_delete.setObjectName(u"toolButton_delete")

        self.horizontalLayout_4.addWidget(self.toolButton_delete)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_icon.setText(QCoreApplication.translate("Form", u"icon", None))
        self.label_filetitle.setText(QCoreApplication.translate("Form", u"filetitle", None))
        self.label_parent_dirpath.setText(QCoreApplication.translate("Form", u"parent dirpath", None))
        self.label_page_count.setText(QCoreApplication.translate("Form", u"page count", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u9875", None))
        self.label_filesize.setText(QCoreApplication.translate("Form", u"filesize", None))
        self.label_preview.setText(QCoreApplication.translate("Form", u"preview", None))
        self.toolButton_open_path.setText(QCoreApplication.translate("Form", u"open path", None))
        self.toolButton_refresh.setText(QCoreApplication.translate("Form", u"refresh", None))
        self.toolButton_delete.setText(QCoreApplication.translate("Form", u"delete", None))
    # retranslateUi

