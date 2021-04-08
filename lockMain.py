from PySide2.QtCore import QSettings

from functions.lockFunctions import LockSystem


class LockMain:

    # constructor
    def __init__(self):
        super().__init__()
        self.settings = QSettings('CAIO', 'Preferences')
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
