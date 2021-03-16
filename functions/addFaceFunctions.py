from PyQt5.QtCore import QObject, pyqtSlot


class AddFace(QObject):

    @pyqtSlot()
    def addFace(self):
        # initialize camera here
        print("Add Button Pressed")

    @pyqtSlot()
    def captureClicked(self):
        # Capture Function here
        print("Capture Btn Clicked")




