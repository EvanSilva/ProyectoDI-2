# Form implementation generated from reading ui file 'venPrincipal.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAceptar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(350, 350, 80, 25))
        self.btnAceptar.setMinimumSize(QtCore.QSize(80, 25))
        self.btnAceptar.setMaximumSize(QtCore.QSize(80, 25))
        self.btnAceptar.setObjectName("btnAceptar")
        self.lblTitulo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(250, 70, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=venPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        venPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(parent=venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(venPrincipal)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "Inmoteis"))
        self.btnAceptar.setText(_translate("venPrincipal", "Aceptar"))
        self.lblTitulo.setText(_translate("venPrincipal", "Empresa inmobiliaria de Teis"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
