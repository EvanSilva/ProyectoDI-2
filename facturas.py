
import conexion

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout
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

                    Facturas.cargaTablaFacturas()

        except Exception as error:
            print('Error al insertar factura: %s' % str(error))

    def bajaFactura(id):
        try:

            if conexion.Conexion.bajaFactura(id):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Factura eliminada')
                mbox.setText('Se ha eliminado la factura correctamente')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

                Facturas.cargaTablaFacturas()


        except Exception as error:
            print('Error al bajar factura: %s' % str(error))

    @staticmethod
    def cargaTablaFacturas():

        """
        Método que carga los datos de facturas en la tabla de la interfaz.
        """

        try:
            listado = conexion.Conexion.cargarFacturas()
            var.ui.tablaFactura.setRowCount(0)  # Limpia la tabla antes de cargar nuevos datos
            for index, registro in enumerate(listado):
                var.ui.tablaFactura.setRowCount(index + 1)
                var.ui.tablaFactura.setItem(index, 0, QtWidgets.QTableWidgetItem(registro[0]))  # id
                var.ui.tablaFactura.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[1]))  # fechafac
                var.ui.tablaFactura.setItem(index, 2, QtWidgets.QTableWidgetItem(registro[2]))

                var.ui.tablaFactura.setColumnWidth(0, 80)
                var.ui.tablaFactura.setColumnWidth(1, 80)
                var.ui.tablaFactura.setColumnWidth(2, 106)

                var.ui.tablaFactura.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)

                botondelfac = QtWidgets.QPushButton()
                botondelfac.setFixedSize(25,25)
                botondelfac.setIconSize(QtCore.QSize(25,25))
                botondelfac.setIcon(QtGui.QIcon("./img/borrar.ico"))


                contenedor = QtWidgets.QWidget()
                layout = QHBoxLayout()
                layout.addWidget(botondelfac)
                layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                contenedor.setLayout(layout)

                container = QWidget()
                container.setLayout(layout)
                var.ui.tablaFactura.setCellWidget(index, 3, container)
                botondelfac.clicked.connect(lambda checked, id=registro[0]: Facturas.bajaFactura(id))



        except Exception as e:
            print("Error en cargaTablaFacturas:", e)

    def cargaOneFactura(self):
        try:
            fila = var.ui.tablaFactura.selectedItems()
            if not fila:
                raise ValueError("No se ha seleccionado ninguna fila en la tabla.")

            datos = [dato.text() for dato in fila]
            if not datos:
                raise ValueError("No se pudieron extraer datos de la fila seleccionada.")

            registro = conexion.Conexion.datosOneFactura((datos[0]))
            if not registro or len(registro) < 3:
                raise ValueError("Los datos de la factura no son válidos o están incompletos.")

            # Convertir a cadenas antes de asignar
            var.ui.txtNumFac.setText(str(registro[0]))
            var.ui.txtFechaFac.setText(str(registro[1]))
            var.ui.txtDniFac.setText(str(registro[2]))

        except Exception as error:
            print(f"Error en cargaOneFactura: {error}")



    def altaVenta(self):
        try:
            if var.ui.txtFacApel.text() == '':
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
            elif  var.ui.txtFacCodigo.text() == '':
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('No hay Propiedad seleccionada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
            elif var.ui.txtFacVendedor.text() == '':
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('No hay Vendedor seleccionado')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
            else:
                nuevaventa = [var.ui.txtNumFac.text(), var.ui.txtFacCodigo.text(), var.ui.txtFacVendedor.text()]
                if conexion.Conexion.altaVenta(nuevaventa):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                    mbox.setWindowTitle('Venta Guardada')
                    mbox.setText('Se ha guardado la venta correctamente')
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()

                    Facturas.cargaTablaFacturas()

        except Exception as error:
            print('Error al insertar venta: %s' % str(error))

    # ARREGLAR
    def cargaTablaVentas():

        """
        Método que carga los datos de facturas en la tabla de la interfaz.
        """

        try:
            listado = conexion.Conexion.cargarVentas()
            var.ui.tablaFactura.setRowCount(0)  # Limpia la tabla antes de cargar nuevos datos
            for index, registro in enumerate(listado):
                var.ui.tablaVenta.setRowCount(index + 1)
                var.ui.tablaVenta.setItem(index, 0, QtWidgets.QTableWidgetItem(registro[0]))  # id
                var.ui.tablaVenta.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[1]))  # facventa
                var.ui.tablaVenta.setItem(index, 2, QtWidgets.QTableWidgetItem(registro[2]))  # codprop
                var.ui.tablaVenta.setItem(index, 3, QtWidgets.QTableWidgetItem(registro[3]))  # vendedor


                var.ui.tablaVenta.setColumnWidth(0, 80)
                var.ui.tablaVenta.setColumnWidth(1, 80)
                var.ui.tablaVenta.setColumnWidth(2, 106)

                var.ui.tablaFactura.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)

                botondelfac = QtWidgets.QPushButton()
                botondelfac.setFixedSize(25,25)
                botondelfac.setIconSize(QtCore.QSize(25,25))
                botondelfac.setIcon(QtGui.QIcon("./img/borrar.ico"))


                contenedor = QtWidgets.QWidget()
                layout = QHBoxLayout()
                layout.addWidget(botondelfac)
                layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                contenedor.setLayout(layout)

                container = QWidget()
                container.setLayout(layout)
                var.ui.tablaFactura.setCellWidget(index, 3, container)
                botondelfac.clicked.connect(lambda checked, id=registro[0]: Facturas.bajaFactura(id))



        except Exception as e:
            print("Error en cargaTablaFacturas:", e)



