# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:00:21 2014

@author: pmaurier
"""

from PyQt4 import QtSql, QtGui, QtCore
from datetime import date

DATA_STRUCTURE = [
    ["nom", "VARCHAR(255)", ""],                        #0
    ["prenom", "VARCHAR(255)", ""],                     #1
    ["date", "DATE", QtCore.QDate.currentDate().toString("yyyy-MM-dd")],       #2
    ["cmu", "BOOLEAN", False],                          #3
    ["port", "TINYINT", 0],                             #4
    ["verres", "TINYINT", 0],                           #5
    ["teinte", "TINYINT", 0],                           #6
    ["reflets", "BOOLEAN", True],                      #7
    ["OD_sphere", "REAL", 0],                           #8
    ["OD_cylindre", "REAL", 0],                         #9
    ["OD_axe", "REAL", 180],                            #10
    ["OD_addition", "REAL", 0],                         #11
    ["OD_prisme", "REAL", 0],                           #12
    ["OD_base", "TINYINT", 2],                          #13
    ["OG_sphere", "REAL", 0],                           #14
    ["OG_cylindre", "REAL", 0],                         #15
    ["OG_axe", "REAL", 180],                            #16
    ["OG_addition", "REAL", 0],                         #17
    ["OG_prisme", "REAL", 1],                           #18
    ["OG_base", "TINYINT", 2],                          #19
    ["REM_acuite", "BOOLEAN", False],                   #20
    ["REM_acuite_OD", "REAL", 0],                       #21
    ["REM_acuite_OG", "REAL", 0],                       #22
    ["REM_amblyopie_value", "TINYINT", 0],              #23
    ["REM_amblyopie_OD", "BOOLEAN", False],             #24
    ["REM_amblyopie_OG", "BOOLEAN", False],             #25
    ["remarques", "TEXT", ""],                           #26
    ["distance_vision", "BOOLEAN", True],               #27
    ["near_vision", "BOOLEAN", True]                    #28
    ]

class MainWindow(QtGui.QMainWindow):
    # Signal returning the selected line
    resultSelected = QtCore.pyqtSignal(list)
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Recherche")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        
        self.table = QtGui.QTableView()
        self.table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.table.doubleClicked.connect(self.returnRow)

        toolbar = QtGui.QToolBar()

        toolbar.addWidget(QtGui.QLabel(" Nom : "))
        self.searchNameEdit = QtGui.QLineEdit()
        self.searchNameEdit.setSizePolicy(QtGui.QSizePolicy.Fixed, 
                                          QtGui.QSizePolicy.Fixed)
        toolbar.addWidget(self.searchNameEdit)

        toolbar.addWidget(QtGui.QLabel(u" Prénom : "))
        self.searchSurnameEdit = QtGui.QLineEdit()
        self.searchSurnameEdit.setSizePolicy(QtGui.QSizePolicy.Fixed, 
                                             QtGui.QSizePolicy.Fixed)
        toolbar.addWidget(self.searchSurnameEdit)
        
        toolbar.addWidget(QtGui.QLabel(u" Date : "))
        self.searchDateEdit = QtGui.QDateEdit()
        toolbar.addWidget(self.searchDateEdit)
        self.searchDateEdit.setDate(date.today())
        self.searchDateEdit.setEnabled(False)
        
        self.dateCheckbox = QtGui.QCheckBox('')
        toolbar.addWidget(self.dateCheckbox)
        
        toolbar.addSeparator()
        deleteAction = toolbar.addAction(u"Supprimer")
        
        self.searchNameEdit.textChanged.connect(self.filterTable)
        self.searchSurnameEdit.textChanged.connect(self.filterTable)
        self.searchDateEdit.dateChanged.connect(self.filterTable)
        self.dateCheckbox.stateChanged.connect(self.checkboxaction)
        deleteAction.triggered.connect(self.deleteSelectedRow)

        self.setCentralWidget(self.table)
        self.addToolBar(toolbar)

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data.db')
        if not self.db.open():
            print self.db.lastError().text()

        query = QtSql.QSqlQuery()
        query_text = "CREATE TABLE IF NOT EXISTS ordonnances("+"".join(
                [elem[0]+" "+elem[1]+", " for elem in DATA_STRUCTURE])
        query_text =  query_text[:-2 ]+ ")"
        query.exec_(query_text)

        self.model = QtSql.QSqlTableModel()
        self.model.setTable("ordonnances")
        self.model.sort(2, QtCore.Qt.AscendingOrder)
        self.table.setModel(self.model)

        for num, elem in enumerate(DATA_STRUCTURE):
            self.model.setHeaderData(num, QtCore.Qt.Horizontal, elem[0])

    def addNewLine(self, data):
        """ Insert a new row into the database """
        self.model.insertRows(0, 1) 
        
        # Enter values
        for num, elem in enumerate(data):
            self.model.setData(self.model.index(0, num), elem)    
        
        # Add data to the model
        self.model.submitAll()

    def filterTable(self):
        """ Filter elements displayed according to edit fields """      
        query_text = ('nom LIKE "'+self.searchNameEdit.text()+'%" AND '
                      'prenom LIKE "'+self.searchSurnameEdit.text()+'%"')
                      
        # Add the date filter if dateCheckbox is checked
        if self.dateCheckbox.isChecked():
            query_text += ('AND date = "'+
                        self.searchDateEdit.date().toString('yyyy-MM-dd')+'"')
        
        # Apply the filter and sort the view
        self.model.setFilter(query_text)
        self.model.sort(2, QtCore.Qt.AscendingOrder)

    def checkboxaction(self):
        """ Enable or disable date edit field according to checkbox state """
        self.searchDateEdit.setEnabled(self.dateCheckbox.isChecked())
        self.filterTable()
    
    def deleteSelectedRow(self):
        """ Remove selected row after a user warning"""
        if len(self.table.selectionModel().selectedRows())>0:
            question = QtGui.QMessageBox.warning(self,
                u'Supprimer la ligne sélectionnée ?',
                u'Voulez-vous vraiment supprimer la ligne sélectionnée ?',
                QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No)
            if question == QtGui.QMessageBox.Yes:
                self.model.removeRow(
                        self.table.selectionModel().selectedRows()[0].row()) 
                self.model.submitAll()

    def returnRow(self):
        """ Return the row selected and hide the search window """
        self.hide()
        if (not self.signalsBlocked()):
            self.resultSelected.emit([item.data().toString() for item 
                in self.table.selectionModel().selectedIndexes()])

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
