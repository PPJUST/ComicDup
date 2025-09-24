# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'similar_group_infoBdAhcO.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QScrollArea,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(248, 168)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_preview = QToolButton(Form)
        self.toolButton_preview.setObjectName(u"toolButton_preview")

        self.horizontalLayout.addWidget(self.toolButton_preview)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_index = QLabel(Form)
        self.label_index.setObjectName(u"label_index")

        self.horizontalLayout.addWidget(self.label_index)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_item_count = QLabel(Form)
        self.label_item_count.setObjectName(u"label_item_count")

        self.horizontalLayout.addWidget(self.label_item_count)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.label_sign = QLabel(Form)
        self.label_sign.setObjectName(u"label_sign")

        self.horizontalLayout.addWidget(self.label_sign)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea_similar_group = QScrollArea(Form)
        self.scrollArea_similar_group.setObjectName(u"scrollArea_similar_group")
        self.scrollArea_similar_group.setWidgetResizable(True)
        self.scrollAreaWidgetContents_similar_group = QWidget()
        self.scrollAreaWidgetContents_similar_group.setObjectName(u"scrollAreaWidgetContents_similar_group")
        self.scrollAreaWidgetContents_similar_group.setGeometry(QRect(0, 0, 240, 134))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents_similar_group)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.scrollArea_similar_group.setWidget(self.scrollAreaWidgetContents_similar_group)

        self.verticalLayout.addWidget(self.scrollArea_similar_group)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton_preview.setText(QCoreApplication.translate("Form", u"preview", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7ec4", None))
        self.label_index.setText(QCoreApplication.translate("Form", u"index", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_item_count.setText(QCoreApplication.translate("Form", u"item count", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u9879", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"[", None))
        self.label_sign.setText(QCoreApplication.translate("Form", u"sign", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"]", None))
    # retranslateUi

