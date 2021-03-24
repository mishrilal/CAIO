## Not in USE


import os
import sys
from PySide2.QtCore import QObject, Slot, Signal, QSettings


class SettingsPage(QObject):
    setStartup = Signal(str)

    # # constructor
    # def __init__(self):
    #     super().__init__()
    #     self.settings = QSettings('CAIO', 'CAIO')

    @Slot()
    def startupClicked(self, isChecked):
        # print(self.settings.fileName())
        # self.settings.setValue('startup', isChecked)
        print("STARTUP")

    @Slot()
    def lockScreen(self):
        print("LOCK")
