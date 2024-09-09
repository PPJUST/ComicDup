# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_informationljEfUl.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(810, 500)
        self.verticalLayout_5 = QVBoxLayout(dialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget_show = QStackedWidget(dialog)
        self.stackedWidget_show.setObjectName(u"stackedWidget_show")
        self.info = QWidget()
        self.info.setObjectName(u"info")
        self.verticalLayout = QVBoxLayout(self.info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.info)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.stackedWidget_show.addWidget(self.info)

        self.verticalLayout_5.addWidget(self.stackedWidget_show)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_last = QToolButton(dialog)
        self.toolButton_last.setObjectName(u"toolButton_last")

        self.horizontalLayout.addWidget(self.toolButton_last)

        self.toolButton_next = QToolButton(dialog)
        self.toolButton_next.setObjectName(u"toolButton_next")

        self.horizontalLayout.addWidget(self.toolButton_next)

        self.label_current_page = QLabel(dialog)
        self.label_current_page.setObjectName(u"label_current_page")

        self.horizontalLayout.addWidget(self.label_current_page)

        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_max_page = QLabel(dialog)
        self.label_max_page.setObjectName(u"label_max_page")

        self.horizontalLayout.addWidget(self.label_max_page)

        self.label_3 = QLabel(dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(dialog)

        self.stackedWidget_show.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u8bf4\u660e", None))
        self.textBrowser.setHtml(QCoreApplication.translate("dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u5f00\u6e90\u5730\u5740</span><span style=\" font-size:10pt;\">\uff1a</span><a href=\"https://github.com/PPJUST/ComicDup\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">\u70b9\u51fb\u76f4\u8fbe</span></a><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-"
                        "paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u4f7f\u7528\u6b65\u9aa4\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. \u5728\u6307\u5b9a\u533a\u57df\u62d6\u5165\u6587\u4ef6\u5939\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. \u8bbe\u7f6e\u76f8\u4f3c\u5ea6\u7b97\u6cd5\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. \u70b9\u51fb\u201c\u5f00\u59cb"
                        "\u201d\u6309\u94ae\uff0c\u5f00\u59cb\u5339\u914d\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u7a0b\u5e8f\u8fd0\u884c\u6b65\u9aa4\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. \u63d0\u53d6\u5bf9\u5e94\u6587\u4ef6\u5939\u4e2d\u7684\u6240\u6709\u6f2b\u753b\u6587\u4ef6\uff08\u5185\u90e8\u56fe\u7247\u6570&gt;=4\uff0c\u538b\u7f29\u5305\u4ec5\u652f\u6301zip\u3001rar\uff09\u3002</span></p>\n"
"<"
                        "p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. \u8ba1\u7b97\u6f2b\u753b\u4fe1\u606f\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. \u8ba1\u7b97\u6f2b\u753b\u4e2d\u6307\u5b9a\u6570\u91cf\u7684\u56fe\u7247\u7684Hash\u503c\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. \u5bf9\u6bd4\u56fe\u7247Hash\u503c\uff0c\u8ba1\u7b97\u6c49\u660e\u8ddd\u79bb\uff0c\u5224\u65ad\u662f\u5426\u76f8\u4f3c\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5. \u663e\u793a\u76f8\u4f3c\u7ed3\u679c\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:em"
                        "pty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u90e8\u5206\u529f\u80fd\u8bf4\u660e\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">1. \u6267\u884c\u533a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.1 \u52a0\u8f7d\u7ed3\u679c\uff1a\u52a0\u8f7d\u4e0a\u4e00\u6b21\u7684\u5339\u914d\u7ed3\u679c\u3002</span></p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">2.\u5339\u914d\u7ed3\u679c\u5904\u7406\u533a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.1 \u5237\u65b0\u7ed3\u679c\uff1a\u7b5b\u9009\u65e0\u6548\u7684\u9879\uff08\u672c\u5730\u4e0d\u5b58\u5728\u7684\u3001\u6587\u4ef6\u5185\u5bb9\u5df2\u4fee\u6539\u7684\uff09\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.2 \u7b5b\u9009\u56681 \u9875\u6570\u3001\u5927\u5c0f\u76f8\u540c\u9879\uff1a\u7b5b\u9009\u76f8\u540c\u7684\u9879\uff08"
                        "\u538b\u7f29\u5305\u7684\u6587\u4ef6\u5927\u5c0f\u4e3a\u89e3\u538b\u540e\u7684\u5927\u5c0f\uff09\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.3 \u7b5b\u9009\u56682 \u9875\u6570\u5dee\u5f02\u8fc7\u5927\u9879\uff1a\u6309\u7ec4\u5185\u6700\u5c0f\u9875\u6570*1.5\u4e3a\u4e0a\u9650\uff0c\u8d85\u8fc7\u7684\u9879\u4f1a\u88ab\u5254\u9664\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">3.\u76f8\u4f3c\u7b97\u6cd5\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fon"
                        "t-size:10pt;\">3.1 \u76f8\u4f3c\u5ea6\u9608\u503c\uff1a70%~100%\uff0c\u63a8\u8350\u8bbe\u7f6e\u4e3a90%\u4ee5\u4e0a\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.2 \u57fa\u7840\u5339\u914d\u7b97\u6cd5\uff1a\u8ba1\u7b97\u7684\u56fe\u7247Hash\u7c7b\u578b\uff0c\u63a8\u8350\u8bbe\u7f6e\u4e3apHash\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.3 \u542f\u7528\u989d\u5916\u76f8\u4f3c\u6821\u9a8c\u7b97\u6cd5SSIM\uff1a\u4ece3\u4e2a\u7ef4\u5ea6\u8fdb\u884c\u76f8\u4f3c\u68c0\u9a8c\uff0c\u63a8\u8350\u9009\u4e2d\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.4 \u5339\u914d\u7f13\u5b58\u6570\u636e\uff1a\u662f\u5426\u5339\u914d\u7f13\u5b58\u4e2d"
                        "\u7684\u56fe\u7247Hash\uff0c\u82e5\u9009\u4e2d\u5219\u4f1a\u6269\u5927\u5339\u914d\u8303\u56f4\uff0c\u53ef\u9009\u53ef\u4e0d\u9009\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.5 \u6bcf\u672c\u6f2b\u753b\u63d0\u53d6\u56fe\u7247\u6570\uff1a1~5\uff0c\u4ece\u6f2b\u753b\u4e2d\u63d0\u53d6\u7684\u56fe\u7247\u6570\u91cf\uff0c\u63d0\u53d6\u6570\u91cf\u8d8a\u5927\uff0c\u8ba1\u7b97\u91cf\u8d8a\u5927\uff08\u975e\u7ebf\u6027\u53d8\u5316\uff09\uff0c\u63a8\u8350\u9009\u62e91~3\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.6 \u56fe\u7247\u8ba1\u7b97\u5c3a\u5bf8\uff1a8~16\uff0c\u8ba1\u7b97\u56fe\u7247Hash\u65f6\u7f29\u653e\u7684\u56fe\u7247\u5c3a\u5bf8\uff0c\u4fee\u6539\u8be5\u9009\u9879\u65f6\u9700\u8981\u91cd\u65b0\u8ba1\u7b97\u5bf9\u5e94\u7684\u56fe\u7247Hash\u3002<"
                        "/span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.7 \u591a\u7ebf\u7a0b\uff1a1~CPU\u6838\u5fc3\u6570\uff0c\u5e76\u884c\u7684\u8fdb\u7a0b\u6570\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">4.\u7f13\u5b58\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4.1 \u7f13\u5b58\u6570\u636e\uff1a\u5f53\u524d\u6570\u636e\u5e93\u7684\u57fa\u7840\u4fe1\u606f\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                        " -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4.2 \u7f13\u5b58\u5185\u90e8\u67e5\u91cd\uff1a\u5728\u6570\u636e\u5e93\u5185\u90e8\u8fdb\u884c\u76f8\u4f3c\u5339\u914d\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4.3 \u66f4\u65b0\u7f13\u5b58\u6570\u636e\uff1a\u91cd\u65b0\u8ba1\u7b97\u6570\u636e\u5e93\u9879\u76ee\u7684\u6570\u636e\uff08\u4ec5\u8ba1\u7b97\u6709\u53d8\u52a8\u7684\uff09</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4.4 \u6e05\u9664\u65e0\u6548\u6570\u636e\uff1a\u6e05\u9664\u6570\u636e\u5e93\u4e2d\u5df2\u7ecf\u5931\u6548\u7684\u9879\u76ee\uff08\u4e0d\u5b58\u5728\u7684\u3001\u6709\u53d8\u52a8\u7684\uff09</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind"
                        "ent:0px;\"><span style=\" font-size:10pt;\">4.5 \u6e05\u7a7a\u7f13\u5b58\uff1a\u6e05\u9664\u6240\u6709\u7f13\u5b58\u6570\u636e\u3002</span></p></body></html>", None))
        self.toolButton_last.setText(QCoreApplication.translate("dialog", u"<", None))
        self.toolButton_next.setText(QCoreApplication.translate("dialog", u">", None))
        self.label_current_page.setText(QCoreApplication.translate("dialog", u"1", None))
        self.label.setText(QCoreApplication.translate("dialog", u"/", None))
        self.label_max_page.setText(QCoreApplication.translate("dialog", u"1", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"\u9875", None))
    # retranslateUi

