# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'similar_result_filterMTnjCi.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(650, 83)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_refresh_result = QPushButton(Form)
        self.pushButton_refresh_result.setObjectName(u"pushButton_refresh_result")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh_result.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh_result.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.pushButton_refresh_result)

        self.pushButton_hide_complete_group = QPushButton(Form)
        self.pushButton_hide_complete_group.setObjectName(u"pushButton_hide_complete_group")

        self.verticalLayout_3.addWidget(self.pushButton_hide_complete_group)

        self.verticalLayout_3.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_filter_same_items = QPushButton(Form)
        self.pushButton_filter_same_items.setObjectName(u"pushButton_filter_same_items")

        self.verticalLayout.addWidget(self.pushButton_filter_same_items)

        self.pushButton_filter_same_filesize_items = QPushButton(Form)
        self.pushButton_filter_same_filesize_items.setObjectName(u"pushButton_filter_same_filesize_items")

        self.verticalLayout.addWidget(self.pushButton_filter_same_filesize_items)

        self.pushButton_exclude_diff_pages = QPushButton(Form)
        self.pushButton_exclude_diff_pages.setObjectName(u"pushButton_exclude_diff_pages")

        self.verticalLayout.addWidget(self.pushButton_exclude_diff_pages)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Raised)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_sort_key = QComboBox(Form)
        self.comboBox_sort_key.setObjectName(u"comboBox_sort_key")

        self.horizontalLayout.addWidget(self.comboBox_sort_key)

        self.comboBox_sort_direction = QComboBox(Form)
        self.comboBox_sort_direction.setObjectName(u"comboBox_sort_direction")

        self.horizontalLayout.addWidget(self.comboBox_sort_direction)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_diff_pages_threshold = QSpinBox(Form)
        self.spinBox_diff_pages_threshold.setObjectName(u"spinBox_diff_pages_threshold")

        self.horizontalLayout_3.addWidget(self.spinBox_diff_pages_threshold)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_3.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Raised)
        self.line_2.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.checkBox_reconfirm_before_delete = QCheckBox(Form)
        self.checkBox_reconfirm_before_delete.setObjectName(u"checkBox_reconfirm_before_delete")
        self.checkBox_reconfirm_before_delete.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox_reconfirm_before_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(6, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_refresh_result.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e\u7ed3\u679c", None))
        self.pushButton_hide_complete_group.setText(QCoreApplication.translate("Form", u"\u5254\u9664\u5df2\u5b8c\u6210", None))
        self.pushButton_filter_same_items.setText(QCoreApplication.translate("Form", u"\u4ec5\u663e\u793a100%\u76f8\u540c\u9879", None))
        self.pushButton_filter_same_filesize_items.setText(QCoreApplication.translate("Form", u"\u4ec5\u663e\u793a\u6587\u4ef6\u5927\u5c0f\u76f8\u540c\u9879", None))
        self.pushButton_exclude_diff_pages.setText(QCoreApplication.translate("Form", u"\u5254\u9664\u9875\u6570\u5dee\u5f02\u8fc7\u5927\u9879", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7ec4\u5185\u6392\u5e8f\u89c4\u5219\uff1a", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9875\u6570\u9608\u503c\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u9875", None))
        self.label_5.setText("")
        self.checkBox_reconfirm_before_delete.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u6f2b\u753b\u524d\u9700\u518d\u6b21\u786e\u8ba4", None))
    # retranslateUi

