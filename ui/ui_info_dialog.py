# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_info_dialoguiXbAk.ui'
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

        self.toolButton_previous = QToolButton(dialog)
        self.toolButton_previous.setObjectName(u"toolButton_previous")

        self.horizontalLayout.addWidget(self.toolButton_previous)

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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u5f00\u6e90\u5730\u5740</span>\uff1a<a href=\"https://github.com/PPJUST/ComicDup\"><span style=\" text-decoration: underline; color:#0000ff;\">\u70b9\u51fb\u76f4\u8fbe</span></a> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-we"
                        "ight:700;\">\u4f7f\u7528\u6b65\u9aa4\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u5728\u6307\u5b9a\u533a\u57df\u62d6\u5165\u6587\u4ef6\u5939</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u8bbe\u7f6e\u76f8\u4f3c\u5ea6\u7b97\u6cd5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u70b9\u51fb\u201c\u5f00\u59cb\u201d\u6309\u94ae</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u7a0b\u5e8f\u8fd0\u884c\u6b65\u9aa4\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u63d0\u53d6\u62d6\u5165\u6587\u4ef6\u5939\u4e2d\u7684\u6240\u6709\u6f2b\u753b\u6587\u4ef6\u5939\uff08\u5185\u90e8\u56fe\u7247\u6570&gt;=4\uff09\u548c\u538b\u7f29\u5305\uff08zip\u3001rar\uff09</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u63d0\u53d6\u6240\u6709\u6f2b\u753b\u6587\u4ef6\u5939\u4e2d\u7684\u524dN\u5f20\u56fe\u7247\u7528\u4e8e\u5339\u914d</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u63d0\u53d6\u7f13\u5b58\u4e2d\u7684Hash\u503c\uff0c\u5e76\u8ba1\u7b97\u6ca1\u6709\u7684\u56fe\u7247Hash\u503c</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.\u56fe\u7247Hash\u503c\u5bf9\u6bd4\uff0cSSIM\u5bf9\u6bd4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px;\">5.\u8fd4\u56de\u76f8\u4f3c\u7ed3\u679c\uff0c\u5e76\u663e\u793a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u5177\u4f53\u8bf4\u660e\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">1.\u529f\u80fd\u533a\u6309\u94ae\u529f\u80fd</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.1 \u5f00\u59cb\u3001\u505c\u6b62\u3001\u7a0b\u5e8f\u8bf4\u660e\uff1a\u7565</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "1.2 \u5237\u65b0\u7ed3\u679c\uff1a\u5237\u65b0\u5f53\u524d\u76f8\u4f3c\u7ed3\u679c\uff08\u53bb\u9664\u5931\u6548\u9879\uff09</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.3 \u52a0\u8f7d\u7ed3\u679c\uff1a\u52a0\u8f7d\u4e0a\u4e00\u6b21\u7684\u76f8\u4f3c\u7ed3\u679c</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.4 \u7f13\u5b58\u8bbe\u7f6e\uff1a\u6253\u5f00\u7f13\u5b58\u8bbe\u7f6e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">2.\u76f8\u4f3c\u5ea6\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\">2.1 ahash/phash/dhash\uff1a\u56fe\u7247\u54c8\u5e0c\u7b97\u6cd5\uff0c3\u79cd\u7b97\u6cd5\u7ed3\u679c\u5dee\u522b\u4e0d\u5927</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.2 SSIM\uff1a\u7ed3\u6784\u76f8\u4f3c\u5ea6\uff0c\u6bd4\u8f83\u7cbe\u51c6\u4f46\u9700\u8981\u989d\u5916\u8ba1\u7b97\uff08\u53ef\u9009\u9879\uff09</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.3 \u63d0\u53d6\u56fe\u7247\u6570\uff1a\u4ece\u6bcf\u672c\u6f2b\u753b\u4e2d\u63d0\u53d6\u7684\u56fe\u7247\u6570\u91cf\uff0c\u7528\u4e8e\u8ba1\u7b97\uff08\u8d8a\u5927\u8ba1\u7b97\u91cf\u8d8a\u5927\uff09</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.4 \u7ebf\u7a0b\u6570\uff1a\u591a\u7ebf\u7a0b\uff08\u672a\u5b8c\u6210\uff09</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-b"
                        "ottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">3.\u62d6\u5165\u533a\u57df</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u62d6\u5165\u6587\u4ef6/\u6587\u4ef6\u5939\u5373\u53ef\u6dfb\u52a0\uff08\u8def\u5f84\u53cd\u5411\u6392\u5217\uff09</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">4.\u8fd0\u884c\u8fdb\u5ea6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u663e"
                        "\u793a\u8fd0\u884c\u8fdb\u5ea6\uff08\u5982\u679c\u8fdb\u5ea6\u5361\u4f4f\u4e86\uff0c\u5e94\u8be5\u662f\u62a5\u9519\u4e86\uff0c\u8bf7\u53cd\u9988\uff09</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">5.\u7f13\u5b58\u8bbe\u7f6e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7528\u4e8e\u63d0\u524d\u8ba1\u7b97\u6240\u9009\u7f13\u5b58\u6587\u4ef6\u5939\u7684\u56fe\u7247\u54c8\u5e0c\u503c\uff0c\u4ee5\u52a0\u5feb\u76f8\u4f3c\u5339\u914d</p></body></html>", None))
        self.toolButton_previous.setText(QCoreApplication.translate("dialog", u"<", None))
        self.toolButton_next.setText(QCoreApplication.translate("dialog", u">", None))
        self.label_current_page.setText(QCoreApplication.translate("dialog", u"1", None))
        self.label.setText(QCoreApplication.translate("dialog", u"/", None))
        self.label_max_page.setText(QCoreApplication.translate("dialog", u"1", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"\u9875", None))
    # retranslateUi

