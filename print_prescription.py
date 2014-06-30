# -*- coding: utf-8 -*-
"""
Created on Fri Feb 7 16:17:00 2014

@author: pmaurier
"""

import sys
    
from PyQt4 import QtGui, QtWebKit, QtCore
from string import Template

from database import DATA_STRUCTURE

class MainWindow(QtGui.QMainWindow):
    # Signal saying that the page have been printed
    pagePrinted = QtCore.pyqtSignal()
    def __init__(self, values=[item[2] for item in DATA_STRUCTURE]):
        super(MainWindow, self).__init__()
        
        DEFAULT_ZOOM = .8
        
        if values[4] == 2:
            port = u"intermittent ou permanent"
        elif values[4] == 1:
            port = u"intermittent"
        else:
            port = u"permanent"
        
        if values[5] == 2:
            verres = u"Bifocaux"
        elif values[5] == 1:
            verres = u"Foyers progressifs"
        else:
            verres = u"Unifocaux"
        
        if values[6] == 5:
            teinte = u"Photochromiques"
        elif values[6] == 1:
            teinte = u"Teinte T1"
        elif values[6] == 2:
            teinte = u"Teinte T2"
        elif values[6] == 3:
            teinte = u"Teinte T3"
        elif values[6] == 4:
            teinte = u"Teinte T4"
        else:
            teinte = u"Non teintés"
            
        if values[12] != 0:
            odprisme = "prisme : %+0.2f" % values[12]
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
            ogprisme = "prisme : %+0.2f" % values[18]
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
            avcorrigee = u"Acuité visuelle corrigée en vision de loin :<br />"
            if values[21] != 0:
                avcorrigee += (u'<span id="marge">Œil Droit %2d/10'+
                                    u'</span><br />') % values[21]
            if values[22] != 0:
                avcorrigee += (u'<span id="marge">Œil Gauche %2d/10'+
                                    u'</span><br />') % values[22]
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
                amblyopie += u'Œil Droit'
            if values[25]:
                amblyopie += u'Œil Gauche'
        
        if avcorrigee != "" or amblyopie != "":
            remarque = u"<u>Remarques :</u>"
        else:
            remarque = u""       
        
        self.values = dict(datePrescription = values[2].toString('dd/MM/yyyy'),
                    prenom = str(values[1]), nom = str(values[0]),
                    cmu = (u"CMU" if values[3] else ''), port = port,
                    verres = verres,
                    teinte = teinte,
                    reflets = (u", antireflets" if values[7] else ''),
                    odsphere = "%+0.2f" % values[8],
                    odcylindre = "%0.2f" % values[9],
                    odaxe = u"%03d°" % values[10],
                    odaddition = self.addition(values[11]),
                    odprisme = odprisme,
                    ogsphere = "%+0.2f" % values[14],
                    ogcylindre = "%0.2f" % values[15],
                    ogaxe = u"%03d°" % values[16],
                    ogaddition = self.addition(values[17]),
                    ogprisme = ogprisme,
                    remarque = remarque, amblyopie = amblyopie,
                    avcorrigee = avcorrigee, remarques = values[26])

        # Define the Web view size and behaviour
        self.web = QtWebKit.QWebView()
        self.web.settings().setDefaultTextEncoding("utf-8")
        self.web.setSizePolicy(QtGui.QSizePolicy.Fixed,
                               QtGui.QSizePolicy.Fixed)
        self.web.page().mainFrame().setScrollBarPolicy(QtCore.Qt.Horizontal,
                    QtCore.Qt.ScrollBarAlwaysOff)
        self.web.page().mainFrame().setScrollBarPolicy(QtCore.Qt.Vertical,
                    QtCore.Qt.ScrollBarAlwaysOff)
        self.web.setDisabled(True) #Allow wheel events to be sent to scrollArea

        scrollArea = QtGui.QScrollArea()
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        scrollArea.setWidget(self.web)
        scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        
        zoomBar = QtGui.QSlider(QtCore.Qt.Horizontal)
        zoomBar.setMinimum(50)
        zoomBar.setMaximum(200)
        zoomBar.setValue(DEFAULT_ZOOM*100)
        zoomBar.setFixedWidth(200)
        zoomBar.setTickPosition(zoomBar.TicksBelow)
        zoomBar.setTickInterval(10)
        zoomBar.valueChanged.connect(lambda: self.changeZoom(
                                                        zoomBar.value()/100.))

        toolbar = QtGui.QToolBar()
        printAction = toolbar.addAction("Imprimer")
        pdfAction = toolbar.addAction("PDF")
        cancelAction = toolbar.addAction("Annuler")
        printAction.triggered.connect(self.printIt)
        pdfAction.triggered.connect(lambda: self.printIt("pdf"))
        cancelAction.triggered.connect(self.close)
        toolbar.addWidget(zoomBar)
        
        # Define the MainWindow Characteristics
        self.setWindowTitle(u'Aperçu avant impression')
        self.setCentralWidget(scrollArea)
        self.addToolBar(toolbar)
        
        maxScreenHeight = QtGui.QDesktopWidget().availableGeometry().height()
        windowHeight = min(maxScreenHeight, int(1500*1.1*DEFAULT_ZOOM))
        windowWidth = int(1000*1.1*DEFAULT_ZOOM)        
        self.resize(windowWidth, windowHeight)
       
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setPageMargins(0, 0, 0, 0, QtGui.QPrinter.Millimeter)

        # Loading template file
        inputTemplate = 'template.htm'
        try:
            with open(inputTemplate) as inputFileHandle:
                self.page = Template(unicode(inputFileHandle.read(),
                                             encoding='utf-8'))
        
        except IOError:
            sys.stderr.write("Error: Could not open %s\n" % (inputTemplate))
            sys.exit(-1)
        
        self.changeZoom(DEFAULT_ZOOM)
        self.web.setHtml(self.loadValues())
        self.show()

    def addition(self, value):
        if value != 0:
            return "Add %+0.2f" % value
        else:
            return ""

    def changeZoom(self, zoomValue=1):
        """ Modify the size and the zoom of the view to given value """
        self.web.setFixedSize(int(992*zoomValue), int(1402*zoomValue))
        self.web.setZoomFactor(zoomValue)

    def loadValues(self):
        """ loading dynamic values """
        data = self.page.substitute(
               datePrescription = self.values['datePrescription'],
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
        
    def printIt(self, output="printer"):
        """ Print the page to the printer, close the preview window and
            send the signal that the page is printed """
        if output == "pdf":
            self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
            self.printer.setOutputFileName(self.values['prenom'].capitalize()+
                           "_"+
                           self.values['nom'].upper()+
                           "_"+
                           self.values['datePrescription'].replace("/","-")+
                           ".pdf")
        self.web.setZoomFactor(1)
        self.web.print_(self.printer)
        if (not self.signalsBlocked()):
            self.pagePrinted.emit()
        self.close()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())
