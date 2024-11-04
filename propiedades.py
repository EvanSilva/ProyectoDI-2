from PyQt6 import QtWidgets, QtGui

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
                var.dlgges.ui.txtGestipoprop.setText("")  # Limpiar solo si se da de alta
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
                         var.ui.txtObservaprop.toPlainText(), var.ui.txtNomeprop.text(), var.ui.txtMovilprop.text()
                         ]
            tipooper = []
            if var.ui.chkAlquiprop.isChecked():
                tipooper.append(var.ui.chkAlquiprop.text())

            if var.ui.chkVentaprop.isChecked():
                tipooper.append(var.ui.chkVentaprop.text())

            if var.ui.chkInterprop.isChecked():
                tipooper.append(var.ui.chkInterprop.text())

            if var.ui.rbtDisponprop.isChecked():
                propiedades.append(var.ui.rbtDisponprop.text())
            elif var.ui.rbtVentaprop.isChecked():
                propiedades.append(var.ui.rbtVentaprop.text())
            elif var.ui.rbtAlquiprop.isChecked():
                propiedades.append(var.ui.rbtAlquiprop.text())

            propiedades.append(var.ui.txtNomeprop.text())
            propiedades.append(var.ui.txtMovilprop.text())
            conexion.Conexion.altaPropiedad(propiedades)


            print(propiedades)
        except Exception as e:
            print("Error en propiedades, altaPropiedad(), " + e)

