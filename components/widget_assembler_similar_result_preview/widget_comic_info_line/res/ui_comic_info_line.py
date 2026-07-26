# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comic_info_linegpnQvo.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(580, 163)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_filepath = QLabel(Form)
        self.label_filepath.setObjectName(u"label_filepath")

        self.verticalLayout_2.addWidget(self.label_filepath)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolButton_open_path = QToolButton(Form)
        self.toolButton_open_path.setObjectName(u"toolButton_open_path")

        self.verticalLayout_3.addWidget(self.toolButton_open_path)

        self.toolButton_refresh = QToolButton(Form)
        self.toolButton_refresh.setObjectName(u"toolButton_refresh")

        self.verticalLayout_3.addWidget(self.toolButton_refresh)

        self.toolButton_delete = QToolButton(Form)
        self.toolButton_delete.setObjectName(u"toolButton_delete")

        self.verticalLayout_3.addWidget(self.toolButton_delete)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.label_preview = QLabel(Form)
        self.label_preview.setObjectName(u"label_preview")

        self.horizontalLayout_2.addWidget(self.label_preview)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_icon = QLabel(Form)
        self.label_icon.setObjectName(u"label_icon")

        self.horizontalLayout.addWidget(self.label_icon)

        self.label_filesize = QLabel(Form)
        self.label_filesize.setObjectName(u"label_filesize")

        self.horizontalLayout.addWidget(self.label_filesize)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_page_count = QLabel(Form)
        self.label_page_count.setObjectName(u"label_page_count")

        self.horizontalLayout_3.addWidget(self.label_page_count)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_file_time = QLabel(Form)
        self.label_file_time.setObjectName(u"label_file_time")

        self.verticalLayout.addWidget(self.label_file_time)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_language = QLabel(Form)
        self.label_language.setObjectName(u"label_language")

        self.gridLayout.addWidget(self.label_language, 3, 1, 1, 1)

        self.label_special_indicators = QLabel(Form)
        self.label_special_indicators.setObjectName(u"label_special_indicators")

        self.gridLayout.addWidget(self.label_special_indicators, 5, 1, 1, 1)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_convention_name = QLabel(Form)
        self.label_convention_name.setObjectName(u"label_convention_name")

        self.gridLayout.addWidget(self.label_convention_name, 2, 1, 1, 1)

        self.label_artist_name = QLabel(Form)
        self.label_artist_name.setObjectName(u"label_artist_name")

        self.gridLayout.addWidget(self.label_artist_name, 1, 1, 1, 1)

        self.label_circle_name = QLabel(Form)
        self.label_circle_name.setObjectName(u"label_circle_name")

        self.gridLayout.addWidget(self.label_circle_name, 0, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.label_translator = QLabel(Form)
        self.label_translator.setObjectName(u"label_translator")

        self.gridLayout.addWidget(self.label_translator, 4, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.label_similarity = QLabel(Form)
        self.label_similarity.setObjectName(u"label_similarity")

        self.horizontalLayout_2.addWidget(self.label_similarity)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_filepath.setText(QCoreApplication.translate("Form", u"filepath", None))
        self.toolButton_open_path.setText(QCoreApplication.translate("Form", u"open path", None))
        self.toolButton_refresh.setText(QCoreApplication.translate("Form", u"refresh", None))
        self.toolButton_delete.setText(QCoreApplication.translate("Form", u"delete", None))
        self.label_preview.setText(QCoreApplication.translate("Form", u"preview", None))
        self.label_icon.setText(QCoreApplication.translate("Form", u"filetype", None))
        self.label_filesize.setText(QCoreApplication.translate("Form", u"filesize", None))
        self.label_page_count.setText(QCoreApplication.translate("Form", u"page_count", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9875", None))
        self.label_file_time.setText(QCoreApplication.translate("Form", u"file time", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\uff1a", None))
        self.label_language.setText("")
        self.label_special_indicators.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u7279\u6b8a\u6807\u8bc6\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u8bed\u8a00\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u5373\u5356\u4f1a\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u793e\u56e2\uff1a", None))
        self.label_convention_name.setText("")
        self.label_artist_name.setText("")
        self.label_circle_name.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u8bd1\u8005\uff1a", None))
        self.label_translator.setText("")
        self.label_similarity.setText(QCoreApplication.translate("Form", u"similarity", None))
    # retranslateUi

