# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwBBZMF.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(890, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_button = QGroupBox(self.centralwidget)
        self.groupBox_button.setObjectName(u"groupBox_button")
        self.groupBox_button.setFocusPolicy(Qt.NoFocus)
        self.groupBox_button.setAutoFillBackground(False)
        self.groupBox_button.setFlat(False)
        self.gridLayout_3 = QGridLayout(self.groupBox_button)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 3)
        self.pushButton_start = QPushButton(self.groupBox_button)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.gridLayout_3.addWidget(self.pushButton_start, 0, 0, 1, 1)

        self.pushButton_stop = QPushButton(self.groupBox_button)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.gridLayout_3.addWidget(self.pushButton_stop, 0, 1, 1, 1)

        self.pushButton_refresh_result = QPushButton(self.groupBox_button)
        self.pushButton_refresh_result.setObjectName(u"pushButton_refresh_result")

        self.gridLayout_3.addWidget(self.pushButton_refresh_result, 1, 0, 1, 1)

        self.pushButton_cache_setting = QPushButton(self.groupBox_button)
        self.pushButton_cache_setting.setObjectName(u"pushButton_cache_setting")

        self.gridLayout_3.addWidget(self.pushButton_cache_setting, 2, 0, 1, 1)

        self.pushButton_load_result = QPushButton(self.groupBox_button)
        self.pushButton_load_result.setObjectName(u"pushButton_load_result")

        self.gridLayout_3.addWidget(self.pushButton_load_result, 1, 1, 1, 1)

        self.pushButton_info = QPushButton(self.groupBox_button)
        self.pushButton_info.setObjectName(u"pushButton_info")

        self.gridLayout_3.addWidget(self.pushButton_info, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_button)

        self.groupBox_similar = QGroupBox(self.centralwidget)
        self.groupBox_similar.setObjectName(u"groupBox_similar")
        self.gridLayout_4 = QGridLayout(self.groupBox_similar)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 0, 3, 3)
        self.line_2 = QFrame(self.groupBox_similar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 3, 0, 1, 3)

        self.spinBox_threshold_hash = QSpinBox(self.groupBox_similar)
        self.spinBox_threshold_hash.setObjectName(u"spinBox_threshold_hash")
        self.spinBox_threshold_hash.setMinimum(50)
        self.spinBox_threshold_hash.setMaximum(100)
        self.spinBox_threshold_hash.setValue(85)

        self.gridLayout_4.addWidget(self.spinBox_threshold_hash, 0, 1, 1, 1)

        self.spinBox_threshold_ssim = QSpinBox(self.groupBox_similar)
        self.spinBox_threshold_ssim.setObjectName(u"spinBox_threshold_ssim")
        self.spinBox_threshold_ssim.setMinimum(50)
        self.spinBox_threshold_ssim.setMaximum(100)
        self.spinBox_threshold_ssim.setValue(85)

        self.gridLayout_4.addWidget(self.spinBox_threshold_ssim, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_similar)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 4, 2, 1, 1)

        self.checkBox_ssim = QCheckBox(self.groupBox_similar)
        self.checkBox_ssim.setObjectName(u"checkBox_ssim")
        self.checkBox_ssim.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_ssim, 2, 0, 1, 1)

        self.comboBox_hash = QComboBox(self.groupBox_similar)
        self.comboBox_hash.addItem("")
        self.comboBox_hash.addItem("")
        self.comboBox_hash.addItem("")
        self.comboBox_hash.setObjectName(u"comboBox_hash")

        self.gridLayout_4.addWidget(self.comboBox_hash, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_similar)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox_similar)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 4, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_similar)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 2, 2, 1, 1)

        self.spinBox_extract_image_number = QSpinBox(self.groupBox_similar)
        self.spinBox_extract_image_number.setObjectName(u"spinBox_extract_image_number")
        self.spinBox_extract_image_number.setMinimum(1)
        self.spinBox_extract_image_number.setMaximum(3)

        self.gridLayout_4.addWidget(self.spinBox_extract_image_number, 4, 1, 1, 1)

        self.line = QFrame(self.groupBox_similar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 1, 0, 1, 3)

        self.spinBox_thread_number = QSpinBox(self.groupBox_similar)
        self.spinBox_thread_number.setObjectName(u"spinBox_thread_number")
        self.spinBox_thread_number.setMinimum(1)
        self.spinBox_thread_number.setMaximum(4)

        self.gridLayout_4.addWidget(self.spinBox_thread_number, 6, 1, 1, 1)

        self.line_3 = QFrame(self.groupBox_similar)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 5, 0, 1, 3)

        self.label_7 = QLabel(self.groupBox_similar)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 6, 0, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)

        self.verticalLayout_3.addWidget(self.groupBox_similar)

        self.groupBox_folderlist = QGroupBox(self.centralwidget)
        self.groupBox_folderlist.setObjectName(u"groupBox_folderlist")
        self.groupBox_folderlist.setMinimumSize(QSize(0, 160))
        self.groupBox_folderlist.setMaximumSize(QSize(180, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox_folderlist)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 3)

        self.verticalLayout_3.addWidget(self.groupBox_folderlist)

        self.groupBox_schedule = QGroupBox(self.centralwidget)
        self.groupBox_schedule.setObjectName(u"groupBox_schedule")
        self.gridLayout_2 = QGridLayout(self.groupBox_schedule)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 3, 3)
        self.label_2 = QLabel(self.groupBox_schedule)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_schedule_time = QLabel(self.groupBox_schedule)
        self.label_schedule_time.setObjectName(u"label_schedule_time")

        self.gridLayout_2.addWidget(self.label_schedule_time, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_schedule)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_schedule_step = QLabel(self.groupBox_schedule)
        self.label_schedule_step.setObjectName(u"label_schedule_step")

        self.gridLayout_2.addWidget(self.label_schedule_step, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_schedule)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_schedule_rate = QLabel(self.groupBox_schedule)
        self.label_schedule_rate.setObjectName(u"label_schedule_rate")

        self.gridLayout_2.addWidget(self.label_schedule_rate, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_schedule)

        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.groupBox_comics = QGroupBox(self.centralwidget)
        self.groupBox_comics.setObjectName(u"groupBox_comics")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_comics)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.groupBox_comics)

        self.horizontalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Doudup", None))
        self.groupBox_button.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u533a", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.pushButton_refresh_result.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u7ed3\u679c", None))
        self.pushButton_cache_setting.setText(QCoreApplication.translate("MainWindow", u"\u7f13\u5b58\u8bbe\u7f6e", None))
        self.pushButton_load_result.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u7ed3\u679c", None))
        self.pushButton_info.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u8bf4\u660e", None))
        self.groupBox_similar.setTitle(QCoreApplication.translate("MainWindow", u"\u76f8\u4f3c\u5ea6\u7b97\u6cd5\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5f20", None))
#if QT_CONFIG(tooltip)
        self.checkBox_ssim.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u7ed3\u6784\u76f8\u4f3c\u6027\uff0c\u8d8a\u5927\u8d8a\u76f8\u4f3c\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_ssim.setText(QCoreApplication.translate("MainWindow", u"SSIM", None))
        self.comboBox_hash.setItemText(0, QCoreApplication.translate("MainWindow", u"ahash", None))
        self.comboBox_hash.setItemText(1, QCoreApplication.translate("MainWindow", u"phash", None))
        self.comboBox_hash.setItemText(2, QCoreApplication.translate("MainWindow", u"dhash", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4ece\u6bcf\u4e2a\u6587\u4ef6\u5939/\u538b\u7f29\u5305\u4e2d\u63d0\u53d6\u7684\u56fe\u7247\u6570\uff0c\u63d0\u53d6\u6570\u8d8a\u591a\u8ba1\u7b97\u91cf\u8d8a\u5927\uff08\u4e0d\u6b62\u7ffb\u500d\uff09</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u56fe\u7247\u6570", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4ece\u6bcf\u4e2a\u6587\u4ef6\u5939/\u538b\u7f29\u5305\u4e2d\u63d0\u53d6\u7684\u56fe\u7247\u6570\uff0c\u63d0\u53d6\u6570\u8d8a\u591a\u8ba1\u7b97\u91cf\u8d8a\u5927\uff08\u4e0d\u6b62\u7ffb\u500d\uff09</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u7a0b\u6570", None))
        self.groupBox_folderlist.setTitle(QCoreApplication.translate("MainWindow", u"\u62d6\u5165\u9700\u8981\u67e5\u8be2\u7684\u6587\u4ef6\u5939", None))
        self.groupBox_schedule.setTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u8fdb\u5ea6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8017\u65f6\uff1a", None))
        self.label_schedule_time.setText(QCoreApplication.translate("MainWindow", u"\u603b\u65f6\u95f4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6b65\u9aa4\uff1a", None))
        self.label_schedule_step.setText(QCoreApplication.translate("MainWindow", u"\u6b65\u9aa4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5b50\u8fdb\u5ea6\uff1a", None))
        self.label_schedule_rate.setText(QCoreApplication.translate("MainWindow", u"-/-", None))
        self.groupBox_comics.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u7ed3\u679c", None))
    # retranslateUi

