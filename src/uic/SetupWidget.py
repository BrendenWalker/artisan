# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SetupWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetupWidget(object):
    def setupUi(self, SetupWidget):
        SetupWidget.setObjectName("SetupWidget")
        SetupWidget.resize(446, 288)
        self.verticalLayout = QtWidgets.QVBoxLayout(SetupWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelOperator = QtWidgets.QLabel(SetupWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelOperator.setFont(font)
        self.labelOperator.setToolTip("")
        self.labelOperator.setText("Operator")
        self.labelOperator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelOperator.setObjectName("labelOperator")
        self.gridLayout.addWidget(self.labelOperator, 1, 0, 1, 1)
        self.labelDrumSpeed = QtWidgets.QLabel(SetupWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDrumSpeed.setFont(font)
        self.labelDrumSpeed.setToolTip("")
        self.labelDrumSpeed.setText("Drum Speed")
        self.labelDrumSpeed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDrumSpeed.setObjectName("labelDrumSpeed")
        self.gridLayout.addWidget(self.labelDrumSpeed, 3, 0, 1, 1)
        self.lineEditMachine = QtWidgets.QLineEdit(SetupWidget)
        self.lineEditMachine.setToolTip("")
        self.lineEditMachine.setText("")
        self.lineEditMachine.setObjectName("lineEditMachine")
        self.gridLayout.addWidget(self.lineEditMachine, 2, 1, 1, 1)
        self.labelMachine = QtWidgets.QLabel(SetupWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMachine.setFont(font)
        self.labelMachine.setToolTip("")
        self.labelMachine.setText("Machine")
        self.labelMachine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelMachine.setObjectName("labelMachine")
        self.gridLayout.addWidget(self.labelMachine, 2, 0, 1, 1)
        self.labelOrganization = QtWidgets.QLabel(SetupWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelOrganization.setFont(font)
        self.labelOrganization.setToolTip("")
        self.labelOrganization.setText("Organization")
        self.labelOrganization.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelOrganization.setObjectName("labelOrganization")
        self.gridLayout.addWidget(self.labelOrganization, 0, 0, 1, 1)
        self.doubleSpinBoxRoasterSize = QtWidgets.QDoubleSpinBox(SetupWidget)
        self.doubleSpinBoxRoasterSize.setToolTip("")
        self.doubleSpinBoxRoasterSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBoxRoasterSize.setSuffix("kg")
        self.doubleSpinBoxRoasterSize.setDecimals(1)
        self.doubleSpinBoxRoasterSize.setMaximum(9999.9)
        self.doubleSpinBoxRoasterSize.setObjectName("doubleSpinBoxRoasterSize")
        self.gridLayout.addWidget(self.doubleSpinBoxRoasterSize, 2, 2, 1, 1)
        self.lineEditOperator = QtWidgets.QLineEdit(SetupWidget)
        self.lineEditOperator.setToolTip("")
        self.lineEditOperator.setText("")
        self.lineEditOperator.setObjectName("lineEditOperator")
        self.gridLayout.addWidget(self.lineEditOperator, 1, 1, 1, 2)
        self.lineEditOrganization = QtWidgets.QLineEdit(SetupWidget)
        self.lineEditOrganization.setToolTip("")
        self.lineEditOrganization.setText("")
        self.lineEditOrganization.setObjectName("lineEditOrganization")
        self.gridLayout.addWidget(self.lineEditOrganization, 0, 1, 1, 2)
        self.lineEditDrumSpeed = QtWidgets.QLineEdit(SetupWidget)
        self.lineEditDrumSpeed.setToolTip("")
        self.lineEditDrumSpeed.setText("")
        self.lineEditDrumSpeed.setObjectName("lineEditDrumSpeed")
        self.gridLayout.addWidget(self.lineEditDrumSpeed, 3, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SetDefaults = QtWidgets.QPushButton(SetupWidget)
        self.SetDefaults.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SetDefaults.setToolTip("")
        self.SetDefaults.setText("Set as Defaults")
        self.SetDefaults.setObjectName("SetDefaults")
        self.horizontalLayout.addWidget(self.SetDefaults)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Defaults = QtWidgets.QPushButton(SetupWidget)
        self.Defaults.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Defaults.setToolTip("")
        self.Defaults.setText("Restore Defaults")
        self.Defaults.setObjectName("Defaults")
        self.horizontalLayout.addWidget(self.Defaults)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(SetupWidget)
        QtCore.QMetaObject.connectSlotsByName(SetupWidget)
        SetupWidget.setTabOrder(self.lineEditOrganization, self.lineEditOperator)
        SetupWidget.setTabOrder(self.lineEditOperator, self.lineEditMachine)
        SetupWidget.setTabOrder(self.lineEditMachine, self.lineEditDrumSpeed)
        SetupWidget.setTabOrder(self.lineEditDrumSpeed, self.doubleSpinBoxRoasterSize)
        SetupWidget.setTabOrder(self.doubleSpinBoxRoasterSize, self.SetDefaults)
        SetupWidget.setTabOrder(self.SetDefaults, self.Defaults)

    def retranslateUi(self, SetupWidget):
        _translate = QtCore.QCoreApplication.translate
        SetupWidget.setWindowTitle(_translate("SetupWidget", "Form"))
