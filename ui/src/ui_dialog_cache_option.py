# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_cache_optionHDqgnm.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(263, 164)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_comic_count = QLabel(self.groupBox)
        self.label_comic_count.setObjectName(u"label_comic_count")

        self.horizontalLayout_2.addWidget(self.label_comic_count)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_image_count = QLabel(self.groupBox)
        self.label_image_count.setObjectName(u"label_image_count")

        self.horizontalLayout_3.addWidget(self.label_image_count)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label_db_filesize = QLabel(self.groupBox)
        self.label_db_filesize.setObjectName(u"label_db_filesize")

        self.horizontalLayout_4.addWidget(self.label_db_filesize)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.label_preview_filesize = QLabel(self.groupBox)
        self.label_preview_filesize.setObjectName(u"label_preview_filesize")

        self.horizontalLayout_5.addWidget(self.label_preview_filesize)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_check_dup_inside = QPushButton(Dialog)
        self.pushButton_check_dup_inside.setObjectName(u"pushButton_check_dup_inside")

        self.verticalLayout.addWidget(self.pushButton_check_dup_inside)

        self.pushButton_update_cache = QPushButton(Dialog)
        self.pushButton_update_cache.setObjectName(u"pushButton_update_cache")

        self.verticalLayout.addWidget(self.pushButton_update_cache)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.pushButton_delete_error_data = QPushButton(Dialog)
        self.pushButton_delete_error_data.setObjectName(u"pushButton_delete_error_data")

        self.verticalLayout.addWidget(self.pushButton_delete_error_data)

        self.pushButton_clear_cache = QPushButton(Dialog)
        self.pushButton_clear_cache.setObjectName(u"pushButton_clear_cache")

        self.verticalLayout.addWidget(self.pushButton_clear_cache)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.pushButton_quit = QPushButton(Dialog)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.verticalLayout.addWidget(self.pushButton_quit)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7f13\u5b58", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u7f13\u5b58\u6570\u636e", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u7f13\u5b58\u6f2b\u753b\u6570\uff1a", None))
        self.label_comic_count.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7f13\u5b58\u56fe\u7247\u6570\uff1a", None))
        self.label_image_count.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6570\u636e\u5e93\u5360\u7528\u7a7a\u95f4\uff1a", None))
        self.label_db_filesize.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"MB", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u9884\u89c8\u56fe\u5360\u7528\u7a7a\u95f4\uff1a", None))
        self.label_preview_filesize.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"MB", None))
        self.pushButton_check_dup_inside.setText(QCoreApplication.translate("Dialog", u"\u7f13\u5b58\u5185\u90e8\u67e5\u91cd", None))
        self.pushButton_update_cache.setText(QCoreApplication.translate("Dialog", u"\u66f4\u65b0\u7f13\u5b58\u6570\u636e", None))
        self.pushButton_delete_error_data.setText(QCoreApplication.translate("Dialog", u"\u6e05\u9664\u65e0\u6548\u6570\u636e", None))
        self.pushButton_clear_cache.setText(QCoreApplication.translate("Dialog", u"\u6e05\u7a7a\u7f13\u5b58", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
    # retranslateUi

