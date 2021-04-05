import time

import numpy as np
import face_recognition as fr
import cv2
from ctypes import CDLL


class detectFace:
    def __init__(self):
        self.showLockScreen = 1

    def lock(self):
        loginPF = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
        loginPF.SACLockScreenImmediate()

    # keeps unlock until you in frame and someone else with you
    def keepUnlocked(self):
        video_capture = cv2.VideoCapture(0)

        mishri_image = fr.load_image_file("/Users/mishrilal/Projects/CAIO/images/mishri.png")
        mishri_face_encoding = fr.face_encodings(mishri_image)[0]

        known_face_encodings = [mishri_face_encoding]
        known_face_names = ["Mishri"]

        while True:
            ret, frame = video_capture.read()

            rgb_frame = frame[:, :, ::-1]

            face_locations = fr.face_locations(rgb_frame)
            face_encodings = fr.face_encodings(rgb_frame, face_locations)

            self.showLockScreen = 1

            for face_encodings in face_encodings:
                matches = fr.compare_faces(known_face_encodings, face_encodings)

                face_distances = fr.face_distance(known_face_encodings, face_encodings)

                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    self.name = known_face_names[best_match_index]
                    self.showLockScreen = 0
                    print(self.name)

                else:
                    self.showLockScreen = 1
                    self.name = "unknown"
                    print(self.name)
                    self.lock()

            if self.showLockScreen == 1:
                print("lock")
                self.lock()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(3)
            print("time")

        video_capture.release()
        cv2.destroyAllWindows()

    # Keeps unlocked if you or no one in frame
    def youNoOne(self):
        video_capture = cv2.VideoCapture(0)

        mishri_image = fr.load_image_file("/Users/mishrilal/Projects/CAIO/images/mishri.png")
        mishri_face_encoding = fr.face_encodings(mishri_image)[0]

        known_face_encodings = [mishri_face_encoding]
        known_face_names = ["Mishri"]

        while True:
            ret, frame = video_capture.read()

            rgb_frame = frame[:, :, ::-1]

            face_locations = fr.face_locations(rgb_frame)
            face_encodings = fr.face_encodings(rgb_frame, face_locations)

            for face_encodings in face_encodings:
                matches = fr.compare_faces(known_face_encodings, face_encodings)

                face_distances = fr.face_distance(known_face_encodings, face_encodings)

                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    self.name = known_face_names[best_match_index]
                    self.showLockScreen = 0
                    print(self.name)

                else:
                    self.showLockScreen = 1
                    self.name = "unknown"
                    print(self.name)
                    self.lock()

            if self.showLockScreen == 1:
                print("lock")
                self.lock()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(3)
            print("time")

        video_capture.release()
        cv2.destroyAllWindows()


lock = detectFace()
lock.youNoOne()
