import os
import sys

# MAIN WINDOW
from PySide2.QtCore import QObject
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


class MainWindow(QObject):
    def __init__(self):
        super(MainWindow, self).__init__()
        # QObject.__init__(self)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()

    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
