import glob
import os
import shutil

import cv2

from PySide2.QtCore import QObject, Slot, Signal, QSettings

# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')


# Load functions
def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces == ():
        return None

    # Crop all faces found
    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]

    return cropped_face


class AddFace(QObject):
    setCaptureDetails = Signal(str)
    person = 0

    # logic = 0
    #
    # constructor
    def __init__(self):
        super().__init__()
        self.settings = QSettings('CAIO', 'Preferences')
        self.person = self.settings.value('person')
        print(self.settings.value('person'))

        if self.person is None:
            self.settings.setValue('person', 1)
            self.person = self.settings.value('person')
            print(self.person)

    #
    #     # getting available cameras
    #     self.available_cameras = QCameraInfo.availableCameras()
    #
    #     # if no camera found
    #     if not self.available_cameras:
    #         # exit the code
    #         sys.exit()
    #
    #     # path to save
    #     self.save_path = "images/captured/"
    #
    #     # Set the default camera.
    #     self.select_camera(0)
    #
    # # method to select camera
    # def select_camera(self, i):
    #     # getting the selected camera
    #     self.camera = QCamera(self.available_cameras[i])
    #
    #     # setting capture mode to the camera
    #     self.camera.setCaptureMode(QCamera.CaptureStillImage)
    #
    #     # start the camera
    #     self.camera.start()
    #
    #     # creating a QCameraImageCapture object
    #     self.capture = QCameraImageCapture(self.camera)
    #
    #
    #     # when image captured showing message
    #     self.capture.imageCaptured.connect(lambda d,
    #                                               i: self.status.showMessage("Image captured : "
    #                                                                          + str(self.save_seq)))
    #
    #     # getting current camera name
    #     self.current_camera_name = self.available_cameras[i].description()
    #
    #     # inital save sequence
    #     self.save_seq = 0
    #
    # # method to take photo
    # def click_photo(self):
    #     # time stamp
    #     timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")
    #
    #     # capture the image and save it on the save path
    #     self.capture.capture(os.path.join(self.save_path,
    #                                       "img_%s_%s.jpg" % (
    #                                           timestamp,
    #                                           self.save_seq
    #                                       )))
    #
    #     # increment the sequence
    #     self.save_seq += 1
    #

    @Slot()
    def captureClicked(self):
        # Capture Function here
        print("Capture Btn Clicked")
        # Initialize Webcam
        cap = cv2.VideoCapture(0)
        count = 0
        # Collect 100 samples of your face from webcam input
        while True:

            ret, frame = cap.read()
            if face_extractor(frame) is not None:
                count += 1
                face = cv2.resize(face_extractor(frame), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                # Save file in specified directory with unique name
                imgName = 'img_person' + str(self.person) + '_' + str(count)
                file_name_path = 'images/captured/' + imgName + '.jpg'
                cv2.imwrite(file_name_path, face)

                if count == 45:
                    cv2.imwrite('images/faces/'+str(self.person)+'.jpg', face)

                # Put count on images and display live count
                # cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                # cv2.imshow('Face Cropper', face)
            else:
                print("Face not found")
                pass

            if cv2.waitKey(1) == 13 or count == 100:  # 13 is the Enter Key
                break
        self.person += 1
        self.settings.setValue('person', self.person)
        cap.release()
        cv2.destroyAllWindows()
        print("Collecting Samples Complete")
        self.setCaptureDetails.emit("Collected Samples Successfully")

