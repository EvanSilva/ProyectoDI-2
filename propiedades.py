from PyQt6 import QtWidgets, QtGui

import conexion
import var


class Propiedades():

    def altaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text()
            registro = conexion.Conexion.altaTipoprop(tipo)
            var.ui.cmbTipoprop.clear()
            var.ui.cmbTipoprop.addItems(registro)
            mbox = QtWidgets.QMessageBox()
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
            mbox.setWindowTitle('Aviso')
            mbox.setText('Tipo de propiedad ' + tipo + ', dado de alta')
            mbox.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Ok)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
            mbox.exec()
            if registro:
                var.ui.cmbTipoprop.clear()
                var.ui.cmbTipoprop.addItems(registro)
            elif not registro:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('Error al dar de alta el tipo de propiedad, ya existe')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
            var.dlgges.ui.txtGestipoprop.setText("")
            print(tipo)
        except Exception as e:
            print(e)

    def bajaTipopropiedad(self):
        try:
            tipo = var.dlggestion.ui.txtGestipoprop.text().title()
            if conexion.Conexion.bajaTipoprop(tipo):
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
            propiedad = [var.ui.txtAltaprop.text(), var.ui.txtBajaprop.text(), var.ui.txtDirprop.text(),
                         var.ui.cmbProvprop.currentText(), var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(),
                         var.ui.spnHabprop.text(), var.ui.spnBanprop.text(), var.ui.txtSuperprop.text(),
                         var.ui.txtPrecioalquilerprop.text(), var.ui.txtPrecioventaprop.text(), var.ui.CPprop.text(),
                         var.ui.txtObservaprop.toPlainText(), var.ui.txtNomeprop.text(), var.ui.txtMovilprop.text()
                         ]
            print(propiedad)
        except Exception as e:
            print("Error en propiedades, altaPropiedad()")
