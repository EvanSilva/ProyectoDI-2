import csv
import json
import locale
import sys
import time
import re
from datetime import datetime
import os
from PyQt6 import QtWidgets, QtGui, QtSql

import clientes
import conexion
import eventos
import propiedades
import var
import zipfile
import shutil

# Establecer configuracion regional.
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Eventos():
    def mensajeSalir(self=None):
        """

        Método para mostrar un mensaje de confirmación al salir de la aplicación.

        :param self:
        :return: None
        :rtype: None

        """
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setWindowIcon(QtGui.QIcon('./img/inmoteis.ico'))
        mbox.setWindowTitle('Salir')
        mbox.setText('¿Desea usted salir?')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Sí')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()

    def cargarProv(self):
        """

        Método para cargar las provincias en los ComboBox

        :param self:
        :return: None
        :rtype: None


        """
        var.ui.cmbProvcli.clear()
        listado = conexion.Conexion.listarProv(self)
        var.ui.cmbProvcli.addItems(listado)

    def cargarMuni(self):
        """

        Método para cargar los municipios en los ComboBox

        :param self:
        :return: None
        :rtype: None

        """
        var.ui.cmbMunicli.clear()
        municipios = conexion.Conexion.listarMunicipios()
        var.ui.cmbMunicli.addItems(municipios)

    # ARREGLAR ESTO

    def cargarProvProp(self):
        """

        Método para cargar las provincias en los ComboBox de propiedades

        :param self:
        :return: None
        :rtype: None


        """
        var.ui.cmbProvprop.clear()
        listado = conexion.Conexion.listarProv(self)
        var.ui.cmbProvprop.addItems(listado)

    def cargarMuniProp(self):
        """

        Método para cargar los municipios en los ComboBox de propiedades

        :param self:
        :return: None
        :rtype: None

        """
        var.ui.cmbMuniprop.clear()
        municipios = conexion.Conexion.listarMunicli(var.ui.cmbProvprop.currentText())
        var.ui.cmbMuniprop.addItems(municipios)

    def cargarProvVendedores(self):
        """

        Método para cargar las provincias en los ComboBox de vendedores

        :param self:
        :return: None
        :rtype: None


        """
        var.ui.cmbProvprop.clear()
        listado = conexion.Conexion.listarProv(self)
        var.ui.cmbProvVendedor.addItems(listado)



    def validarDNI(dni):
        """

        Método para validar un DNI

        :param dni:
        :return: bool
        :rtype: true si el DNI es válido, false en caso contrario

        """
        try:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    return True
                else:
                    return False
            else:
                return False

        except Exception as error:
            print("error en validar dni ", error)

    def abrirCalendar(pan, btn):
        """

        Método para abrir el calendario

        :param btn:


                """
        try:
            var.panel = pan
            var.btn = btn
            var.uicalendar.show()
        except Exception as error:
            print("error en abrir calendar ", error)

    def cargaFecha(qDate):
        """

        Método para cargar la fecha en el campo correspondiente

        :param qDate:
        :return: date
        :rtype: objeto tipo date
        :return: data

        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            if var.panel == 0 and var.btn == 0:
                var.ui.txtAltacli.setText(str(data))
            elif var.panel == 0 and var.btn == 1:
                var.ui.txtBajacli.setText(str(data))
            elif var.panel == 1 and var.btn == 0:
                var.ui.txtAltaprop.setText(str(data))
            elif var.panel == 1 and var.btn == 1:
                var.ui.txtBajaprop.setText(str(data))
            elif var.panel == 3 and var.btn == 0:
                var.ui.txtFechaFac.setText(str(data))


            time.sleep(0.5)
            var.uicalendar.hide()
            return data
        except Exception as error:
            print("error en cargar fecha: ", error)

    def validarMail(mail):
        """

        Método para validar un correo electrónico

        :return: bool
        :rtype: True si el correo es válido, False en caso contrario

        """
        mail = mail.lower()
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, mail):
            return True
        else:
            return False

    def resizeTablaClientes(self):
        """

        Método para redimensionar la tabla de clientes

        :param self:
        :return: None

        """
        try:
            header = var.ui.tablaClientes.horizontalHeader()
            for i in range(header.count()):
                if (i == 1 or i == 2 or i == 4 or i == 5):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                    header_items = var.ui.tablaClientes.horizontalHeaderItem(i)
                    font = header_items.font()
                    font.setBold(True)
                    header_items.setFont(font)
        except Exception as error:
            print("error en resize tabla clientes ", error)

    def resizeTablaVentas(self):
        """

        Método para redimensionar la tabla de ventas

        :param self:
        :return: None

        """
        try:
            header = var.ui.tablaVenta.horizontalHeader()
            for i in range(header.count()):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error en resize tabla clientes ", error)



    def resizeTablaVendedor(self):
        """

        Método para redimensionar la tabla de vendedores

        :param self:
        :return: None

        """
        try:
            header = var.ui.tablaVendedor.horizontalHeader()
            for i in range(header.count()):
                if (i == 1 or i == 2 or i == 4 or i == 5):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                    header_items = var.ui.tablaVendedor.horizontalHeaderItem(i)
                    font = header_items.font()
                    font.setBold(True)
                    header_items.setFont(font)
        except Exception as error:
            print("error en resize tabla clientes ", error)


    def resizeTablaPropiedades(self):
        """

        Método para redimensionar la tabla de propiedades

        :param self:
        :return: None


        """
        try:
            header = var.ui.tablaProp.horizontalHeader()
            for i in range(header.count()):
                if (i == 1 or i == 6 or i == 7 or i == 8):
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                    header_items = var.ui.tablaProp.horizontalHeaderItem(i)
                    font = header_items.font()
                    font.setBold(True)
                    header_items.setFont(font)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                    header_items = var.ui.tablaProp.horizontalHeaderItem(i)
                    font = header_items.font()
                    font.setBold(True)
                    header_items.setFont(font)
        except Exception as error:
            print("error en resize tabla clientes ", error)

    def crearBackup(self):
        """

        Método para crear una copia de seguridad de la base de datos

        :param self:
        :return: None

        """
        try:
            fecha = datetime.now()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = str(fecha) + "_backup.zip"
            directorio, fichero = var.dlgAbrir.getSaveFileName(None, "Guardar Copia Seguridad", copia, '.zip')
            if var.dlgAbrir.accept and fichero:
                fichzip = zipfile.ZipFile(fichero, 'w')
                fichzip.write('bbdd.sqlite', os.path.basename('bbdd.sqlite'), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(fichero, directorio)

                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle("Copia de Seguridad")
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setText("Copia de Seguridad Guardada")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()


        except Exception as error:
            print("error en crear backup: ", error)

    def restaurarBackup(self):
        """

        Método para restaurar una copia de seguridad de la base de datos

        :param self:
        :return: None

        """
        try:
            filename = var.dlgAbrir.getOpenFileName(None, "Restaurar Copia Seguridad", '',
                                                    '*.zip;;All Files(*)')
            file = filename[0]
            if file:
                with zipfile.ZipFile(file, 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle("Copia de Seguridad")
                mbox.setWindowIcon(QtGui.QIcon('./img/icono.ico'))
                mbox.setText("Copia de Seguridad Restaurada")
                mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()


        except Exception as error:
            print("error en crear backup: ", error)

    def limpiarPanel(self):
        """

        Método para limpiar los campos del panel

        :param self:
        :return: None

        """
        if var.ui.panPrincipal.currentIndex() == 0:
            objetosPanel = [
                var.ui.txtDnicli, var.ui.txtAltacli, var.ui.txtApelcli,
                var.ui.txtNomecli, var.ui.txtEmailcli, var.ui.txtMovilcli,
                var.ui.txtDircli, var.ui.cmbProvcli, var.ui.cmbMunicli
            ]

            for i, dato in enumerate(objetosPanel):
                if i == 7 or i == 8:
                    pass  # Se omiten las acciones para `cmbProvcli` y `cmbMunicli`
                else:
                    dato.setText("")  # Limpia el texto en los campos

            # Cargar provincias solo en los ComboBox
            eventos.Eventos.cargarProv(var.ui.cmbProvcli)
            eventos.Eventos.cargarProv(var.ui.cmbMunicli)

        elif var.ui.panPrincipal.currentIndex() == 1:
            objetosPanel = [
                var.ui.txtProp, var.ui.txtAltaprop, var.ui.txtBajaprop,
                var.ui.txtDirprop, var.ui.cmbProvprop, var.ui.cmbMuniprop,
                var.ui.cmbTipoprop, var.ui.spnHabprop, var.ui.spnBanosprop,
                var.ui.txtSuperprop, var.ui.txtPrecioalquilerprop,
                var.ui.txtPrecioventaprop, var.ui.txtCPprop, var.ui.txtObservaprop,
                var.ui.chkAlquiprop, var.ui.chkVentaprop, var.ui.chkInterprop,
                var.ui.rbtDisponprop, var.ui.rbtAlquiprop, var.ui.rbtVentaprop,
                var.ui.txtNomeprop, var.ui.txtMovilprop
            ]

            for casilla in objetosPanel:
                if isinstance(casilla, QtWidgets.QComboBox):
                    casilla.setCurrentText("")
                elif isinstance(casilla, QtWidgets.QCheckBox):
                    casilla.setChecked(False)
                elif isinstance(casilla, QtWidgets.QRadioButton):
                    var.ui.rbtDisponprop.setChecked(True)  # Selecciona este radio botón por defecto
                elif isinstance(casilla, QtWidgets.QSpinBox):
                    casilla.setValue(0)  # Usa 0 como valor por defecto
                elif isinstance(casilla, QtWidgets.QTextEdit):
                    casilla.setPlainText("")  # Limpia el contenido de QTextEdit
                else:
                    casilla.setText("")  # Limpia los QLineEdit

    def validarMovil(telefono):
        """

        Método para validar un número de teléfono

        :param telefono:
        :return: bool
        :rtype: True si el número es válido, False en caso contrario

        """
        regex = r"^[67]\d{8}$"
        if re.match(regex, telefono):
            return True
        else:
            return False

    def checkTxtVacio(string):
        """

        Método para comprobar si un campo de texto está vacío

        :param string:
        :return: bool
        :rtype: True si el campo está vacío, False en caso contrario

        """
        if string == "":
            return True
        else:
            return False

    def abrirTipoprop(self):
        """

        Método para abrir el diálogo de tipos de propiedades

        :param self:
        :return: None

        """
        try:
            var.dlggestion.show()
        except Exception as error:
            print("Error en abrir tipo tipo: ", error)

    def cargarTipoprop(self):
        """

        Método para cargar los tipos de propiedades en el ComboBox

        :param self:
        :return: None

        """
        registro = conexion.Conexion.cargarTipoprop(self)
        var.ui.cmbTipoprop.clear()
        var.ui.cmbTipoprop.addItems(registro)

    def exportCSVProp(self):
        """

        Método para exportar los datos de las propiedades a un archivo CSV

        :param self:
        :return: None

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = (str(fecha) + '_DatosPropiedades.csv')
            directorio, fichero = var.dlgAbrir.getSaveFileName(None, "Exporta Datos en CSV", file, ".csv")
            if fichero:
                registros = conexion.Conexion.listadoPropiedades()
                with open(fichero, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(
                        ["Codigo", "Alta", "Baja", "Dirección", "Provincia", "Municipio", "Tipo", "NºHabitaciones",
                         "NºBaños", "Superficie", "Precio Alquiler", "Precio Compra",
                         "Código Postal", "Observaciones", "Operación", "Estado", "Propietario", "Móvil"])
                    for registro in registros:
                        writer.writerow(registro)
                shutil.move(fichero, directorio)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowTitle("Error")
                mbox.setText("Error Exportación de Datos propiedades.")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

        except Exception as e:
            print("Error al intentar exportar a CSV en Eventos exportCSVProp ", e)

    def exportJSONProp(self):
        """

        Método para exportar los datos de las propiedades a un archivo JSON

        :param self:
        :return: None

        """
        try:
            var.historico = 0
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = (str(fecha) + '_DatosPropiedades.json')
            directorio, fichero = var.dlgAbrir.getSaveFileName(None, "Exporta Datos en JSON", file, ".json")
            if fichero:
                keys = ["Codigo", "Alta", "Baja", "Dirección", "Provincia", "Municipio", "Tipo", "NºHabitaciones",
                        "NºBaños", "Superficie", "Precio Alquiler", "Precio Compra",
                        "Código Postal", "Observaciones", "Operación", "Estado", "Propietario", "Móvil"]
                registros = conexion.Conexion.listadoPropiedades()
                lista_propiedades = [dict(zip(keys, registro)) for registro in registros]
                with open(fichero, 'w', newline='', encoding='utf-8') as jsonfile:
                    json.dump(lista_propiedades, jsonfile, ensure_ascii=False, indent=4)
                shutil.move(fichero, directorio)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowTitle("Error")
                mbox.setText("Error Exportación de Datos propiedades.")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

        except Exception as e:
            print("Error al intentar exportar a CSV en Eventos exportCSVProp ", e)

    def abrirAbout(self):
        """

        Método para abrir el diálogo de Acerca de

        :param self:
        :return: None

        """
        try:
            var.dlgAbout.show()
        except Exception as error:
            print("error en al abrir About ", error)



    def creditsToBua(self):
        """

        Método para mostrar un mensaje de créditos a David Bua

        :param self:
        :return: None


        """
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        mbox.setWindowTitle("BUA TEIJEIRO")
        mbox.setText("IDEA EASTER EGG POR DAVID BUA")
        mbox.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Ok)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
        mbox.exec()



    #############################################  CLIENTES   #############################################

    def retrocederTablaCli(self):
        """

        Método para retroceder la tabla de clientes

        :param self:
        :return: None

        """
        try:
            if var.tablaActualCli <= 1:
                var.tablaActualCli = 1

            else:
                var.tablaActualCli -= 1
                eventos.Eventos.aplicarTablaCli(self)


        except Exception as error:
            print("error en avanzar tabla ", error)

    def avanzarTablaCli(self):
        """

        Método para avanzar la tabla de clientes

        :param self:
        :return: None



        """
        try:

            tablamaxima = eventos.Eventos.calcularTablaMaximaCli(self)

            if var.tablaActualCli >=  tablamaxima:
                var.tablaActualCli = tablamaxima
            else:
                var.tablaActualCli += 1
                eventos.Eventos.aplicarTablaCli(self)

        except Exception as error:
            print("error en avanzar tabla ", error)

    def calcularTablaMaximaCli(self):
        """

        Método para calcular la tabla máxima de clientes

        :param self:
        :return: list[objetos.Cliente]

        """
        try:
            listado = conexion.Conexion.listadoClientes(self)
            total = len(listado)

            tablaMaxima = (total + 4) // 5

            return tablaMaxima
        except Exception as e:
            # Maneja posibles errores durante el cálculo.
            print(f"Error al calcular la tabla máxima: {e}")
            return 0  # Devuelve un valor predeterminado si ocurre un error.
        except Exception as error:
            print("error en calcular tabla maxima ", error)

    def cortaClientes(self):
        """

        Método para cortar la lista de clientes

        :return: list[objetos.Cliente]
        :rtype: list[objetos.Cliente]
        """
        listado = conexion.Conexion.listadoClientes(self)

        x = (var.tablaActualCli * 5)
        y = x - 5
        listadoCortado = listado[y:x]
        return listadoCortado


    def aplicarTablaCli(self):
        """

        Método para aplicar la tabla de clientes

        :param self:
        :return: None

        """
        try:
            print("tabla actual: ", var.tablaActualCli)

            clientes.Clientes.cargaTablaCincoClientes(self, eventos.Eventos.cortaClientes(self))

            var.ui.lblNumPaginaCli.setText(f"Página {var.tablaActualCli}/{eventos.Eventos.calcularTablaMaximaCli(self)}")

            tablamaxima = eventos.Eventos.calcularTablaMaximaCli(self)

            if var.tablaActualCli == tablamaxima:
                var.ui.btnTablaAlante.setDisabled(True)
            else:
                var.ui.btnTablaAlante.setEnabled(True)

            if var.tablaActualCli == 1:
                var.ui.btnTablaAtras.setDisabled(True)
            else:
                var.ui.btnTablaAtras.setEnabled(True)

        except Exception as error:
            print("error en aplicar tabla ", error)

    #############################################  PROPIEDADES  #############################################

    def retrocederTablaProp(self):
        """

        Método para retroceder la tabla de propiedades

        :param self:
        :return: None


        """
        try:
            if var.tablaActualProp <= 1:
                var.tablaActualProp = 1

            else:
                var.tablaActualProp -= 1
                eventos.Eventos.aplicarTablaProp(self)


        except Exception as error:
            print("error en avanzar tabla ", error)

    def avanzarTablaProp(self):
        """

        Método para avanzar la tabla de propiedades

        :param self:
        :return: None


        """
        try:

            tablaMaximaProp = eventos.Eventos.calcularTablaMaximaProp(self)

            if var.tablaActualProp >=  tablaMaximaProp:
                var.tablaActualProp = tablaMaximaProp
            else:
                var.tablaActualProp += 1
                eventos.Eventos.aplicarTablaProp(self)

        except Exception as error:
            print("error en avanzar tabla ", error)

    def calcularTablaMaximaProp(self):
        """

        Método para calcular la tabla máxima de propiedades

        :param self:
        :return: int
        :rtype: int


        """
        try:
            listadoProp = conexion.Conexion.listadoPropiedades()
            total = len(listadoProp)

            tablaMaximaProp = (total + 1) // 2

            return tablaMaximaProp
        except Exception as e:
            print(f"Error al calcular la tabla máxima: {e}")
            return 0
        except Exception as error:
            print("error en calcular tabla maxima ", error)

    def cortaPropiedades(self):
        """

        Método para cortar la lista de propiedades

        :return: list[objetos.Propiedad]
        :rtype: list[objetos.Propiedad]


        """
        listadoProp = conexion.Conexion.listadoPropiedades()

        x = (var.tablaActualProp * 2)
        y = x - 2
        listadoCortadoProp = listadoProp[y:x]
        return listadoCortadoProp

    def aplicarTablaProp(self):
        """

        Método para aplicar la tabla de propiedades

        :param self:
        :return: None


        """
        try:
            propiedades.Propiedades.cargaDosPropiedades(self, eventos.Eventos.cortaPropiedades(self))

            var.ui.lblNumPaginaProp.setText(f"Página {var.tablaActualProp}/{eventos.Eventos.calcularTablaMaximaProp(self)}")

            tablaMaximaProp = eventos.Eventos.calcularTablaMaximaProp(self)

            if var.tablaActualProp == tablaMaximaProp:
                var.ui.btnAlanteProp.setDisabled(True)
            else:
                var.ui.btnAlanteProp.setEnabled(True)

            if var.tablaActualProp == 1:
                var.ui.btnAtrasProp.setDisabled(True)
            else:
                var.ui.btnAtrasProp.setEnabled(True)

        except Exception as error:
            print("error en aplicar tabla ", error)

    def comprobarFechaBaja(self):
        """

        Método para comprobar si la fecha de baja es anterior a la fecha actual

        :return: bool
        :rtype: True si la fecha de baja es anterior a la fecha actual, False en caso contrario


        """

        try:

            fechaActual = datetime.now()
            fechaBaja = var.ui.txtBajaprop.text()
            fechaBaja = datetime.strptime(fechaBaja, '%d/%m/%Y')

            if fechaActual < fechaBaja:
                return True
            else:
                return False

        except Exception as error:
            print("La fecha de baja es ", error)

    #############################################  PRUEBAS  #############################################

    def abrirPrueba(self):
        """

        Método para abrir el diálogo de Prueba

        :param self:
        :return: None


        """
        try:
            var.dlgPrueba.show()
        except Exception as error:
            print("error en al abrir Prueba ", error)

    def exportJSONVendedor(self):
        """

        Método para exportar los datos de los vendedores a un archivo JSON

        :param self:
        :return: None


        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = (str(fecha) + '_DatosVendedores.json')
            directorio, fichero = var.dlgAbrir.getSaveFileName(None, "Exporta Datos en JSON", file, ".json")
            if fichero:
                keys = ["ID", "DNI", "Nombre", "Alta", "Baja", "Movil", "Mail", "Delegacion"]
                registros = conexion.Conexion.listadoVendedores(self)
                lista_propiedades = [dict(zip(keys, registro)) for registro in registros]
                with open(fichero, 'w', newline='', encoding='utf-8') as jsonfile:
                    json.dump(lista_propiedades, jsonfile, ensure_ascii=False, indent=4)
                shutil.move(fichero, directorio)
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowTitle("Exportacion Exitosa")
                mbox.setText("Datos exportados adecuadamente")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setWindowTitle("Error")
                mbox.setText("Error Exportación de Datos propiedades.")
                mbox.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                mbox.exec()

        except Exception as e:
            print("Error al intentar exportar a CSV en Eventos exportCSVProp ", e)

    #############################################  INFORMES  #############################################

    def abrirInformeProp(self):
        """

        Método para abrir el diálogo de Informe de Propiedades

        :param self:
        :return: None

        """
        try:
            var.dlgInformeProp.show()
        except Exception as error:
            print("error en al abrir informeprop ", error)



