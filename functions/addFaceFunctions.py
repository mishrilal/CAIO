import datetime
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap


class AddFace(QObject):
    @pyqtSlot()
    def addFace(self):
        # initialize camera here
        print("Add Button Pressed")
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")
        self.logic = 0
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)

            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif self.logic == 2:
                # SPACE pressed
                date = datetime.datetime.now()
                img_name = 'images/captured/img_%s%s%sT%s%s%s.png' % (
                    date.year, date.month, date.day, date.hour, date.minute, date.second)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                self.logic = 1

        cam.release()

        cv2.destroyAllWindows()

    @pyqtSlot()
    def captureClicked(self):
        # Capture Function here
        print("Capture Btn Clicked")
        self.logic = 2
