from PySide2.QtCore import QObject, Slot

from functions.detectFace import detectFace


class DashboardPage(QObject):

    @Slot()
    def detectFaceClicked(self):
        detectFace(self)


