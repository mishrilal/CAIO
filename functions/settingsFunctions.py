from PySide2.QtCore import QObject, Slot, QSettings


def convertBool(value):
    if value == "true":
        return True
    return False


# Called from main.py to set preference
def setSettingsValue(self):
    self.settings = QSettings('CAIO', 'Preferences')
    self.setAutoUnlock.emit(self.settings.value('autoUnlock'))
    self.setOnlyAdmin.emit(self.settings.value('onlyAdmin'))
    self.setOnlyAdminStrict.emit(self.settings.value('onlyAdminStrict'))
    self.setSomeoneAppears.emit(self.settings.value('someoneAppears'))
    self.setSomeoneAppearsStrict.emit(self.settings.value('someoneAppearsStrict'))


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
    def autoUnlockClicked(self, isChecked):
        self.settings.setValue('autoUnlock', isChecked)
        # print(isChecked)

    # When "Lock when other appears" Clicked
    @Slot('QString')
    def onlyAdminClicked(self, isChecked):
        self.settings.setValue('onlyAdmin', isChecked)
        if isChecked == "true":
            self.settings.setValue('onlyAdminStrict', "false")
            self.settings.setValue('someoneAppears', "false")
            self.settings.setValue('someoneAppearsStrict', "false")

    # When "Lock when other appears" Clicked
    @Slot('QString')
    def onlyAdminStrictClicked(self, isChecked):
        self.settings.setValue('onlyAdminStrict', isChecked)
        if isChecked == "true":
            self.settings.setValue('onlyAdmin', "false")
            self.settings.setValue('someoneAppears', "false")
            self.settings.setValue('someoneAppearsStrict', "false")

    # When "Auto Unlock when you are there" Clicked
    @Slot('QString')
    def someoneAppearsClicked(self, isChecked):
        self.settings.setValue('someoneAppears', isChecked)
        if isChecked == "true":
            self.settings.setValue('onlyAdminStrict', "false")
            self.settings.setValue('onlyAdmin', "false")
            self.settings.setValue('someoneAppearsStrict', "false")

    @Slot('QString')
    def someoneAppearsStrictClicked(self, isChecked):
        self.settings.setValue('someoneAppearsStrict', isChecked)
        if isChecked == "true":
            self.settings.setValue('onlyAdminStrict', "false")
            self.settings.setValue('someoneAppears', "false")
            self.settings.setValue('onlyAdmin', "false")
