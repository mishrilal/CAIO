import datetime
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap


class AddFace(QObject):
    #setCameraLabel = pyqtSignal(str, arguments=['cameraLabel'])
    setCameraLabel = pyqtSignal(QPixmap)
    @pyqtSlot()
    def addFace(self):
        # initialize camera here
        print("Add Button Pressed")
        cam = cv2.VideoCapture(0)

        #cv2.namedWindow("test")
        self.logic = 0
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            #cv2.imshow("test", frame)

            k = cv2.waitKey()
            #self.setCameraLabel.emit("Camera is On")
            self.displayImage(frame, 1)
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

    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA888

            else:
                qformat = QImage.Format_RGB888

        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        img = QPixmap.fromImage(img)
        #self.setCameraLabel.setPixmap(QPixmap.fromImage(img))
        #self.setCameraLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


