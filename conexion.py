import os
import sqlite3
from csv import excel
from datetime import datetime
from http.cookiejar import strip_quotes
from idlelib import query

from PyQt6 import QtSql, QtWidgets, QtCore

import var


class Conexion:
    '''

    GESTION CLIENTES
    método de una clase que no depende de una instancia específica de esa clase.
    Se puede llamarlo directamente a través de la clase, sin necesidad de crear un objeto de esa clase.
    Es útil en comportamientos o funcionalidades que son más a una clase en general que a una instancia en particular.

    '''

    @staticmethod
    def db_conexion(self):
        """

        :param self: None
        :type self: None
        :return: False/True
        :rtype: bool

        Módulo que realiza la conexión con la base de datos SQLite.
        Si exito devuelve True, si no False.

        """
        # Verifica si el archivo de base de datos existe
        if not os.path.isfile('bbdd.sqlite'):
            QtWidgets.QMessageBox.critical(None, 'Error', 'El archivo de la base de datos no existe.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        # Crear la conexión con la base de datos SQLite
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')

        if db.open():
            # Verificar si la base de datos contiene tablas
            query = QtSql.QSqlQuery()
            query.exec("SELECT name FROM sqlite_master WHERE type='table';")

            if not query.next():  # Si no hay tablas
                QtWidgets.QMessageBox.critical(None, 'Error', 'Base de datos vacía o no válida.',
                                               QtWidgets.QMessageBox.StandardButton.Cancel)
                return False
            else:
                QtWidgets.QMessageBox.information(None, 'Aviso', 'Conexión Base de Datos realizada',
                                                  QtWidgets.QMessageBox.StandardButton.Ok)
                return True
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'No se pudo abrir la base de datos.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

    def listarProv(self):
        """
        :param self: None
        :type self: None
        :return: lista de provincias
        :rtype: list

        Método que devuelve una lista con las provincias almacenadas en la base de datos.

        """
        listarProv = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM provincias")
        if query.exec():
            while query.next():
                listarProv.append(query.value(1))
        return listarProv

    def listarMunicli(provincia):
        """
        :param provincia: nombre de la provincia
        :type provincia: str
        :return: lista de municipios
        :rtype: list

        Método que devuelve una lista con los municipios de una provincia almacenados en la base de datos.

        """
        listamunicipios = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM municipios where idprov = (select idprov from provincias where provincia = :provincia)")
        query.bindValue(":provincia", provincia)
        if query.exec():
            while query.next():
                listamunicipios.append(query.value(1))
        return listamunicipios


    def listarMunicipios():
        """
        :param provincia: none
        :type provincia: none
        :return: lista de municipios
        :rtype: list

        Método que devuelve una lista con los municipios de una provincia almacenados en la base de datos.

        """
        listamunicipios = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT municipio FROM municipios")
        if query.exec():
            while query.next():
                listamunicipios.append(query.value(0))
        return listamunicipios


    def altaCliente(nuevocli):
        """
        :param nuevocli: lista con los datos del nuevo cliente
        :type nuevocli: list
        :return: True/False
        :rtype: bool

        Método que inserta un nuevo cliente en la base de datos.

        """
        try:

            query = QtSql.QSqlQuery()
            query.prepare( "INSERT INTO clientes ( dnicli, altacli, apelcli, nomecli, emailcli, movilcli, dircli, provcli, municli ) VALUES ( :dnicli, :altacli, :apelcli, :nomecli, :emailcli, :movilcli, :dircli, :provcli, :municli ) " )
            query.bindValue(":dnicli", str(nuevocli[0]))
            query.bindValue(":altacli",  str(nuevocli[1]))
            query.bindValue(":apelcli",  str(nuevocli[2]))
            query.bindValue(":nomecli",  str(nuevocli[3]))
            query.bindValue(":emailcli",  str(nuevocli[4]))
            query.bindValue(":movilcli",  str(nuevocli[5]))
            query.bindValue(":dircli",  str(nuevocli[6]))
            query.bindValue(":provcli",  str(nuevocli[7]))
            query.bindValue(":municli",  str(nuevocli[8]))

            if query.exec():
                return True
            else:
                return False
        except sqlite3.IntegrityError:
                return False

    def listadoClientes(self):
        """
        :param self: None
        :type self: None
        :return: listado de clientes
        :rtype: list

        Método que devuelve un listado con los clientes almacenados en la base de datos.

        """
        try:
            listado = []
            if var.historico == 1:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM CLIENTES where bajacli is NULL ORDER BY apelcli, nomecli ASC")
                query.bindValue(":dato", QtCore.QVariant())
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range (query.record().count())]
                        listado.append(fila)
                return listado
            elif var.historico == 0:
                query = QtSql.QSqlQuery()
                query.prepare("SELECT * FROM CLIENTES ORDER BY apelcli, nomecli ASC")
                query.bindValue(":dato", QtCore.QVariant())
                if query.exec():
                    while query.next():
                        fila = [query.value(i) for i in range(query.record().count())]
                        listado.append(fila)
                return listado

            return listado

        except Exception as e:
            print("Error Listado en Conexion", e)

    def datosOneCliente(dni):
        """
        :param dni: dni del cliente
        :type dni: str
        :return: datos del cliente
        :rtype: list

        Método que devuelve los datos de un cliente en concreto.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM CLIENTES WHERE dnicli = :dni")
            query.bindValue(":dni", str(dni))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(query.value(i))
            return registro

        except Exception as e:
            print("Error datos un Cliente", e)

    def modifCliente(registro):
        """
        :param registro: datos del cliente a modificar
        :type registro: list
        :return: True/False
        :rtype: bool

        Método que modifica los datos de un cliente en concreto.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from clientes where dnicli = :dni")
            query.bindValue(":dni", str(registro[0]))
            if query.exec():
                if query.next() and query.value(0) > 0:
                    if query.exec():
                        query = QtSql.QSqlQuery()
                        query.prepare("UPDATE clientes set altacli = :altacli, apelcli = :apelcli, nomecli = :nomecli, "
                                      " emailcli = :emailcli, movilcli = :movilcli, dircli = :dircli, provcli = :provcli, "
                                      " municli = :municli, bajacli = :bajacli where dnicli = :dni")
                        query.bindValue(":dni", str(registro[0]))
                        query.bindValue(":altacli", str(registro[1]))
                        query.bindValue(":apelcli", str(registro[2]))
                        query.bindValue(":nomecli", str(registro[3]))
                        query.bindValue(":emailcli", str(registro[4]))
                        query.bindValue(":movilcli", str(registro[5]))
                        query.bindValue(":dircli", str(registro[6]))
                        query.bindValue(":provcli", str(registro[7]))
                        query.bindValue(":municli", str(registro[8]))
                        if registro[9] == "":
                            query.bindValue(":bajacli", QtCore.QVariant())
                        else:
                            query.bindValue(":bajacli", str(registro[9]))
                        if query.exec():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except Exception as error:
            print("error modificar cliente", error)

    def bajaCliente(datos):
        """
        :param datos: dni del cliente
        :type datos: str
        :return: True/False
        :rtype: bool

        Método que da de baja a un cliente en concreto.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE clientes SET bajacli = :bajacli WHERE DNICLI = :dni")
            query.bindValue(":bajacli", datetime.now().strftime("%d/%m/%Y"))
            query.bindValue(":dni", str(datos[1]))
            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error bajaCliente", e)


    '''

    GESTION CLIENTES

    '''

    def altaTipoprop(tipo):
        """
        :param tipo: tipo de propiedad
        :type tipo: str
        :return: registro
        :rtype: list

        Método que inserta un nuevo tipo de propiedad en la base de datos.

        """
        try:
            # Verificar si el tipo ya existe antes de intentar insertarlo
            check_query = QtSql.QSqlQuery()
            check_query.prepare("SELECT COUNT(*) FROM tipopropiedad WHERE tipo = :tipo")
            check_query.bindValue(":tipo", str(tipo))
            if check_query.exec() and check_query.next() and check_query.value(0) > 0:
                return False  # Tipo ya existe, no se puede insertar

            # Proceder a insertar el nuevo tipo de propiedad
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO tipopropiedad (tipo) VALUES (:tipo)")
            query.bindValue(":tipo", str(tipo))
            if query.exec():
                # Obtener todos los tipos de propiedad después de la inserción
                query = QtSql.QSqlQuery()
                query.prepare("SELECT tipo FROM tipopropiedad")
                if query.exec():
                    registro = []
                    while query.next():
                        registro.append(str(query.value(0)))
                    return registro
            else:
                return False  # Inserción fallida
        except Exception as e:
            print("Error en altaTipoprop:", e)
            return False  # Retornar False si ocurre un error

    def cargarTipoprop(self):
        """
        :param self: None
        :type self: None
        :return: registro
        :rtype: list

        Método que carga los tipos de propiedad almacenados en la base de datos.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare( "select * from tipopropiedad ASC" )
            if query.exec():
                while query.next():
                    registro.append(str(query.value(0)))
                return registro
        except Exception as e:
            print("Error cargarTipoprop", e)

    def bajaTipoprop(tipo):
        """
        :param tipo: tipo de propiedad
        :type tipo: str
        :return: True/False
        :rtype: bool

        Método que da de baja un tipo de propiedad en concreto.

        """
        try:
            # Verifica si el tipo existe antes de intentar eliminarlo
            check_query = QtSql.QSqlQuery()
            check_query.prepare("SELECT COUNT(*) FROM tipopropiedad WHERE tipo = :tipo")
            check_query.bindValue(":tipo", str(tipo))
            check_query.exec()
            check_query.next()
            if check_query.value(0) == 0:
                print(f"El tipo {tipo} no existe.")
                return False
            else:

                query = QtSql.QSqlQuery()
                query.prepare("DELETE FROM tipopropiedad WHERE tipo = :tipo")
                query.bindValue(":tipo", str(tipo))

                if query.exec() and query.numRowsAffected() == 1:
                    print(f"Eliminación exitosa del tipo: {tipo}")
                    return True

                else:
                    print("Error en query:", query.lastError().text())
                    return False

        except Exception as e:
            print("Error en bajaTipoprop:", e)
            return False

    def altaPropiedad(propiedades):
        """

        :param propiedades: lista con los datos de la propiedad
        :type propiedades: list
        :return: True/False
        :rtype: bool

        Método que inserta una nueva propiedad en la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                "INSERT INTO propiedades ( altaprop, dirprop, provprop, muniprop, tipoprop, habprop, banprop, superprop, prealquiprop, prevenprop, cpprop, obserprop, tipooper, estadoprop, nomeprop, movilprop ) VALUES ( :altaprop, :dirprop, :provprop, :muniprop, :tipoprop, :habprop, :banprop, :superprop, :prealquiprop, :prevenprop, :cpprop, :obserprop, :tipooper, :estadoprop, :nomeprop, :movilprop ) ")

            query.bindValue(":altaprop", str(propiedades[0]))
            query.bindValue(":dirprop", str(propiedades[1]))
            query.bindValue(":provprop", str(propiedades[2]))
            query.bindValue(":muniprop", str(propiedades[3]))
            query.bindValue(":tipoprop", str(propiedades[4]))
            query.bindValue(":habprop", int(propiedades[5]))
            query.bindValue(":banprop", int(propiedades[6]))
            query.bindValue(":superprop", str(propiedades[7]))
            query.bindValue(":prealquiprop", str(propiedades[8]))
            query.bindValue(":prevenprop", str(propiedades[9]))
            query.bindValue(":cpprop", str(propiedades[10]))
            query.bindValue(":obserprop", str(propiedades[11]))
            query.bindValue(":tipooper", str(propiedades[12]))
            query.bindValue(":estadoprop", str(propiedades[13]))
            query.bindValue(":nomeprop", str(propiedades[14]))
            query.bindValue(":movilprop", str(propiedades[15]))

            if query.exec():
                return True

        except Exception as e:
            print("Error en altaPropiedad:", e)
            return False


    # Menos mal que Yelko es un máquina, el resto de '''mi codigo''' tiene mas deuda tecnica que Venezuela. Llamen a Javier Milei.

    def listadoPropiedades():
        """

        :return: listado
        :rtype: list

        Método que devuelve un listado con las propiedades almacenadas en la base de datos.

        """
        try:
            listado = []
            historico = var.ui.chkHistoricoprop.isChecked()
            municipio = var.ui.cmbMuniprop.currentText()
            filtrado = var.ui.btnBuscaTipoProp.isChecked()
            tipoSeleccionado = var.ui.cmbTipoprop.currentText()

            # Construir la base de la consulta
            base_query = "SELECT * FROM propiedades WHERE 1=1"

            # Condiciones para el filtro de historico
            if historico:
                base_query = base_query + " ORDER BY muniprop ASC"

            # Condiciones adicionales para filtro por bajaprop y disponibilidad
            if not historico:
                base_query = base_query + " AND bajaprop IS NULL AND estadoprop IN ('Disponible', 'Alquilado', 'Vendido') "

            # Filtrar por tipo de propiedad y municipio si está activado el filtro
            if filtrado:
                base_query += " AND tipoprop = :tipo_propiedad AND muniprop = :municipio"

            query = QtSql.QSqlQuery()
            query.prepare(base_query)

            # Vincular parámetros de la consulta si se necesitan
            if filtrado:
                query.bindValue(":tipo_propiedad", str(tipoSeleccionado))
                query.bindValue(":municipio", str(municipio))

            # Ejecutar la consulta
            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range(query.record().count())]
                    listado.append(fila)

            return listado

        except Exception as e:
            print("Error al listar propiedades en listadoPropiedades:", e)
            return []


        except Exception as e:
            print("Error al listar propiedades en listadoPropiedades:", e)
            return []

    def modifPropiedad(registro):
        """
        :param registro: datos de la propiedad a modificar
        :type registro: list
        :return: True/False
        :rtype: bool

        Método que modifica los datos de una propiedad en concreto.

        """
        try:

            print("Tamaño de la lista propiedades:", len(registro))
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from propiedades where codigo = :codigo")
            query.bindValue(":codigo", str(registro[0]))
            if query.exec():
                if query.next() and query.value(0) > 0:
                    if query.exec():
                        query = QtSql.QSqlQuery()
                        query.prepare(
                            "UPDATE propiedades SET altaprop = :altaprop, bajaprop = :bajaprop, dirprop = :dirprop, provprop = :provprop, muniprop = :muniprop, tipoprop = :tipoprop, habprop = :habprop, banprop = :banprop, superprop = :superprop, prealquiprop = :prealquiprop, prevenprop = :prevenprop, cpprop = :cpprop, obserprop = :obserprop, tipooper = :tipooper, estadoprop = :estadoprop, nomeprop = :nomeprop, movilprop = :movilprop WHERE CODIGO = :codigo")

                        # Asignación de parámetros
                        query.bindValue(":codigo", str(registro[0]))
                        query.bindValue(":altaprop", str(registro[1]))
                        query.bindValue(":dirprop", str(registro[3]))
                        query.bindValue(":provprop", str(registro[4]))
                        query.bindValue(":muniprop", str(registro[5]))
                        query.bindValue(":tipoprop", str(registro[6]))
                        query.bindValue(":habprop", int(registro[7]))
                        query.bindValue(":banprop", int(registro[8]))
                        query.bindValue(":superprop", str(registro[9]))
                        query.bindValue(":prealquiprop", str(registro[10]))
                        query.bindValue(":prevenprop", str(registro[11]))
                        query.bindValue(":cpprop", str(registro[12]))
                        query.bindValue(":obserprop", str(registro[13]))
                        query.bindValue(":tipooper", str(registro[14]))
                        query.bindValue(":estadoprop", str(registro[15]))
                        query.bindValue(":nomeprop", str(registro[16]))
                        query.bindValue(":movilprop", (registro[17]))

                        if registro[2] == "":
                            query.bindValue(":bajaprop", QtCore.QVariant())
                        else:
                            query.bindValue(":bajaprop", str(registro[2]))
                        if query.exec():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except Exception as error:
            print("error modificar propiedad (Conexion)", error)


    def datosOnePropiedad(codigo):
        """
        :param codigo: código de la propiedad
        :type codigo: str
        :return: registro
        :rtype: list

        Método que devuelve los datos de una propiedad en concreto.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM PROPIEDADES WHERE codigo = :codigo")
            query.bindValue(":codigo", str(codigo))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(query.value(i))
            return registro

        except Exception as e:
            print("Error datos un Cliente", e)

    def bajaPropiedad(datos):
        """
        :param datos: código de la propiedad
        :type datos: str
        :return: True/False
        :rtype: bool

        Método que da de baja una propiedad en concreto.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE propiedades SET bajaprop = :bajaprop WHERE codigo = :codigo")
            query.bindValue(":bajaprop", datetime.now().strftime("%d/%m/%Y"))
            query.bindValue(":codigo", int(datos[1]))
            return query.exec()

        except Exception as e:
            print("Error bajaCliente", e)


            ########################### VENDEDORES ###########################

    def altaVendedor(nuevoVendedor):
        """
        :param nuevoVendedor: datos del nuevo vendedor
        :type nuevoVendedor: list
        :return: True/False
        :rtype: bool

        Método que inserta un nuevo vendedor en la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            registro = query.prepare( "INSERT INTO vendedores ( dniVendedor, nombreVendedor, altaVendedor, bajaVendedor, movilVendedor, mailVendedor, delegacionVendedor ) VALUES ( :dniVendedor, :nombreVendedor, :altaVendedor, :bajaVendedor, :movilVendedor, :mailVendedor, :delegacionVendedor ) " )

            query.bindValue(":dniVendedor",  str(nuevoVendedor[0]))
            query.bindValue(":nombreVendedor",  str(nuevoVendedor[1]))
            query.bindValue(":altaVendedor",  str(nuevoVendedor[2]))
            query.bindValue(":bajaVendedor",  str(nuevoVendedor[3]))
            query.bindValue(":movilVendedor",  str(nuevoVendedor[4]))
            query.bindValue(":mailVendedor",  str(nuevoVendedor[5]))
            query.bindValue(":delegacionVendedor",  str(nuevoVendedor[6]))

            if query.exec():
                return True
            else:
                return False

        except sqlite3.IntegrityError:
                return False

    def listadoVendedores(self):
        """
        :param self: None
        :type self: None
        :return: listado
        :rtype: list

        Método que devuelve un listado con los vendedores almacenados en la base de datos.
        """
        try:
            listado = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM vendedores ORDER BY idVendedor ASC")
            query.bindValue(":dato", QtCore.QVariant())
            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range (query.record().count())]
                    listado.append(fila)
            return listado

        except Exception as e:
            print("Error Listado en Conexion", e)

    def datosOneVendedor(id):
        """

        :param id: id del vendedor
        :type id: str
        :return: registro
        :rtype: list

        Método que devuelve los datos de un vendedor en concreto.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM vendedores WHERE idVendedor = :idVendedor")
            query.bindValue(":idVendedor", id)
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(query.value(i))
            return registro

        except Exception as e:
            print("Error datos un Cliente", e)

    def modifVendedor(registro):
        """
        :param registro: datos del vendedor a modificar
        :type registro: list
        :return: True/False
        :rtype: bool

        Método que modifica los datos de un vendedor en concreto.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from vendedores where idVendedor = :id")
            query.bindValue(":id", str(registro[0]))

            if query.exec():
                if query.next() and query.value(0) > 0:
                    if query.exec():
                        query = QtSql.QSqlQuery()
                        query.prepare("UPDATE vendedores set nombreVendedor = :nombreVendedor, "
                                      " altaVendedor = :altaVendedor, bajaVendedor = :bajaVendedor, movilVendedor = :movilVendedor, mailVendedor = :mailVendedor, "
                                      "delegacionVendedor  = :delegacionVendedor where idVendedor = :idVendedor")
                        query.bindValue(":idVendedor", str(registro[0]))
                        query.bindValue(":dniVendedor", str(registro[1]))
                        query.bindValue(":nombreVendedor", str(registro[2]))
                        query.bindValue(":altaVendedor", str(registro[3]))
                        query.bindValue(":bajaVendedor", str(registro[4]))
                        query.bindValue(":movilVendedor", str(registro[5]))
                        query.bindValue(":mailVendedor", str(registro[6]))
                        query.bindValue(":delegacionVendedor", str(registro[7]))

                        if query.exec():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except Exception as error:
            print("error modificar cliente", error)


    def bajaVendedor(datos):
        """
        :param datos: id del vendedor
        :type datos: str
        :return: True/False
        :rtype: bool

        Método que da de baja a un vendedor en concreto.

        """
        try:


            query = QtSql.QSqlQuery()
            query.prepare("UPDATE vendedores SET bajaVendedor = :bajaVendedor WHERE idVendedor = :idVendedor")
            query.bindValue(":bajaVendedor", "hoy")
            query.bindValue(":idVendedor", int(datos))
            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error bajaVendedor", e)

    def altafactura(nuevafactura):
        """

        Método que inserta una nueva factura en la base de datos.

        :param nuevafactura: datos de la nueva factura
        :return: True/False
        :rtype: bool


        """
        try:
            query = QtSql.QSqlQuery()

            query.prepare('INSERT INTO facturas (fechafac, dnifac) VALUES (:fecha, :dni)')


            query.bindValue(':fecha', nuevafactura[0])
            query.bindValue(':dni', nuevafactura[1])


            if query.exec():
                return True
            else:
                return False

        except Exception as error:
            print('Error al insertar factura2: %s' % str(error))

    @staticmethod
    def cargarFacturas():
        """
        Método que carga los registros de la tabla facturas desde la base de datos.

        :return: Lista de registros de facturas, cada uno con id, fechafac y dnifac.
        :rtype: list
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM facturas")

            if query.exec():
                while query.next():
                    # Agrega los valores de todas las columnas en una lista
                    fila = [str(query.value(0)),  # id
                            str(query.value(1)),  # fechafac
                            str(query.value(2))]  # dnifac
                    registro.append(fila)
                return registro
            else:
                print("Error al ejecutar la consulta:", query.lastError().text())
                return []

        except Exception as e:
            print("Error en cargarFacturas:", e)
            return []

    def datosOneFactura(id):
        """

        Método que devuelve los datos de una factura en concreto.

        :return: registro
        :param id: id de la factura
        :type id: str
        :rtype: list
        """

        try:

            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM facturas WHERE id = :id")
            query.bindValue(":id", str(id))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(query.value(i))
            return registro

        except Exception as e:
            print("Error datos una factura", e)

    def bajaFactura(id):

        """

        Método que da de baja una factura en concreto.

        :return: True/False
        :param id: id de la factura
        :type id: str
        :rtype: bool
        """

        try:



            query = QtSql.QSqlQuery()
            query.prepare("delete from facturas where id = :id")
            query.bindValue(":id", id)
            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error bajaVendedor", e)

    def altaVenta(nuevaventa):
        try:
            query = QtSql.QSqlQuery()

            query.prepare('INSERT INTO ventas (facventa, codprop, agente) VALUES (:facventa, :codprop, :agente)')

            query.bindValue(':facventa', nuevaventa[0])
            query.bindValue(':codprop', nuevaventa[1])
            query.bindValue(':agente', nuevaventa[2])

            if query.exec():
                return True
            else:
                return False

        except Exception as error:
            print('Error al insertar factura2: %s' % str(error))

    #ARREGLAR

    @staticmethod
    def cargarVentas(facventa):
        """

        Método que carga los registros de la tabla ventas desde la base de datos.

        :param facventa: ID de la factura
        :return: Lista de registros de ventas, cada uno con idventa, facventa, muniprop, tipoprop, dirprop y prevenprop.
        :rtype: list


        """
        try:

            registro = []
            query = QtSql.QSqlQuery()

            query.prepare("""
                SELECT    v.idventa AS "ID Venta",
                          v.facventa AS "ID Factura",
                          p.muniprop AS "Localidad",
                          p.tipoprop AS "Tipo propiedad",
                          p.dirprop AS "Dirección de la propiedad",
                          p.prevenprop AS "Precio de venta"
                FROM ventas AS v
                INNER JOIN propiedades AS p
                ON v.codprop = p.codigo
                WHERE v.facventa = :facventa;
            """)

            query.bindValue(":facventa", facventa)

            if query.exec():
                while query.next():
                    # Usar una lista para cada fila
                    fila = [
                        str(query.value(0)),  # ID Venta
                        str(query.value(1)),  # ID Factura
                        str(query.value(2)),  # Localidad
                        str(query.value(3)),  # Tipo propiedad
                        str(query.value(4)),  # Dirección de la propiedad
                        str(query.value(5)),  # Precio de venta
                    ]
                    registro.append(fila)  # Agregar la lista de valores a la lista principal

                return registro

            else:
                print(f"Error en la consulta SQL: {query.lastError().text()}")
                return []

        except Exception as e:
            print("Error en cargarVentas:", str(e))
            return []

    def bajaVenta(id):

        """

        Método que da de baja una factura en concreto.

        :return: True/False
        :param id: id de la factura
        :type id: str
        :rtype: bool
        """

        try:



            query = QtSql.QSqlQuery()
            query.prepare("delete from ventas where idventa = :id")
            query.bindValue(":id", id)
            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error bajaVendedor", e)

    from PyQt6 import QtSql
    from datetime import datetime

    def altaAlquiler(nuevoAlquiler):
        try:
            query = QtSql.QSqlQuery()

            query.prepare(
                'INSERT INTO alquileres (Propiedad_ID, Cliente_DNI, Agente_ID, Fecha_Inicio, Fecha_fin, Precio_Alquiler) '
                'VALUES (:Propiedad_ID, :Cliente_DNI, :Agente_ID, :Fecha_Inicio, :Fecha_fin, :Precio_Alquiler)')

            # Convertir los valores a sus tipos correctos
            query.bindValue(':Propiedad_ID', int(nuevoAlquiler[0]))
            query.bindValue(':Cliente_DNI', nuevoAlquiler[1])
            query.bindValue(':Agente_ID', int(nuevoAlquiler[2]))

            # Convertir fechas al formato correcto
            fecha_inicio = datetime.strptime(nuevoAlquiler[3], "%d/%m/%Y").strftime("%Y-%m-%d")
            fecha_fin = datetime.strptime(nuevoAlquiler[4], "%d/%m/%Y").strftime("%Y-%m-%d")

            query.bindValue(':Fecha_Inicio', fecha_inicio)
            query.bindValue(':Fecha_fin', fecha_fin)
            query.bindValue(':Precio_Alquiler', float(nuevoAlquiler[5]))

            if query.exec():
                return True
            else:
                print(f'Error en la ejecución de la consulta : {query.lastError().text()}')
                return False

        except Exception as error:
            print(f'Error al insertar factura: {error}')
            return False

    def findLastAlquilerID():
        """
        Método que busca el último ID de alquiler en la base de datos.

        :return: Último ID de alquiler
        :rtype: int
        """
        try:
            query = QtSql.QSqlQuery(QtSql.QSqlDatabase.database())

            if  query.exec("SELECT id FROM alquileres order by id Desc limit 1"):
                if query.next():
                    return query.value(0)
                else:
                    print("No se encontraron registros en la tabla alquileres.")
            else:
                print("Error al ejecutar la consulta:", query.lastError().text())

            return 0  # Si no hay registros en la tabla, devolver 0

        except Exception as e:
            print("Error en findLastAlquilerID:", e)
            return 0

    @staticmethod
    def cargaAlquileres():

        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM alquileres")

            if query.exec():
                while query.next():
                    fila = [str(query.value(0)),
                            str(query.value(1)),
                            str(query.value(2)),
                            str(query.value(3)),
                            str(query.value(4)),
                            str(query.value(5)),
                            str(query.value(6))]

                    registro.append(fila)

                return registro
            else:
                print("Error al ejecutar la consulta:", query.lastError().text())
                return []

        except Exception as e:
            print("Error en cargarFacturas:", e)
            return []

    def bajaAlquiler(id):

        """

        Método que da de baja una factura en concreto.

        :return: True/False
        :param id: id de la factura
        :type id: str
        :rtype: bool
        """

        try:
            query = QtSql.QSqlQuery()
            query.prepare("delete from alquileres where id = :id")
            query.bindValue(":id", id)
            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error bajaVendedor", e)

    @staticmethod
    def bajaMensualidades(idAlquiler):

        try:
            query = QtSql.QSqlQuery()
            query.prepare("delete from mensualidades where AlquilerAsociado = :idAlquiler")
            query.bindValue(":idAlquiler", idAlquiler)
            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error bajaVendedor", e)






    def altaMensualidades(nuevoAlquiler):
        try:
            query = QtSql.QSqlQuery()

            query.prepare(
                'INSERT INTO mensualidades (AlquilerAsociado, Mes, Precio, Abono) '
                'VALUES (:AlquilerAsociado, :Mes, :Precio, :Abono)')

            query.bindValue(':AlquilerAsociado', int(nuevoAlquiler[0]))
            query.bindValue(':Mes', str(nuevoAlquiler[1]))
            query.bindValue(':Precio', int(float(nuevoAlquiler[2])))  # Convierte a float primero y luego a int
            query.bindValue(':Abono', nuevoAlquiler[3])  # Asegúrate de pasar el valor correcto, ya sea "False" o "True"

            if query.exec():
                return True
            else:
                print(f'Error en la ejecución de la consulta altaMensualidades: {query.lastError().text()}')
                return False
        except Exception as e:
            print("Error en altaMensualidades:", e)

    @staticmethod
    def cargaMensualidades():
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM mensualidades")

            if query.exec():
                while query.next():
                    fila = [str(query.value(0)),
                            str(query.value(1)),
                            str(query.value(2)),
                            str(query.value(3)),
                            str(query.value(4))]
                    registro.append(fila)
                return registro
            else:
                print("Error al ejecutar la consulta:", query.lastError().text())
                return []

        except Exception as e:
            print("Error en cargarFacturas:", e)
            return []

    @staticmethod
    def pagaMensualidad(id):


        try:
            # Crear el query de actualización
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE mensualidades SET abono = 'True' WHERE id = :id")
            query.bindValue(":id", id)

            # Ejecutar la consulta
            if query.exec():
                print(f"Abono actualizado correctamente para la mensualidad con ID {id}")
            else:
                print("Error al actualizar el abono:", query.lastError().text())
        except Exception as e:
            print(f"Se produjo un error: {e}")

    @staticmethod
    def desPagaMensualidad(id):
        try:
            # Crear el query de actualización
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE mensualidades SET abono = 'False' WHERE id = :id")
            query.bindValue(":id", id)

            # Ejecutar la consulta
            if query.exec():
                print(f"Abono actualizado correctamente para la mensualidad con ID {id}")
            else:
                print("Error al actualizar el abono:", query.lastError().text())
        except Exception as e:
            print(f"Se produjo un error: {e}")

    @staticmethod
    def mensualidadesOneAlquiler(id):
        try:
            listado = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM mensualidades WHERE AlquilerAsociado = :id")
            query.bindValue(":id", str(id))
            if query.exec():
                while query.next():
                    fila = []
                    for i in range(query.record().count()):
                        fila.append(query.value(i))  # Guarda los valores en una lista separada
                    listado.append(fila)  # Agrega la fila completa a la lista
            return listado  # Devuelve una lista de listas

        except Exception as e:
            print("Error datos un Cliente", e)

    def datosOneAlquiler(id):
        """

        Método que devuelve los datos de un alquiler en concreto.

        :return: registro
        :param id: id de la factura
        :type id: str
        :rtype: list
        """

        try:

            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM facturas WHERE id = :id")
            query.bindValue(":id", str(id))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(query.value(i))
            return registro

        except Exception as e:
            print("Error datos una factura", e)

    @staticmethod
    def bbddModificarPropiedadVendida(idPropiedad):

        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE propiedades SET estadoprop = :estadoprop, prealquiprop = :prealquiprop WHERE codigo = :codigo")

            print(" LLEGO A bbddModificarPropiedadVendida ")
            print(idPropiedad)

            query.bindValue(":estadoprop", "Vendido")
            query.bindValue(":prealquiprop", "")
            query.bindValue(":codigo", int(idPropiedad))
            query.exec()
            return True

        except Exception as e:
            print("Error bbddModificarPropiedadVendida, ", e)




