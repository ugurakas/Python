import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets

i=0

def initializeModel(model):
    model.setTable('student')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    # model.setFilter("id<10")
    model.select()

    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Surname")


def refreshModel(model):
    model.select()

def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    view.horizontalHeader().setSortIndicatorShown(True)
    view.setMinimumSize(400,300)
    return view


def addrow():

    model.rowCount()
    ret = model.insertRows(model.rowCount(), 1)
    if ret:
        print ("Adding Succeed")



def removerow():
    model.removeRow(view1.currentIndex().row())
    refreshModel(model)

def sirala(i,sira):
    view1.sortByColumn(i,sira)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('Trial.db')
    model = QtSql.QSqlTableModel()

    delrow = -1
    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)



    view1.horizontalHeader().sortIndicatorChanged.connect(sirala)


    dlg = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view1)

    button = QtWidgets.QPushButton("Add line")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    btn1 = QtWidgets.QPushButton("Delete line")
    btn1.clicked.connect(removerow)
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Sample")
    dlg.show()
    sys.exit(app.exec_())