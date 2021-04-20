from PySide2.QtCore import QObject, QSettings, QTimer
from PySide2.QtSql import QSqlDatabase, QSqlQueryModel


class AllLogsPage(QObject):
    def __init__(self):
        super().__init__()
        self.allLogsModel = ""
        self.settings = QSettings('CAIO', 'Preferences')
        self.initialRun = True
        # self.dbAllLog = QSqlDatabase.addDatabase("QSQLITE")
        # self.dbAllLog.setDatabaseName("caio.db")
        # self.dbAllLog.open()

        # AUTO REFRESH
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(lambda: self.setLogs())

    def setLogs(self):
        isLogChanged = self.settings.value('logChanged')
        if isLogChanged == 1 or self.initialRun:
            self.allLogsModel = QSqlQueryModel()
            dbAllLog = QSqlDatabase.addDatabase("QSQLITE")
            dbAllLog.setDatabaseName("caio.db")
            dbAllLog.open()
            self.allLogsModel.setQuery("select * from allLogs order by id desc ", dbAllLog)
            dbAllLog.close()
            print(self.allLogsModel)
            self.settings.setValue('logChanged', 0)
            QSqlDatabase.removeDatabase("QSQLITE")
            self.initialRun = False
