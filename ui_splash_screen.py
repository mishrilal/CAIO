# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setMinimumSize(QSize(660, 380))
        self.dropShadowFrame.setMaximumSize(QSize(660, 380))
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(67, 67, 67, 255));\n"
"	border-radius: 7px\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 80, 661, 101))
        font = QFont()
        font.setFamily(u"Gabriola")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_title.setFont(font)
        self.label_title.setTabletTracking(False)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setWordWrap(False)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(20, 340, 621, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color:none;")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CA</span><span style=\" text-decoration: underline;\">IO</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<strong>Developed By: </strong> THE PYTHONS", None))
    # retranslateUi

