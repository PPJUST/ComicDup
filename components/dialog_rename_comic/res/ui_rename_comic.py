# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rename_comiccOZuzm.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(343, 494)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_original_filename = QLineEdit(Dialog)
        self.lineEdit_original_filename.setObjectName(u"lineEdit_original_filename")

        self.gridLayout.addWidget(self.lineEdit_original_filename, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_new_filename = QLineEdit(Dialog)
        self.lineEdit_new_filename.setObjectName(u"lineEdit_new_filename")

        self.gridLayout.addWidget(self.lineEdit_new_filename, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_auto_dup_name = QCheckBox(Dialog)
        self.checkBox_auto_dup_name.setObjectName(u"checkBox_auto_dup_name")

        self.horizontalLayout.addWidget(self.checkBox_auto_dup_name)

        self.lineEdit_suffix = QLineEdit(Dialog)
        self.lineEdit_suffix.setObjectName(u"lineEdit_suffix")

        self.horizontalLayout.addWidget(self.lineEdit_suffix)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_rename = QPushButton(Dialog)
        self.pushButton_rename.setObjectName(u"pushButton_rename")

        self.horizontalLayout_2.addWidget(self.pushButton_rename)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_quit = QPushButton(Dialog)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.horizontalLayout_2.addWidget(self.pushButton_quit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_rename_pattern = QCheckBox(Dialog)
        self.checkBox_rename_pattern.setObjectName(u"checkBox_rename_pattern")

        self.horizontalLayout_3.addWidget(self.checkBox_rename_pattern)

        self.comboBox_rename_pattern = QComboBox(Dialog)
        self.comboBox_rename_pattern.setObjectName(u"comboBox_rename_pattern")

        self.horizontalLayout_3.addWidget(self.comboBox_rename_pattern)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_choose_field = QCheckBox(Dialog)
        self.checkBox_choose_field.setObjectName(u"checkBox_choose_field")

        self.horizontalLayout_4.addWidget(self.checkBox_choose_field)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.label_field_pattern = QLabel(Dialog)
        self.label_field_pattern.setObjectName(u"label_field_pattern")

        self.horizontalLayout_4.addWidget(self.label_field_pattern)

        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, -1, -1, -1)
        self.toolButton_add_circle = QToolButton(Dialog)
        self.toolButton_add_circle.setObjectName(u"toolButton_add_circle")

        self.gridLayout_2.addWidget(self.toolButton_add_circle, 0, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.lineEdit_circle = QLineEdit(Dialog)
        self.lineEdit_circle.setObjectName(u"lineEdit_circle")

        self.gridLayout_2.addWidget(self.lineEdit_circle, 0, 2, 1, 1)

        self.toolButton_add_artist = QToolButton(Dialog)
        self.toolButton_add_artist.setObjectName(u"toolButton_add_artist")

        self.gridLayout_2.addWidget(self.toolButton_add_artist, 1, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.lineEdit_artist = QLineEdit(Dialog)
        self.lineEdit_artist.setObjectName(u"lineEdit_artist")

        self.gridLayout_2.addWidget(self.lineEdit_artist, 1, 2, 1, 1)

        self.toolButton_add_title = QToolButton(Dialog)
        self.toolButton_add_title.setObjectName(u"toolButton_add_title")

        self.gridLayout_2.addWidget(self.toolButton_add_title, 2, 0, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)

        self.lineEdit_title = QLineEdit(Dialog)
        self.lineEdit_title.setObjectName(u"lineEdit_title")

        self.gridLayout_2.addWidget(self.lineEdit_title, 2, 2, 1, 1)

        self.toolButton_add_convention = QToolButton(Dialog)
        self.toolButton_add_convention.setObjectName(u"toolButton_add_convention")

        self.gridLayout_2.addWidget(self.toolButton_add_convention, 3, 0, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 1, 1, 1)

        self.lineEdit_convention = QLineEdit(Dialog)
        self.lineEdit_convention.setObjectName(u"lineEdit_convention")

        self.gridLayout_2.addWidget(self.lineEdit_convention, 3, 2, 1, 1)

        self.toolButton_add_parody = QToolButton(Dialog)
        self.toolButton_add_parody.setObjectName(u"toolButton_add_parody")

        self.gridLayout_2.addWidget(self.toolButton_add_parody, 4, 0, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 4, 1, 1, 1)

        self.lineEdit_parody = QLineEdit(Dialog)
        self.lineEdit_parody.setObjectName(u"lineEdit_parody")

        self.gridLayout_2.addWidget(self.lineEdit_parody, 4, 2, 1, 1)

        self.toolButton_add_language = QToolButton(Dialog)
        self.toolButton_add_language.setObjectName(u"toolButton_add_language")

        self.gridLayout_2.addWidget(self.toolButton_add_language, 5, 0, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 5, 1, 1, 1)

        self.lineEdit_language = QLineEdit(Dialog)
        self.lineEdit_language.setObjectName(u"lineEdit_language")

        self.gridLayout_2.addWidget(self.lineEdit_language, 5, 2, 1, 1)

        self.toolButton_add_translator = QToolButton(Dialog)
        self.toolButton_add_translator.setObjectName(u"toolButton_add_translator")

        self.gridLayout_2.addWidget(self.toolButton_add_translator, 6, 0, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 6, 1, 1, 1)

        self.lineEdit_translator = QLineEdit(Dialog)
        self.lineEdit_translator.setObjectName(u"lineEdit_translator")

        self.gridLayout_2.addWidget(self.lineEdit_translator, 6, 2, 2, 1)

        self.toolButton_add_special_indicator = QToolButton(Dialog)
        self.toolButton_add_special_indicator.setObjectName(u"toolButton_add_special_indicator")

        self.gridLayout_2.addWidget(self.toolButton_add_special_indicator, 7, 0, 2, 1)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 7, 1, 2, 1)

        self.lineEdit_special_indicator = QLineEdit(Dialog)
        self.lineEdit_special_indicator.setObjectName(u"lineEdit_special_indicator")

        self.gridLayout_2.addWidget(self.lineEdit_special_indicator, 8, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u91cd\u547d\u540d", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u539f\u6587\u4ef6\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u65b0\u6587\u4ef6\u540d\uff1a", None))
        self.checkBox_auto_dup_name.setText(QCoreApplication.translate("Dialog", u"\u81ea\u52a8\u5904\u7406\u91cd\u590d\u6587\u4ef6\u540d\uff0c\u6dfb\u52a0\u6307\u5b9a\u540e\u7f00", None))
        self.pushButton_rename.setText(QCoreApplication.translate("Dialog", u"\u91cd\u547d\u540d", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
        self.checkBox_rename_pattern.setText(QCoreApplication.translate("Dialog", u"\u547d\u540d\u6a21\u677f", None))
        self.checkBox_choose_field.setText(QCoreApplication.translate("Dialog", u"\u624b\u52a8\u6dfb\u52a0", None))
        self.label_field_pattern.setText(QCoreApplication.translate("Dialog", u"\u6a21\u677f\u9884\u89c8", None))
        self.toolButton_add_circle.setText(QCoreApplication.translate("Dialog", u"\uff0b", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u793e\u56e2", None))
        self.toolButton_add_artist.setText(QCoreApplication.translate("Dialog", u"\uff0b", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u4f5c\u8005", None))
        self.toolButton_add_title.setText(QCoreApplication.translate("Dialog", u"\uff0b", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u6807\u9898", None))
        self.toolButton_add_convention.setText(QCoreApplication.translate("Dialog", u"\uff0b", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u5373\u5356\u4f1a", None))
        self.toolButton_add_parody.setText(QCoreApplication.translate("Dialog", u"\uff0b", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u539f\u4f5c", None))
        self.toolButton_add_language.setText(QCoreApplication.translate("Dialog", u"\uff0b", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u8bed\u8a00", None))
        self.toolButton_add_translator.setText(QCoreApplication.translate("Dialog", u"\uff0b", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u8bd1\u8005", None))
        self.toolButton_add_special_indicator.setText(QCoreApplication.translate("Dialog", u"\uff0b", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u6807\u793a", None))
    # retranslateUi

