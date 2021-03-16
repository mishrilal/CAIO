import os
import sys

# MAIN WINDOW
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

from functions.addFaceFunctions import AddFace


class MainWindow(QObject):
    def __init__(self):
        super(MainWindow, self).__init__()
        QObject.__init__(self)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    addFace = AddFace()
    engine.rootContext().setContextProperty("addFaceBackend", addFace)

    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
