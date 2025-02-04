import conexion

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout
import var

class Alquileres:

    def altaAlquiler(self):
        """

        Método para dar de alta una factura en la base de datos.

        :return: None
        :rtype: None

        """
        try:
            if var.ui.txtDniAlq.text() == '':
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

            elif var.ui.txtFechaInicioAlq.text() == '':
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('No hay fecha de inicio selecionada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

            elif var.ui.txtFechaFinAlq.text() == '':
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('No hay fecha de fin selecionada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
            else:
                nuevoalquiler = [var.ui.txtAlqCodigo.text(), var.ui.txtDniAlq.text(), var.ui.txtAlqVendedor.text(), var.ui.txtFechaInicioAlq.text(), var.ui.txtFechaFinAlq.text(), var.ui.txtAlqPrecio.text()]

                if conexion.Conexion.altaAlquiler(nuevoalquiler):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                    mbox.setWindowTitle('Factura Guardada')
                    mbox.setText('Se ha guardado la factura correctamente')
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()

                    Alquileres.cargaTablaAlquileres()

        except Exception as error:
            print('Error al guardar alquiler: %s' % str(error))

    def bajaAlquiler(id):

        try:

            if conexion.Conexion.bajaAlquiler(id):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Factura eliminada')
                mbox.setText('Se ha eliminado el alquiler correctamente')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

                Alquileres.cargaTablaAlquileres()
                #   Facturas.cargaTablaVentas(id)


        except Exception as error:
            print('Error al bajar factura: %s' % str(error))

    @staticmethod
    def cargaTablaAlquileres():

        """
        Método que carga los datos de facturas en la tabla de la interfaz.

        :return: None
        :rtype: None

        """

        try:
            listado = conexion.Conexion.cargaAlquileres()
            var.ui.tablaFactura.setRowCount(0)  # Limpia la tabla antes de cargar nuevos datos
            for index, registro in enumerate(listado):
                var.ui.tablaFactura.setRowCount(index + 1)
                var.ui.tablaFactura.setItem(index, 0, QtWidgets.QTableWidgetItem(registro[0]))
                var.ui.tablaFactura.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[2]))

                var.ui.tablaFactura.setColumnWidth(0, 80)
                var.ui.tablaFactura.setColumnWidth(1, 80)


                var.ui.tablaFactura.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)

                botondelfac = QtWidgets.QPushButton()
                botondelfac.setFixedSize(25, 25)
                botondelfac.setIconSize(QtCore.QSize(25, 25))
                botondelfac.setIcon(QtGui.QIcon("./img/borrar.ico"))

                contenedor = QtWidgets.QWidget()
                layout = QHBoxLayout()
                layout.addWidget(botondelfac)
                layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                contenedor.setLayout(layout)

                container = QWidget()
                container.setLayout(layout)
                var.ui.tablaFactura.setCellWidget(index, 2, container)
                botondelfac.clicked.connect(lambda checked, id=registro[0]: Alquileres.bajaAlquiler(id))



        except Exception as e:
            print("Error en cargaTablaFacturas:", e)

