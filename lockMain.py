import os
import sys

from PySide2.QtCore import QObject
from PySide2.QtGui import QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication


class LockWindow(QObject):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/svg_images/logo_icon.svg"))
    engine = QQmlApplicationEngine()

    # Get Context
    lock = LockWindow()

    engine.rootContext().setContextProperty("lockBackend", lock)

    engine.load(os.path.join(os.path.dirname(__file__), "qml/lockMain.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
