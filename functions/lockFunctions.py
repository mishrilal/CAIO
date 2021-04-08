import platform
import re
import time
from pathlib import Path
from os import path
import ctypes

import numpy as np
import face_recognition as fr
import cv2
from ctypes import CDLL


class LockSystem:
    def __init__(self):
        self.imgPath = str(Path.home()) + '/CAIO/img_1.jpg'
        self.showLockScreen = True
        self.captureTime = 3    # in seconds

        # Checking OS for Lock() function
        self.osName = platform.platform()
        if re.search("macOS", self.osName):
            self.osName = "macOS"
        elif re.search("Windows", self.osName):
            self.osName = "Windows"

    # Lock Function for MacOS and Windows
    def lock(self):
        if self.osName == "macOS":
            loginPF = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
            loginPF.SACLockScreenImmediate()
        elif self.osName == "Windows":
            ctypes.windll.user32.LockWorkStation()
        else:
            pass

    # keeps unlock until you in frame
    def onlyAdminStrict(self):
        video_capture = cv2.VideoCapture(0)

        if path.isfile(self.imgPath):
            user_image = fr.load_image_file(self.imgPath)
            user_face_encoding = fr.face_encodings(user_image)[0]

            known_face_encodings = [user_face_encoding]
            known_face_names = ["ADMIN"]

            while True:
                ret, frame = video_capture.read()

                rgb_frame = frame[:, :, ::-1]

                face_locations = fr.face_locations(rgb_frame)
                face_encodings = fr.face_encodings(rgb_frame, face_locations)

                self.showLockScreen = True

                for face_encodings in face_encodings:
                    matches = fr.compare_faces(known_face_encodings, face_encodings)

                    face_distances = fr.face_distance(known_face_encodings, face_encodings)

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        self.name = known_face_names[best_match_index]
                        self.showLockScreen = False
                        print(self.name)

                    else:
                        self.showLockScreen = True
                        self.name = "unknown"
                        print(self.name)
                        self.lock()

                if self.showLockScreen:
                    print("lock")
                    self.lock()

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                time.sleep(self.captureTime)
                print("time")

        video_capture.release()
        cv2.destroyAllWindows()

    # Keeps unlocked if you or no one in frame
    def onlyAdmin(self):
        video_capture = cv2.VideoCapture(0)

        if path.isfile(self.imgPath):
            user_image = fr.load_image_file(self.imgPath)
            user_face_encoding = fr.face_encodings(user_image)[0]

            known_face_encodings = [user_face_encoding]
            known_face_names = ["ADMIN"]

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
                        self.showLockScreen = False
                        print(self.name)

                    else:
                        self.showLockScreen = True
                        self.name = "unknown"
                        print(self.name)
                        self.lock()

                if self.showLockScreen:
                    print("lock")
                    self.lock()

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                time.sleep(self.captureTime)
                print("time")

        video_capture.release()
        cv2.destroyAllWindows()

    # keep Unlocked when someone else appears in the frame with admin
    def someoneAppears(self):
        video_capture = cv2.VideoCapture(0)

        if path.isfile(self.imgPath):
            user_image = fr.load_image_file(self.imgPath)
            user_face_encoding = fr.face_encodings(user_image)[0]

            known_face_encodings = [user_face_encoding]
            known_face_names = ["ADMIN"]

            while True:
                ret, frame = video_capture.read()

                rgb_frame = frame[:, :, ::-1]

                face_locations = fr.face_locations(rgb_frame)
                face_encodings = fr.face_encodings(rgb_frame, face_locations)

                print("FaceEncodings ", len(face_encodings))

                # faces = len(face_encodings)

                checkSelf = False

                for face_encodings in face_encodings:
                    matches = fr.compare_faces(known_face_encodings, face_encodings)

                    face_distances = fr.face_distance(known_face_encodings, face_encodings)

                    best_match_index = np.argmin(face_distances)
                    # Test this code with TWO peoples
                    # if faces == 1:
                    #     if matches[best_match_index]:
                    #         print("Face Found")
                    #         self.name = known_face_names[best_match_index]
                    #         self.showLockScreen = 0
                    #         print(self.name)
                    #     else:
                    #         print("Not found")
                    #         self.showLockScreen = True
                    #         self.name = "unknown"
                    #         print(self.name)
                    #         self.lock()
                    # else:
                    #     if matches[best_match_index]:
                    #         print("Face Found in else")
                    #         print("Face Found")
                    #         self.name = known_face_names[best_match_index]
                    #         self.showLockScreen = 0
                    #         print(self.name)

                    if matches[best_match_index]:
                        self.name = known_face_names[best_match_index]
                        self.showLockScreen = False
                        print(self.name)
                        checkSelf = True

                    else:
                        self.name = "unknown"
                        print(self.name)
                        if checkSelf:
                            self.showLockScreen = False
                            print("Admin Found")
                        else:
                            self.showLockScreen = True
                            self.lock()

                if self.showLockScreen:
                    print("lock")
                    self.lock()

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                # time.sleep(self.captureTime)
                print("time")

        video_capture.release()
        cv2.destroyAllWindows()

    # Lock when no one is there also keep unlocked till admin is there with others
    def someoneAppearsStrict(self):
        video_capture = cv2.VideoCapture(0)

        if path.isfile(self.imgPath):
            user_image = fr.load_image_file(self.imgPath)
            user_face_encoding = fr.face_encodings(user_image)[0]

            known_face_encodings = [user_face_encoding]
            known_face_names = ["ADMIN"]

            while True:
                ret, frame = video_capture.read()

                rgb_frame = frame[:, :, ::-1]

                face_locations = fr.face_locations(rgb_frame)
                face_encodings = fr.face_encodings(rgb_frame, face_locations)

                print("FaceEncodings ", len(face_encodings))

                self.showLockScreen = True

                # faces = len(face_encodings)

                checkSelf = False

                for face_encodings in face_encodings:
                    matches = fr.compare_faces(known_face_encodings, face_encodings)

                    face_distances = fr.face_distance(known_face_encodings, face_encodings)

                    best_match_index = np.argmin(face_distances)
                    # Test this code with TWO peoples
                    # if faces == 1:
                    #     if matches[best_match_index]:
                    #         print("Face Found")
                    #         self.name = known_face_names[best_match_index]
                    #         self.showLockScreen = False
                    #         print(self.name)
                    #     else:
                    #         print("Not found")
                    #         self.showLockScreen = True
                    #         self.name = "unknown"
                    #         print(self.name)
                    #         self.lock()
                    # else:
                    #     if matches[best_match_index]:
                    #         print("Face Found in else")
                    #         print("Face Found")
                    #         self.name = known_face_names[best_match_index]
                    #         self.showLockScreen = False
                    #         print(self.name)

                    if matches[best_match_index]:
                        self.name = known_face_names[best_match_index]
                        self.showLockScreen = False
                        print(self.name)
                        checkSelf = True

                    else:
                        self.name = "unknown"
                        print(self.name)
                        if checkSelf:
                            self.showLockScreen = False
                            print("Admin Found")
                        else:
                            self.showLockScreen = True
                            self.lock()

                if self.showLockScreen:
                    print("lock")
                    self.lock()

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                # time.sleep(self.captureTime)
                print("time")

        video_capture.release()
        cv2.destroyAllWindows()


# lock = LockSystem()
# lock.onlyAdminStrict()
