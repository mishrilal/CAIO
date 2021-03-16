import os
import sys

# MAIN WINDOW
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine


class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    engine.rootContext().setContextProperty("backend", main)

    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
