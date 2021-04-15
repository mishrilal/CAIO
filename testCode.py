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

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# Creating table
# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#         )""")

# c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 50000)")
c.execute("INSERT INTO employees VALUES ('sedrftgyhu', '12mnjhbgftdr32131', 9876543)")

c.execute("SELECT * FROM employees")

print(c.fetchall())

conn.commit()

conn.close()