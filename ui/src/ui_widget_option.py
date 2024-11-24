# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_optionifFeqG.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(258, 248)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.spinBox_similarity_threshold = QSpinBox(self.groupBox)
        self.spinBox_similarity_threshold.setObjectName(u"spinBox_similarity_threshold")

        self.horizontalLayout_6.addWidget(self.spinBox_similarity_threshold)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_hash_algorithm = QComboBox(self.groupBox)
        self.comboBox_hash_algorithm.setObjectName(u"comboBox_hash_algorithm")

        self.horizontalLayout.addWidget(self.comboBox_hash_algorithm)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_ssim = QCheckBox(self.groupBox)
        self.checkBox_ssim.setObjectName(u"checkBox_ssim")

        self.horizontalLayout_2.addWidget(self.checkBox_ssim)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.checkBox_match_similar = QCheckBox(self.groupBox)
        self.checkBox_match_similar.setObjectName(u"checkBox_match_similar")

        self.verticalLayout.addWidget(self.checkBox_match_similar)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_match_cache = QCheckBox(self.groupBox)
        self.checkBox_match_cache.setObjectName(u"checkBox_match_cache")

        self.horizontalLayout_7.addWidget(self.checkBox_match_cache)

        self.pushButton_cache_option = QPushButton(self.groupBox)
        self.pushButton_cache_option.setObjectName(u"pushButton_cache_option")

        self.horizontalLayout_7.addWidget(self.pushButton_cache_option)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.spinBox_extract_images = QSpinBox(self.groupBox)
        self.spinBox_extract_images.setObjectName(u"spinBox_extract_images")

        self.horizontalLayout_3.addWidget(self.spinBox_extract_images)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.comboBox_image_size = QComboBox(self.groupBox)
        self.comboBox_image_size.setObjectName(u"comboBox_image_size")

        self.horizontalLayout_8.addWidget(self.comboBox_image_size)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.spinBox_threads = QSpinBox(self.groupBox)
        self.spinBox_threads.setObjectName(u"spinBox_threads")

        self.horizontalLayout_4.addWidget(self.spinBox_threads)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u76f8\u4f3c\u7b97\u6cd5\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u76f8\u4f3c\u5ea6\u9608\u503c\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"%", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u57fa\u7840\u5339\u914d\u7b97\u6cd5\uff1a", None))
        self.checkBox_ssim.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u989d\u5916\u76f8\u4f3c\u6821\u9a8c\u7b97\u6cd5\uff1aSSIM\u6821\u9a8c", None))
        self.checkBox_match_similar.setText(QCoreApplication.translate("Form", u"\u4ec5\u5339\u914d\u76f8\u4f3c\u6587\u4ef6\u540d\u7684\u9879\u76ee", None))
        self.checkBox_match_cache.setText(QCoreApplication.translate("Form", u"\u5339\u914d\u7f13\u5b58\u6570\u636e", None))
        self.pushButton_cache_option.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u7f13\u5b58", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u6bcf\u672c\u6f2b\u753b\u63d0\u53d6\u56fe\u7247\u6570\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5f20", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u8ba1\u7b97\u5c3a\u5bf8\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u591a\u7ebf\u7a0b-\u7ebf\u7a0b\u6570\uff1a", None))
    # retranslateUi

