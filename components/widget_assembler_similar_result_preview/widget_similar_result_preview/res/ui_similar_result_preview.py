# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'similar_result_previewuNHxpv.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(484, 378)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_group_count = QLabel(Form)
        self.label_group_count.setObjectName(u"label_group_count")

        self.horizontalLayout.addWidget(self.label_group_count)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_comic_count = QLabel(Form)
        self.label_comic_count.setObjectName(u"label_comic_count")

        self.horizontalLayout.addWidget(self.label_comic_count)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.label_size_count = QLabel(Form)
        self.label_size_count.setObjectName(u"label_size_count")

        self.horizontalLayout.addWidget(self.label_size_count)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_show_group_count = QComboBox(Form)
        self.comboBox_show_group_count.addItem("")
        self.comboBox_show_group_count.addItem("")
        self.comboBox_show_group_count.addItem("")
        self.comboBox_show_group_count.addItem("")
        self.comboBox_show_group_count.addItem("")
        self.comboBox_show_group_count.addItem("")
        self.comboBox_show_group_count.setObjectName(u"comboBox_show_group_count")

        self.horizontalLayout.addWidget(self.comboBox_show_group_count)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget_group = QListWidget(Form)
        self.listWidget_group.setObjectName(u"listWidget_group")

        self.verticalLayout.addWidget(self.listWidget_group)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_previous_page = QPushButton(Form)
        self.pushButton_previous_page.setObjectName(u"pushButton_previous_page")

        self.horizontalLayout_2.addWidget(self.pushButton_previous_page)

        self.label_current_page = QLabel(Form)
        self.label_current_page.setObjectName(u"label_current_page")

        self.horizontalLayout_2.addWidget(self.label_current_page)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_total_page = QLabel(Form)
        self.label_total_page.setObjectName(u"label_total_page")

        self.horizontalLayout_2.addWidget(self.label_total_page)

        self.pushButton_next_page = QPushButton(Form)
        self.pushButton_next_page.setObjectName(u"pushButton_next_page")

        self.horizontalLayout_2.addWidget(self.pushButton_next_page)

        self.toolButton_jump_page = QToolButton(Form)
        self.toolButton_jump_page.setObjectName(u"toolButton_jump_page")

        self.horizontalLayout_2.addWidget(self.toolButton_jump_page)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5171", None))
        self.label_group_count.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7ec4", None))
        self.label_comic_count.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u9879", None))
        self.label_size_count.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u6bcf\u9875\u663e\u793a\u7ec4\u6570", None))
        self.comboBox_show_group_count.setItemText(0, QCoreApplication.translate("Form", u"5", None))
        self.comboBox_show_group_count.setItemText(1, QCoreApplication.translate("Form", u"10", None))
        self.comboBox_show_group_count.setItemText(2, QCoreApplication.translate("Form", u"15", None))
        self.comboBox_show_group_count.setItemText(3, QCoreApplication.translate("Form", u"20", None))
        self.comboBox_show_group_count.setItemText(4, QCoreApplication.translate("Form", u"30", None))
        self.comboBox_show_group_count.setItemText(5, QCoreApplication.translate("Form", u"50", None))

        self.pushButton_previous_page.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u9875", None))
        self.label_current_page.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"/", None))
        self.label_total_page.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_next_page.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u9875", None))
        self.toolButton_jump_page.setText(QCoreApplication.translate("Form", u"...", None))
    # retranslateUi

