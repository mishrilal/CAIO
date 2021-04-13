from PySide2.QtCore import QObject, Slot, Signal, QAbstractListModel, QModelIndex, Qt, QSettings, QTimer


class DashboardPage(QObject):
    # setRows = Signal(str)
    setMaxValue = Signal(int)
    setAdminLocks = Signal(int)
    setSomeoneElseLocks = Signal(int)
    setNobodyLocks = Signal(int)

    def __init__(self):
        super().__init__()
        self.settings = QSettings('CAIO', 'Preferences')
        self.totalLocks = self.settings.value('totalLocks')
        self.noOfLocksAdmin = self.settings.value('noOfLocksAdmin')
        self.noOfSomeoneElseLocks = self.settings.value('noOfSomeoneElseLocks')
        self.noOfNobodyLocks = self.settings.value('noOfNobodyLocks')

        # AUTO REFRESH
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(lambda: self.setDashboard())

    def setDashboard(self):
        self.totalLocks = self.settings.value('totalLocks')
        self.noOfLocksAdmin = self.settings.value('noOfLocksAdmin')
        self.noOfSomeoneElseLocks = self.settings.value('noOfSomeoneElseLocks')
        self.noOfNobodyLocks = self.settings.value('noOfNobodyLocks')

        self.setMaxValue.emit(self.totalLocks)
        self.setAdminLocks.emit(self.noOfLocksAdmin)
        self.setSomeoneElseLocks.emit(self.noOfSomeoneElseLocks)
        self.setNobodyLocks.emit(self.noOfNobodyLocks)



