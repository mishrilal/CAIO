import os
import pathlib
from os import path
from pathlib import Path

import cv2
from PySide2.QtCore import QObject, Slot, Signal, QSettings


class AddFace(QObject):
    setCaptureDetails = Signal(str)
    setCaptureBtn = Signal(str)
    person = 0

    # constructor
    def __init__(self):
        super().__init__()
        self.settings = QSettings('CAIO', 'Preferences')
        # self.person = self.settings.value('person')
        self.person = self.settings.value('person')
        # self.settings.setValue('person', 0)

        print(self.settings.value('person'))
        pathImage = str(Path.home()) + '/CAIO/img_%s.jpg' % str(self.person)

        if not path.isfile(pathImage):
            self.settings.setValue('person', 0)
            self.person = 0

        if self.person is None:
            self.settings.setValue('person', 0)
            # self.person = self.settings.value('person')
            self.person = 0
            print(self.person)

        # path to save
        self.createCAIOdir = str(Path.home()) + '/CAIO'
        pathlib.Path(self.createCAIOdir).mkdir(parents=True, exist_ok=True)
        self.save_path2 = self.createCAIOdir + "/"
        self.save_path = "images/captured/"

    @Slot()
    def captureClicked(self):
        # Capture Function here
        print("Capture Btn Clicked")
        # Initialize Webcam
        cap = cv2.VideoCapture(0)
        count = 0

        self.person = 1
        self.settings.setValue('person', self.person)

        while True:

            ret, frame = cap.read()
            if ret:
                count += 1
                cv2.imwrite(os.path.join(self.save_path2, "img_%s.jpg" % (str(self.person))), frame)
            else:
                print("Face not found")

            if cv2.waitKey(1) == 13 or count == 1:  # 13 is the Enter Key
                break

        # self.person += 1
        # self.settings.setValue('person', self.person)
        cap.release()
        cv2.destroyAllWindows()
        # print("Collecting Samples Complete")
        # self.click_photo()
        # self.person += 1

        self.setCaptureDetails.emit("Captured Successfully")
        self.setCaptureBtn.emit("false")
