import os
import sys

# MAIN WINDOW
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMainWindow

from ui.ui_main import Ui_MainWindow

# SPLASH SCREEN
from ui.ui_splash_screen import Ui_SplashScreen

# LOCK SCREEN
from ui.ui_lock_screen import Ui_LockScreen

# GLOBALS
counter = 0


# YOUR APPLICATION
class MainWindow(QMainWindow):

    # Opens Lock Screen Window
    def lockScreen(self):
        self.lockui.setupUi(self)
        self.showFullScreen()

    def __init__(self):
        QMainWindow.__init__(self)
        self.lockui = Ui_LockScreen()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Show main Window
        self.show()


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 10:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())

