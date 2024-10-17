import os
import sqlite3
from csv import excel
from idlelib import query

from PyQt6 import QtSql, QtWidgets

import var


class Conexion:
    '''

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
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM CLIENTES ORDER BY apelcli, nomecli ASC")
            if query.exec():
                while query.next():
                    fila = [query.value(i) for i in range (query.record().count())]
                    listado.append(fila)

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
            query.prepare(" UPDATE clientes set altacli = :altacli,  apelcli = :apelcli, nomecli = :nomecli, "
                          " emailcli = :emailcli, movilcli = :movicli, dircli = :dircli, provcli = :provcli, "
                          " municli = :municli, bajacli = :bajacli WHERE dnicli = :dnicli ")


            query.bindValue(":dnicli", str(registro[0]))
            query.bindValue(":altacli", str(registro[1]))
            query.bindValue(":apelcli", str(registro[2]))
            query.bindValue(":nomecli", str(registro[3]))
            query.bindValue(":emailcli", str(registro[4]))
            query.bindValue(":movicli", str(registro[5]))
            query.bindValue(":dircli", str(registro[6]))
            query.bindValue(":provcli", str(registro[7]))
            query.bindValue(":municli", str(registro[8]))
            query.bindValue(":bajacli", str(registro[9]))

            if query.exec():
                print(registro)
                return True
            else:
                print(query.lastError().text())
                return False

        except Exception as e:
            print("Error datos un modifCliente", e)

    def bajaCliente(datos):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE clientes SET bajacli = :bajacli WHERE DNICLI = :dni")
            query.bindValue(":bajacli", str(datos[0]))
            query.bindValue(":dni", str(datos[1]))
            if query.exec():
                return True
            else:
                return False

        except Exception as e:
            print("Error bajaCliente", e)

