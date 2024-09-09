# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_comic_viewjbQFKO.ui'
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
        Form.resize(371, 289)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.label_preview = QLabel(self.frame)
        self.label_preview.setObjectName(u"label_preview")

        self.verticalLayout.addWidget(self.label_preview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_comic_type = QLabel(self.frame)
        self.label_comic_type.setObjectName(u"label_comic_type")

        self.horizontalLayout.addWidget(self.label_comic_type)

        self.label_filesize = QLabel(self.frame)
        self.label_filesize.setObjectName(u"label_filesize")

        self.horizontalLayout.addWidget(self.label_filesize)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_filename = QLabel(self.frame)
        self.label_filename.setObjectName(u"label_filename")

        self.horizontalLayout.addWidget(self.label_filename)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.toolButton_open_file = QToolButton(self.frame)
        self.toolButton_open_file.setObjectName(u"toolButton_open_file")

        self.horizontalLayout_4.addWidget(self.toolButton_open_file)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toolButton_last = QToolButton(self.frame)
        self.toolButton_last.setObjectName(u"toolButton_last")

        self.horizontalLayout_3.addWidget(self.toolButton_last)

        self.toolButton_next = QToolButton(self.frame)
        self.toolButton_next.setObjectName(u"toolButton_next")

        self.horizontalLayout_3.addWidget(self.toolButton_next)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_page_index = QLabel(self.frame)
        self.label_page_index.setObjectName(u"label_page_index")

        self.horizontalLayout_2.addWidget(self.label_page_index)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_page_count = QLabel(self.frame)
        self.label_page_count.setObjectName(u"label_page_count")

        self.horizontalLayout_2.addWidget(self.label_page_count)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.toolButton_delete = QToolButton(self.frame)
        self.toolButton_delete.setObjectName(u"toolButton_delete")

        self.horizontalLayout_4.addWidget(self.toolButton_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout.setStretch(0, 1)

        self.horizontalLayout_5.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_preview.setText(QCoreApplication.translate("Form", u"preview", None))
        self.label_comic_type.setText(QCoreApplication.translate("Form", u"comic_type", None))
        self.label_filesize.setText(QCoreApplication.translate("Form", u"filesize", None))
        self.label.setText(QCoreApplication.translate("Form", u"|", None))
        self.label_filename.setText(QCoreApplication.translate("Form", u"filename", None))
        self.toolButton_open_file.setText(QCoreApplication.translate("Form", u"open", None))
        self.toolButton_last.setText(QCoreApplication.translate("Form", u"<", None))
        self.toolButton_next.setText(QCoreApplication.translate("Form", u">", None))
        self.label_page_index.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"/", None))
        self.label_page_count.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"|", None))
        self.toolButton_delete.setText(QCoreApplication.translate("Form", u"delete", None))
    # retranslateUi

