# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lock_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LockScreen(object):
    def setupUi(self, LockScreen):
        if not LockScreen.objectName():
            LockScreen.setObjectName(u"LockScreen")
        LockScreen.resize(800, 600)
        LockScreen.setStyleSheet(u"background-color: rgb(35, 33, 30);")
        self.centralwidget = QWidget(LockScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Gabriola")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        LockScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LockScreen)

        QMetaObject.connectSlotsByName(LockScreen)
    # setupUi

    def retranslateUi(self, LockScreen):
        LockScreen.setWindowTitle(QCoreApplication.translate("LockScreen", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LockScreen", u"LOCKED", None))
    # retranslateUi

