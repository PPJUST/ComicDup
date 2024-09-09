# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_comic_infoMnJJPg.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(256, 270)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_type = QLabel(Form)
        self.label_type.setObjectName(u"label_type")

        self.horizontalLayout_2.addWidget(self.label_type)

        self.horizontalLayout_filename = QHBoxLayout()
        self.horizontalLayout_filename.setSpacing(0)
        self.horizontalLayout_filename.setObjectName(u"horizontalLayout_filename")

        self.horizontalLayout_2.addLayout(self.horizontalLayout_filename)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_filesize = QLabel(Form)
        self.label_filesize.setObjectName(u"label_filesize")

        self.horizontalLayout_3.addWidget(self.label_filesize)

        self.label_image_count = QLabel(Form)
        self.label_image_count.setObjectName(u"label_image_count")

        self.horizontalLayout_3.addWidget(self.label_image_count)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_preview = QLabel(self.frame)
        self.label_preview.setObjectName(u"label_preview")

        self.verticalLayout.addWidget(self.label_preview)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_view = QToolButton(Form)
        self.toolButton_view.setObjectName(u"toolButton_view")

        self.horizontalLayout.addWidget(self.toolButton_view)

        self.toolButton_open_file = QToolButton(Form)
        self.toolButton_open_file.setObjectName(u"toolButton_open_file")

        self.horizontalLayout.addWidget(self.toolButton_open_file)

        self.toolButton_delete = QToolButton(Form)
        self.toolButton_delete.setObjectName(u"toolButton_delete")

        self.horizontalLayout.addWidget(self.toolButton_delete)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_type.setText(QCoreApplication.translate("Form", u"icon", None))
        self.label_filesize.setText(QCoreApplication.translate("Form", u"filesize", None))
        self.label_image_count.setText(QCoreApplication.translate("Form", u"image_count", None))
        self.label_preview.setText(QCoreApplication.translate("Form", u"preview", None))
        self.toolButton_view.setText(QCoreApplication.translate("Form", u"view", None))
        self.toolButton_open_file.setText(QCoreApplication.translate("Form", u"open", None))
        self.toolButton_delete.setText(QCoreApplication.translate("Form", u"delete", None))
    # retranslateUi

