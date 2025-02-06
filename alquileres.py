import calendar
from datetime import datetime


from PyQt6.QtCore import Qt

import conexion

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QTableWidgetItem

import eventos
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
            elif var.ui.txtAlqCodigo.text() == '':
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
                nuevoalquiler = [var.ui.txtAlqCodigo.text(), var.ui.txtDniAlq.text(), var.ui.txtAlqVendedor.text(), var.ui.txtFechaInicioAlq.text(), var.ui.txtFechaFinAlq.text(), var.ui.txtAlqPrecio.text()]
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
                Alquileres.cargaTablaMensualidades()


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

    @staticmethod
    def cargaTablaMensualidades():
        try:
            listado = conexion.Conexion.mensualidadesOneAlquiler()
            var.ui.tablaMensualidades.setRowCount(0)  # Limpia la tabla antes de cargar nuevos datos

            for index, registro in enumerate(listado):
                var.ui.tablaMensualidades.setRowCount(index + 1)
                var.ui.tablaMensualidades.setItem(index, 0, QTableWidgetItem(registro[0]))
                var.ui.tablaMensualidades.setItem(index, 1, QTableWidgetItem(registro[1]))
                var.ui.tablaMensualidades.setItem(index, 2, QTableWidgetItem(registro[2]))
                var.ui.tablaMensualidades.setItem(index, 3, QTableWidgetItem(registro[3]))

                checkbox = QCheckBox()
                checkbox.setChecked(registro[4] == "True")  # Marcar si el valor es "True"

                def togglePago(checked, id=registro[0]):
                    if checked:
                        Alquileres.pagaMensualidad(id)
                    else:
                        Alquileres.despagaMensualidad(id)

                checkbox.stateChanged.connect(
                    lambda state, id=registro[0]: togglePago(state == Qt.CheckState.Checked, id))

                container = QWidget()
                layout = QHBoxLayout()
                layout.addWidget(checkbox)
                layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                container.setLayout(layout)

                var.ui.tablaMensualidades.setCellWidget(index, 4, container)

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

