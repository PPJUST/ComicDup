# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_algorithmxRIqpP.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(190, 107)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_basic_algorithm = QComboBox(Form)
        self.comboBox_basic_algorithm.setObjectName(u"comboBox_basic_algorithm")

        self.horizontalLayout.addWidget(self.comboBox_basic_algorithm)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_enhance_algorithm = QCheckBox(Form)
        self.checkBox_enhance_algorithm.setObjectName(u"checkBox_enhance_algorithm")

        self.horizontalLayout_2.addWidget(self.checkBox_enhance_algorithm)

        self.comboBox_enhance_algorithm = QComboBox(Form)
        self.comboBox_enhance_algorithm.setObjectName(u"comboBox_enhance_algorithm")

        self.horizontalLayout_2.addWidget(self.comboBox_enhance_algorithm)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_similarity_threshold = QSpinBox(Form)
        self.spinBox_similarity_threshold.setObjectName(u"spinBox_similarity_threshold")
        self.spinBox_similarity_threshold.setMinimum(50)
        self.spinBox_similarity_threshold.setMaximum(100)

        self.horizontalLayout_3.addWidget(self.spinBox_similarity_threshold)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBox_hash_length = QComboBox(Form)
        self.comboBox_hash_length.setObjectName(u"comboBox_hash_length")

        self.horizontalLayout_4.addWidget(self.comboBox_hash_length)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700;\">aHash</span>\uff1a\u5747\u503c\u54c8\u5e0c\uff0c\u8ba1\u7b97\u6700\u5feb\uff0c\u6548\u679c\u6700\u5dee</p><p><span style=\" font-weight:700;\">pHash</span>\uff1a\u611f\u77e5\u54c8\u5e0c\uff0c\u8ba1\u7b97\u6700\u6162\uff0c\u6548\u679c\u6700\u597d</p><p><span style=\" font-weight:700;\">dHash</span>\uff1a\u5dee\u5f02\u54c8\u5e0c\uff0c\u8ba1\u7b97\u4e2d\u7b49\uff0c\u6548\u679c\u4e2d\u7b49</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"\u57fa\u7840\u7b97\u6cd5", None))
#if QT_CONFIG(tooltip)
        self.comboBox_basic_algorithm.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:700;\">aHash</span>\uff1a\u5747\u503c\u54c8\u5e0c\uff0c\u8ba1\u7b97\u6700\u5feb\uff0c\u6548\u679c\u6700\u5dee</p><p><span style=\" font-weight:700;\">pHash</span>\uff1a\u611f\u77e5\u54c8\u5e0c\uff0c\u8ba1\u7b97\u6700\u6162\uff0c\u6548\u679c\u6700\u597d</p><p><span style=\" font-weight:700;\">dHash</span>\uff1a\u5dee\u5f02\u54c8\u5e0c\uff0c\u8ba1\u7b97\u4e2d\u7b49\uff0c\u6548\u679c\u4e2d\u7b49</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_enhance_algorithm.setText(QCoreApplication.translate("Form", u"\u589e\u5f3a\u7b97\u6cd5\u518d\u6821\u9a8c", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5224\u65ad\u4e3a\u56fe\u7247\u76f8\u4f3c\u7684\u6700\u4f4e\u76f8\u4f3c\u5ea6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"\u76f8\u4f3c\u5ea6\u9608\u503c", None))
#if QT_CONFIG(tooltip)
        self.spinBox_similarity_threshold.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5224\u65ad\u4e3a\u56fe\u7247\u76f8\u4f3c\u7684\u6700\u4f4e\u76f8\u4f3c\u5ea6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"%", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8ba1\u7b97\u56fe\u7247\u54c8\u5e0c\u7684\u54c8\u5e0c\u957f\u5ea6\uff0c\u957f\u5ea6\u8d8a\u957f\u8ba1\u7b97\u7ed3\u679c\u7cbe\u786e\u4f46\u8ba1\u7b97\u901f\u5ea6\u8d8a\u6162</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Hash\u957f\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.comboBox_hash_length.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u8ba1\u7b97\u56fe\u7247\u54c8\u5e0c\u7684\u54c8\u5e0c\u957f\u5ea6\uff0c\u957f\u5ea6\u8d8a\u957f\u8ba1\u7b97\u7ed3\u679c\u7cbe\u786e\u4f46\u8ba1\u7b97\u901f\u5ea6\u8d8a\u6162</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

