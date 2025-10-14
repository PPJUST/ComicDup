# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowPLdxIc.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_home)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_exec = QGroupBox(self.tab_home)
        self.groupBox_exec.setObjectName(u"groupBox_exec")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_exec)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.groupBox_exec)

        self.groupBox_setting = QGroupBox(self.tab_home)
        self.groupBox_setting.setObjectName(u"groupBox_setting")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_setting)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_setting_1 = QVBoxLayout()
        self.verticalLayout_setting_1.setSpacing(3)
        self.verticalLayout_setting_1.setObjectName(u"verticalLayout_setting_1")

        self.verticalLayout_6.addLayout(self.verticalLayout_setting_1)

        self.line = QFrame(self.groupBox_setting)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.verticalLayout_setting_2 = QVBoxLayout()
        self.verticalLayout_setting_2.setSpacing(3)
        self.verticalLayout_setting_2.setObjectName(u"verticalLayout_setting_2")

        self.verticalLayout_6.addLayout(self.verticalLayout_setting_2)

        self.line_2 = QFrame(self.groupBox_setting)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)

        self.verticalLayout_setting_3 = QVBoxLayout()
        self.verticalLayout_setting_3.setSpacing(3)
        self.verticalLayout_setting_3.setObjectName(u"verticalLayout_setting_3")

        self.verticalLayout_6.addLayout(self.verticalLayout_setting_3)


        self.verticalLayout_3.addWidget(self.groupBox_setting)

        self.groupBox_cache = QGroupBox(self.tab_home)
        self.groupBox_cache.setObjectName(u"groupBox_cache")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_cache)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.groupBox_cache)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.stackedWidget = QStackedWidget(self.tab_home)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_search_list = QGroupBox(self.page)
        self.groupBox_search_list.setObjectName(u"groupBox_search_list")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_search_list)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)

        self.verticalLayout.addWidget(self.groupBox_search_list)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_back_to_search_list = QPushButton(self.page_2)
        self.pushButton_back_to_search_list.setObjectName(u"pushButton_back_to_search_list")

        self.horizontalLayout_3.addWidget(self.pushButton_back_to_search_list)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.groupBox_runtime_info = QGroupBox(self.page_2)
        self.groupBox_runtime_info.setObjectName(u"groupBox_runtime_info")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_runtime_info)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)

        self.verticalLayout_2.addWidget(self.groupBox_runtime_info)

        self.verticalLayout_2.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.tabWidget.addTab(self.tab_home, "")
        self.tab_result = QWidget()
        self.tab_result.setObjectName(u"tab_result")
        self.verticalLayout_4 = QVBoxLayout(self.tab_result)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.groupBox_result_filter = QGroupBox(self.tab_result)
        self.groupBox_result_filter.setObjectName(u"groupBox_result_filter")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_result_filter)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)

        self.verticalLayout_4.addWidget(self.groupBox_result_filter)

        self.groupBox_result_preview = QGroupBox(self.tab_result)
        self.groupBox_result_preview.setObjectName(u"groupBox_result_preview")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_result_preview)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)

        self.verticalLayout_4.addWidget(self.groupBox_result_preview)

        self.verticalLayout_4.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_result, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ComicDup", None))
        self.groupBox_exec.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u533a", None))
        self.groupBox_setting.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9009\u9879", None))
        self.groupBox_cache.setTitle(QCoreApplication.translate("MainWindow", u"\u7f13\u5b58\u7ba1\u7406", None))
        self.groupBox_search_list.setTitle(QCoreApplication.translate("MainWindow", u"\u68c0\u7d22\u8def\u5f84", None))
        self.pushButton_back_to_search_list.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u81f3\u68c0\u7d22\u8def\u5f84\u9875", None))
        self.groupBox_runtime_info.setTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u4fe1\u606f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.groupBox_result_filter.setTitle(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009\u5668", None))
        self.groupBox_result_preview.setTitle(QCoreApplication.translate("MainWindow", u"\u76f8\u4f3c\u7ec4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_result), QCoreApplication.translate("MainWindow", u"\u5339\u914d\u7ed3\u679c", None))
    # retranslateUi

