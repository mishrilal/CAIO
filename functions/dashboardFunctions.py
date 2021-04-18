from PySide2.QtCore import QObject, Slot, Signal, QAbstractListModel, QModelIndex, Qt, QSettings, QTimer
from PySide2.QtSql import QSqlDatabase, QSqlQueryModel


class DashboardPage(QObject):
    # setRows = Signal(str)
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
        self.counter = 0

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("caio.db")
        self.db.open()

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

        # self.db.open()
        # self.projectModel.setQuery("select * from allLogs order by 'Sr.No.' asc", self.db)
        # self.db.close()

    def setLogs(self):
        # Auto update for logs gets Application Crashed
        # using counter to setup UI properly
        if self.counter < 3:
            self.projectModel.setQuery("select * from allLogs order by id desc limit 20 ", self.db)
            self.counter += 1
        if self.counter == 3:
            self.db.close()
