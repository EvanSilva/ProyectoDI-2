# Form implementation generated from reading ui file '.\\templates\\venPrincipal.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(1097, 812)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/a20evansg/.designer/img/inmoteis.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        venPrincipal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.panPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.panPrincipal.setEnabled(True)
        self.panPrincipal.setMinimumSize(QtCore.QSize(1024, 753))
        self.panPrincipal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.panPrincipal.setObjectName("panPrincipal")
        self.pesClientes = QtWidgets.QWidget()
        self.pesClientes.setObjectName("pesClientes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pesClientes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 5, 1, 1)
        self.txtDircli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDircli.setMinimumSize(QtCore.QSize(400, 0))
        self.txtDircli.setObjectName("txtDircli")
        self.gridLayout.addWidget(self.txtDircli, 3, 2, 1, 3)
        self.lblDircli = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDircli.sizePolicy().hasHeightForWidth())
        self.lblDircli.setSizePolicy(sizePolicy)
        self.lblDircli.setObjectName("lblDircli")
        self.gridLayout.addWidget(self.lblDircli, 3, 1, 1, 1)
        self.lblMovilcli = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMovilcli.sizePolicy().hasHeightForWidth())
        self.lblMovilcli.setSizePolicy(sizePolicy)
        self.lblMovilcli.setObjectName("lblMovilcli")
        self.gridLayout.addWidget(self.lblMovilcli, 2, 4, 1, 1)
        self.txtMovilcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtMovilcli.sizePolicy().hasHeightForWidth())
        self.txtMovilcli.setSizePolicy(sizePolicy)
        self.txtMovilcli.setMinimumSize(QtCore.QSize(120, 0))
        self.txtMovilcli.setObjectName("txtMovilcli")
        self.gridLayout.addWidget(self.txtMovilcli, 2, 5, 1, 3)
        self.cmbProvcli = QtWidgets.QComboBox(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProvcli.sizePolicy().hasHeightForWidth())
        self.cmbProvcli.setSizePolicy(sizePolicy)
        self.cmbProvcli.setMinimumSize(QtCore.QSize(120, 0))
        self.cmbProvcli.setObjectName("cmbProvcli")
        self.gridLayout.addWidget(self.cmbProvcli, 3, 7, 1, 1)
        self.lblProvcli = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblProvcli.sizePolicy().hasHeightForWidth())
        self.lblProvcli.setSizePolicy(sizePolicy)
        self.lblProvcli.setObjectName("lblProvcli")
        self.gridLayout.addWidget(self.lblProvcli, 3, 6, 1, 1)
        self.lblMunicli_2 = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMunicli_2.sizePolicy().hasHeightForWidth())
        self.lblMunicli_2.setSizePolicy(sizePolicy)
        self.lblMunicli_2.setObjectName("lblMunicli_2")
        self.gridLayout.addWidget(self.lblMunicli_2, 3, 8, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 3, 1, 1)
        self.lblEmailcli = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblEmailcli.sizePolicy().hasHeightForWidth())
        self.lblEmailcli.setSizePolicy(sizePolicy)
        self.lblEmailcli.setObjectName("lblEmailcli")
        self.gridLayout.addWidget(self.lblEmailcli, 2, 1, 1, 1)
        self.txtEmailcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtEmailcli.setMinimumSize(QtCore.QSize(300, 0))
        self.txtEmailcli.setMaximumSize(QtCore.QSize(320, 16777215))
        self.txtEmailcli.setText("")
        self.txtEmailcli.setObjectName("txtEmailcli")
        self.gridLayout.addWidget(self.txtEmailcli, 2, 2, 1, 1)
        self.chkHistoriacli = QtWidgets.QCheckBox(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkHistoriacli.sizePolicy().hasHeightForWidth())
        self.chkHistoriacli.setSizePolicy(sizePolicy)
        self.chkHistoriacli.setObjectName("chkHistoriacli")
        self.gridLayout.addWidget(self.chkHistoriacli, 1, 11, 1, 1)
        self.txtDnicli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtDnicli.setMinimumSize(QtCore.QSize(120, 0))
        self.txtDnicli.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtDnicli.setStyleSheet("background-color: rgb(255, 254, 230);")
        self.txtDnicli.setObjectName("txtDnicli")
        self.gridLayout.addWidget(self.txtDnicli, 0, 2, 1, 1)
        self.lblDnicli = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDnicli.sizePolicy().hasHeightForWidth())
        self.lblDnicli.setSizePolicy(sizePolicy)
        self.lblDnicli.setObjectName("lblDnicli")
        self.gridLayout.addWidget(self.lblDnicli, 0, 1, 1, 1)
        self.lblNomcli = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNomcli.sizePolicy().hasHeightForWidth())
        self.lblNomcli.setSizePolicy(sizePolicy)
        self.lblNomcli.setObjectName("lblNomcli")
        self.gridLayout.addWidget(self.lblNomcli, 1, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        self.txtNomecli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtNomecli.setMinimumSize(QtCore.QSize(300, 0))
        self.txtNomecli.setMaximumSize(QtCore.QSize(320, 16777215))
        self.txtNomecli.setText("")
        self.txtNomecli.setObjectName("txtNomecli")
        self.gridLayout.addWidget(self.txtNomecli, 1, 5, 1, 5)
        self.txtApelcli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtApelcli.setMinimumSize(QtCore.QSize(300, 0))
        self.txtApelcli.setMaximumSize(QtCore.QSize(320, 16777215))
        self.txtApelcli.setObjectName("txtApelcli")
        self.gridLayout.addWidget(self.txtApelcli, 1, 2, 1, 1)
        self.lblApelcli = QtWidgets.QLabel(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblApelcli.sizePolicy().hasHeightForWidth())
        self.lblApelcli.setSizePolicy(sizePolicy)
        self.lblApelcli.setObjectName("lblApelcli")
        self.gridLayout.addWidget(self.lblApelcli, 1, 1, 1, 1)
        self.cmbMunicli = QtWidgets.QComboBox(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbMunicli.sizePolicy().hasHeightForWidth())
        self.cmbMunicli.setSizePolicy(sizePolicy)
        self.cmbMunicli.setMinimumSize(QtCore.QSize(160, 0))
        self.cmbMunicli.setObjectName("cmbMunicli")
        self.gridLayout.addWidget(self.cmbMunicli, 3, 9, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 12, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 10, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 12, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 12, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem10, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem11, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem12, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem13, 0, 12, 1, 1)
        self.lblAltacli = QtWidgets.QLabel(parent=self.pesClientes)
        self.lblAltacli.setObjectName("lblAltacli")
        self.gridLayout.addWidget(self.lblAltacli, 0, 5, 1, 1)
        self.txtAltacli = QtWidgets.QLineEdit(parent=self.pesClientes)
        self.txtAltacli.setMaximumSize(QtCore.QSize(80, 20))
        self.txtAltacli.setObjectName("txtAltacli")
        self.gridLayout.addWidget(self.txtAltacli, 0, 6, 1, 1)
        self.btnAltacli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnAltacli.setMaximumSize(QtCore.QSize(32, 16777215))
        self.btnAltacli.setSizeIncrement(QtCore.QSize(32, 0))
        self.btnAltacli.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.PreventContextMenu)
        self.btnAltacli.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnAltacli.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/a20evansg/.designer/img/calendar.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAltacli.setIcon(icon1)
        self.btnAltacli.setObjectName("btnAltacli")
        self.gridLayout.addWidget(self.btnAltacli, 0, 7, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.btnGrabarcli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnGrabarcli.setMinimumSize(QtCore.QSize(80, 25))
        self.btnGrabarcli.setObjectName("btnGrabarcli")
        self.horizontalLayout.addWidget(self.btnGrabarcli)
        self.btnModifcli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnModifcli.setMinimumSize(QtCore.QSize(80, 25))
        self.btnModifcli.setObjectName("btnModifcli")
        self.horizontalLayout.addWidget(self.btnModifcli)
        self.btnElimcli = QtWidgets.QPushButton(parent=self.pesClientes)
        self.btnElimcli.setMinimumSize(QtCore.QSize(80, 25))
        self.btnElimcli.setObjectName("btnElimcli")
        self.horizontalLayout.addWidget(self.btnElimcli)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=self.pesClientes)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.pesClientes)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 1)
        self.tablaClientes = QtWidgets.QTableWidget(parent=self.pesClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablaClientes.sizePolicy().hasHeightForWidth())
        self.tablaClientes.setSizePolicy(sizePolicy)
        self.tablaClientes.setAutoFillBackground(True)
        self.tablaClientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaClientes.setObjectName("tablaClientes")
        self.tablaClientes.setColumnCount(7)
        self.tablaClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaClientes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaClientes.setHorizontalHeaderItem(6, item)
        self.tablaClientes.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tablaClientes, 3, 0, 1, 1)
        self.panPrincipal.addTab(self.pesClientes, "")
        self.tabConstruccion = QtWidgets.QWidget()
        self.tabConstruccion.setObjectName("tabConstruccion")
        self.label = QtWidgets.QLabel(parent=self.tabConstruccion)
        self.label.setGeometry(QtCore.QRect(260, 110, 291, 141))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.panPrincipal.addTab(self.tabConstruccion, "")
        self.gridLayout_2.addWidget(self.panPrincipal, 0, 1, 1, 1)
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=venPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHerramientas = QtWidgets.QMenu(parent=self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        self.menuAyuda = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        venPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(parent=venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCrearBackup = QtGui.QAction(parent=venPrincipal)
        self.actionCrearBackup.setObjectName("actionCrearBackup")
        self.actionRestaurar = QtGui.QAction(parent=venPrincipal)
        self.actionRestaurar.setObjectName("actionRestaurar")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHerramientas.addAction(self.actionCrearBackup)
        self.menuHerramientas.addAction(self.actionRestaurar)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(venPrincipal)
        self.panPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)
        venPrincipal.setTabOrder(self.txtDnicli, self.txtAltacli)
        venPrincipal.setTabOrder(self.txtAltacli, self.txtApelcli)
        venPrincipal.setTabOrder(self.txtApelcli, self.txtNomecli)
        venPrincipal.setTabOrder(self.txtNomecli, self.txtEmailcli)
        venPrincipal.setTabOrder(self.txtEmailcli, self.txtMovilcli)
        venPrincipal.setTabOrder(self.txtMovilcli, self.txtDircli)
        venPrincipal.setTabOrder(self.txtDircli, self.cmbProvcli)
        venPrincipal.setTabOrder(self.cmbProvcli, self.cmbMunicli)
        venPrincipal.setTabOrder(self.cmbMunicli, self.btnGrabarcli)
        venPrincipal.setTabOrder(self.btnGrabarcli, self.btnModifcli)
        venPrincipal.setTabOrder(self.btnModifcli, self.btnElimcli)
        venPrincipal.setTabOrder(self.btnElimcli, self.btnAltacli)
        venPrincipal.setTabOrder(self.btnAltacli, self.tablaClientes)
        venPrincipal.setTabOrder(self.tablaClientes, self.chkHistoriacli)
        venPrincipal.setTabOrder(self.chkHistoriacli, self.panPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "Inmoteis"))
        self.lblDircli.setText(_translate("venPrincipal", "Dirección:"))
        self.lblMovilcli.setText(_translate("venPrincipal", "Móvil:"))
        self.lblProvcli.setText(_translate("venPrincipal", "Provincia:"))
        self.lblMunicli_2.setText(_translate("venPrincipal", "Municipio:"))
        self.lblEmailcli.setText(_translate("venPrincipal", "Email:"))
        self.chkHistoriacli.setText(_translate("venPrincipal", "Histórico"))
        self.lblDnicli.setText(_translate("venPrincipal", "DNI/CIF:"))
        self.lblNomcli.setText(_translate("venPrincipal", "Nombre:"))
        self.lblApelcli.setText(_translate("venPrincipal", "Apellidos:"))
        self.lblAltacli.setText(_translate("venPrincipal", "Fecha Alta:"))
        self.btnGrabarcli.setText(_translate("venPrincipal", "Grabar"))
        self.btnModifcli.setText(_translate("venPrincipal", "Modificar"))
        self.btnElimcli.setText(_translate("venPrincipal", "Eliminar"))
        item = self.tablaClientes.horizontalHeaderItem(0)
        item.setText(_translate("venPrincipal", "DNI/NIE"))
        item = self.tablaClientes.horizontalHeaderItem(1)
        item.setText(_translate("venPrincipal", "Apellidos"))
        item = self.tablaClientes.horizontalHeaderItem(2)
        item.setText(_translate("venPrincipal", "Nombre"))
        item = self.tablaClientes.horizontalHeaderItem(3)
        item.setText(_translate("venPrincipal", "Movil"))
        item = self.tablaClientes.horizontalHeaderItem(4)
        item.setText(_translate("venPrincipal", "Provincia"))
        item = self.tablaClientes.horizontalHeaderItem(5)
        item.setText(_translate("venPrincipal", "Municipio"))
        item = self.tablaClientes.horizontalHeaderItem(6)
        item.setText(_translate("venPrincipal", "Fecha de Baja"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.pesClientes), _translate("venPrincipal", "CLIENTES"))
        self.label.setText(_translate("venPrincipal", "PANEL EN CONSTRUCCIÓN"))
        self.panPrincipal.setTabText(self.panPrincipal.indexOf(self.tabConstruccion), _translate("venPrincipal", "Tab 2"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.menuHerramientas.setTitle(_translate("venPrincipal", "Herramientas"))
        self.menuAyuda.setTitle(_translate("venPrincipal", "Ayuda"))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
        self.actionCrearBackup.setText(_translate("venPrincipal", "CrearBackup"))
        self.actionRestaurar.setText(_translate("venPrincipal", "Restaurar"))
