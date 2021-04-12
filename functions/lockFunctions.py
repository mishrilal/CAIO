import platform
import re
import time
from pathlib import Path
from os import path
import ctypes
import getpass

import numpy as np
import face_recognition as fr
import cv2
from ctypes import CDLL

from PySide2.QtCore import QSettings


class LockSystem:
    def __init__(self):
        self.imgPath = str(Path.home()) + '/CAIO/img_1.jpg'
        self.showLockScreen = True
        self.captureTime = 3  # in seconds

        self.userName = getpass.getuser()
        self.userName = self.userName.capitalize()

        self.settings = QSettings('CAIO', 'Preferences')
        self.noOfLocksAdmin = self.settings.value('noOfLocksAdmin')
        self.totalLocks = self.settings.value('totalLocks')

        if self.noOfLocksAdmin is None:
            self.noOfLocksAdmin = 0
            self.settings.setValue('noOfLocksAdmin', self.noOfLocksAdmin)

        if self.totalLocks is None:
            self.totalLocks = 0
            self.settings.setValue('totalLocks', self.totalLocks)

        # Checking OS for Lock() function
        self.osName = platform.platform()
        if re.search("macOS", self.osName):
            self.osName = "macOS"
        elif re.search("Windows", self.osName):
            self.osName = "Windows"

        self.isLocked = False
        self.isUnlocked = True

    # Lock Function for MacOS and Windows
    def lock(self):
        self.isLocked = True
        # if self.osName == "macOS":
        #     loginPF = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
        #     loginPF.SACLockScreenImmediate()
        # elif self.osName == "Windows":
        #     ctypes.windll.user32.LockWorkStation()
        # else:
        #     pass

    # keeps unlock until you in frame
    def onlyAdminStrict(self):
        video_capture = cv2.VideoCapture(0)

        if path.isfile(self.imgPath):
            user_image = fr.load_image_file(self.imgPath)
            user_face_encoding = fr.face_encodings(user_image)[0]

            known_face_encodings = [user_face_encoding]
            known_face_names = [self.userName]

            while True:
                ret, frame = video_capture.read()

                rgb_frame = frame[:, :, ::-1]

                face_locations = fr.face_locations(rgb_frame)
                face_encodings = fr.face_encodings(rgb_frame, face_locations)

                self.showLockScreen = True
                self.isUnlocked = False

                for face_encodings in face_encodings:
                    matches = fr.compare_faces(known_face_encodings, face_encodings)

                    face_distances = fr.face_distance(known_face_encodings, face_encodings)

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        self.name = known_face_names[best_match_index]
                        self.showLockScreen = False
                        print(self.name)
                        self.isUnlocked = True

                    else:
                        self.showLockScreen = True
                        self.name = "unknown"
                        print(self.name)
                        self.lock()

                if self.showLockScreen:
                    print("lock")
                    self.lock()

                if self.isUnlocked:
                    if self.isLocked:
                        self.noOfLocksAdmin += 1
                        self.totalLocks += 1
                        self.settings.setValue('noOfLocksAdmin', self.noOfLocksAdmin)
                        self.settings.setValue('totalLocks', self.totalLocks)
                        print("noOfLocks: ", self.noOfLocksAdmin)
                        print("TotalLocks: ", self.totalLocks)
                        self.isLocked = False

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                time.sleep(self.captureTime)
                # time.sleep(1)
                print("time")
                print("isLocked: ", self.isLocked)
                print("isUnlocked: ", self.isUnlocked)

        video_capture.release()
        cv2.destroyAllWindows()

    # Keeps unlocked if you or no one in frame
    def onlyAdmin(self):
        video_capture = cv2.VideoCapture(0)

        if path.isfile(self.imgPath):
            user_image = fr.load_image_file(self.imgPath)
            user_face_encoding = fr.face_encodings(user_image)[0]

            known_face_encodings = [user_face_encoding]
            known_face_names = [self.userName]

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
            known_face_names = [self.userName]

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
            known_face_names = [self.userName]

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
