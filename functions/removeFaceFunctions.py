import os
from pathlib import Path

from PySide2.QtCore import Slot, QObject, QSettings, Signal


class RemoveFace(QObject):
    removeImage = Signal(str)

    def __init__(self):
        super().__init__()
        self.settings = QSettings('CAIO', 'Preferences')
        self.imagePath = str(Path.home()) + '/CAIO/'
        self.person = self.settings.value('person')

    @Slot()
    def deleteImage(self):
        self.person = self.settings.value('person')
        os.remove(os.path.join(self.imagePath, "img_%s.jpg" % (str(self.person))))
        self.person = 0
        self.removeImage.emit("true")
        self.settings.setValue('person', self.person)
        print("Delete: ", self.person)
