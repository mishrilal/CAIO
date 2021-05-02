import os
import pathlib
import signal
import sys
from pathlib import Path
import platform
import re

from PySide2.QtCore import QObject, Slot, Signal, QSettings, QTimer
from PySide2.QtGui import QIcon
from PySide2.QtMultimedia import QCameraInfo, QCamera, QCameraImageCapture
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication

from functions.addFaceFunctions import AddFace
from functions.dashboardFunctions import DashboardPage
from functions.removeFaceFunctions import RemoveFace
from functions.settingsFunctions import SettingsPage, setSettingsValue
from lockMain import LockMain

from multiprocessing import Process
import psutil


def checkLock(self):
    if self.osName == 'macOS':
        # Ask user for the name of process
        name = 'CAIOLock'
        try:
            # iterating through each instance of the process
            for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
                print("Line: ", line)
                fields = line.split()
                print("Fields ", fields)
                print("Filed 0 ", fields[0])
                # extracting Process ID from the output
                pid = fields[0]
                print("Pid: ", pid)

                # terminating process
                return True
            print("Process Successfully terminated")
        except:
            print("Error Encountered while running script")
            return False
        return False

    elif self.osName == 'Windows':
        processName = 'CAIOLock'
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                # Check if process name contains the given name string.
                if processName.lower() in pinfo['name'].lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                print("Some Error while killing")
                return False
        return False


def process(self):
    if self.osName == 'macOS':
        # Ask user for the name of process
        name = 'CAIOLock'
        try:
            # iterating through each instance of the process
            for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
                print("Line: ", line)
                fields = line.split()
                print("Fields ", fields)
                print("Filed 0 ", fields[0])
                # extracting Process ID from the output
                pid = fields[0]
                print("Pid: ", pid)

                # terminating process
                os.kill(int(pid), signal.SIGKILL)
            print("Process Successfully terminated")
        except:
            print("Error Encountered while running script")

    elif self.osName == 'Windows':
        processName = 'CAIOLock'
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                # Check if process name contains the given name string.
                if processName.lower() in pinfo['name'].lower():
                    print("Check Killing")
                    os.system("taskkill /f /im  CAIOLock.exe")
                    print("Check Killed")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                print("Some Error while killing")
                pass


# def findProcessId():
#     processName = 'CAIO Lock'
#     for proc in psutil.process_iter():
#         try:
#             pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
#             # Check if process name contains the given name string.
#             if processName.lower() in pinfo['name'].lower():
#                 print("Check Killing")
#                 os.system("taskkill /f /im  CAIO\ Lock.exe")
#                 print("Check Killed")
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             print("Some Error while killing")
#             pass


def invokeLock():
    if getattr(sys, "frozen", False):
        # print("FROM-> build")
        os.popen((os.path.join(os.path.dirname(sys.executable), "CAIOLock")))
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
    setCaptureDetails = Signal(str)
    setCaptureBtn2 = Signal(str)


    def __init__(self):
        super().__init__()
        self.osName = platform.platform()
        if re.search("macOS", self.osName):
            self.osName = "macOS"
        elif re.search("Windows", self.osName):
            self.osName = "Windows"
        self.settings = QSettings('CAIO', 'Preferences')
        self.changeLockBtn = self.settings.value('changeLockBtn')
        self.lock = self.settings.value("lockFile")

        if self.changeLockBtn is None:
            self.changeLockBtn = 0
            self.settings.setValue('changeLockBtn', self.changeLockBtn)

        if self.lock is None:
            self.lock = 0
            self.settings.setValue('lockFile', self.lock)

        self.lock = 0
        self.settings.setValue('lockFile', self.lock)

        # Remove below code when independent lockMain is Created
        self.changeLockBtn = 0
        self.settings.setValue('changeLockBtn', self.changeLockBtn)

        # and uncomment this code
        self.counter = 0
        timer = QTimer(self)
        timer.start(500)
        timer.timeout.connect(lambda: self.setLockBtnInitial())

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
        self.camera.stop()
        # print("DashBoardClicked")
        dashboard = DashboardPage()
        # dashboard.initialRunCircular = True
        # dashboard.counter = 0
        # print(dashboard.initialRunCircular)
        engine.rootContext().setContextProperty("tableModel", dashboard.projectModel)

    @Slot()
    def viewClicked(self):
        self.camera.stop()
        # print("ViewClicked")

        settings = QSettings('CAIO', 'Preferences')
        person = settings.value('person')

        pathImage = str(Path.home()) + '/CAIO/img_%s.jpg' % str(person)

        # print("Check ", person)
        if os.path.isfile(pathImage):
            # print("Image Found")
            # if person == 1:
            self.checkImage.emit("true")
            if self.osName == 'macOS':
                self.setImagePath.emit(pathImage)
            elif self.osName == 'Windows':
                newPath = 'file:///' + pathImage
                self.setImagePath.emit(newPath)
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

        # path to save
        self.createCAIOdir = str(Path.home()) + '/CAIO'
        pathlib.Path(self.createCAIOdir).mkdir(parents=True, exist_ok=True)
        self.save_path2 = self.createCAIOdir + "/"
        self.save_path = "images/captured/"

        # getting available cameras
        self.available_cameras = QCameraInfo.availableCameras()

        # if no camera found
        if not self.available_cameras:
            # exit the code
            sys.exit()

        # Set the default camera.
        self.select_camera(0)

    @Slot()
    def captureClicked(self):
        self.person = 1
        self.settings.setValue('person', self.person)
        self.click_photo()
        self.setCaptureDetails.emit("Captured Successfully")
        self.setCaptureBtn2.emit("false")

    @Slot()
    def removeClicked(self):
        self.camera.stop()
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
            if self.osName == "macOS":
                self.setImagePath.emit(pathImage)
                print("image found")
            elif self.osName == "Windows":
                newPath = 'file:///' + pathImage
                self.setImagePath.emit(newPath)
                print("image found", newPath)

    @Slot()
    def settingsClicked(self):
        self.camera.stop()
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
    def aboutClicked(self):
        self.camera.stop()

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
            # findProcessId(self)
            if getattr(sys, "frozen", False):
                process(self)
            self.changeLockBtn = 0
            self.settings.setValue('changeLockBtn', self.changeLockBtn)
            self.setLockBtn.emit(0)

    def setLockBtnInitial(self):
        # print("counter: ", self.counter)
        if getattr(sys, "frozen", False):
            if checkLock(self):
                print("Checking lock")
                self.changeLockBtn = 1
                self.settings.setValue('changeLockBtn', self.changeLockBtn)
                self.setLockBtn.emit(1)
            else:
                self.changeLockBtn = 0
                self.settings.setValue('changeLockBtn', self.changeLockBtn)
                self.setLockBtn.emit(0)
        else:
            if self.counter < 3:
                print("setBTN")
                if self.changeLockBtn == 0:
                    self.setLockBtn.emit(0)
                else:
                    self.setLockBtn.emit(1)
                self.counter += 1

    # method to take photo
    def click_photo(self):
        # time stamp
        # timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")

        # capture the image and save it on the save path
        self.capture.capture(os.path.join(self.save_path2,
                                          "img_%s.jpg" % (
                                              str(self.person)
                                          )))
        print()
        # increment the sequence
        self.save_seq += 1

    # method to select camera
    def select_camera(self, i):
        # getting the selected camera
        self.camera = QCamera(self.available_cameras[i])

        # setting capture mode to the camera
        self.camera.setCaptureMode(QCamera.CaptureStillImage)

        # start the camera
        self.camera.start()

        # creating a QCameraImageCapture object
        self.capture = QCameraImageCapture(self.camera)

        # when image captured showing message
        self.capture.imageCaptured.connect(lambda d,
                                                  i: self.status.showMessage("Image captured : "
                                                                             + str(self.save_seq)))

        # getting current camera name
        self.current_camera_name = self.available_cameras[i].description()

        # inital save sequence
        self.save_seq = 0


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
