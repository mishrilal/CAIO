import os
import sys
from pathlib import Path
import platform
import re

from PySide2.QtCore import QObject, Slot, Signal, QSettings, QTimer
from PySide2.QtGui import QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication

from functions.addFaceFunctions import AddFace
from functions.dashboardFunctions import DashboardPage
from functions.removeFaceFunctions import RemoveFace
from functions.settingsFunctions import SettingsPage, setSettingsValue
from lockMain import LockMain

from multiprocessing import Process


def invokeLock():
    if getattr(sys, "frozen", False):
        # print("FROM-> build")
        os.popen((os.path.join(os.path.dirname(sys.executable), "lockMain")))
    else:
        # print("In invokeLock")
        lock = LockMain()
        lock.runLock()

    # lock = LockMain()
    # lock.runLock()


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
    setLockBtn = Signal(int)

    def __init__(self):
        super().__init__()
        self.osName = platform.platform()
        if re.search("macOS", self.osName):
            self.osName = "macOS"
        elif re.search("Windows", self.osName):
            self.osName = "Windows"
        self.settings = QSettings('CAIO', 'Preferences')

        self.changeLockBtn = self.settings.value('changeLockBtn')
        if self.changeLockBtn is None:
            self.changeLockBtn = 0
            self.settings.setValue('changeLockBtn', self.changeLockBtn)

        # Remove below code when independent lockMain is Created
        self.changeLockBtn = 0
        self.settings.setValue('changeLockBtn', self.changeLockBtn)

        # and uncomment this code
        # self.counter = 0
        # timer = QTimer(self)
        # timer.start(500)
        # timer.timeout.connect(lambda: self.setLockBtnInitial())

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
        # print("DashBoardClicked")
        dashboard = DashboardPage()
        # dashboard.initialRunCircular = True
        # dashboard.counter = 0
        # print(dashboard.initialRunCircular)
        engine.rootContext().setContextProperty("tableModel", dashboard.projectModel)

    @Slot()
    def viewClicked(self):
        # print("ViewClicked")

        settings = QSettings('CAIO', 'Preferences')
        person = settings.value('person')

        if self.osName == "macOS":
            pathImage = str(Path.home()) + '/CAIO/img_%s.jpg' % str(person)
        elif self.osName == "Windows":
            pathImage = 'file:\\\\\\' + str(Path.home()) + '\\CAIO\\img_%s.jpg' % str(person)

        # print("Check ", person)
        if os.path.isfile(pathImage):
            # print("Image Found")
            # if person == 1:
            self.checkImage.emit("true")
            self.setImagePath.emit(pathImage)
        else:
            settings.setValue('person', 0)
            self.checkImage.emit("false")

    @Slot()
    def addClicked(self):
        # print("AddClicked")
        settings = QSettings('CAIO', 'Preferences')
        person = settings.value('person')
        # print("ads", person)
        if person == 0:
            self.setCaptureBtn.emit("true")
            # print("true")
        else:
            self.setCaptureBtn.emit("false")
            # print("false")

    @Slot()
    def removeClicked(self):
        # print("RemoveClicked")
        settings = QSettings('CAIO', 'Preferences')
        person = settings.value('person')

        pathImage = str(Path.home()) + '/CAIO/img_%s.jpg' % str(person)
        # print("Rm ", person)
        # if person == 0:
        if not os.path.isfile(pathImage):
            settings.setValue('person', 0)
            self.removeImage.emit("true")
        else:
            self.setImagePath.emit(pathImage)

    @Slot()
    def settingsClicked(self):
        # print("SettingsClicked")
        setSettingsValue(self)

    # @Slot()
    # def allLogsClicked(self):
    #     print("Logs Clicked")
    #     allLogs = AllLogsPage()
    #     allLogs.initialRun = True
    #     engine.rootContext().setContextProperty("allLogsBackend", allLogs)
    #     engine.rootContext().setContextProperty("allLogsModel", allLogs.allLogsModel)

    @Slot()
    def runLock(self):
        if self.changeLockBtn == 0:
            # print("runLock Clicked")
            if getattr(sys, "frozen", False):
                invokeLock()
            else:
                # print("in runLock --> process")
                proc = Process(target=invokeLock, args=())
                # proc.daemon = True
                proc.start()

            self.changeLockBtn = 1
            self.settings.setValue('changeLockBtn', self.changeLockBtn)
            self.setLockBtn.emit(1)
        # import subprocess
        # subprocess.run(os.path.join(os.path.dirname(__file__), 'lockMain.py'))
        # subprocess.Popen([sys.executable, 'lockMain.py'])

        else:
            self.changeLockBtn = 0
            self.settings.setValue('changeLockBtn', self.changeLockBtn)
            self.setLockBtn.emit(0)

    def setLockBtnInitial(self):
        # print("counter: ", self.counter)
        if self.counter < 3:
            # print("setBTN")
            if self.changeLockBtn == 0:
                self.setLockBtn.emit(0)
            else:
                self.setLockBtn.emit(1)
            self.counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if getattr(sys, "frozen", False):
        app.setWindowIcon(QIcon(os.path.join(os.path.dirname(sys.executable), "logo_icon.svg")))
    else:
        app.setWindowIcon(QIcon("logo_icon.svg"))
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

    if getattr(sys, "frozen", False):
        engine.load(os.path.join(os.path.dirname(sys.executable), "qml/splashScreen.qml"))
    else:
        engine.load(os.path.join(os.path.dirname(__file__), "qml/splashScreen.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
