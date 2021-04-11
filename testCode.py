import sys

from PySide2.QtSql import QSqlDatabase, QSqlQueryModel
from PySide2.QtWidgets import QApplication, QTableView

app = QApplication(sys.argv)

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("employee.db")
db.open()

projectModel = QSqlQueryModel()
projectModel.setQuery("select * from employees", db)

projectView = QTableView()
projectView.setModel(projectModel)

projectView.show()
app.exec_()