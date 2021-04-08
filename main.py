import os
import sys

# MAIN WINDOW
from PySide2.QtCore import QObject, Slot, Signal, QSettings
from PySide2.QtGui import QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication

from functions.addFaceFunctions import AddFace
from functions.dashboardFunctions import DashboardPage
from functions.settingsFunctions import SettingsPage, setSettingsValue


class MainWindow(QObject):
    setAutoUnlock = Signal(str)
    setOnlyAdmin = Signal(str)
    setOnlyAdminStrict = Signal(str)
    setSomeoneAppears = Signal(str)
    setSomeoneAppearsStrict = Signal(str)
    setCaptureBtn = Signal(str)

    def __init__(self):
        super().__init__()
    #     try:
    #         print("load")
    #         self.resize(self.settings.value('window size'))
    #         self.move(self.settings.value('window position'))
    #     except:
    #         pass
    #
    # def closeEvent(self, event):
    #     print('window')
    #     self.settings.setValue('window size', self.size())
    #     self.settings.setValue('window position', self.pos())

    @Slot()
    def dashboardClicked(self):
        print("DashBoardClicked")

    @Slot()
    def viewClicked(self):
        print("ViewClicked")

    @Slot()
    def addClicked(self):
        print("AddClicked")
        settings = QSettings('CAIO', 'Preferences')
        person = settings.value('person')
        if person == 0:
            self.setCaptureBtn.emit("true")
            print("true")
        else:
            self.setCaptureBtn.emit("false")
            print("false")

    @Slot()
    def removeClicked(self):
        print("RemoveClicked")

    @Slot()
    def settingsClicked(self):
        print("SettingsClicked")
        setSettingsValue(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/svg_images/logo_icon.svg"))
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    addFace = AddFace()
    settingsPage = SettingsPage()
    dashboardPage = DashboardPage()

    engine.rootContext().setContextProperty("backend", main)
    engine.rootContext().setContextProperty("addFaceBackend", addFace)
    engine.rootContext().setContextProperty("settingsBackend", settingsPage)
    engine.rootContext().setContextProperty("dashboardBackend", dashboardPage)

    engine.load(os.path.join(os.path.dirname(__file__), "qml/splashScreen.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
