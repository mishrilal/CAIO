import os
import sys

# MAIN WINDOW
from PySide2.QtCore import QObject, Slot, Signal
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication

from functions.addFaceFunctions import AddFace
from functions.settingsFunctions import SettingsPage, setSettingsValue


class MainWindow(QObject):
    setStartup = Signal(str)
    setLockOthers = Signal(str)
    setAutoLock = Signal(str)
    setAutoUnlock = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()

    @Slot()
    def dashboardClicked(self):
        print("DashBoardClicked")

    @Slot()
    def viewClicked(self):
        print("ViewClicked")

    @Slot()
    def addClicked(self):
        print("AddClicked")

    @Slot()
    def removeClicked(self):
        print("RemoveClicked")

    @Slot()
    def settingsClicked(self):
        print("SettingsClicked")
        setSettingsValue(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    addFace = AddFace()
    settingsPage = SettingsPage()

    engine.rootContext().setContextProperty("backend", main)
    engine.rootContext().setContextProperty("addFaceBackend", addFace)
    engine.rootContext().setContextProperty("settingsBackend", settingsPage)

    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
