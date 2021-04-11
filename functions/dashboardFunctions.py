from PySide2.QtCore import QObject, Slot, Signal, QAbstractListModel, QModelIndex, Qt


class DashboardPage(QObject):
    setRows = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot()
    def detectFaceClicked(self):
        pass


