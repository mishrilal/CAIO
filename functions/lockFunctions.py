import datetime
import getpass
import platform
import re
import sqlite3
import time
from os import path
from pathlib import Path

import cv2
import face_recognition as fr
import numpy as np
from PySide2.QtCore import QSettings


class LockSystem:
    def __init__(self):
        self.imgPath = str(Path.home()) + '/CAIO/img_1.jpg'
        self.showLockScreen = True
        self.captureTime = 3  # in seconds

        self.userName = getpass.getuser()
        self.userName = self.userName.title()

        self.settings = QSettings('CAIO', 'Preferences')

        # self.settings.setValue('noOfLocksAdmin', 0)
        # self.settings.setValue('noOfSomeoneElseLocks', 0)
        # self.settings.setValue('noOfNobodyLocks', 0)
        # self.settings.setValue('totalLocks', 0)

        self.noOfLocksAdmin = self.settings.value('noOfLocksAdmin')
        self.totalLocks = self.settings.value('totalLocks')
        self.noOfSomeoneElseLocks = self.settings.value('noOfSomeoneElseLocks')
        self.noOfNobodyLocks = self.settings.value('noOfNobodyLocks')
        self.isLogChanged = self.settings.value('logChanged')

        if self.noOfLocksAdmin is None:
            self.noOfLocksAdmin = 0
            self.settings.setValue('noOfLocksAdmin', self.noOfLocksAdmin)

        if self.noOfSomeoneElseLocks is None:
            self.noOfSomeoneElseLocks = 0
            self.settings.setValue('noOfSomeoneElseLocks', self.noOfSomeoneElseLocks)

        if self.noOfNobodyLocks is None:
            self.noOfNobodyLocks = 0
            self.settings.setValue('noOfNobodyLocks', self.noOfNobodyLocks)

        if self.totalLocks is None:
            self.totalLocks = 0
            self.settings.setValue('totalLocks', self.totalLocks)

        if self.isLogChanged is None:
            self.isLogChanged = 1
            self.settings.setValue('logChanged', self.isLogChanged)

        # Checking OS for Lock() function
        self.osName = platform.platform()
        if re.search("macOS", self.osName):
            self.osName = "macOS"
        elif re.search("Windows", self.osName):
            self.osName = "Windows"

        self.isLocked = False
        self.isUnlocked = True
        self.isSomeoneElse = False
        self.someoneElseLocked = False
        self.isNobody = False
        self.countFace = 0

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

    def logs(self, who):
        lockedBy = "Locked when "
        eventLock = "Locked to System Lock Screen"

        unix = int(time.time())
        dateLog = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y'))
        timeLog = str(datetime.datetime.fromtimestamp(unix).strftime('%H:%M:%S'))

        conn = sqlite3.connect('caio.db')
        c = conn.cursor()

        if who == "admin":
            lockedBy = lockedBy + self.userName + " Left"
            c.execute("insert into adminLogs(Date, Time, lockedBy, Event) values(?, ?, ?, ?)",
                      (dateLog, timeLog, lockedBy, eventLock))
        elif who == "someone":
            lockedBy = lockedBy + "Someone came"
            c.execute("insert into someoneLogs(Date, Time, lockedBy, Event) values(?, ?, ?, ?)",
                      (dateLog, timeLog, lockedBy, eventLock))
        elif who == "nobody":
            lockedBy = lockedBy + "No One there"
            c.execute("insert into nobodyLogs(Date, Time, lockedBy, Event) values(?, ?, ?, ?)",
                      (dateLog, timeLog, lockedBy, eventLock))

        c.execute("insert into allLogs(Date, Time, lockedBy, Event) values(?, ?, ?, ?)",
                  (dateLog, timeLog, lockedBy, eventLock))

        conn.commit()
        conn.close()

        self.isLogChanged = 1
        self.settings.setValue('logChanged', self.isLogChanged)

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

                self.countFace = len(face_encodings)

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
                        if self.countFace == 1:
                            self.isUnlocked = True

                    else:
                        self.showLockScreen = True
                        self.someoneElseLocked = True
                        self.name = "unknown"
                        # print("Someone else ", self.name)
                        self.lock()

                if self.showLockScreen:
                    print("lock")
                    self.lock()

                print("FaceCount: ", self.countFace)
                if self.countFace == 0:
                    self.isNobody = True

                if self.isUnlocked:
                    if self.isLocked:
                        # print("In is Locked")
                        print("isNobody: ", self.isNobody)
                        if self.countFace <= 1:
                            self.isSomeoneElse = False
                            # print("isSomeElse", self.isSomeoneElse)
                        else:
                            self.isSomeoneElse = True
                            self.someoneElseLocked = True
                        if not self.someoneElseLocked:
                            if not self.isSomeoneElse:
                                self.totalLocks += 1
                                self.settings.setValue('totalLocks', self.totalLocks)

                                if self.isNobody:
                                    self.noOfNobodyLocks += 1
                                    self.settings.setValue('noOfNobodyLocks', self.noOfNobodyLocks)
                                    self.noOfLocksAdmin += 1
                                    self.settings.setValue('noOfLocksAdmin', self.noOfLocksAdmin)
                                    self.isNobody = False
                                    self.logs("admin")
                                    self.logs("nobody")
                                else:
                                    self.noOfLocksAdmin += 1
                                    self.settings.setValue('noOfLocksAdmin', self.noOfLocksAdmin)
                                    self.logs("admin")
                                # print("noOfLocks: ", self.noOfLocksAdmin)
                                # print("TotalLocks: ", self.totalLocks)
                                self.isLocked = False
                            else:
                                pass
                        else:
                            if self.someoneElseLocked:
                                self.totalLocks += 1
                                self.noOfSomeoneElseLocks += 1
                                self.settings.setValue('noOfSomeoneElseLocks', self.noOfSomeoneElseLocks)
                                self.settings.setValue('totalLocks', self.totalLocks)
                                # print("In last Else isSomeone ", self.isSomeoneElse)
                                self.someoneElseLocked = False
                                self.isLocked = False
                                self.logs("someone")
                                # print("In last Else someoneElseLocked ", self.someoneElseLocked)

                        # print("****************")
                        # print("isUnlocked: ", self.isUnlocked)
                        # print("isLocked: ", self.isLocked)
                        # print("isSomeOneElse: ", self.isSomeoneElse)
                        # print("someoneElseLocked: ", self.someoneElseLocked)
                        # print("****************")

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                # time.sleep(self.captureTime)
                time.sleep(1)
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

                self.countFace = len(face_encodings)
                self.isUnlocked = False

                for face_encodings in face_encodings:
                    matches = fr.compare_faces(known_face_encodings, face_encodings)

                    face_distances = fr.face_distance(known_face_encodings, face_encodings)

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        self.name = known_face_names[best_match_index]
                        self.showLockScreen = False
                        print(self.name)
                        if self.countFace == 1:
                            self.isUnlocked = True

                    else:
                        self.showLockScreen = True
                        self.someoneElseLocked = True
                        self.name = "unknown"
                        # print("Someone else ", self.name)
                        self.lock()

                if self.showLockScreen:
                    print("lock")
                    self.lock()

                print("FaceCount: ", self.countFace)
                if self.isUnlocked:
                    if self.isLocked:
                        # print("In is Locked")
                        if self.countFace <= 1:
                            self.isSomeoneElse = False
                            # print("isSomeElse", self.isSomeoneElse)
                        else:
                            self.isSomeoneElse = True
                            self.someoneElseLocked = True

                        if self.someoneElseLocked:
                            self.totalLocks += 1
                            self.noOfSomeoneElseLocks += 1
                            self.settings.setValue('noOfSomeoneElseLocks', self.noOfSomeoneElseLocks)
                            self.settings.setValue('totalLocks', self.totalLocks)
                            # print("In last Else isSomeone ", self.isSomeoneElse)
                            self.someoneElseLocked = False
                            self.isLocked = False
                            self.logs("someone")

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
                self.isUnlocked = False

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
                        self.isUnlocked = True

                    else:
                        self.name = "unknown"
                        print(self.name)
                        if checkSelf:
                            self.showLockScreen = False
                            print("Admin Found")
                            self.isUnlocked = True
                        else:
                            self.showLockScreen = True
                            self.lock()

                if self.showLockScreen:
                    print("lock")
                    self.lock()

                if self.isUnlocked:
                    if self.isLocked:
                        print("Someone Came and Now unlocked")
                        self.isLocked = False
                        self.noOfSomeoneElseLocks += 1
                        self.totalLocks += 1
                        self.settings.setValue('noOfSomeoneElseLocks', self.noOfSomeoneElseLocks)
                        self.settings.setValue('totalLocks', self.totalLocks)
                        self.logs("someone")

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

                self.countFace = len(face_encodings)

                checkSelf = False
                self.isUnlocked = False

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
                        self.isUnlocked = True

                    else:
                        self.name = "unknown"
                        print(self.name)
                        if checkSelf:
                            self.showLockScreen = False
                            print("Admin Found")
                            self.isUnlocked = True
                        else:
                            self.showLockScreen = True
                            if self.countFace != 0:
                                self.someoneElseLocked = True
                            self.lock()

                if self.showLockScreen:
                    print("lock")
                    self.lock()

                if self.countFace == 0:
                    self.isNobody = True

                if self.isUnlocked:
                    if self.isLocked:
                        self.isLocked = False

                        self.totalLocks += 1
                        self.settings.setValue('totalLocks', self.totalLocks)

                        if self.isNobody:
                            self.noOfNobodyLocks += 1
                            # self.noOfSomeoneElseLocks += 1
                            self.settings.setValue('noOfNobodyLocks', self.noOfNobodyLocks)
                            # self.settings.setValue('noOfSomeoneElseLocks', self.noOfSomeoneElseLocks)
                            print("isNobody", self.isNobody, self.someoneElseLocked)
                            self.isNobody = False
                            self.logs("nobody")
                        else:
                            if self.someoneElseLocked:
                                if not self.isNobody:
                                    self.noOfSomeoneElseLocks += 1
                                    print("someoneElseLocked", self.isNobody, self.someoneElseLocked)
                                    self.settings.setValue('noOfSomeoneElseLocks', self.noOfSomeoneElseLocks)
                                    self.someoneElseLocked = False
                                    self.logs("someone")

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                time.sleep(self.captureTime)
                print("time")

        video_capture.release()
        cv2.destroyAllWindows()

# lock = LockSystem()
# lock.onlyAdminStrict()
