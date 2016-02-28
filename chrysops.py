# -*- coding: utf-8 -*-
"""
Created on Sun Feb 02 2014

@author: pmaurier
"""

from PyQt4 import QtCore, QtGui

from chrysopsUI import Ui_MainWindow 

import print_prescription
import database

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from config import (MAX_SPHERE, MIN_SPHERE, STEP_SPHERE, DEFAULT_SPHERE,
                    MAX_CYL, MIN_CYL, STEP_CYL, DEFAULT_CYL,
                    MAX_AXIS, MIN_AXIS, STEP_AXIS, DEFAULT_AXIS,
                    MAX_ADD, MIN_ADD, STEP_ADD, DEFAULT_ADD)

def str2bool(value):
    """ Convert a string value to boolean 
        True is returned for (case insensitive):
            yes
            true
            t
            1
    """
    return str(value).lower() in ("yes", "true", "t", "1")

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()
        
        self.search_window = database.MainWindow()        
        
        self.search_window.resultSelected.connect(self.loadValues)
        
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        """ create actions and default values of the interface """
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.printButton.clicked.connect(self.printAction)
        self.searchButton.clicked.connect(self.searchAction)
        self.clearButton.clicked.connect(self.clearAction)  
    
        self.normalGlassesRadio.toggled.connect(self.glassesGroupChanged)
        self.progressiveGlassesRadio.toggled.connect(self.glassesGroupChanged)
        self.bifocalGlassesRadio.toggled.connect(self.glassesGroupChanged)
        
        # Right Eye     
        # Correction
        self.rSphereSpin.setMaximum(MAX_SPHERE)
        self.rSphereSpin.setMinimum(MIN_SPHERE)
        self.rSphereSpin.setSingleStep(STEP_SPHERE)
        self.rSphereSpin.setValue(DEFAULT_SPHERE)
        self.rSphereSpin.valueChanged.connect(self.modified)
        
        self.rCylSpin.setMaximum(MAX_CYL)
        self.rCylSpin.setMinimum(MIN_CYL)
        self.rCylSpin.setSingleStep(STEP_CYL)
        self.rCylSpin.setValue(DEFAULT_CYL)
        self.rCylSpin.valueChanged.connect(self.modified)
        
        self.rLabelCylPos.setVisible(False)
        
        self.rAxisSpin.setMaximum(MAX_AXIS)
        self.rAxisSpin.setMinimum(MIN_AXIS)
        self.rAxisSpin.setSingleStep(STEP_AXIS)
        self.rAxisSpin.setValue(DEFAULT_AXIS)
        self.rAxisSpin.valueChanged.connect(self.modified)
        
        self.r90Button.clicked.connect(self.r90Action)
        self.rFineCheckbox.stateChanged.connect(self.rFineChanged)
        
        self.rAddSpin.setMaximum(MAX_ADD)
        self.rAddSpin.setMinimum(MIN_ADD)
        self.rAddSpin.setSingleStep(STEP_ADD)
        self.rAddSpin.setValue(DEFAULT_ADD)
        self.rAddSpin.valueChanged.connect(self.additionChanged)
        
        self.rLinkCheckbox.stateChanged.connect(self.linkChanged)
        self.rPrismGroup.toggled.connect(self.prismGroupChanged)
        
        # Left Eye
        # Correction
        self.lSphereSpin.setMaximum(MAX_SPHERE)
        self.lSphereSpin.setMinimum(MIN_SPHERE)
        self.lSphereSpin.setSingleStep(STEP_SPHERE)
        self.lSphereSpin.setValue(DEFAULT_SPHERE)
        self.lSphereSpin.valueChanged.connect(self.modified)
        
        self.lCylSpin.setMaximum(MAX_CYL)
        self.lCylSpin.setMinimum(MIN_CYL)
        self.lCylSpin.setSingleStep(STEP_CYL)
        self.lCylSpin.setValue(DEFAULT_CYL)
        self.lCylSpin.valueChanged.connect(self.modified)
        
        self.lLabelCylPos.setVisible(False)
        
        self.lAxisSpin.setMaximum(MAX_AXIS)
        self.lAxisSpin.setMinimum(MIN_AXIS)
        self.lAxisSpin.setSingleStep(STEP_AXIS)
        self.lAxisSpin.setValue(DEFAULT_AXIS)
        self.lAxisSpin.valueChanged.connect(self.modified)
        
        self.l90Button.clicked.connect(self.l90Action)
        self.lFineCheckbox.stateChanged.connect(self.lFineChanged)
        
        self.lAddSpin.setMaximum(MAX_ADD)
        self.lAddSpin.setMinimum(MIN_ADD)
        self.lAddSpin.setSingleStep(STEP_ADD)
        self.lAddSpin.setValue(DEFAULT_ADD)
        self.lAddSpin.valueChanged.connect(self.additionChanged)
        
        self.lLinkCheckbox.stateChanged.connect(self.linkChanged)
        self.lPrismGroup.toggled.connect(self.prismGroupChanged)
        
        self.visualAcuityGroup.toggled.connect(self.visualAcuityGroupChanged)
        self.amblyopiaGroup.toggled.connect(self.amblyopiaGroupChanged)        
        
        self.rLinkCheckbox.setChecked(True)
        self.glassesGroupChanged()
        
        self.modified()

    def printAction(self):
        """ Send form data to the preview window and display it """
        if ((self.glasses != 0) and (self.rAddSpin.value() ==  0) and
                (self.lAddSpin.value() ==  0)):
            QtGui.QMessageBox.warning(self,
                u'Incohérence',
                (u"Les verres sélectionnés sont multifocaux mais aucune "+
                u"addition n'est précisée."),
                QtGui.QMessageBox.Ok)
        else:
            self.print_window = print_prescription.MainWindow(values=self.data)
            
            # Save data if the signal says that the page have been printed
            self.print_window.pagePrinted.connect(self.saveAction)
    
    def searchAction(self):
        """ Show the search window """
        self.search_window.show()
    
    def saveAction(self):
        """ Add a new line to the database with data from the current form """
        self.search_window.addNewLine(self.data)
    
    def clearAction(self):
        """ Reset the form """
        self.data = [item[2] for item in database.DATA_STRUCTURE]
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.nameEdit.setFocus()

    def getData(self):
        """ Returns all form data """
        return [self.nameEdit.text(),
                self.surnameEdit.text(),
                self.dateEdit.date(),
                self.CMUCheckBox.isChecked(),
                self.use,
                self.glasses,
                self.tint,
                self.antiglareCheckBox.isChecked(),
                self.rSphereSpin.value(),
                self.rCylSpin.value(),
                self.rAxisSpin.value(),
                self.rAddSpin.value(),
                self.rPrismValue.value(),
                self.rBase,
                self.lSphereSpin.value(),
                self.lCylSpin.value(),
                self.lAxisSpin.value(),
                self.lAddSpin.value(),
                self.lPrismValue.value(),
                self.lBase,
                self.visualAcuityGroup.isChecked(),
                self.rVASpin.value(),
                self.lVASpin.value(),
                self.amblyopia,
                self.amblyopiaRightEye.isChecked(),
                self.amblyopiaLeftEye.isChecked(),
                self.remarksEdit.toPlainText(),
                self.distanceVisionCheckbox.isChecked(),
                self.nearVisionCheckbox.isChecked()
                ]

    def loadValues(self, data):
        """ Change form values to given data """
        self.nameEdit.setText(data[0])
        self.surnameEdit.setText(data[1])
        self.dateEdit.setDate(QtCore.QDate.fromString(data[2],
                                                      "yyyy-MM-dd"))
        self.CMUCheckBox.setChecked(str2bool(data[3]))
        self.use = int(data[4])
        self.glasses = int(data[5])
        self.tint = int(data[6])
        self.antiglareCheckBox.setChecked(str2bool(data[7]))
        
        self.rSphereSpin.setValue(float(data[8]))
        self.rCylSpin.setValue(float(data[9]))
        if int(data[10]) % 5 != 0:
            self.rFineCheckbox.setChecked(True)
        else:
            self.rFineCheckbox.setChecked(False)
        self.rAxisSpin.setValue(int(data[10]))
        self.rAddSpin.setValue(float(data[11]))
        self.rPrismGroup.setChecked(float(data[12]) != 0)
        self.rPrismValue.setValue(float(data[12]))
        self.rBase = int(data[13])
        
        self.lSphereSpin.setValue(float(data[14]))
        self.lCylSpin.setValue(float(data[15]))
        if int(data[16]) % 5 != 0:
            self.lFineCheckbox.setChecked(True)
        else:
            self.lFineCheckbox.setChecked(False)
        self.lAxisSpin.setValue(int(data[16]))
        self.lAddSpin.setValue(float(data[17]))
        self.lPrismGroup.setChecked(float(data[18]) != 0)
        self.lPrismValue.setValue(float(data[18]))
        self.lBase = int(data[19])
        
        if float(data[11]) == float(data[17]):
            self.rLinkCheckbox.setChecked(True)
        
        self.visualAcuityGroup.setChecked(str2bool(data[20]))
        self.rVASpin.setValue(int(data[21]))
        self.lVASpin.setValue(int(data[22]))
        
        self.amblyopia = int(data[23])
        self.amblyopiaRightEye.setChecked(str2bool(data[24]))
        self.amblyopiaLeftEye.setChecked(str2bool(data[25]))
        
        self.remarksEdit.setText(data[26])
        
        self.distanceVisionCheckbox.setChecked(str2bool(data[27]))
        self.nearVisionCheckbox.setChecked(str2bool(data[28]))
        
        self.glassesGroupChanged()
        self.visualAcuityGroupChanged()
        self.amblyopiaGroupChanged()
        self.prismGroupChanged()
    
    data = property(getData, loadValues)

    def setUse(self, value=0):
        """ Change glasses usage radio selection according to given value
        0 (default): permanent usage
        1: intermittant usage
        2: both """
        if value == 1:
            self.itermUseRadio.setChecked(True)
        elif value == 2:
            self.bothUseRadio.setChecked(True)
        else:
            self.permUseRadio.setChecked(True)
    
    def getUse(self):
        """ Returns glasses usage radio selection
        0 (default): permanent usage
        1: intermittant usage
        2: both """
        if self.itermUseRadio.isChecked():
            return 1
        elif self.bothUseRadio.isChecked():
            return 2
        else:
            return 0

    use = property(getUse, setUse)

    def setGlasses(self, value=0):
        """ Change glasses type radio selection according to given value
        0 (default): normal
        1: progressive
        2: bifocal """
        if value == 1:
            self.progressiveGlassesRadio.setChecked(True)
        elif value == 2:
            self.bifocalGlassesRadio.setChecked(True)
        else:
            self.normalGlassesRadio.setChecked(True)
    
    def getGlasses(self):
        """ Returns glasses type radio selection
        0 (default): normal
        1: progressive
        2: bifocal """
        if self.progressiveGlassesRadio.isChecked():
            return 1
        elif self.bifocalGlassesRadio.isChecked():
            return 2
        else:
            return 0
        
    glasses = property(getGlasses, setGlasses)
            
    def setTint(self, value=0):
        """ Change tint radio selection according to given value
        0 (default): no tint
        1: T1
        2: T2
        3: T3
        4: T4
        5: Photochromic """
        self.tintGroupBox.setChecked(True)
        if value == 1:
            self.T1Radio.setChecked(True)
        elif value == 2:
            self.T2Radio.setChecked(True)
        elif value == 3:
            self.T3Radio.setChecked(True)
        elif value == 4:
            self.T4Radio.setChecked(True)
        elif value == 5:
            self.photochromicRadio.setChecked(True) 
        else:
            self.photochromicRadio.setChecked(True)
            self.tintGroupBox.setChecked(False)

    def getTint(self):
        """ Returns tint radio selection
        0 (default): no tint
        1: T1
        2: T2
        3: T3
        4: T4
        5: Photochromic """
        if not self.tintGroupBox.isChecked():
            return 0
        elif self.T1Radio.isChecked():
            return 1
        elif self.T2Radio.isChecked():
            return 2
        elif self.T3Radio.isChecked():
            return 3
        elif self.T4Radio.isChecked():
            return 4
        else:
            return 5

    tint = property(getTint, setTint)

    def setRBase(self, value=0):
        """ Change right base radio selection according to given value
        0 (default): Inferior
        1: Superior
        2: External
        3: Internal """
        if value == 1:
            self.rSuperiorRadio.setChecked(True)
        elif value == 2:
            self.rExternalRadio.setChecked(True)
        elif value == 3:
            self.rInternalRadio.setChecked(True)
        else:
            self.rInferiorRadio.setChecked(True)
        
    def getRBase(self):
        """ Retruns right base radio selection
        0 (default): Inferior
        1: Superior
        2: External
        3: Internal """
        if self.rInferiorRadio.isChecked():
            return 0
        elif self.rSuperiorRadio.isChecked():
            return 1
        elif self.rExternalRadio.isChecked():
            return 2
        else:
            return 3
    
    rBase = property(getRBase, setRBase)

    def setLBase(self, value=0):
        """ Change left base radio selection according to given value
        0 (default): Inferior
        1: Superior
        2: External
        3: Internal """
        if value == 1:
            self.lSuperiorRadio.setChecked(True)
        elif value == 2:
            self.lExternalRadio.setChecked(True)
        elif value == 3:
            self.lInternalRadio.setChecked(True)
        else:
            self.lInferiorRadio.setChecked(True)
            
    def getLBase(self):
        """ Retruns left base radio selection
        0 (default): Inferior
        1: Superior
        2: External
        3: Internal """
        if self.lInferiorRadio.isChecked():
            return 0
        elif self.lSuperiorRadio.isChecked():
            return 1
        elif self.lExternalRadio.isChecked():
            return 2
        else:
            return 3
            
    lBase = property(getLBase, setLBase)
            
    def setAmblyopia(self, value=0):
        """ Change amblyopia radio selection according to given value
        0 (default): no amblyopia set
        1: Functionnal
        2: organic """
        if value == 1:
            self.amblyopiaGroup.setChecked(True)
            self.functionnalRadio.setChecked(True)
        elif value == 2:
            self.amblyopiaGroup.setChecked(True)
            self.organicRadio.setChecked(True)
        else:
            self.amblyopiaGroup.setChecked(False)
            self.functionnalRadio.setChecked(True)
        self.amblyopiaGroupChanged()

    def getAmblyopia(self):
        """ Returns amblyopia radio selection
        0 (default): no amblyopia set
        1: Functionnal
        2: organic """
        if not self.amblyopiaGroup.isChecked():
            return 0
        elif self.functionnalRadio.isChecked():
            return 1
        elif self.organicRadio.isChecked():
            return 2
    
    amblyopia = property(getAmblyopia, setAmblyopia)

    def glassesGroupChanged(self):
        if self.normalGlassesRadio.isChecked():
            self.rAddSpin.setValue(0)
            self.lAddSpin.setValue(0)
            self.rLinkCheckbox.setChecked(True)
            self.distanceVisionCheckbox.setDisabled(False)
            self.nearVisionCheckbox.setDisabled(False)
        else:
            self.distanceVisionCheckbox.setChecked(True)
            self.nearVisionCheckbox.setChecked(True)
            self.distanceVisionCheckbox.setDisabled(True)
            self.nearVisionCheckbox.setDisabled(True)
        
        self.rAddSpin.setDisabled(self.normalGlassesRadio.isChecked())
        self.lAddSpin.setDisabled(self.normalGlassesRadio.isChecked())
        self.rLinkCheckbox.setDisabled(self.normalGlassesRadio.isChecked())
        self.lLinkCheckbox.setDisabled(self.normalGlassesRadio.isChecked())
    
    def additionChanged(self):
        """ Change the other addition value if link is checked """
        if self.rLinkCheckbox.isChecked():
            value = self.sender().value()
            self.rAddSpin.setValue(value)
            self.lAddSpin.setValue(value)
            self.modified()
    
    def linkChanged(self):
        """ Link the state of the two checkboxes """
        state = self.sender().isChecked()
        self.lLinkCheckbox.setChecked(state)
        self.rLinkCheckbox.setChecked(state)
    
    def prismGroupChanged(self):
        """ values if prism group is unchecked """
        if not self.rPrismGroup.isChecked():
            self.rPrismValue.setValue(0)
            self.rInferiorRadio.setChecked(True)
        if not self.lPrismGroup.isChecked():
            self.lPrismValue.setValue(0)
            self.lInferiorRadio.setChecked(True)
    
    def visualAcuityGroupChanged(self):
        """ Reset values if visual acuity group is unchecked """
        if not self.visualAcuityGroup.isChecked():
            self.rVASpin.setValue(0)
            self.lVASpin.setValue(0)
    
    def amblyopiaGroupChanged(self):
        """ Reset radio selection if amblyopia group is unchecked """
        if not self.amblyopiaGroup.isChecked():
            self.functionnalRadio.setChecked(True)
            self.amblyopiaRightEye.setChecked(False)
            self.amblyopiaLeftEye.setChecked(False)
            
    def r90Action(self):
        self.rAxisSpin.setValue(90)
    
    def l90Action(self):
        self.lAxisSpin.setValue(90)
        
    def rFineChanged(self):
        if self.rFineCheckbox.isChecked():
            self.rAxisSpin.setSingleStep(1)
            self.rAxisSpin.setMinimum(1)
        else:
            self.rAxisSpin.setMinimum(MIN_AXIS)
            self.rAxisSpin.setSingleStep(5)
            self.rAxisSpin.setValue(self.rAxisSpin.value()-self.rAxisSpin.value()%5)

    def lFineChanged(self):
        if self.lFineCheckbox.isChecked():
            self.lAxisSpin.setSingleStep(1)
            self.lAxisSpin.setMinimum(1)
        else:
            self.lAxisSpin.setMinimum(MIN_AXIS)
            self.lAxisSpin.setSingleStep(5)
            self.lAxisSpin.setValue(self.lAxisSpin.value()-self.lAxisSpin.value()%5)
        
    def modified(self):
        """ Action when a value is modified """
        if self.rCylSpin.value() == 0:
            self.rAxisSpin.setMinimum(0)
            self.rAxisSpin.setValue(0)
            self.rAxisSpin.setDisabled(True)
            self.rFineCheckbox.setDisabled(True)
            self.r90Button.setDisabled(True)
        else:
            if self.rFineCheckbox.isChecked():
                self.rAxisSpin.setMinimum(1)
            else:
                self.rAxisSpin.setMinimum(MIN_AXIS)
            self.rAxisSpin.setDisabled(False)
            self.rFineCheckbox.setDisabled(False)
            self.r90Button.setDisabled(False)
        if self.lCylSpin.value() == 0:
            self.lAxisSpin.setMinimum(0)
            self.lAxisSpin.setValue(0)
            self.lAxisSpin.setDisabled(True)
            self.lFineCheckbox.setDisabled(True)
            self.l90Button.setDisabled(True)
        else:
            if self.lFineCheckbox.isChecked():
                self.lAxisSpin.setMinimum(1)
            else:
                self.lAxisSpin.setMinimum(MIN_AXIS)
            self.lAxisSpin.setDisabled(False)
            self.lFineCheckbox.setDisabled(False)
            self.l90Button.setDisabled(False)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
