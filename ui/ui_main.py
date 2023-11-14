# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainRSDjfI.ui'
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
        MainWindow.resize(678, 502)
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
        self.horizontalLayout = QHBoxLayout(self.groupBox_button)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_start = QPushButton(self.groupBox_button)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout.addWidget(self.pushButton_start)

        self.pushButton_stop = QPushButton(self.groupBox_button)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout.addWidget(self.pushButton_stop)


        self.verticalLayout_3.addWidget(self.groupBox_button)

        self.groupBox_folderlist = QGroupBox(self.centralwidget)
        self.groupBox_folderlist.setObjectName(u"groupBox_folderlist")
        self.groupBox_folderlist.setMinimumSize(QSize(0, 160))
        self.groupBox_folderlist.setMaximumSize(QSize(180, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox_folderlist)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.groupBox_folderlist)

        self.groupBox_similar = QGroupBox(self.centralwidget)
        self.groupBox_similar.setObjectName(u"groupBox_similar")
        self.gridLayout = QGridLayout(self.groupBox_similar)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.checkBox_ahash = QCheckBox(self.groupBox_similar)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.checkBox_ahash)
        self.checkBox_ahash.setObjectName(u"checkBox_ahash")
        self.checkBox_ahash.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_ahash, 0, 0, 1, 1)

        self.spinBox_threshold_phash = QSpinBox(self.groupBox_similar)
        self.spinBox_threshold_phash.setObjectName(u"spinBox_threshold_phash")
        self.spinBox_threshold_phash.setMaximum(30)
        self.spinBox_threshold_phash.setValue(10)

        self.gridLayout.addWidget(self.spinBox_threshold_phash, 1, 1, 1, 1)

        self.checkBox_phash = QCheckBox(self.groupBox_similar)
        self.buttonGroup.addButton(self.checkBox_phash)
        self.checkBox_phash.setObjectName(u"checkBox_phash")
        self.checkBox_phash.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_phash, 1, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox_similar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 2)

        self.doubleSpinBox_threshold_ssim = QDoubleSpinBox(self.groupBox_similar)
        self.doubleSpinBox_threshold_ssim.setObjectName(u"doubleSpinBox_threshold_ssim")
        self.doubleSpinBox_threshold_ssim.setDecimals(2)
        self.doubleSpinBox_threshold_ssim.setMaximum(1.000000000000000)
        self.doubleSpinBox_threshold_ssim.setSingleStep(0.050000000000000)
        self.doubleSpinBox_threshold_ssim.setValue(0.900000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_threshold_ssim, 4, 1, 1, 1)

        self.spinBox_extract_image_number = QSpinBox(self.groupBox_similar)
        self.spinBox_extract_image_number.setObjectName(u"spinBox_extract_image_number")
        self.spinBox_extract_image_number.setMinimum(1)
        self.spinBox_extract_image_number.setMaximum(3)

        self.gridLayout.addWidget(self.spinBox_extract_image_number, 6, 1, 1, 1)

        self.checkBox_ssim = QCheckBox(self.groupBox_similar)
        self.checkBox_ssim.setObjectName(u"checkBox_ssim")

        self.gridLayout.addWidget(self.checkBox_ssim, 4, 0, 1, 1)

        self.label = QLabel(self.groupBox_similar)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.spinBox_threshold_ahash = QSpinBox(self.groupBox_similar)
        self.spinBox_threshold_ahash.setObjectName(u"spinBox_threshold_ahash")
        self.spinBox_threshold_ahash.setMaximum(30)
        self.spinBox_threshold_ahash.setValue(10)

        self.gridLayout.addWidget(self.spinBox_threshold_ahash, 0, 1, 1, 1)

        self.line = QFrame(self.groupBox_similar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)

        self.checkBox_dhash = QCheckBox(self.groupBox_similar)
        self.buttonGroup.addButton(self.checkBox_dhash)
        self.checkBox_dhash.setObjectName(u"checkBox_dhash")

        self.gridLayout.addWidget(self.checkBox_dhash, 2, 0, 1, 1)

        self.spinBox_threshold_dhash = QSpinBox(self.groupBox_similar)
        self.spinBox_threshold_dhash.setObjectName(u"spinBox_threshold_dhash")
        self.spinBox_threshold_dhash.setMaximum(30)
        self.spinBox_threshold_dhash.setValue(10)

        self.gridLayout.addWidget(self.spinBox_threshold_dhash, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_similar)

        self.groupBox_schedule = QGroupBox(self.centralwidget)
        self.groupBox_schedule.setObjectName(u"groupBox_schedule")
        self.gridLayout_2 = QGridLayout(self.groupBox_schedule)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
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

        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.groupBox_result = QGroupBox(self.centralwidget)
        self.groupBox_result.setObjectName(u"groupBox_result")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_result)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.treeWidget_show = QTreeWidget(self.groupBox_result)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_show.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_show.setObjectName(u"treeWidget_show")
        self.treeWidget_show.header().setVisible(False)

        self.verticalLayout_2.addWidget(self.treeWidget_show)


        self.horizontalLayout_2.addWidget(self.groupBox_result)

        self.horizontalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_button.setTitle(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.groupBox_folderlist.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.groupBox_similar.setTitle(QCoreApplication.translate("MainWindow", u"\u76f8\u4f3c\u5ea6\u7b97\u6cd5", None))
        self.checkBox_ahash.setText(QCoreApplication.translate("MainWindow", u"aHash", None))
        self.checkBox_phash.setText(QCoreApplication.translate("MainWindow", u"pHash", None))
        self.checkBox_ssim.setText(QCoreApplication.translate("MainWindow", u"SSIM", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u56fe\u7247\u6570", None))
        self.spinBox_threshold_ahash.setSuffix("")
        self.checkBox_dhash.setText(QCoreApplication.translate("MainWindow", u"dHash", None))
        self.groupBox_schedule.setTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u8fdb\u5ea6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8017\u65f6\uff1a", None))
        self.label_schedule_time.setText(QCoreApplication.translate("MainWindow", u"\u603b\u65f6\u95f4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6b65\u9aa4\uff1a", None))
        self.label_schedule_step.setText(QCoreApplication.translate("MainWindow", u"\u6b65\u9aa4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5b50\u8fdb\u5ea6\uff1a", None))
        self.label_schedule_rate.setText(QCoreApplication.translate("MainWindow", u"-/-", None))
        self.groupBox_result.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u7ed3\u679c", None))
    # retranslateUi

