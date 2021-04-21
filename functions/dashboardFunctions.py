from PySide2.QtCore import QObject, Signal, QSettings, QTimer
from PySide2.QtSql import QSqlDatabase, QSqlQueryModel
from pathlib import Path


class DashboardPage(QObject):
    setMaxValue = Signal(int)
    setAdminLocks = Signal(int)
    setSomeoneElseLocks = Signal(int)
    setNobodyLocks = Signal(int)

    def __init__(self):
        super().__init__()
        self.projectModel = QSqlQueryModel()
        self.settings = QSettings('CAIO', 'Preferences')
        self.totalLocks = self.settings.value('totalLocks')
        self.noOfLocksAdmin = self.settings.value('noOfLocksAdmin')
        self.noOfSomeoneElseLocks = self.settings.value('noOfSomeoneElseLocks')
        self.noOfNobodyLocks = self.settings.value('noOfNobodyLocks')
        self.initialRun = True
        self.initialRunCircular = True
        self.counter = 0
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        dbLocation = str(Path.home()) + '/CAIO/caio.db'
        self.db.setDatabaseName(dbLocation)

        # AUTO REFRESH
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(lambda: self.setWidget())
        timer.timeout.connect(lambda: self.setLogs())

    def setWidget(self):
        self.totalLocks = self.settings.value('totalLocks')
        self.noOfLocksAdmin = self.settings.value('noOfLocksAdmin')
        self.noOfSomeoneElseLocks = self.settings.value('noOfSomeoneElseLocks')
        self.noOfNobodyLocks = self.settings.value('noOfNobodyLocks')

        self.setMaxValue.emit(self.totalLocks)
        self.setAdminLocks.emit(self.noOfLocksAdmin)
        self.setSomeoneElseLocks.emit(self.noOfSomeoneElseLocks)
        self.setNobodyLocks.emit(self.noOfNobodyLocks)

    def setLogs(self):
        isLogChanged = self.settings.value('logChanged')
        if isLogChanged == 1 or self.initialRun:
            self.db.open()
            self.projectModel.setQuery("select ID, Date, Time, LockedBy from allLogs order by id desc",
                                       self.db)
            self.db.close()
            QSqlDatabase.removeDatabase("QSQLITE")
            self.settings.setValue('logChanged', 0)
            self.initialRun = False
