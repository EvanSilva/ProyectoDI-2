from PyQt6 import QtWidgets, QtGui, QtCore
import conexion
import eventos
import var

class Clientes:

    def checkDNI(dni):
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

    def altaCliente(self):

        try:
            nuevocli = [var.ui.txtDnicli.text(), var.ui.txtAltacli.text(), var.ui.txtApelcli.text(), var.ui.txtNomecli.text(), var.ui.txtEmailcli.text(), var.ui.txtMovilcli.text(), var.ui.txtDircli.text(), var.ui.cmbProvcli.currentText(), var.ui.cmbMunicli.currentText()]

            if conexion.Conexion.altaCliente(nuevocli):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
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
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setText("Error al dar de alta el cliente")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel)
                mbox.exec()
                return False

        except Exception as e:
            print("error altaCliente", e)






    def checkEmail(mail):
        try:
            mail = str(var.ui.txtEmailcli.text())
            if eventos.Eventos.validarMail(mail):
                var.ui.txtEmailcli.setStyleSheet('background-color: rgb(255, 255, 255);')
                var.ui.txtEmailcli.setText(mail.lower())

            else:
                var.ui.txtEmailcli.setStyleSheet('background-color:#FFC0CB; font-style: italic;')
                var.ui.txtEmailcli.setText(None)
                var.ui.txtEmailcli.setText("correo no válido")
                var.ui.txtEmailcli.setFocus()

        except Exception as error:
            print("error check cliente", error)

    def cargaTablaClientes(self):
        try:
            listado = conexion.Conexion.listadoClientes(self)
            print(listado)

            if not listado:
                print("No se encontraron clientes.")
                return

            var.ui.tablaClientes.setRowCount(0)  # Limpiar tabla antes de rellenarla

            index = 0
            for registro in listado:
                var.ui.tablaClientes.setRowCount(index + 1)

                item_apellido = QtWidgets.QTableWidgetItem(registro[2])  # Apellido
                item_nombre = QtWidgets.QTableWidgetItem(registro[3])  # Nombre
                item_movil = QtWidgets.QTableWidgetItem(registro[5])  # Movil
                item_provincia = QtWidgets.QTableWidgetItem(registro[7])  # Provincia
                item_municipio = QtWidgets.QTableWidgetItem(registro[8])  # Municipio
                item_fecha_baja = QtWidgets.QTableWidgetItem(registro[9])  # FechaBaja

                # Añadir items a la tabla
                var.ui.tablaClientes.setItem(index, 0, item_apellido)
                var.ui.tablaClientes.setItem(index, 1, item_nombre)
                var.ui.tablaClientes.setItem(index, 2, item_movil)
                var.ui.tablaClientes.setItem(index, 3, item_provincia)
                var.ui.tablaClientes.setItem(index, 4, item_municipio)
                var.ui.tablaClientes.setItem(index, 5, item_fecha_baja)

                # Alineación de textos
                item_apellido.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
                item_nombre.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
                item_movil.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                item_provincia.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
                item_municipio.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
                item_fecha_baja.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                index += 1

        except Exception as e:
            print("Error CargaTablaCliente", e)
            import traceback
            print(traceback.format_exc())