import os
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

from PySide2.QtCore import QObject, Slot, Signal


class AddFace(QObject):
    setCaptureDetails = Signal(str)
    logic = 0

    # constructor
    def __init__(self):
        super().__init__()

        # getting available cameras
        self.available_cameras = QCameraInfo.availableCameras()

        # if no camera found
        if not self.available_cameras:
            # exit the code
            sys.exit()

        # path to save
        self.save_path = "images/captured/"

        # Set the default camera.
        self.select_camera(0)

    # method to select camera
    def select_camera(self, i):
        # getting the selected camera
        self.camera = QCamera(self.available_cameras[i])

        # setting capture mode to the camera
        self.camera.setCaptureMode(QCamera.CaptureStillImage)

        # start the camera
        self.camera.start()

        # creating a QCameraImageCapture object
        self.capture = QCameraImageCapture(self.camera)


        # when image captured showing message
        self.capture.imageCaptured.connect(lambda d,
                                                  i: self.status.showMessage("Image captured : "
                                                                             + str(self.save_seq)))

        # getting current camera name
        self.current_camera_name = self.available_cameras[i].description()

        # inital save sequence
        self.save_seq = 0

    # method to take photo
    def click_photo(self):
        # time stamp
        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")

        # capture the image and save it on the save path
        self.capture.capture(os.path.join(self.save_path,
                                          "img_%s_%s.jpg" % (
                                              timestamp,
                                              self.save_seq
                                          )))

        # increment the sequence
        self.save_seq += 1

    @Slot()
    def captureClicked(self):
        # Capture Function here
        print("Capture Btn Clicked")
        self.logic = 2
        n = 0
        while n < 100:
            self.click_photo()
            self.setCaptureDetails.emit("Captured %s of 100" % (n + 1))
            time.sleep(0.001)
            print(n)
            n += 1
