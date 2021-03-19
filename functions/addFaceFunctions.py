import datetime

import cv2
from PySide2.QtCore import QObject, Slot


class AddFace(QObject):

    @Slot()
    def addFace(self):
        # initialize camera here
        print("Add Button Pressed")

        cam = cv2.VideoCapture(0)

        cv2.namedWindow("")
        cv2.destroyAllWindows()
        self.logic = 0
        while True:

            # cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            # self.setCameraLabel.emit("Camera is On")
            # self.displayImage(frame, 1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif self.logic == 2:
                n = 0

                while n < 100:
                    ret, frame = cam.read()
                    if not ret:
                        print("failed to grab frame")
                        break
                    # SPACE pressed
                    date = datetime.datetime.now()
                    img_name = 'images/captured/img_%s%s%sT%s%s%s_%s.png' % (
                        date.year, date.month, date.day, date.hour, date.minute, date.second, n)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    n += 1

                self.logic = 1
                break

        cam.release()

        cv2.destroyAllWindows()

    @Slot()
    def captureClicked(self):
        # Capture Function here
        print("Capture Btn Clicked")
        self.logic = 2
