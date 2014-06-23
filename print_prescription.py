# -*- coding: utf-8 -*-
"""
Created on Fri Feb 7 16:17:00 2014

@author: pmaurier
"""

import sys
    
from PyQt4 import QtGui, QtWebKit, QtCore
from string import Template

class MainWindow(QtGui.QMainWindow):
    
    pagePrinted = QtCore.pyqtSignal()
    
    def __init__(self, values=["","",QtCore.QDate.currentDate(), False, 0, 0, 0, False,
                         0, 0, 180, 0, 0, 0, 0, 0, 180, 0, 0, 0, False, 0, 0, 0,
                         False, False, ""], output="pdf"):
        super(MainWindow, self).__init__()

        # Parameters
        self.zoomValue = .7
        
        if values[4] == 2:
            port = u"Intermittent ou Permanent"
        elif values[4] == 1:
            port = u"Intermittent"
        else:
            port = u"Permanent"
        
        if values[5] == 2:
            verres = u"Bifocaux"
        elif values[5] == 1:
            verres = u"Foyers progressif"
        else:
            verres = u"Unifocaux"
        
        if values[6] == 5:
            teinte = u"Photochromiques"
        elif values[6] == 1:
            teinte = u"teinte T1"
        elif values[6] == 2:
            teinte = u"teinte T2"
        elif values[6] == 3:
            teinte = u"teinte T3"
        elif values[6] == 4:
            teinte = u"teinte T4"
        else:
            teinte = u"Non teintés"
            
        if values[12] != 0:
            odprisme = "prisme : "+str(values[12])
            if values[13] == 0:
                odprisme += u" base inférieure<br />"
            elif values[13] == 1:
                odprisme += u" base supérieure<br />"
            elif values[13] == 2:
                odprisme += u" base externe<br />"
            elif values[13] == 3:
                odprisme += u" base interne<br />"
        else:
            odprisme = u""
            
        if values[18] != 0:
            ogprisme = "prisme : "+str(values[18])
            if values[19] == 0:
                ogprisme += u" base inférieure<br />"
            elif values[19] == 1:
                ogprisme += u" base supérieure<br />"
            elif values[19] == 2:
                ogprisme += u" base externe<br />"
            elif values[19] == 3:
                ogprisme += u" base interne<br />"
        else:
            ogprisme = u""
        
        if values[20]:
            avcorrigee = u"Acuité visuelle corrigée en vision de loin:<br />"
            if values[21] != 0:
                avcorrigee += u"Œil Droit "+str(values[21])+"/10<br />"
            if values[22] != 0:
                avcorrigee += u"Œil Gauche "+str(values[22])+"/10<br />"
        else:
            avcorrigee = u""
        
        if values[23] == 1:
            amblyopie = u"Amblyopie fonctionnelle "
        elif values[23] == 2:
            amblyopie = u"Amblyopie organique "
        else:
            amblyopie = u""
        
        if values[24] and values[25]:
            amblyopie += u"Œil Droit et Œil Gauche"
        else:
            if values[24]:
                amblyopie += u"Œil Droit"
            if values[25]:
                amblyopie += u"Œil Gauche"
        
        if avcorrigee != "" or amblyopie != "":
            remarque = u"<u>Remarques :</u>"
        else:
            remarque = u""       
        
        self.values = dict(datePrescription = values[2].toString('dd/MM/yyyy'),
                    prenom = str(values[1]), nom = str(values[0]), cmu = (u"CMU" if values[3] else ''),
                    port = port, verres = verres,
                    teinte = teinte, reflets = (u"antireflets" if values[7] else ''),
                    odsphere = values[8], odcylindre = values[9], odaxe = str(values[10])+u"°",
                    odaddition = values[11], odprisme = odprisme, ogsphere = values[14],
                    ogcylindre = values[15], ogaxe = str(values[16])+u"°", ogaddition = values[17],
                    ogprisme = ogprisme, remarque = remarque, amblyopie = amblyopie,
                    avcorrigee = avcorrigee, remarques = values[26])

        self.web = QtWebKit.QWebView()
        self.web.settings().setDefaultTextEncoding("utf-8")
        self.web.setFixedSize(int(1000*self.zoomValue), int(1500*self.zoomValue))
        self.web.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)

        toolbar = QtGui.QToolBar()
        printAction = toolbar.addAction("Imprimer")
        cancelAction = toolbar.addAction("Annuler")
        printAction.triggered.connect(self.printIt)
        cancelAction.triggered.connect(self.close)

        self.setWindowTitle(u'Aperçu avant impression')
        self.setCentralWidget(self.web)
        self.addToolBar(toolbar)
        
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setPageMargins(0, 0, 0, 0, QtGui.QPrinter.Millimeter)

        if output == "pdf":
            self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
            self.printer.setOutputFileName("test.pdf")

        # Loading template file
        inputTemplate = 'template.htm'
        try:
            with open(inputTemplate) as inputFileHandle:
                self.page = Template(unicode(inputFileHandle.read(), encoding='utf-8'))
        
        except IOError:
            sys.stderr.write("Error: Could not open %s\n" % (inputTemplate))
            sys.exit(-1)
        
        self.preview()

    def loadValues(self):
        # loading dynamic values
        data = self.page.substitute(datePrescription = self.values['datePrescription'],
                           prenom = self.values['prenom'].capitalize(),
                           nom = self.values['nom'].upper(),
                           cmu = self.values['cmu'],
                           port = self.values['port'],
                           verres = self.values['verres'],
                           teinte = self.values['teinte'],
                           reflets = self.values['reflets'],
                           odsphere = self.values['odsphere'],
                           odcylindre = self.values['odcylindre'],
                           odaxe = self.values['odaxe'],
                           odaddition = self.values['odaddition'],
                           odprisme = self.values['odprisme'],
                           ogsphere = self.values['ogsphere'],
                           ogcylindre = self.values['ogcylindre'],
                           ogaxe = self.values['ogaxe'],
                           ogaddition = self.values['ogaddition'],
                           ogprisme = self.values['ogprisme'],
                           remarque = self.values['remarque'],
                           amblyopie = self.values['amblyopie'],
                           avcorrigee = self.values['avcorrigee'],
                           remarques = self.values['remarques'].replace("\n", "<br />"))
        return data
       
    def preview(self):
        # Display preview window
        self.web.setHtml(self.loadValues())
        self.web.setZoomFactor(self.zoomValue)
        
        self.show()
        
    def printIt(self):
        self.web.setZoomFactor(1)
        self.web.print_(self.printer)
        if (not self.signalsBlocked()):
            self.pagePrinted.emit()
        self.close()
        
#web.loadFinished.connect(printIt)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())


#from PyQt4 import QtCore, QtGui, QtWebKit
#
#def printprescription():
#    filename = 'test.pdf'
#    printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
#    printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
##    printer.setOrientation(QtGui.QPrinter.Landscape)
#    
#    printer.setOutputFileName(filename)
#    
##    fichier = open('test.htm')    
#    def printdoc():
#        view.print_(printer)
#        print 'plip'
#        
#    view = QtWebKit.QWebView()  
##    view.load(QtCore.QUrl('http://www.google.fr'))
#    view.setHtml('<b>TEST</b>')
#    print 'plop'
##    view.loadFinished.connect(printdoc)
#    printdoc()
    


#from printUI import Ui_Dialog 
#
#import os, time
#
#NormalFormat = QtGui.QTextCharFormat()
#
#ItalicFormat = QtGui.QTextCharFormat()
#ItalicFormat.setFontItalic(True)
#
#TitleFormat = QtGui.QTextCharFormat()  
#TitleFormat.setFontPointSize(15) 
#TitleFormat.setFontWeight(QtGui.QFont.Bold)  
#TitleFormat.setVerticalAlignment(QtGui.QTextCharFormat.AlignMiddle)  
## TitleFormat.setUnderlineStyle(QtGui.QTextCharFormat.SingleUnderline)
#
#tableFormat = QtGui.QTextTableFormat()
#tableFormat.setAlignment(QtCore.Qt.AlignHCenter) 
#tableFormat.setAlignment(QtCore.Qt.AlignLeft)
##tableFormat.setBackground(QtGui.QColor("#ffffff"))
#tableFormat.setCellPadding(0)
#tableFormat.setCellSpacing(0)
#tableFormat.setBorder(1)
#tableFormat.setHeaderRowCount(1)
##tableFormat.PageBreakFlag(tableFormat.PageBreak_AlwaysAfter)
#
#headerFormat = QtGui.QTextCharFormat()
#headerFormat.setFontPointSize(10)  
#headerFormat.setFontWeight(QtGui.QFont.Bold)
#
#cellFormat = QtGui.QTextCharFormat()
#cellFormat.setFontPointSize(10)
#
#centerAlignment = QtGui.QTextBlockFormat()
#centerAlignment.setAlignment(QtCore.Qt.AlignCenter)
#
#OG = 5
#OD = 1
#stockColumn = 13
#
#class myDialog(QtGui.QDialog, Ui_Dialog):
#    def __init__(self):
#        super(myDialog, self).__init__()
#        super(Ui_Dialog, self).__init__()
#        
#        self.setupUi(self)
#    
#    def getValues(self):
#        if self.numRadio.isChecked():
#            sort = 0
#        elif self.rRadio.isChecked():
#            sort = OD
#        elif self.lRadio.isChecked():
#            sort = OG
#        return sort, self.stockCheckBox.isChecked()
#    
#    def on_acceptButton_clicked(self):
#        print "pwet"
#        self.close()
#    
#    def on_rejectButton_clicked(self):
#        print "prout"
#        self.close()
#
#def createpdf(model):
#    
#    dlg = myDialog()
#    if dlg.exec_():
#        sort, stock = dlg.getValues()
#    
#        new_filename = os.path.join(os.getcwd(), 'oryx_print_'+time.strftime('%Y-%m-%d_%Hh%M',time.localtime())+'.pdf')
#        filename = QtGui.QFileDialog.getSaveFileName(None,
#                       u'Choix du nom du fichier PDF', 
#                       new_filename, u'PDF (*.pdf)')   
#                       
#        if filename != '':
#            printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
#            printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
#            printer.setOrientation(QtGui.QPrinter.Landscape)
#            
#            printer.setOutputFileName(filename)
#            printtable(model, printer, sort, stock)
#
#def printtable(model, printer, sortedcolum, stock):
#    editor = QtGui.QTextBrowser()
#
#    #Print title and print date/time
#    editor.setCurrentCharFormat(TitleFormat)  
#    editor.setAlignment(QtCore.Qt.AlignCenter)
#    editor.append(u'Trié par '+model.horizontalHeaderItem(sortedcolum).text())
#
#    timestamp = u'Imprimé le : ' + time.strftime('%Y-%m-%d_%Hh%M',time.localtime())
#    editor.setCurrentCharFormat(ItalicFormat)
#    editor.append(timestamp)
#    
#    editor.setCurrentCharFormat(NormalFormat)  
#
#    cursor = editor.textCursor() 
#    cursor.beginEditBlock()
#
#    # Calculate the number of rows to print
#    if stock:
#        rowCount = 0
#        for row in xrange(model.rowCount()):
#            if model.item(row, stockColumn).text() == "1":
#                rowCount += 1
#    else:
#        rowCount = model.rowCount()
#
#    #Create the table with the right number of rows and columns
#    table = cursor.insertTable(rowCount+1, model.columnCount(), tableFormat) 
#
#    frame = cursor.currentFrame()
#    frameFormat = frame.frameFormat()
#    frameFormat.setBorder(0)
#    frame.setFrameFormat(frameFormat)
#
#    #Headers
#    for i in xrange(model.columnCount()):
#        # selecting the right cell
#        titre = table.cellAt(0,i) 
#          
#        # place cursor in the right place 
#        cellCursor = titre.firstCursorPosition()  
#        cellCursor.setBlockFormat(centerAlignment)
#        
#        # writing into the cell
#        cellCursor.insertText(model.horizontalHeaderItem(i).text(), headerFormat)
#
#    cell = QtGui.QTextTableCell()
#    cellCursor = QtGui.QTextCursor()
#
#    model.sort(sortedcolum, QtCore.Qt.AscendingOrder)
#    
#    rowPrint = 0
#    for row in xrange(0, model.rowCount()):
#        if (model.item(row, stockColumn).text() == "1") or (not stock):
#            rowPrint += 1
#            for col in xrange(table.columns()):
#                cell = table.cellAt(rowPrint,col)
#                cellCursor = cell.firstCursorPosition()
#                cellCursor.setBlockFormat(centerAlignment)
#                cellCursor.insertText(model.item(row,col).text(), cellFormat)   
#
#    model.sort(0, QtCore.Qt.AscendingOrder)    
#    
#    # End editing table  
#    cursor.endEditBlock()
#
#    # Printing 
#    editor.print_(printer)



#if __name__ == '__main__':
#    import sys
#    app = QtGui.QApplication(sys.argv)
#    printprescription()
#    sys.exit(app.exec_())