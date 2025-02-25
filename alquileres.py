import calendar
from datetime import datetime
from functools import partial

from PyQt6.QtCore import Qt

import conexion

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QTableWidgetItem

import eventos
import var
from var import informes


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
            elif var.ui.txtPropAlq.text() == '':
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('No hay propiedad de fin selecionada')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
            elif var.ui.txtAlqVendedor.text() == '':
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Aviso')
                mbox.setText('No hay representante de fin selecionado')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()


            else:
                nuevoalquiler = [var.ui.txtPropAlq.text(), var.ui.txtDniAlq.text(), var.ui.txtAlqVendedor.text(), var.ui.txtFechaInicioAlq.text(), var.ui.txtFechaFinAlq.text(), var.ui.txtAlqPrecio.text()]
                print("LISTA DE ATRIBUTOS DEL ALQUILER:" + str(nuevoalquiler))

                if conexion.Conexion.altaAlquiler(nuevoalquiler):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                    mbox.setWindowTitle('Factura Guardada')
                    mbox.setText('Se ha guardado el alquiler correctamente')
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()

                    Alquileres.cargaTablaAlquileres()
                    var.ui.txtNumAlq.setText(str(conexion.Conexion.findLastAlquilerID()))

                    Alquileres.altaMensualidades(self)
                    Alquileres.cargaTablaMensualidades()


        except Exception as error:
            print('Error al guardar alquiler: %s' % str(error))

    def altaMensualidades(self):
        meses = Alquileres.diferenciaFechasEnMeses()
        fecha_inicio = datetime.strptime(var.ui.txtFechaInicioAlq.text(), "%d/%m/%Y")

        for i in range(meses):
            mes_actual = (fecha_inicio.month + i - 1) % 12 + 1
            ano_actual = fecha_inicio.year + (fecha_inicio.month + i - 1) // 12

            nombre_mes = calendar.month_name[mes_actual]

            # Asegurarte de que Abono sea "False" inicialmente
            mensualidad = [var.ui.txtNumAlq.text(), f"{nombre_mes} {ano_actual}", var.ui.txtAlqPrecio.text(), "False"]

            conexion.Conexion.altaMensualidades(mensualidad)

    @staticmethod
    def diferenciaFechasEnMeses():
        fechaInicio = var.ui.txtFechaInicioAlq.text()
        fechaFin = var.ui.txtFechaFinAlq.text()
        meses = 0
        anoInicio = fechaInicio[-4:]
        anofin = fechaFin[-4:]
        meses += (int(anofin) - int(anoInicio)) * 12
        mesInicio = fechaInicio[3:5]
        mesFin = fechaFin[3:5]
        meses += int(mesFin) - int(mesInicio)
        return meses

    def bajaAlquiler(id):

        try:

            if conexion.Conexion.bajaMensualidades(id):
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
                    var.ui.tablaMensualidades.clearContents()

                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                    mbox.setWindowTitle('Error')
                    mbox.setText('Error al eliminar el alquiler')
                    mbox.setStandardButtons(
                        QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    mbox.exec()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Error')
                mbox.setText('Error al eliminar las mensualidades')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()




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
            var.ui.tablaAlquiler.setRowCount(0)  # Limpia la tabla antes de cargar nuevos datos
            for index, registro in enumerate(listado):
                var.ui.tablaAlquiler.setRowCount(index + 1)
                var.ui.tablaAlquiler.setItem(index, 0, QtWidgets.QTableWidgetItem(registro[0]))
                var.ui.tablaAlquiler.setItem(index, 1, QtWidgets.QTableWidgetItem(registro[2]))

                var.ui.tablaAlquiler.setColumnWidth(0, 80)
                var.ui.tablaAlquiler.setColumnWidth(1, 80)


                var.ui.tablaAlquiler.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignVCenter)

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
                var.ui.tablaAlquiler.setCellWidget(index, 2, container)
                botondelfac.clicked.connect(lambda checked, id=registro[0]: Alquileres.bajaAlquiler(id))



        except Exception as e:
            print("Error en cargaTablaFacturas:", e)

    from functools import partial

    @staticmethod
    def cargaTablaMensualidades():
        print("hola desde mensualidades")
        try:
            fila = var.ui.tablaAlquiler.currentRow()

            total = 0


            if fila == -1:
                print("No hay ninguna fila seleccionada en la tabla de alquileres.")
                return

            id_alquiler_item = var.ui.tablaAlquiler.item(fila, 0)



            if id_alquiler_item is None:
                print("No se pudo obtener el ID del alquiler.")
                return

            id_alquiler = id_alquiler_item.text()
            print("Fila seleccionada - ID Alquiler:", id_alquiler)

            listado = conexion.Conexion.mensualidadesOneAlquiler(id_alquiler)
            print("Mensualidades encontradas:", listado)

            # Limpiar la tabla antes de cargar nuevos datos
            var.ui.tablaMensualidades.setRowCount(0)

            for index, registro in enumerate(listado):
                var.ui.tablaMensualidades.setRowCount(index + 1)
                var.ui.tablaMensualidades.setItem(index, 0, QTableWidgetItem(str(registro[0])))
                var.ui.tablaMensualidades.setItem(index, 1, QTableWidgetItem(str(registro[1])))
                var.ui.tablaMensualidades.setItem(index, 2, QTableWidgetItem(str(registro[2]).title()))
                var.ui.tablaMensualidades.setItem(index, 3, QTableWidgetItem(str(registro[3])))

                total += registro[3];var.ui.txtFacSubtotal.setText(str(total) + " €")
                var.ui.txtFacIVA.setText(str(total * 0.1) + " €")
                var.ui.txtFacTotal.setText(str(total * 1.1) + " €")

                # Crear checkbox de pago
                checkbox = QCheckBox()
                checkbox.setChecked(registro[4] == "True")  # Marcar si el valor es "True"

                # Usar partial para pasar el parámetro `id` de forma segura
                def togglePago(checked, id):
                    if checked:
                        print("Suputamadre")
                        Alquileres.pagaMensualidad(id)
                    else:
                        Alquileres.desPagaMensualidad(id)

                # Conectar la señal `stateChanged` y usar `partial` para pasar el id correctamente
                checkbox.stateChanged.connect(partial(togglePago, id=registro[0]))

                container = QWidget()
                layout = QHBoxLayout()
                layout.addWidget(checkbox)
                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                container.setLayout(layout)

                var.ui.tablaMensualidades.setCellWidget(index, 4, container)

            var.ui.txtAlqSubtotal.setText(str(total) + " €")
            var.ui.txtAlqIVA.setText(str(total * 0.1) + " €")
            var.ui.txtAlqTotal.setText(str(round(total * 1.1)) + " €")

        except Exception as e:
            print("Error en cargaTablaMensualidades:", e)

    @staticmethod
    def pagaMensualidad(id):

        try:



            if conexion.Conexion.pagaMensualidad(id):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Factura eliminada')
                mbox.setText('Se ha pagado la mensualidad')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

                Alquileres.cargaTablaMensualidades()



        except Exception as error:
            print('Error al bajar factura: %s' % str(error))

    @staticmethod
    def desPagaMensualidad(id):

        try:
            if conexion.Conexion.desPagaMensualidad(id):
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
                mbox.setWindowTitle('Factura eliminada')
                mbox.setText('Se ha retirado el pago la mensualidad')
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

                Alquileres.cargaTablaMensualidades()

        except Exception as error:
            print('Error al bajar factura: %s' % str(error))

    @staticmethod
    def generaInformeMensualidad():

        print("informemensualidades: -----------------")

        fila = var.ui.tablaMensualidades.selectedItems()
        idFila = fila[0].text()


        print("LA FILA ACTUAL DE LA MENSUALIDAD ES: " + idFila)

        informes.Informes.reportMensualidadActual(idFila)

        print(var.ui.txtAlqSubtotal.text())



