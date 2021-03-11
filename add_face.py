import cv2
import string
import random

from PyQt5.QtGui import QImage, QPixmap

from main import *


class AddFace(MainWindow):
    def __init__(self):
        super().__init__()
        self.value = 1

        self.ui.turn_on.clicked.connect(lambda: self.turnOnCamera())
        self.ui.capture.clicked.connect(lambda: self.captureImage())
        self.ui.turn_off.clicked.connect(lambda: self.turnOffCamera())


# Turn On Camera
def turnOnCamera(self):
    cap = cv2.VideoCapture(1)

    while cap.isOpened():

        ret, frame = cap.read()

        if ret:
            self.displayImage(frame, 1)
            cv2.waitKey()

            if self.logic == 2:
                imgName = string.ascii_letters
                imgName = ''.join(random.choice(imgName) for i in range(10))
                imgName = 'C:/Users/mishrilalchhaparia/Pictures/CAIO/IC_%s.png'%(imgName)
                print(imgName)
                cv2.imwrite(imgName, frame)

                self.logic = 1

            else:
                print("Not Found")

        cap.release()
        cv2.destroyAllWindows()


# Turn OFF Camera
def turnOffCamera(self):
    cap.close()


# Capture Image
def captureImage(self):
    self.logic = 2


def imageDisplay(self, img, window=1):
    qformat = QImage.Format_Indexed8

    if len(img.shape) == 3:
        if len(img.shape) == 4:
            qformat = QImage.Format_RGBA8888

        else:
            qformat = QImage.Format_RGB888

        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.image.setPixmap(QPixmap.fromImage(img))
        self.image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
