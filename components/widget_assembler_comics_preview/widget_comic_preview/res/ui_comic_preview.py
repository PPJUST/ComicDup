# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comic_previewCXhSJH.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(283, 212)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_preview = QVBoxLayout()
        self.verticalLayout_preview.setSpacing(0)
        self.verticalLayout_preview.setObjectName(u"verticalLayout_preview")

        self.verticalLayout_2.addLayout(self.verticalLayout_preview)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_icon = QLabel(Form)
        self.label_icon.setObjectName(u"label_icon")

        self.horizontalLayout.addWidget(self.label_icon)

        self.label_filesize = QLabel(Form)
        self.label_filesize.setObjectName(u"label_filesize")

        self.horizontalLayout.addWidget(self.label_filesize)

        self.label_filename = QLabel(Form)
        self.label_filename.setObjectName(u"label_filename")

        self.horizontalLayout.addWidget(self.label_filename)

        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_parent_dirpath = QLabel(Form)
        self.label_parent_dirpath.setObjectName(u"label_parent_dirpath")

        self.verticalLayout.addWidget(self.label_parent_dirpath)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.toolButton_previous = QToolButton(Form)
        self.toolButton_previous.setObjectName(u"toolButton_previous")

        self.horizontalLayout_2.addWidget(self.toolButton_previous)

        self.toolButton_next = QToolButton(Form)
        self.toolButton_next.setObjectName(u"toolButton_next")

        self.horizontalLayout_2.addWidget(self.toolButton_next)

        self.label_current_page = QLabel(Form)
        self.label_current_page.setObjectName(u"label_current_page")

        self.horizontalLayout_2.addWidget(self.label_current_page)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_page_count = QLabel(Form)
        self.label_page_count.setObjectName(u"label_page_count")

        self.horizontalLayout_2.addWidget(self.label_page_count)

        self.toolButton_open = QToolButton(Form)
        self.toolButton_open.setObjectName(u"toolButton_open")

        self.horizontalLayout_2.addWidget(self.toolButton_open)

        self.toolButton_delete = QToolButton(Form)
        self.toolButton_delete.setObjectName(u"toolButton_delete")

        self.horizontalLayout_2.addWidget(self.toolButton_delete)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_icon.setText(QCoreApplication.translate("Form", u"icon", None))
        self.label_filesize.setText(QCoreApplication.translate("Form", u"filesize", None))
        self.label_filename.setText(QCoreApplication.translate("Form", u"filename", None))
        self.label_parent_dirpath.setText(QCoreApplication.translate("Form", u"parent_dirpath", None))
        self.toolButton_previous.setText(QCoreApplication.translate("Form", u"previous", None))
        self.toolButton_next.setText(QCoreApplication.translate("Form", u"next", None))
        self.label_current_page.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"/", None))
        self.label_page_count.setText(QCoreApplication.translate("Form", u"1", None))
        self.toolButton_open.setText(QCoreApplication.translate("Form", u"open", None))
        self.toolButton_delete.setText(QCoreApplication.translate("Form", u"delete", None))
    # retranslateUi

