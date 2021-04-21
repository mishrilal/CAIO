import sqlite3

from PySide2.QtCore import QSettings

from functions.lockFunctions import LockSystem
from pathlib import Path


def createDB():
    dbLocation = str(Path.home()) + '/CAIO/caio.db'
    conn = sqlite3.connect(dbLocation)

    c = conn.cursor()

    c.execute("""CREATE TABLE allLogs(ID integer primary key autoincrement,
                                        Date TEXT,
                                        Time TEXT,
                                        lockedBy TEXT,
                                        Event TEXT);
        """)
    c.execute("""CREATE TABLE adminLogs(ID integer primary key autoincrement,
                                        Date TEXT,
                                        Time TEXT,
                                        lockedBy TEXT,
                                        Event TEXT);
        """)
    c.execute("""CREATE TABLE someoneLogs(ID integer primary key autoincrement,
                                        Date TEXT,
                                        Time TEXT,
                                        lockedBy TEXT,
                                        Event TEXT);
        """)
    c.execute("""CREATE TABLE nobodyLogs(ID integer primary key autoincrement,
                                        Date TEXT,
                                        Time TEXT,
                                        lockedBy TEXT,
                                        Event TEXT);
        """)

    conn.commit()
    conn.close()


class LockMain:

    # constructor
    def __init__(self):
        super().__init__()
        self.settings = QSettings('CAIO', 'Preferences')
        self.settings.setValue('firstRun', 1)
        self.firstRun = self.settings.value('firstRun')

        if self.firstRun is None:
            self.firstRun = 1
            self.settings.setValue('firstRun', self.firstRun)

        if self.firstRun == 1:
            createDB()
            self.firstRun = 0
            self.settings.setValue('firstRun', self.firstRun)
        self.lock = LockSystem()

    def runLock(self):

        if self.settings.value('onlyAdmin') == 'true':
            print("onlyAdmin()")
            self.lock.onlyAdmin()

        elif self.settings.value('onlyAdminStrict') == 'true':
            print("onlyAdminStrict()")
            self.lock.onlyAdminStrict()

        elif self.settings.value('someoneAppears') == 'true':
            print("someoneAppears()")
            self.lock.someoneAppears()

        elif self.settings.value('someoneAppearsStrict') == 'true':
            print("someoneAppearsStrict()")
            self.lock.someoneAppearsStrict()


lock = LockMain()
lock.runLock()
