# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.frame_left_menu = QFrame(self.centralwidget)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashboard_btn = QPushButton(self.frame_left_menu)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setMinimumSize(QSize(0, 40))
        self.dashboard_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.dashboard_btn)

        self.view_btn = QPushButton(self.frame_left_menu)
        self.view_btn.setObjectName(u"view_btn")
        self.view_btn.setMinimumSize(QSize(0, 40))
        self.view_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.view_btn)

        self.add_btn = QPushButton(self.frame_left_menu)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(0, 40))
        self.add_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.add_btn)

        self.remove_btn = QPushButton(self.frame_left_menu)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setMinimumSize(QSize(0, 40))
        self.remove_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.remove_btn)

        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_top_menus)

        self.setting_btn = QPushButton(self.frame_left_menu)
        self.setting_btn.setObjectName(u"setting_btn")
        self.setting_btn.setMinimumSize(QSize(0, 40))
        self.setting_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.setting_btn)


        self.horizontalLayout.addWidget(self.frame_left_menu)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(715, 600))
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.gridLayout = QGridLayout(self.dashboard_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.dashboard_page)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(False)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lockscreen_btn = QPushButton(self.dashboard_page)
        self.lockscreen_btn.setObjectName(u"lockscreen_btn")

        self.gridLayout.addWidget(self.lockscreen_btn, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.view_page = QWidget()
        self.view_page.setObjectName(u"view_page")
        self.gridLayout_2 = QGridLayout(self.view_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.view_page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.view_page)
        self.add_page = QWidget()
        self.add_page.setObjectName(u"add_page")
        self.page_name = QLabel(self.add_page)
        self.page_name.setObjectName(u"page_name")
        self.page_name.setGeometry(QRect(280, 10, 121, 31))
        sizePolicy.setHeightForWidth(self.page_name.sizePolicy().hasHeightForWidth())
        self.page_name.setSizePolicy(sizePolicy)
        self.page_name.setFont(font)
        self.page_name.setAutoFillBackground(False)
        self.page_name.setStyleSheet(u"color: #ffffff;")
        self.page_name.setAlignment(Qt.AlignCenter)
        self.image = QLabel(self.add_page)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(220, 110, 231, 221))
        self.image.setMinimumSize(QSize(231, 221))
        self.image.setFrameShape(QFrame.Box)
        self.image.setFrameShadow(QFrame.Sunken)
        self.image.setLineWidth(2)
        self.image.setMidLineWidth(2)
        self.splitter = QSplitter(self.add_page)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(100, 450, 491, 41))
        self.splitter.setOrientation(Qt.Horizontal)
        self.turn_on = QPushButton(self.splitter)
        self.turn_on.setObjectName(u"turn_on")
        self.turn_on.setMinimumSize(QSize(131, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        self.turn_on.setFont(font1)
        self.turn_on.setStyleSheet(u"color: #ffffff;")
        self.splitter.addWidget(self.turn_on)
        self.capture = QPushButton(self.splitter)
        self.capture.setObjectName(u"capture")
        self.capture.setMinimumSize(QSize(131, 41))
        self.capture.setFont(font1)
        self.capture.setStyleSheet(u"color: #ffffff;")
        self.splitter.addWidget(self.capture)
        self.turn_off = QPushButton(self.splitter)
        self.turn_off.setObjectName(u"turn_off")
        self.turn_off.setMinimumSize(QSize(131, 41))
        self.turn_off.setFont(font1)
        self.turn_off.setStyleSheet(u"color: #ffffff;")
        self.splitter.addWidget(self.turn_off)
        self.stackedWidget.addWidget(self.add_page)
        self.remove_page = QWidget()
        self.remove_page.setObjectName(u"remove_page")
        self.gridLayout_4 = QGridLayout(self.remove_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.remove_page)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.remove_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.gridLayout_5 = QGridLayout(self.setting_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(self.setting_page)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.setting_page)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.view_btn.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.remove_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.setting_btn.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.lockscreen_btn.setText(QCoreApplication.translate("MainWindow", u"LOCK SCREEN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"View Faces", None))
        self.page_name.setText(QCoreApplication.translate("MainWindow", u"Add Faces", None))
        self.image.setText("")
        self.turn_on.setText(QCoreApplication.translate("MainWindow", u"Turn On Camera", None))
        self.capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.turn_off.setText(QCoreApplication.translate("MainWindow", u"Turn Off Camera", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Remove Faces", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
    # retranslateUi

