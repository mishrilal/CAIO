## Not in USE


import os
import sys
from PySide2.QtCore import QObject, Slot, Signal, QSettings


def convertBool(value):
    if value == "true":
        return True
    return False


class SettingsPage(QObject):
    setStartup = Signal(str)
    setLockOther = Signal(str)
    setAutoLock = Signal(str)
    setAutoUnlock = Signal(str)

    # constructor
    def __init__(self):
        super(SettingsPage, self).__init__()
        self.settings = QSettings('CAIO', 'CAIO')

        self.setStartup.emit(str(self.settings.value('startup')))
        print("STARTUP: " + self.settings.value('startup'))

    # When "Unlock at StartUp" Clicked
    @Slot('QString')
    def startupClicked(self, isChecked):
        self.settings.setValue('startup', isChecked)
        # print(isChecked)

    # When "Lock when other appears" Clicked
    @Slot('QString')
    def lockOther(self, isChecked):
        self.settings.setValue('lockOther', convertBool(isChecked))

    # When "Lock when other appears" Clicked
    @Slot('QString')
    def autoLock(self, isChecked):
        self.settings.setValue('autoLock', convertBool(isChecked))

    # When "Auto Unlock when you are there" Clicked
    @Slot('QString')
    def autoUnlock(self, isChecked):
        self.settings.setValue('autoUnlock', convertBool(isChecked))
