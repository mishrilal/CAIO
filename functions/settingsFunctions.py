## Not in USE


import os
import sys
from PySide2.QtCore import QObject, Slot, QSettings


def convertBool(value):
    if value == "true":
        return True
    return False


# Called from main.py to set preference
def setSettingsValue(self):
    self.settings = QSettings('CAIO', 'Preferences')
    self.setStartup.emit(self.settings.value('startup'))
    self.setLockOthers.emit(self.settings.value('lockOther'))
    self.setAutoLock.emit(self.settings.value('autoLock'))
    self.setAutoUnlock.emit(self.settings.value('autoUnlock'))


# def setSettingsValue():
#     setStartup = Signal(str)
#     settings = QSettings('CAIO', 'Preference')
#     setStartup.emit(settings.value('startup'))


class SettingsPage(QObject):

    # constructor
    def __init__(self):
        QObject.__init__(self)
        self.settings = QSettings('CAIO', 'Preferences')

    # When "Unlock at StartUp" Clicked
    @Slot('QString')
    def startupClicked(self, isChecked):
        self.settings.setValue('startup', isChecked)
        # print(isChecked)

    # When "Lock when other appears" Clicked
    @Slot('QString')
    def lockOther(self, isChecked):
        self.settings.setValue('lockOther', isChecked)

    # When "Lock when other appears" Clicked
    @Slot('QString')
    def autoLock(self, isChecked):
        self.settings.setValue('autoLock', isChecked)

    # When "Auto Unlock when you are there" Clicked
    @Slot('QString')
    def autoUnlock(self, isChecked):
        self.settings.setValue('autoUnlock', isChecked)
