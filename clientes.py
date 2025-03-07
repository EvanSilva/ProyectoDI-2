from PyQt6 import QtWidgets, QtGui, QtCore


import clientes
import conexion
import eventos
import var

class Clientes:

    def checkDNI(dni):
        """

        Método para validar un DNI

        :param dni: DNI a validar
        :type dni: str
        :return: None
        :rtype: None

        """
        try:
            dni = str(dni).upper()
            var.ui.txtDnicli.setText(str(dni))
            check = eventos.Eventos.validarDNI(dni)
            if check:
                var.ui.txtDnicli.setStyleSheet("background-color: #BEEEBA;")
            else:
                var.ui.txtDnicli.setStyleSheet('background-color:#FFC0CB;')  # y si no un aspa en color rojo
                var.ui.txtDnicli.setText(None)
                var.ui.txtDnicli.setFocus()
        except Exception as e:
            print("error check cliente", e)

    def checkEmail(mail):
        """

        Método para validar un correo electrónico

        :param mail: correo electrónico a validar
        :type mail: str
        :return: None
        :rtype: None


        """
        try:
            mail = str(var.ui.txtEmailcli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailcli.setStyleSheet('background-color: rgb(255, 255, 255);')
                var.ui.txtEmailcli.setText(mail.lower())

            else:
                var.ui.txtEmailcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtEmailcli.setText(None)
                var.ui.txtEmailcli.setPlaceholderText("correo no válido")
                var.ui.txtEmailcli.setFocus()

        except Exception as error:
            print("error check cliente", error)


    def checkNumero(numero):
        """

        Método para validar un número de teléfono

        :param numero: número de teléfono a validar
        :type numero: str
        :return: None
        :rtype: None

        """
        try:

            var.ui.txtMovilcli.setText(str(numero))
            check = eventos.Eventos.validarMovil(numero)
            if check:
                var.ui.txtMovilcli.setStyleSheet("background-color: #BEEEBA;")
            else:
                var.ui.txtMovilcli.setStyleSheet('background-color:#FFC0CB;')
                var.ui.txtMovilcli.setText(None)
                var.ui.txtMovilcli.setFocus()

        except Exception as e:
            print("error check cliente", e)

    def checkObligatorios(self):
        """

        Método para validar los campos obligatorios

        :param self:
        :type self: object
        :return: True si los campos obligatorios están completos, False si no
        :rtype: bool

        """
        try:
            textos = [var.ui.txtDnicli.text(),
                      var.ui.txtAltacli.text(),
                      var.ui.txtApelcli.text(),
                      var.ui.txtNomecli.text(),
                      var.ui.txtMovilcli.text(),
                      var.ui.txtDircli.text(),
                      var.ui.cmbProvcli.currentText()]

            for texto in textos:
                if eventos.Eventos.checkTxtVacio(texto):
                    return False
            return True

        except Exception as e:
            print("error check cliente", e)


    def altaCliente(self):
        """

        Método para dar de alta un cliente en la base de datos

        :param self:
        :type self: object
        :return: True si el cliente se ha dado de alta correctamente, False si no
        :rtype: bool


        """
        try:
            nuevocli = [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text(), var.ui.txtNomecli.text(), var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText()]

            if clientes.Clientes.checkObligatorios(self):
                if conexion.Conexion.altaCliente(nuevocli):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText('Cliente Alta en Base de Datos')
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Clientes.cargaTablaClientes(self)
                    return True
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                    mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                    mbox.setText("Error al dar de alta el cliente")
                    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                    mbox.exec()
                    return False

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setText("Faltan Datos Obligatorios")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()
                return False

        except Exception as e:
            print("error altaCliente", e)


    @staticmethod
    def cargaTablaClientes(self):
        """

        Método para cargar la tabla de clientes


        :param self: objeto de la clase
        :type self: object
        :return: None
        :rtype: None


        """
        try:
            listado = conexion.Conexion.listadoClientes(self)
            index = 0
            for registro in listado:
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(registro[0]))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[2]))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(registro[3]))
                var.ui.tablaClientes.setItem(index, 3, QtWidgets.QTableWidgetItem("  " + registro[5] + "  "))
                var.ui.tablaClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(registro[7]))
                var.ui.tablaClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(registro[8]))
                var.ui.tablaClientes.setItem(index, 6, QtWidgets.QTableWidgetItem("  " + registro[9] + "  "))
                var.ui.tablaClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                index += 1

        except Exception as e:
            print("error cargaTablaCientes", e)

    def cargaTablaCincoClientes(self, listado):
        """

        Método para cargar la tabla de clientes con los cinco primeros registros

        :param listado: lista de clientes
        :type listado: list
        :return: None
        :rtype: None


        """
        try:
            index = 0
            for registro in listado:
                var.ui.tablaClientes.setRowCount(index + 1)
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(registro[0]))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[2]))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(registro[3]))
                var.ui.tablaClientes.setItem(index, 3, QtWidgets.QTableWidgetItem("  " + registro[5] + "  "))
                var.ui.tablaClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(registro[7]))
                var.ui.tablaClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(registro[8]))
                var.ui.tablaClientes.setItem(index, 6, QtWidgets.QTableWidgetItem("  " + registro[9] + "  "))
                var.ui.tablaClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaClientes.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                index += 1

        except Exception as e:
            print("error cargaTablaCientes", e)

    def cargaOneCliente(self):
        """

        Método para cargar los datos de un cliente en los campos de texto

        :return: None
        :rtype: None


        """
        try:
            fila = var.ui.tablaClientes.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneCliente(str(datos[0]))
            listado = [var.ui.txtDnicli, var.ui.txtAltacli, var.ui.txtApelcli, var.ui.txtNomecli, var.ui.txtEmailcli, var.ui.txtMovilcli, var.ui.txtDircli, var.ui.cmbProvcli, var.ui.cmbMunicli]

            var.ui.txtDniFac.setText(registro[0])
            var.ui.txtDniAlq.setText(registro[0])

            var.ui.txtFacApel.setText(registro[2])
            var.ui.txtFacNombre.setText(registro[3])
            var.ui.txtFacDir.setText(registro[6])

            for i in range(len(listado)):
                if i == 7 or i == 8:
                    listado[i].setCurrentText(registro[i])
                else:
                    listado[i].setText(registro[i])

        except Exception as e:
            print("Error en cargaOneCliente", e)

    def modifCliente(self):
        """

        Método para modificar los datos de un cliente

        :return: None
        :rtype: None

        """
        try:
            modifcli = [var.ui.txtDnicli.text(),
                        var.ui.txtAltacli.text(),
                        var.ui.txtApelcli.text(),
                        var.ui.txtNomecli.text(),
                        var.ui.txtEmailcli.text(),
                        var.ui.txtMovilcli.text(),
                        var.ui.txtDircli.text(),
                        var.ui.cmbProvcli.currentText(),
                        var.ui.cmbMunicli.currentText(),
                        var.ui.txtBajacli.text()]

            if conexion.Conexion.modifCliente(modifcli):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Datos Cliente Modificados')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('ERROR AL MODIFICAR CLIENTE')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

        except Exception as e:
            print("Error en modifCliente", e)


    def bajaCliente(self):
        """

        Método para dar de baja a un cliente

        :return: None
        :rtype: None


        """
        try:
            datos = [var.ui.txtBajacli.text(), var.ui.txtDnicli.text()]
            if conexion.Conexion.bajaCliente(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Cliente Dado de Baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('ERROR AL DAR DE BAJA AL CLIENTE')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)

        except Exception as e:
            print("Error en bajaCliente", e)

    def historicoCli(Self):
        """

        Método para activar o desactivar el histórico de clientes

        :return: None
        :rtype: None

        """
        try:
            if var.ui.chkHistoriacli.isChecked():
                var.historico = 0

            else:
                var.historico = 1

            Clientes.cargaTablaClientes(Self)
        except Exception as Error:
            print("Checkbox Historico", Error)

    def buscarOneCliente(self):
        """

        Método para buscar un cliente por DNI

        :return: None
        :rtype: None

        """
        try:
            dni = var.ui.txtDnicli.text()
            registro = conexion.Conexion.datosOneCliente(dni)

            if conexion.Conexion.datosOneCliente(dni):
                listado = [var.ui.txtDnicli, var.ui.txtAltacli, var.ui.txtApelcli, var.ui.txtNomecli,
                           var.ui.txtEmailcli, var.ui.txtMovilcli, var.ui.txtDircli, var.ui.cmbProvcli,
                           var.ui.cmbMunicli]
                for i in range(len(listado)):
                    if i == 7 or i == 8:
                        listado[i].setCurrentText(registro[i])
                    else:
                        listado[i].setText(registro[i])
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('EL CLIENTE CON DNI ' + dni +  ' NO EXISTE')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Clientes.cargaTablaClientes(self)

        except Exception as e:
            print("Error en cargaOneCliente", e)
