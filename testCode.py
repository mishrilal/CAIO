# import sys
#
# from PySide2.QtSql import QSqlDatabase, QSqlQueryModel
# from PySide2.QtWidgets import QApplication, QTableView
#
# app = QApplication(sys.argv)
#
# db = QSqlDatabase.addDatabase("QSQLITE")
# db.setDatabaseName("employee.db")
# db.open()
#
# projectModel = QSqlQueryModel()
# projectModel.setQuery("select * from employees", db)
#
# projectView = QTableView()
# projectView.setModel(projectModel)
#
# projectView.show()
# app.exec_()
# from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
#
# app = QApplication([])  # Start an application.
# window = QWidget()  # Create a window.
# layout = QVBoxLayout()  # Create a layout.
# button = QPushButton("I'm just a Button man")  # Define a button
# layout.addWidget(QLabel('Hello World!'))  # Add a label
# layout.addWidget(button)  # Add the button man
# window.setLayout(layout)  # Pass the layout to the window
# window.show()  # Show window
# app.exec_()  # Execute the App


# import os
# import sys
#
# from PySide2.QtCore import QObject
# from PySide2.QtGui import QIcon
# from PySide2.QtQml import QQmlApplicationEngine
# from PySide2.QtWidgets import QApplication
#
#
# class MainWindow(QObject):
#     def __init__(self):
#         super().__init__()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon("images/svg_images/logo_icon.svg"))
#     engine = QQmlApplicationEngine()
#
#     # Get Context
#     main = MainWindow()
#
#     engine.load(os.path.join(os.path.dirname(__file__), "qml/lockMain.qml"))
#
#     if not engine.rootObjects():
#         sys.exit(-1)
#     sys.exit(app.exec_())
# import sys
#
# from PySide2.QtWidgets import QApplication
#
#
# class MainWindow:
#     pass
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec_())

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('caio.db')

c = conn.cursor()

# c.execute("""CREATE TABLE allLogs(ID integer primary key autoincrement,
#                                     Date TEXT,
#                                     Time TEXT,
#                                     lockedBy TEXT,
#                                     Event TEXT);
#     """)
# c.execute("""CREATE TABLE adminLogs(ID integer primary key autoincrement,
#                                     Date TEXT,
#                                     Time TEXT,
#                                     lockedBy TEXT,
#                                     Event TEXT);
#     """)
# c.execute("""CREATE TABLE someoneLogs(ID integer primary key autoincrement,
#                                     Date TEXT,
#                                     Time TEXT,
#                                     lockedBy TEXT,
#                                     Event TEXT);
#     """)
# c.execute("""CREATE TABLE nobodyLogs(ID integer primary key autoincrement,
#                                     Date TEXT,
#                                     Time TEXT,
#                                     lockedBy TEXT,
#                                     Event TEXT);
#     """)
# name = "Known" + " Left"
# eventlock = "Locked to main screen"
#
# unix = int(time.time())
# date = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y'))
# time = str(datetime.datetime.fromtimestamp(unix).strftime('%H:%M:%S'))
#
# c.execute("insert into allLogs(Date, Time, lockedBy, Event) values(?, ?, ?, ?)",
#           (date, time, name, eventlock))

# c.execute("select * from allLogs order by id desc")
# print(c.fetchall())
#
c.execute("select * from allLogs order by id desc")
print(c.fetchall())

# c.execute("drop table allLogs")
# c.execute("drop table adminLogs")
# c.execute("drop table someoneLogs")
# c.execute("drop table nobodyLogs")


conn.commit()

conn.close()

# conn = sqlite3.connect('tutorial.db')
# c = conn.cursor()
#
#
# def create_table():
#     c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
#
#
# def data_entry():
#     c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
#
#     conn.commit()
#     c.close()
#     conn.close()
#
#
# def dynamic_data_entry():
#     unix = int(time.time())
#     date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
#     keyword = 'Python'
#     value = random.randrange(0, 10)
#
#     c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
#               (unix, date, keyword, value))
#
#     conn.commit()
#
#
# # create_table()
# # # for i in range(10):
# # #     dynamic_data_entry()
# # #     time.sleep(1)
# #
# # c.execute("SELECT * FROM stuffToPlot")
# # print(c.fetchall())
#
# c.close
# conn.close()

# functions
#     6 Python Files
# images
#     svg_images
#         13 svg files
# qml
#     controls
#         8 qml files
#     pages
#         6 qml files
#     3 more qml files
#
# sqlite3 database - caio.db
# main.py
# lockMain.py
