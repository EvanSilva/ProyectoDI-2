import conexion
import eventos
import var

from PyQt6 import QtWidgets, QtGui, QtCore


class Vendedores:

    def altaVendedor(self):

        try:
            nuevoVendedor = [var.ui.txtDniVendedor.text(), var.ui.txtNombreVendedor.text(),
                        var.ui.txtAltaVendedor.text(), var.ui.txtBajaVendedor.text(), var.ui.txtMovilVendedor.text(),
                        var.ui.txtMailVendedor.text(), var.ui.cmbProvVendedor.currentText()]

            if Vendedores.checkObligatorios(self):
                if conexion.Conexion.altaVendedor(nuevoVendedor) :
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                    mbox.setWindowTitle('Aviso')
                    mbox.setText('Vendedor dado de Alta en Base de Datos')
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()
                    Vendedores.cargaTablaVendedores(self)
                    return True
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setText("Error al dar de alta el vendedor, faltan datos obligatorios")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()
                return False

        except Exception as e:
            print("error altavendedor", e)


    def historicoVendedor(Self):
        try:
            if var.ui.chkHistoricoVendedores.isChecked():
                var.historico = 0

            else:
                var.historico = 1

            Vendedores.cargaTablaVendedores(Self)
        except Exception as Error:
            print("Checkbox Historico", Error)


    def cargaTablaVendedores(self):
        try:
            listado = conexion.Conexion.listadoVendedores(self)
            index = 0
            for registro in listado:

                var.ui.tablaVendedor.setRowCount(index + 1)

                var.ui.tablaVendedor.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaVendedor.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[2]))
                var.ui.tablaVendedor.setItem(index, 2, QtWidgets.QTableWidgetItem(registro[5]))
                var.ui.tablaVendedor.setItem(index, 3, QtWidgets.QTableWidgetItem(registro[7]))



                var.ui.tablaVendedor.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaVendedor.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaVendedor.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaVendedor.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)

                index += 1

        except Exception as e:
            print("error cargaTablaCientes", e)
            import traceback
            print(traceback.format_exc())

    def cargaOneVendedor(self):
        try:
            fila = var.ui.tablaVendedor.selectedItems()
            datos = [dato.text() for dato in fila]
            registro = conexion.Conexion.datosOneVendedor(str(datos[0]))

            listado = [var.ui.txtIdVendedor, var.ui.txtDniVendedor, var.ui.txtNombreVendedor,
                             var.ui.txtAltaVendedor, var.ui.txtBajaVendedor,
                             var.ui.txtMovilVendedor,
                             var.ui.txtMailVendedor]

            for i in range(len(listado)):
                    listado[i].setText(str(registro[i]))
            print(registro)

        except Exception as e:
            print("Error en cargaOneVendedor", e)


    def modifVendedor(self):
        try:
            modificarVendedor = [var.ui.txtIdVendedor.text(), var.ui.txtDniVendedor.text(), var.ui.txtNombreVendedor.text(),
                             var.ui.txtAltaVendedor.text(), var.ui.txtBajaVendedor.text(),
                             var.ui.txtMovilVendedor.text(),
                             var.ui.txtMailVendedor.text(), var.ui.cmbProvVendedor.currentText()]

            if conexion.Conexion.modifVendedor(modificarVendedor):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Datos Vendedor Modificados (El DNI y el ID nunca se modifican)')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Vendedores.cargaTablaVendedores(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('ERROR AL MODIFICAR VENDEDOR')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

        except Exception as e:
            print("Error en modifCliente", e)


    def bajaVendedor(self):
        try:
            datos = var.ui.txtIdVendedor.text()
            print(datos)
            if conexion.Conexion.bajaVendedor(datos):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Vendedor Dado de Baja')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Vendedores.cargaTablaVendedores(self)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('ERROR AL DAR DE BAJA AL VENDEDOR')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                Vendedores.cargaTablaVendedores(self)

        except Exception as e:
            print("Error en bajaCliente", e)

    def checkObligatorios(self):
        try:
            textos = [var.ui.txtDniVendedor.text(),
                      var.ui.txtNombreVendedor.text(),
                      var.ui.txtMovilVendedor.text(),
                      var.ui.cmbProvVendedor.currentText()]

            for texto in textos:
                if eventos.Eventos.checkTxtVacio(texto):
                    return False
            return True

        except Exception as e:
            print("error check vendedores", e)

    def checkDNI(dni):
        try:
            dni = str(dni).upper()
            var.ui.txtDniVendedor.setText(str(dni))
            check = eventos.Eventos.validarDNI(dni)
            if check:
                var.ui.txtDniVendedor.setStyleSheet("background-color: #BEEEBA;")
            else:
                var.ui.txtDniVendedor.setStyleSheet('background-color:#FFC0CB;')  # y si no un aspa en color rojo
                var.ui.txtMailVendedor.setPlaceholderText("Dni no válido")
                var.ui.txtDniVendedor.setText(None)
                var.ui.txtDniVendedor.setFocus()
        except Exception as e:
            print("error check cliente", e)

    def checkEmail(mail):
        try:
            mail = str(var.ui.txtMailVendedor.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtMailVendedor.setStyleSheet('background-color: rgb(255, 255, 255);')
                var.ui.txtMailVendedor.setText(mail.lower())

            else:
                var.ui.txtMailVendedor.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtMailVendedor.setText(None)
                var.ui.txtMailVendedor.setPlaceholderText("correo no válido")
                var.ui.txtMailVendedor.setFocus()

        except Exception as error:
            print("error check cliente", error)

    def checkNumero(numero):
        try:

            var.ui.txtMovilVendedor.setText(str(numero))
            check = eventos.Eventos.validarMovil(numero)
            if check:
                var.ui.txtMovilVendedor.setStyleSheet("background-color: #BEEEBA;")
            else:
                var.ui.txtMovilVendedor.setStyleSheet('background-color:#FFC0CB;')
                var.ui.txtMailVendedor.setPlaceholderText("Numero no válido")
                var.ui.txtMovilVendedor.setText(None)
                var.ui.txtMovilVendedor.setFocus()

        except Exception as e:
            print("error check cliente", e)