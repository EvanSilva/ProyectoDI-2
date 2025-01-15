
import conexion

from PyQt6 import QtWidgets, QtGui, QtCore
import var

class Facturas:

    def altafactura(self):
        try:
            if var.ui.txtDniFac.text() == '':
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('No hay cliente seleccionado')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
            else:
                nuevafactura = [var.ui.txtFechaFac.text(), var.ui.txtDniFac.text()]
                if conexion.Conexion.altafactura(nuevafactura):
                    var.ui.lblstatus.setText('Factura %s añadida' % nuevafactura[0])
                    var.ui.txtFechaFac.setText('')
                    var.ui.txtDniFac.setText('')
                    var.ui.lblstatus.setStyleSheet('QLabel {color: green;}')
                    var.ui.lblstatus.show()
                    conexion.Conexion.mostrarfacturas()

        except Exception as error:
            print('Error al insertar factura: %s' % str(error))


