# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chrysops.ui'
#
# Created: Fri Dec 26 19:36:46 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(914, 796)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_9.addWidget(self.label_17, 1, 0, 1, 1)
        self.amblyopiaGroup = QtGui.QGroupBox(self.groupBox_4)
        self.amblyopiaGroup.setCheckable(True)
        self.amblyopiaGroup.setChecked(False)
        self.amblyopiaGroup.setObjectName(_fromUtf8("amblyopiaGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.amblyopiaGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.amblyopiaRightEye = QtGui.QCheckBox(self.amblyopiaGroup)
        self.amblyopiaRightEye.setObjectName(_fromUtf8("amblyopiaRightEye"))
        self.gridLayout_2.addWidget(self.amblyopiaRightEye, 1, 1, 1, 1)
        self.amblyopiaLeftEye = QtGui.QCheckBox(self.amblyopiaGroup)
        self.amblyopiaLeftEye.setObjectName(_fromUtf8("amblyopiaLeftEye"))
        self.gridLayout_2.addWidget(self.amblyopiaLeftEye, 2, 1, 1, 1)
        self.organicRadio = QtGui.QRadioButton(self.amblyopiaGroup)
        self.organicRadio.setObjectName(_fromUtf8("organicRadio"))
        self.gridLayout_2.addWidget(self.organicRadio, 2, 0, 1, 1)
        self.functionnalRadio = QtGui.QRadioButton(self.amblyopiaGroup)
        self.functionnalRadio.setChecked(True)
        self.functionnalRadio.setObjectName(_fromUtf8("functionnalRadio"))
        self.gridLayout_2.addWidget(self.functionnalRadio, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.amblyopiaGroup, 0, 1, 1, 1)
        self.visualAcuityGroup = QtGui.QGroupBox(self.groupBox_4)
        self.visualAcuityGroup.setCheckable(True)
        self.visualAcuityGroup.setChecked(False)
        self.visualAcuityGroup.setObjectName(_fromUtf8("visualAcuityGroup"))
        self.gridLayout_6 = QtGui.QGridLayout(self.visualAcuityGroup)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_16 = QtGui.QLabel(self.visualAcuityGroup)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_6.addWidget(self.label_16, 2, 2, 1, 1)
        self.lVASpin = QtGui.QSpinBox(self.visualAcuityGroup)
        self.lVASpin.setMaximum(20)
        self.lVASpin.setObjectName(_fromUtf8("lVASpin"))
        self.gridLayout_6.addWidget(self.lVASpin, 2, 1, 1, 1)
        self.rVASpin = QtGui.QSpinBox(self.visualAcuityGroup)
        self.rVASpin.setMaximum(20)
        self.rVASpin.setObjectName(_fromUtf8("rVASpin"))
        self.gridLayout_6.addWidget(self.rVASpin, 0, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.visualAcuityGroup)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_6.addWidget(self.label_15, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.visualAcuityGroup)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.visualAcuityGroup)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_6.addWidget(self.label_18, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.visualAcuityGroup, 0, 0, 1, 1)
        self.remarksEdit = QtGui.QTextEdit(self.groupBox_4)
        self.remarksEdit.setTabChangesFocus(True)
        self.remarksEdit.setObjectName(_fromUtf8("remarksEdit"))
        self.gridLayout_9.addWidget(self.remarksEdit, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_4, 8, 0, 1, 4)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.surnameEdit = QtGui.QLineEdit(self.centralwidget)
        self.surnameEdit.setObjectName(_fromUtf8("surnameEdit"))
        self.gridLayout.addWidget(self.surnameEdit, 1, 1, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 1, 3, 1, 1)
        self.nameEdit = QtGui.QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.normalGlassesRadio = QtGui.QRadioButton(self.groupBox_2)
        self.normalGlassesRadio.setChecked(True)
        self.normalGlassesRadio.setObjectName(_fromUtf8("normalGlassesRadio"))
        self.verticalLayout_2.addWidget(self.normalGlassesRadio)
        self.progressiveGlassesRadio = QtGui.QRadioButton(self.groupBox_2)
        self.progressiveGlassesRadio.setObjectName(_fromUtf8("progressiveGlassesRadio"))
        self.verticalLayout_2.addWidget(self.progressiveGlassesRadio)
        self.bifocalGlassesRadio = QtGui.QRadioButton(self.groupBox_2)
        self.bifocalGlassesRadio.setObjectName(_fromUtf8("bifocalGlassesRadio"))
        self.verticalLayout_2.addWidget(self.bifocalGlassesRadio)
        self.gridLayout.addWidget(self.groupBox_2, 4, 1, 1, 1)
        self.tintGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.tintGroupBox.setCheckable(True)
        self.tintGroupBox.setChecked(False)
        self.tintGroupBox.setObjectName(_fromUtf8("tintGroupBox"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tintGroupBox)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.T1Radio = QtGui.QRadioButton(self.tintGroupBox)
        self.T1Radio.setObjectName(_fromUtf8("T1Radio"))
        self.gridLayout_10.addWidget(self.T1Radio, 1, 0, 1, 1)
        self.photochromicRadio = QtGui.QRadioButton(self.tintGroupBox)
        self.photochromicRadio.setChecked(True)
        self.photochromicRadio.setObjectName(_fromUtf8("photochromicRadio"))
        self.gridLayout_10.addWidget(self.photochromicRadio, 0, 0, 1, 1)
        self.T3Radio = QtGui.QRadioButton(self.tintGroupBox)
        self.T3Radio.setObjectName(_fromUtf8("T3Radio"))
        self.gridLayout_10.addWidget(self.T3Radio, 4, 0, 1, 1)
        self.T2Radio = QtGui.QRadioButton(self.tintGroupBox)
        self.T2Radio.setObjectName(_fromUtf8("T2Radio"))
        self.gridLayout_10.addWidget(self.T2Radio, 1, 1, 1, 1)
        self.T4Radio = QtGui.QRadioButton(self.tintGroupBox)
        self.T4Radio.setObjectName(_fromUtf8("T4Radio"))
        self.gridLayout_10.addWidget(self.T4Radio, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.tintGroupBox, 4, 2, 1, 1)
        self.rightEyeGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.rightEyeGroupBox.setMinimumSize(QtCore.QSize(380, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rightEyeGroupBox.setFont(font)
        self.rightEyeGroupBox.setObjectName(_fromUtf8("rightEyeGroupBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.rightEyeGroupBox)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.rightEyeLayout = QtGui.QGridLayout()
        self.rightEyeLayout.setObjectName(_fromUtf8("rightEyeLayout"))
        self.rCylSpin = negativeZeroSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rCylSpin.setFont(font)
        self.rCylSpin.setObjectName(_fromUtf8("rCylSpin"))
        self.rightEyeLayout.addWidget(self.rCylSpin, 1, 1, 1, 1)
        self.rAddSpin = dotSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rAddSpin.setFont(font)
        self.rAddSpin.setObjectName(_fromUtf8("rAddSpin"))
        self.rightEyeLayout.addWidget(self.rAddSpin, 1, 4, 1, 1)
        self.rLinkCheckbox = QtGui.QCheckBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rLinkCheckbox.setFont(font)
        self.rLinkCheckbox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.rLinkCheckbox.setObjectName(_fromUtf8("rLinkCheckbox"))
        self.rightEyeLayout.addWidget(self.rLinkCheckbox, 2, 4, 1, 1)
        self.label_8 = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.rightEyeLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.rightEyeLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.rSphereSpin = dotSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rSphereSpin.setFont(font)
        self.rSphereSpin.setObjectName(_fromUtf8("rSphereSpin"))
        self.rightEyeLayout.addWidget(self.rSphereSpin, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.rightEyeLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.rLabelCylPos = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.rLabelCylPos.setFont(font)
        self.rLabelCylPos.setObjectName(_fromUtf8("rLabelCylPos"))
        self.rightEyeLayout.addWidget(self.rLabelCylPos, 2, 1, 1, 1)
        self.r90Button = QtGui.QPushButton(self.rightEyeGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r90Button.sizePolicy().hasHeightForWidth())
        self.r90Button.setSizePolicy(sizePolicy)
        self.r90Button.setObjectName(_fromUtf8("r90Button"))
        self.rightEyeLayout.addWidget(self.r90Button, 2, 2, 1, 1)
        self.rFineCheckbox = QtGui.QCheckBox(self.rightEyeGroupBox)
        self.rFineCheckbox.setObjectName(_fromUtf8("rFineCheckbox"))
        self.rightEyeLayout.addWidget(self.rFineCheckbox, 2, 3, 1, 1)
        self.rAxisSpin = angleSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rAxisSpin.setFont(font)
        self.rAxisSpin.setWrapping(True)
        self.rAxisSpin.setMinimum(5)
        self.rAxisSpin.setMaximum(180)
        self.rAxisSpin.setSingleStep(5)
        self.rAxisSpin.setProperty("value", 180)
        self.rAxisSpin.setObjectName(_fromUtf8("rAxisSpin"))
        self.rightEyeLayout.addWidget(self.rAxisSpin, 1, 2, 1, 2)
        self.label_7 = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.rightEyeLayout.addWidget(self.label_7, 0, 2, 1, 2)
        self.gridLayout_7.addLayout(self.rightEyeLayout, 0, 0, 1, 1)
        self.rPrismGroup = QtGui.QGroupBox(self.rightEyeGroupBox)
        self.rPrismGroup.setCheckable(True)
        self.rPrismGroup.setChecked(False)
        self.rPrismGroup.setObjectName(_fromUtf8("rPrismGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.rPrismGroup)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.rInternalRadio = QtGui.QRadioButton(self.rPrismGroup)
        self.rInternalRadio.setObjectName(_fromUtf8("rInternalRadio"))
        self.gridLayout_4.addWidget(self.rInternalRadio, 3, 1, 1, 1)
        self.rSuperiorRadio = QtGui.QRadioButton(self.rPrismGroup)
        self.rSuperiorRadio.setObjectName(_fromUtf8("rSuperiorRadio"))
        self.gridLayout_4.addWidget(self.rSuperiorRadio, 3, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.rPrismGroup)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)
        self.rExternalRadio = QtGui.QRadioButton(self.rPrismGroup)
        self.rExternalRadio.setObjectName(_fromUtf8("rExternalRadio"))
        self.gridLayout_4.addWidget(self.rExternalRadio, 2, 1, 1, 1)
        self.rInferiorRadio = QtGui.QRadioButton(self.rPrismGroup)
        self.rInferiorRadio.setChecked(True)
        self.rInferiorRadio.setObjectName(_fromUtf8("rInferiorRadio"))
        self.gridLayout_4.addWidget(self.rInferiorRadio, 2, 0, 1, 1)
        self.rPrismValue = dotSpinBox(self.rPrismGroup)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rPrismValue.setFont(font)
        self.rPrismValue.setSingleStep(0.5)
        self.rPrismValue.setObjectName(_fromUtf8("rPrismValue"))
        self.gridLayout_4.addWidget(self.rPrismValue, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.rPrismGroup, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.rightEyeGroupBox, 7, 0, 1, 2)
        self.leftEyeGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.leftEyeGroupBox.setMinimumSize(QtCore.QSize(380, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leftEyeGroupBox.setFont(font)
        self.leftEyeGroupBox.setObjectName(_fromUtf8("leftEyeGroupBox"))
        self.gridLayout_8 = QtGui.QGridLayout(self.leftEyeGroupBox)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.leftEyeLayout = QtGui.QGridLayout()
        self.leftEyeLayout.setObjectName(_fromUtf8("leftEyeLayout"))
        self.label_10 = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.leftEyeLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.leftEyeLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.lLinkCheckbox = QtGui.QCheckBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lLinkCheckbox.setFont(font)
        self.lLinkCheckbox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lLinkCheckbox.setObjectName(_fromUtf8("lLinkCheckbox"))
        self.leftEyeLayout.addWidget(self.lLinkCheckbox, 2, 4, 1, 1)
        self.label_12 = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.leftEyeLayout.addWidget(self.label_12, 0, 4, 1, 1)
        self.lSphereSpin = dotSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lSphereSpin.setFont(font)
        self.lSphereSpin.setObjectName(_fromUtf8("lSphereSpin"))
        self.leftEyeLayout.addWidget(self.lSphereSpin, 1, 0, 1, 1)
        self.lCylSpin = negativeZeroSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lCylSpin.setFont(font)
        self.lCylSpin.setObjectName(_fromUtf8("lCylSpin"))
        self.leftEyeLayout.addWidget(self.lCylSpin, 1, 1, 1, 1)
        self.lAddSpin = dotSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lAddSpin.setFont(font)
        self.lAddSpin.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.lAddSpin.setObjectName(_fromUtf8("lAddSpin"))
        self.leftEyeLayout.addWidget(self.lAddSpin, 1, 4, 1, 1)
        self.lLabelCylPos = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lLabelCylPos.setFont(font)
        self.lLabelCylPos.setObjectName(_fromUtf8("lLabelCylPos"))
        self.leftEyeLayout.addWidget(self.lLabelCylPos, 2, 1, 1, 1)
        self.l90Button = QtGui.QPushButton(self.leftEyeGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l90Button.sizePolicy().hasHeightForWidth())
        self.l90Button.setSizePolicy(sizePolicy)
        self.l90Button.setObjectName(_fromUtf8("l90Button"))
        self.leftEyeLayout.addWidget(self.l90Button, 2, 2, 1, 1)
        self.lFineCheckbox = QtGui.QCheckBox(self.leftEyeGroupBox)
        self.lFineCheckbox.setObjectName(_fromUtf8("lFineCheckbox"))
        self.leftEyeLayout.addWidget(self.lFineCheckbox, 2, 3, 1, 1)
        self.lAxisSpin = angleSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lAxisSpin.setFont(font)
        self.lAxisSpin.setWrapping(True)
        self.lAxisSpin.setMinimum(5)
        self.lAxisSpin.setMaximum(180)
        self.lAxisSpin.setSingleStep(5)
        self.lAxisSpin.setProperty("value", 180)
        self.lAxisSpin.setObjectName(_fromUtf8("lAxisSpin"))
        self.leftEyeLayout.addWidget(self.lAxisSpin, 1, 2, 1, 2)
        self.label_9 = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.leftEyeLayout.addWidget(self.label_9, 0, 2, 1, 2)
        self.gridLayout_8.addLayout(self.leftEyeLayout, 0, 0, 1, 1)
        self.lPrismGroup = QtGui.QGroupBox(self.leftEyeGroupBox)
        self.lPrismGroup.setCheckable(True)
        self.lPrismGroup.setChecked(False)
        self.lPrismGroup.setObjectName(_fromUtf8("lPrismGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.lPrismGroup)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_14 = QtGui.QLabel(self.lPrismGroup)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)
        self.lInternalRadio = QtGui.QRadioButton(self.lPrismGroup)
        self.lInternalRadio.setObjectName(_fromUtf8("lInternalRadio"))
        self.gridLayout_5.addWidget(self.lInternalRadio, 3, 1, 1, 1)
        self.lSuperiorRadio = QtGui.QRadioButton(self.lPrismGroup)
        self.lSuperiorRadio.setObjectName(_fromUtf8("lSuperiorRadio"))
        self.gridLayout_5.addWidget(self.lSuperiorRadio, 3, 0, 1, 1)
        self.lInferiorRadio = QtGui.QRadioButton(self.lPrismGroup)
        self.lInferiorRadio.setChecked(True)
        self.lInferiorRadio.setObjectName(_fromUtf8("lInferiorRadio"))
        self.gridLayout_5.addWidget(self.lInferiorRadio, 2, 0, 1, 1)
        self.lExternalRadio = QtGui.QRadioButton(self.lPrismGroup)
        self.lExternalRadio.setObjectName(_fromUtf8("lExternalRadio"))
        self.gridLayout_5.addWidget(self.lExternalRadio, 2, 1, 1, 1)
        self.lPrismValue = dotSpinBox(self.lPrismGroup)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lPrismValue.setFont(font)
        self.lPrismValue.setSingleStep(0.5)
        self.lPrismValue.setObjectName(_fromUtf8("lPrismValue"))
        self.gridLayout_5.addWidget(self.lPrismValue, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.lPrismGroup, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.leftEyeGroupBox, 7, 2, 1, 2)
        self.CMUCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.CMUCheckBox.setObjectName(_fromUtf8("CMUCheckBox"))
        self.gridLayout.addWidget(self.CMUCheckBox, 0, 3, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.permUseRadio = QtGui.QRadioButton(self.groupBox)
        self.permUseRadio.setChecked(True)
        self.permUseRadio.setObjectName(_fromUtf8("permUseRadio"))
        self.verticalLayout.addWidget(self.permUseRadio)
        self.itermUseRadio = QtGui.QRadioButton(self.groupBox)
        self.itermUseRadio.setObjectName(_fromUtf8("itermUseRadio"))
        self.verticalLayout.addWidget(self.itermUseRadio)
        self.bothUseRadio = QtGui.QRadioButton(self.groupBox)
        self.bothUseRadio.setObjectName(_fromUtf8("bothUseRadio"))
        self.verticalLayout.addWidget(self.bothUseRadio)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.antiglareCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.antiglareCheckBox.setObjectName(_fromUtf8("antiglareCheckBox"))
        self.verticalLayout_3.addWidget(self.antiglareCheckBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.distanceVisionCheckbox = QtGui.QCheckBox(self.centralwidget)
        self.distanceVisionCheckbox.setChecked(True)
        self.distanceVisionCheckbox.setObjectName(_fromUtf8("distanceVisionCheckbox"))
        self.verticalLayout_3.addWidget(self.distanceVisionCheckbox)
        self.nearVisionCheckbox = QtGui.QCheckBox(self.centralwidget)
        self.nearVisionCheckbox.setChecked(True)
        self.nearVisionCheckbox.setObjectName(_fromUtf8("nearVisionCheckbox"))
        self.verticalLayout_3.addWidget(self.nearVisionCheckbox)
        self.gridLayout.addLayout(self.verticalLayout_3, 4, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.printButton = QtGui.QPushButton(self.centralwidget)
        self.printButton.setObjectName(_fromUtf8("printButton"))
        self.horizontalLayout.addWidget(self.printButton)
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout.addWidget(self.searchButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.nameEdit, self.surnameEdit)
        MainWindow.setTabOrder(self.surnameEdit, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.permUseRadio)
        MainWindow.setTabOrder(self.permUseRadio, self.itermUseRadio)
        MainWindow.setTabOrder(self.itermUseRadio, self.bothUseRadio)
        MainWindow.setTabOrder(self.bothUseRadio, self.normalGlassesRadio)
        MainWindow.setTabOrder(self.normalGlassesRadio, self.progressiveGlassesRadio)
        MainWindow.setTabOrder(self.progressiveGlassesRadio, self.bifocalGlassesRadio)
        MainWindow.setTabOrder(self.bifocalGlassesRadio, self.tintGroupBox)
        MainWindow.setTabOrder(self.tintGroupBox, self.photochromicRadio)
        MainWindow.setTabOrder(self.photochromicRadio, self.T1Radio)
        MainWindow.setTabOrder(self.T1Radio, self.T2Radio)
        MainWindow.setTabOrder(self.T2Radio, self.T3Radio)
        MainWindow.setTabOrder(self.T3Radio, self.T4Radio)
        MainWindow.setTabOrder(self.T4Radio, self.antiglareCheckBox)
        MainWindow.setTabOrder(self.antiglareCheckBox, self.distanceVisionCheckbox)
        MainWindow.setTabOrder(self.distanceVisionCheckbox, self.nearVisionCheckbox)
        MainWindow.setTabOrder(self.nearVisionCheckbox, self.rSphereSpin)
        MainWindow.setTabOrder(self.rSphereSpin, self.rCylSpin)
        MainWindow.setTabOrder(self.rCylSpin, self.rAxisSpin)
        MainWindow.setTabOrder(self.rAxisSpin, self.rAddSpin)
        MainWindow.setTabOrder(self.rAddSpin, self.lSphereSpin)
        MainWindow.setTabOrder(self.lSphereSpin, self.lCylSpin)
        MainWindow.setTabOrder(self.lCylSpin, self.lAxisSpin)
        MainWindow.setTabOrder(self.lAxisSpin, self.lAddSpin)
        MainWindow.setTabOrder(self.lAddSpin, self.rPrismGroup)
        MainWindow.setTabOrder(self.rPrismGroup, self.rPrismValue)
        MainWindow.setTabOrder(self.rPrismValue, self.rInferiorRadio)
        MainWindow.setTabOrder(self.rInferiorRadio, self.rSuperiorRadio)
        MainWindow.setTabOrder(self.rSuperiorRadio, self.rExternalRadio)
        MainWindow.setTabOrder(self.rExternalRadio, self.rInternalRadio)
        MainWindow.setTabOrder(self.rInternalRadio, self.lPrismGroup)
        MainWindow.setTabOrder(self.lPrismGroup, self.lPrismValue)
        MainWindow.setTabOrder(self.lPrismValue, self.lInferiorRadio)
        MainWindow.setTabOrder(self.lInferiorRadio, self.lExternalRadio)
        MainWindow.setTabOrder(self.lExternalRadio, self.lSuperiorRadio)
        MainWindow.setTabOrder(self.lSuperiorRadio, self.lInternalRadio)
        MainWindow.setTabOrder(self.lInternalRadio, self.visualAcuityGroup)
        MainWindow.setTabOrder(self.visualAcuityGroup, self.rVASpin)
        MainWindow.setTabOrder(self.rVASpin, self.lVASpin)
        MainWindow.setTabOrder(self.lVASpin, self.amblyopiaGroup)
        MainWindow.setTabOrder(self.amblyopiaGroup, self.functionnalRadio)
        MainWindow.setTabOrder(self.functionnalRadio, self.organicRadio)
        MainWindow.setTabOrder(self.organicRadio, self.amblyopiaRightEye)
        MainWindow.setTabOrder(self.amblyopiaRightEye, self.amblyopiaLeftEye)
        MainWindow.setTabOrder(self.amblyopiaLeftEye, self.remarksEdit)
        MainWindow.setTabOrder(self.remarksEdit, self.printButton)
        MainWindow.setTabOrder(self.printButton, self.clearButton)
        MainWindow.setTabOrder(self.clearButton, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.CMUCheckBox)
        MainWindow.setTabOrder(self.CMUCheckBox, self.r90Button)
        MainWindow.setTabOrder(self.r90Button, self.rFineCheckbox)
        MainWindow.setTabOrder(self.rFineCheckbox, self.l90Button)
        MainWindow.setTabOrder(self.l90Button, self.lFineCheckbox)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chrysops", None))
        self.label_2.setText(_translate("MainWindow", "Nom :", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Remarques", None))
        self.label_17.setText(_translate("MainWindow", "Champ libre :", None))
        self.amblyopiaGroup.setTitle(_translate("MainWindow", "Amblyopie", None))
        self.amblyopiaRightEye.setText(_translate("MainWindow", "OD (Œil Droit)", None))
        self.amblyopiaLeftEye.setText(_translate("MainWindow", "OG (Œil Gauche)", None))
        self.organicRadio.setText(_translate("MainWindow", "Organique", None))
        self.functionnalRadio.setText(_translate("MainWindow", "Fonctionnelle", None))
        self.visualAcuityGroup.setTitle(_translate("MainWindow", "Acuité Visuelle Corrigée en vision de loin", None))
        self.label_16.setText(_translate("MainWindow", "/10", None))
        self.label_15.setText(_translate("MainWindow", "/10", None))
        self.label_4.setText(_translate("MainWindow", "Œil Droit", None))
        self.label_18.setText(_translate("MainWindow", "Œil Gauche", None))
        self.label_3.setText(_translate("MainWindow", "Date :", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Verres", None))
        self.normalGlassesRadio.setText(_translate("MainWindow", "Unifocaux", None))
        self.progressiveGlassesRadio.setText(_translate("MainWindow", "Foyers progressifs", None))
        self.bifocalGlassesRadio.setText(_translate("MainWindow", "Bifocaux", None))
        self.tintGroupBox.setTitle(_translate("MainWindow", "Teinté", None))
        self.T1Radio.setText(_translate("MainWindow", "T1", None))
        self.photochromicRadio.setText(_translate("MainWindow", "Photochromiques", None))
        self.T3Radio.setText(_translate("MainWindow", "T3", None))
        self.T2Radio.setText(_translate("MainWindow", "T2", None))
        self.T4Radio.setText(_translate("MainWindow", "T4", None))
        self.rightEyeGroupBox.setTitle(_translate("MainWindow", "OD (Œil Droit)", None))
        self.rLinkCheckbox.setText(_translate("MainWindow", "Lié", None))
        self.label_8.setText(_translate("MainWindow", "Cylindre", None))
        self.label_5.setText(_translate("MainWindow", "Sphere", None))
        self.label_6.setText(_translate("MainWindow", "Addition", None))
        self.rLabelCylPos.setToolTip(_translate("MainWindow", "Le cylindre indiqué est positif, une conversion sera effectuée lors de la Sauvegarde", None))
        self.rLabelCylPos.setText(_translate("MainWindow", "Cylindre positif", None))
        self.r90Button.setText(_translate("MainWindow", "90°", None))
        self.rFineCheckbox.setText(_translate("MainWindow", "fin", None))
        self.label_7.setText(_translate("MainWindow", "Axe", None))
        self.rPrismGroup.setTitle(_translate("MainWindow", "Prisme", None))
        self.rInternalRadio.setText(_translate("MainWindow", "Interne", None))
        self.rSuperiorRadio.setText(_translate("MainWindow", "Supérieure", None))
        self.label_13.setText(_translate("MainWindow", "Base :", None))
        self.rExternalRadio.setText(_translate("MainWindow", "Externe", None))
        self.rInferiorRadio.setText(_translate("MainWindow", "Inférieure", None))
        self.leftEyeGroupBox.setTitle(_translate("MainWindow", "OG (Œil Gauche)", None))
        self.label_10.setText(_translate("MainWindow", "Cylindre", None))
        self.label_11.setText(_translate("MainWindow", "Sphere", None))
        self.lLinkCheckbox.setText(_translate("MainWindow", "Lié", None))
        self.label_12.setText(_translate("MainWindow", "Addition", None))
        self.lLabelCylPos.setToolTip(_translate("MainWindow", "Le cylindre indiqué est positif, une conversion sera effectuée lors de la Sauvegarde", None))
        self.lLabelCylPos.setText(_translate("MainWindow", "Cylindre positif", None))
        self.l90Button.setText(_translate("MainWindow", "90°", None))
        self.lFineCheckbox.setText(_translate("MainWindow", "fin", None))
        self.label_9.setText(_translate("MainWindow", "Axe", None))
        self.lPrismGroup.setTitle(_translate("MainWindow", "Prisme", None))
        self.label_14.setText(_translate("MainWindow", "Base :", None))
        self.lInternalRadio.setText(_translate("MainWindow", "Interne", None))
        self.lSuperiorRadio.setText(_translate("MainWindow", "Supérieure", None))
        self.lInferiorRadio.setText(_translate("MainWindow", "Inférieure", None))
        self.lExternalRadio.setText(_translate("MainWindow", "Externe", None))
        self.CMUCheckBox.setText(_translate("MainWindow", "CMU", None))
        self.groupBox.setTitle(_translate("MainWindow", "Port", None))
        self.permUseRadio.setText(_translate("MainWindow", "Permanent", None))
        self.itermUseRadio.setText(_translate("MainWindow", "Intermittent", None))
        self.bothUseRadio.setText(_translate("MainWindow", "Intermittent ou Permanent", None))
        self.label.setText(_translate("MainWindow", "Prénom :", None))
        self.antiglareCheckBox.setText(_translate("MainWindow", "Antireflets", None))
        self.distanceVisionCheckbox.setText(_translate("MainWindow", "Vision de loin", None))
        self.nearVisionCheckbox.setText(_translate("MainWindow", "Vision de près", None))
        self.printButton.setText(_translate("MainWindow", "Aperçu avant Impression", None))
        self.clearButton.setText(_translate("MainWindow", "Remise à zéro", None))
        self.searchButton.setText(_translate("MainWindow", "Rechercher", None))

from anglespinbox import angleSpinBox
from negativezerospinbox import negativeZeroSpinBox
from dotspinbox import dotSpinBox
