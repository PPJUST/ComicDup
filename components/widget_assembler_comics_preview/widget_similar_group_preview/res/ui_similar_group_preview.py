# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'similar_group_previewVuWwfw.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(662, 309)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.toolButton_previous2 = QToolButton(Form)
        self.toolButton_previous2.setObjectName(u"toolButton_previous2")

        self.horizontalLayout.addWidget(self.toolButton_previous2)

        self.toolButton_previous = QToolButton(Form)
        self.toolButton_previous.setObjectName(u"toolButton_previous")

        self.horizontalLayout.addWidget(self.toolButton_previous)

        self.toolButton_next = QToolButton(Form)
        self.toolButton_next.setObjectName(u"toolButton_next")

        self.horizontalLayout.addWidget(self.toolButton_next)

        self.toolButton_next2 = QToolButton(Form)
        self.toolButton_next2.setObjectName(u"toolButton_next2")

        self.horizontalLayout.addWidget(self.toolButton_next2)

        self.toolButton_reset = QToolButton(Form)
        self.toolButton_reset.setObjectName(u"toolButton_reset")

        self.horizontalLayout.addWidget(self.toolButton_reset)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Raised)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.pushButton_quit = QPushButton(Form)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.horizontalLayout.addWidget(self.pushButton_quit)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Raised)
        self.line_2.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout.addWidget(self.line_2)

        self.checkBox_auto_calc_similar = QCheckBox(Form)
        self.checkBox_auto_calc_similar.setObjectName(u"checkBox_auto_calc_similar")

        self.horizontalLayout.addWidget(self.checkBox_auto_calc_similar)

        self.checkBox_auto_image_diff = QCheckBox(Form)
        self.checkBox_auto_image_diff.setObjectName(u"checkBox_auto_image_diff")

        self.horizontalLayout.addWidget(self.checkBox_auto_image_diff)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_group = QHBoxLayout()
        self.horizontalLayout_group.setObjectName(u"horizontalLayout_group")

        self.verticalLayout.addLayout(self.horizontalLayout_group)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5168\u5c40\u7ffb\u9875", None))
        self.toolButton_previous2.setText(QCoreApplication.translate("Form", u"previous2", None))
        self.toolButton_previous.setText(QCoreApplication.translate("Form", u"previous", None))
        self.toolButton_next.setText(QCoreApplication.translate("Form", u"next", None))
        self.toolButton_next2.setText(QCoreApplication.translate("Form", u"next2", None))
        self.toolButton_reset.setText(QCoreApplication.translate("Form", u"reset", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.checkBox_auto_calc_similar.setText(QCoreApplication.translate("Form", u"\u5b9e\u65f6\u663e\u793a\u76f8\u4f3c\u5ea6", None))
        self.checkBox_auto_image_diff.setText(QCoreApplication.translate("Form", u"\u5b9e\u65f6\u663e\u793a\u56fe\u7247\u5dee\u5f02", None))
    # retranslateUi

