# Form implementation generated from reading ui file '.\\templates\\dlgInformeProp.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgInformeProp(object):
    def setupUi(self, dlgInformeProp):
        dlgInformeProp.setObjectName("dlgInformeProp")
        dlgInformeProp.resize(400, 300)
        self.btnInformeProp = QtWidgets.QPushButton(parent=dlgInformeProp)
        self.btnInformeProp.setGeometry(QtCore.QRect(160, 240, 80, 25))
        self.btnInformeProp.setObjectName("btnInformeProp")
        self.label_2 = QtWidgets.QLabel(parent=dlgInformeProp)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 151, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\\\templates\\../img/inmoteis.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(parent=dlgInformeProp)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 180, 331, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.cmbInformProp = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.cmbInformProp.setEditable(True)
        self.cmbInformProp.setObjectName("cmbInformProp")
        self.horizontalLayout.addWidget(self.cmbInformProp)

        self.retranslateUi(dlgInformeProp)
        QtCore.QMetaObject.connectSlotsByName(dlgInformeProp)

    def retranslateUi(self, dlgInformeProp):
        _translate = QtCore.QCoreApplication.translate
        dlgInformeProp.setWindowTitle(_translate("dlgInformeProp", "Informe Propiedades"))
        self.btnInformeProp.setText(_translate("dlgInformeProp", "Crear Informe"))
        self.label.setText(_translate("dlgInformeProp", "Selecciona el municipio:"))
