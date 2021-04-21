import os
import sys
from os import path
from pathlib import Path

from PySide2.QtCore import QObject, Slot, Signal, QSettings
from PySide2.QtGui import QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication

from functions.addFaceFunctions import AddFace
from functions.dashboardFunctions import DashboardPage
from functions.removeFaceFunctions import RemoveFace
from functions.settingsFunctions import SettingsPage, setSettingsValue


class MainWindow(QObject):
    setAutoUnlock = Signal(str)
    setOnlyAdmin = Signal(str)
    setOnlyAdminStrict = Signal(str)
    setSomeoneAppears = Signal(str)
    setSomeoneAppearsStrict = Signal(str)
    setCaptureBtn = Signal(str)
    removeImage = Signal(str)
    checkImage = Signal(str)
    setImagePath = Signal(str)

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
        dashboard = DashboardPage()
        # dashboard.initialRunCircular = True
        # dashboard.counter = 0
        # print(dashboard.initialRunCircular)
        engine.rootContext().setContextProperty("tableModel", dashboard.projectModel)

    @Slot()
    def viewClicked(self):
        print("ViewClicked")

        settings = QSettings('CAIO', 'Preferences')
        person = settings.value('person')

        pathImage = str(Path.home()) + '/CAIO/img_%s.jpg' % str(person)

        print("Check ", person)
        if path.isfile(pathImage):
            print("Image Found")
            # if person == 1:
            self.checkImage.emit("true")
            self.setImagePath.emit(pathImage)
        else:
            settings.setValue('person', 0)
            self.checkImage.emit("false")

    @Slot()
    def addClicked(self):
        print("AddClicked")
        settings = QSettings('CAIO', 'Preferences')
        person = settings.value('person')
        print("ads", person)
        if person == 0:
            self.setCaptureBtn.emit("true")
            print("true")
        else:
            self.setCaptureBtn.emit("false")
            print("false")

    @Slot()
    def removeClicked(self):
        print("RemoveClicked")
        settings = QSettings('CAIO', 'Preferences')
        person = settings.value('person')

        pathImage = str(Path.home()) + '/CAIO/img_%s.jpg' % str(person)
        print("Rm ", person)
        # if person == 0:
        if not path.isfile(pathImage):
            settings.setValue('person', 0)
            self.removeImage.emit("true")
        else:
            self.setImagePath.emit(pathImage)

    @Slot()
    def settingsClicked(self):
        print("SettingsClicked")
        setSettingsValue(self)

    # @Slot()
    # def allLogsClicked(self):
    #     print("Logs Clicked")
    #     allLogs = AllLogsPage()
    #     allLogs.initialRun = True
    #     engine.rootContext().setContextProperty("allLogsBackend", allLogs)
    #     engine.rootContext().setContextProperty("allLogsModel", allLogs.allLogsModel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/svg_images/logo_icon.svg"))
    engine = QQmlApplicationEngine()

    # db = QSqlDatabase.addDatabase("QSQLITE")
    # db.setDatabaseName("employee.db")
    # db.open()
    #
    # projectModel = QSqlQueryModel()
    # projectModel.setQuery("select * from employees", db)
    # db.close()

    # print(projectModel)

    # list_model = ['item1', 'item2']
    # root_context.setContextProperty('listModel', list_model)

    # Get Context
    main = MainWindow()
    addFace = AddFace()
    settingsPage = SettingsPage()
    dashboardPage = DashboardPage()
    removePage = RemoveFace()
    # allLogs = AllLogsPage()

    engine.rootContext().setContextProperty("backend", main)
    engine.rootContext().setContextProperty("addFaceBackend", addFace)
    engine.rootContext().setContextProperty("settingsBackend", settingsPage)
    engine.rootContext().setContextProperty("dashboardBackend", dashboardPage)
    engine.rootContext().setContextProperty("removeBackend", removePage)
    # engine.rootContext().setContextProperty("allLogsBackend", allLogs)
    engine.rootContext().setContextProperty("tableModel", dashboardPage.projectModel)

    engine.load(os.path.join(os.path.dirname(__file__), "qml/splashScreen.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
