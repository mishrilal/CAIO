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
"	color: rgb(220, 220, 220);\n"
"	border-radius: 7px\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(661, 150))
        self.label_title.setMaximumSize(QSize(1000, 1000))
        font = QFont()
        font.setFamily(u"Gabriola")
        font.setPointSize(60)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)

        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_credits.sizePolicy().hasHeightForWidth())
        self.label_credits.setSizePolicy(sizePolicy)
        self.label_credits.setMinimumSize(QSize(621, 50))
        self.label_credits.setMaximumSize(QSize(1000, 1000))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: none;")
        self.label_credits.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.label_credits.setMargin(0)

        self.verticalLayout_2.addWidget(self.label_credits)


        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<strong>CA</strong>IO", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<strong>Developed By: </strong> THE PYTHONS", None))
    # retranslateUi

