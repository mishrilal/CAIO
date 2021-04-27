from PySide2.QtCore import QSettings

from lockMain import LockMain

settings = QSettings('CAIO', 'Preferences')
settings.setValue('lockFile', 1)
lock = LockMain()
lock.runLock()
