import os
import sqlite3
from csv import excel
from datetime import datetime
from http.cookiejar import strip_quotes
from idlelib import query

from PyQt6 import QtSql, QtWidgets
from PyQt6.uic.Compiler.qtproxies import QtCore

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
        listarProv = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM provincias")
        if query.exec():
            while query.next():
                listarProv.append(query.value(1))
        return listarProv

    def listarMunicli(provincia):
        listamunicipios = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM municipios where idprov = (select idprov from provincias where provincia = :provincia)")
        query.bindValue(":provincia", provincia)
        if query.exec():
            while query.next():
                listamunicipios.append(query.value(1))
        return listamunicipios

    def altaCliente(nuevocli):
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


            print(listado)
            return listado

        except Exception as e:
            print("Error Listado en Conexion", e)

    def datosOneCliente(dni):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM CLIENTES WHERE dnicli = :dni")
            query.bindValue(":dni", str(dni))
            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        registro.append(query.value(i))
            print(registro)
            return registro

        except Exception as e:
            print("Error datos un Cliente", e)

    def modifCliente(registro):
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

    def listadoPropiedades(self):
        try:
            listado = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM propiedades ORDER BY codigo ASC")

            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range(query.record().count())]
                    listado.append(fila)
                print(listado)  # Para verificar todos los registros obtenidos
                return listado

            else:
                print("Error al listar Propiedades")
                return []  # En caso de error, retornar una lista vacía

        except Exception as e:
            print("Error Listado en Conexion", e)
            return []  # En caso de excepción, retornar una lista vacía

    def modifCliente(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select count(*) from propiedades where codigo = :codigo")
            query.bindValue(":codigo", str(registro[0]))
            if query.exec():
                if query.next() and query.value(0) > 0:
                    if query.exec():
                        query = QtSql.QSqlQuery()
                        query.prepare("UPDATE propiedades set altaprop = :altaprop,bajaprop = :bajaprop,dirprop = :dirprop, dirprop = :dirprop, dirprop = :dirprop, tipoprop = :tipoprop, habprop = :habprop, superprop = :superprop, prealquiprop = :prealquiprop, prevenprop = :prevenprop, cpprop = :cpprop, obserprop = :obserprop, tipooper = :tipooper, estadoprop = :estadoprop, nomeprop = :nomeprop, movilprop = :movilprop)

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