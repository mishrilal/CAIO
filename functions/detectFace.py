import numpy as np
import face_recognition as fr
import cv2
from PySide2.QtWidgets import QMainWindow

# LOCK SCREEN
from ui.ui_lock_screen import Ui_LockScreen


# class lockWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Lock Screen")


def lockScreen(self):
    self.lockui = Ui_LockScreen()
    self.lockui.setupUi(self)
    self.showFullScreen()


def detectFace(self):
    # self.lockui.setupUi(self)
    # # self.lcok = lockWindow()
    self.showLockScreen = 0
    video_capture = cv2.VideoCapture(0)

    mishri_image = fr.load_image_file("/Users/mishrilal/Projects/CAIO/images/mishri.png")
    mishri_face_encoding = fr.face_encodings(mishri_image)[0]

    known_face_encondings = [mishri_face_encoding]
    known_face_names = ["Mishri"]

    while True:
        ret, frame = video_capture.read()

        rgb_frame = frame[:, :, ::-1]

        face_loactions = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_loactions)

        for (top, right, bottom, left), face_encodings in zip(face_loactions, face_encodings):

            matches = fr.compare_faces(known_face_encondings, face_encodings)

            name = "Unknown"

            face_distances = fr.face_distance(known_face_encondings, face_encodings)

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                print(name)
                # self.close()
                # print("Window Closed")

            else:
                print(name)
                lockScreen(self)
                print("Window Shown")
                self.showLockScreen = 1

        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #
        #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #
        # cv2.imshow('webcame_facerecognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if self.showLockScreen:
            break

    video_capture.release()
    cv2.destroyAllWindows()
