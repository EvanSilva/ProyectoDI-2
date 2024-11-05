from PyQt6 import QtWidgets, QtGui
from PyQt6 import QtCore

import conexion
import var


class Propiedades():

    def altaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text().strip()  # Eliminar espacios
            if not tipo:  # Verificar que el tipo no esté vacío
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Por favor, ingrese un tipo de propiedad válido.')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                return
            registro = conexion.Conexion.altaTipoprop(tipo)

            if registro is False:  # Si el registro es False, hubo un error al insertar
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al dar de alta el tipo de propiedad, ya existe.')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
            else:  # Si se insertó correctamente, actualizar el combo box
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText(f'Tipo de propiedad "{tipo}", dado de alta.')
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                var.dlggestion.ui.txtGestipoprop.setText("")  # Limpiar solo si se da de alta
            print(tipo)

        except Exception as e:
            print("Error en altaTipopropiedad:", e)

    def bajaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text().title()
            if (tipo):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Propiedad eliminada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
                conexion.Conexion.bajaTipoprop(tipo)
                registro = conexion.Conexion.cargarTipoprop(self)
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
                print(tipo)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Tipo de propiedad no existe')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()


        except Exception as e:
            print(e)

    def altaPropiedad(self):
        try:
            propiedades = [var.ui.txtAltaprop.text(), var.ui.txtDirprop.text(),
                         var.ui.cmbProvprop.currentText(), var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(),
                         var.ui.spnHabprop.text(), var.ui.spnBanosprop.text(), var.ui.txtSuperprop.text(),
                         var.ui.txtPrecioalquilerprop.text(), var.ui.txtPrecioventaprop.text(), var.ui.txtCPprop.text(),
                         var.ui.txtObservaprop.toPlainText()
                         ]

            tipooper = []
            if var.ui.chkAlquiprop.isChecked():
                tipooper.append(var.ui.chkAlquiprop.text())

            if var.ui.chkVentaprop.isChecked():
                tipooper.append(var.ui.chkVentaprop.text())

            if var.ui.chkInterprop.isChecked():
                tipooper.append(var.ui.chkInterprop.text())
            propiedades.append(tipooper)
            if var.ui.rbtDisponprop.isChecked():
                propiedades.append(var.ui.rbtDisponprop.text())
            elif var.ui.rbtVentaprop.isChecked():
                propiedades.append(var.ui.rbtVentaprop.text())
            elif var.ui.rbtAlquiprop.isChecked():
                propiedades.append(var.ui.rbtAlquiprop.text())

            propiedades.append(var.ui.txtNomeprop.text())
            propiedades.append(var.ui.txtMovilprop.text())
            conexion.Conexion.altaPropiedad(propiedades)
            Propiedades.cargaTablaPropiedades(self)


            print(propiedades)
        except Exception as e:
            print("Error en propiedades, altaPropiedad(), " + e)

    def cargaTablaPropiedades(self):
        try:
            listado = conexion.Conexion.listadoPropiedades(self)
            print("Registros obtenidos:", listado)  # Esto te mostrará si se obtuvieron varios registros o solo uno.
            index = 0
            for registro in listado:
                var.ui.tablaProp.setRowCount(index + 1)
                var.ui.tablaProp.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaProp.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tablaProp.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[6])))
                var.ui.tablaProp.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[7])))
                var.ui.tablaProp.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[8])))
                if registro[10] == "":
                    registro[10] = "-"
                if registro[11] == "":
                    registro[11] = "-"
                var.ui.tablaProp.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[10]) + " €" ))
                var.ui.tablaProp.setItem(index, 6, QtWidgets.QTableWidgetItem(str(registro[11]) + " €" ))

                string_limpio = registro[14].replace("[", "").replace("]", "").replace("'", "").strip()

                var.ui.tablaProp.setItem(index, 7, QtWidgets.QTableWidgetItem(string_limpio))
                var.ui.tablaProp.setItem(index, 8, QtWidgets.QTableWidgetItem(str(registro[15])))

                var.ui.tablaProp.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaProp.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaProp.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaProp.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaProp.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                var.ui.tablaProp.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)
                var.ui.tablaProp.item(index, 6).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                index += 1

        except Exception as e:
            print("error cargaTablaCientes", e)
            import traceback
            print(traceback.format_exc())

    def modifCliente(self):
        try:
            propiedad = [var.ui.txtDnicli.text(),
                        var.ui.txtAltacli.text(),
                        var.ui.txtApelcli.text(),
                        var.ui.txtNomecli.text(),
                        var.ui.txtEmailcli.text(),
                        var.ui.txtMovilcli.text(),
                        var.ui.txtDircli.text(),
                        var.ui.cmbProvcli.currentText(),
                        var.ui.cmbMunicli.currentText(),
                        var.ui.txtBajacli.text()]

            if conexion.Conexion.modifCliente(propiedad):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
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
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('ERROR AL MODIFICAR CLIENTE')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

        except Exception as e:
            print("Error en modifCliente", e)

