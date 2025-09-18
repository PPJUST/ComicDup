# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'runtime_infovJGktZ.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(406, 304)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_runtime_total = QLabel(Form)
        self.label_runtime_total.setObjectName(u"label_runtime_total")

        self.horizontalLayout.addWidget(self.label_runtime_total)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_step_index = QLabel(Form)
        self.label_step_index.setObjectName(u"label_step_index")

        self.horizontalLayout_4.addWidget(self.label_step_index)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_step_count = QLabel(Form)
        self.label_step_count.setObjectName(u"label_step_count")

        self.horizontalLayout_4.addWidget(self.label_step_count)

        self.label_step_title = QLabel(Form)
        self.label_step_title.setObjectName(u"label_step_title")

        self.horizontalLayout_4.addWidget(self.label_step_title)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_runtime_current = QLabel(Form)
        self.label_runtime_current.setObjectName(u"label_runtime_current")

        self.horizontalLayout_2.addWidget(self.label_runtime_current)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_progress_current = QLabel(Form)
        self.label_progress_current.setObjectName(u"label_progress_current")

        self.horizontalLayout_3.addWidget(self.label_progress_current)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.textBrowser_runtime_info = QTextBrowser(Form)
        self.textBrowser_runtime_info.setObjectName(u"textBrowser_runtime_info")

        self.verticalLayout.addWidget(self.textBrowser_runtime_info)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u603b\u8017\u65f6\uff1a", None))
        self.label_runtime_total.setText(QCoreApplication.translate("Form", u"0:00:00", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u603b\u8fdb\u5ea6\uff1a", None))
        self.label_step_index.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"/", None))
        self.label_step_count.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_step_title.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8017\u65f6\uff1a", None))
        self.label_runtime_current.setText(QCoreApplication.translate("Form", u"0:00:00", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5b50\u8fdb\u5ea6\uff1a", None))
        self.label_progress_current.setText(QCoreApplication.translate("Form", u"-/-", None))
    # retranslateUi

