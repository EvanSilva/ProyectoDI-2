import math
from datetime import datetime

from PyQt6 import QtSql
from reportlab.pdfgen import canvas
from PIL import Image
import os,shutil

import var


class Informes:

    ################################################### CLIENTES #########################################################

    def reportClientes(self):
        """

        Método para generar un informe de clientes

        :return: None
        :rtype: None


        """
        try:
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.mkdirs(rootPath)
            titulo = "Listado Clientes"
            fecha = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
            nomepdfcli = fecha + "_listadoclientes.pdf"
            query0 = QtSql.QSqlQuery()
            query0.exec('select count(*) from clientes')
            if query0.next():
                print(query0.value(0))
                registros = int(query0.value(0))
                paginas = math.ceil(registros / 28)
            pdf_path = os.path.join(rootPath, nomepdfcli)
            var.report = canvas.Canvas(pdf_path)
            Informes.topInforme(titulo)
            Informes.footInforme(titulo, paginas)
            items = ['DNI', 'APELLIDOS', 'NOMBRE', 'MOVIL', 'PROVINCIA', 'MUNICIPIO']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))
            var.report.drawString(100, 650, str(items[1]))
            var.report.drawString(190, 650, str(items[2]))
            var.report.drawString(285, 650, str(items[3]))
            var.report.drawString(360, 650, str(items[4]))
            var.report.drawString(450, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)

            query = QtSql.QSqlQuery()
            query.prepare('select dnicli, apelcli, nomecli, movilcli, provcli, municli from clientes order by apelcli')

            if query.exec():
                x = 55
                y = 635
                while query.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=9)
                        var.report.drawString(450,70, "Pagina siguiente")
                        var.report.showPage()
                        Informes.footInforme(titulo, paginas)
                        Informes.topInforme(titulo)
                        items = ['DNI', 'APELLIDOS', 'NOMBRE', 'MOVIL', 'PROVINCIA', 'MUNICIPIO']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 645, str(items[0]))
                        var.report.drawString(100, 645, str(items[1]))
                        var.report.drawString(190, 645, str(items[2]))
                        var.report.drawString(285, 645, str(items[3]))
                        var.report.drawString(360, 645, str(items[4]))
                        var.report.drawString(450, 645, str(items[5]))
                        var.report.line(50, 645, 525, 645)
                        x = 55
                        y = 625

                    var.report.setFont('Helvetica', size=9)
                    dni = '***' + str(query.value(0)[4:7] + '***')
                    var.report.drawCentredString(x + 5, y, str(dni))
                    var.report.drawString(x + 30, y, str(query.value(1)))
                    var.report.drawString(x + 140, y, str(query.value(2)))
                    var.report.drawString(x + 220, y, str(query.value(3)))
                    var.report.drawString(x + 320, y, str(query.value(4)))
                    var.report.drawString(x + 405, y, str(query.value(5)))
                    y -= 20
            else:
                print(query.lastError().text())

            var.report.save()
            rootPath = '.\\informes'

            for file in os.listdir(rootPath):
                if file.endswith(nomepdfcli):
                    os.startfile(pdf_path)
        except Exception as e:
            print(e)

    def topInforme(titulo):
        """

        Método para generar la cabecera de un informe

        :param titulo: Título del informe
        :type titulo: str
        :return: None
        :rtype: None


        """
        try:
            ruta_logo = '.\\img\\inmoteis.ico'
            logo = Image.open(ruta_logo)

            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'InmoTeis')
                var.report.drawString(230, 680, titulo)
                var.report.line(50, 665, 525, 665)

                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Chapela, Vigo - 36320 - España')
                var.report.drawString(55, 725, 'Teléfono: 654 333 979')
                var.report.drawString(55, 710, 'e-mail: evanchapela@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)

    def footInforme(titulo, paginas):
        """

        Método para generar el pie de un informe

        :param titulo: Título del informe
        :type titulo: str
        :param paginas: Número de páginas del informe
        :type paginas: int
        :return: None
        :rtype: None

        """
        try:
            total_pages = 0
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber() + '/' + str(paginas)))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    ################################################### PROPIEDADES #########################################################

    def reportPropiedades(self):
        """

        Método para generar un informe de propiedades

        :return: None
        :rtype: None


        """
        try:
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.mkdirs(rootPath)
            municipio = var.dlgInformeProp.ui.cmbInformProp.currentText()
            print(municipio)
            titulo = "Listado Propiedades de " + municipio
            fecha = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
            nomepdfcli = fecha + "_listadopropiedades.pdf"
            query0 = QtSql.QSqlQuery()
            query0.exec('select count(*) from propiedades')
            if query0.next():
                print(query0.value(0))
                registros = int(query0.value(0))
                paginas = math.ceil(registros / 28)
            pdf_path = os.path.join(rootPath, nomepdfcli)
            var.report = canvas.Canvas(pdf_path)
            Informes.topInformePropiedades(titulo)
            Informes.footInformePropiedades(titulo, paginas)
            items = ['CÓDIGO', 'DIRECCION', 'TIPO', 'OPERACIÓN', 'PRECIO ALQUILER', 'PRECIO COMPRA']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))
            var.report.drawString(110, 650, str(items[1]))
            var.report.drawString(190, 650, str(items[2]))
            var.report.drawString(240, 650, str(items[3]))
            var.report.drawString(330, 650, str(items[4]))
            var.report.drawString(440, 650, str(items[5]))
            var.report.line(50, 645, 525, 645)

            query = QtSql.QSqlQuery()
            query.prepare('select codigo, dirprop, tipoprop, tipooper, prealquiprop, prevenprop from propiedades where muniprop = :muniprop order by codigo')
            municipio = var.dlgInformeProp.ui.cmbInformProp.currentText()
            query.bindValue(":muniprop", municipio)

            if query.exec():
                x = 55
                y = 635
                while query.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=9)
                        var.report.drawString(450,70, "Pagina siguiente")
                        var.report.showPage()
                        Informes.footInformePropiedades(titulo, paginas)
                        Informes.topInformePropiedades(titulo)
                        items = ['CÓDIGO', 'DIRECCION', 'TIPO', 'OPERACIÓN', 'PRECIO ALQUILER', 'PRECIO COMPRA']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 645, str(items[0]))
                        var.report.drawString(100, 645, str(items[1]))
                        var.report.drawString(190, 645, str(items[2]))
                        var.report.drawString(285, 645, str(items[3]))
                        var.report.drawString(360, 645, str(items[4]))
                        var.report.drawString(450, 645, str(items[5]))
                        var.report.line(50, 645, 525, 645)
                        x = 55
                        y = 625

                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(x + 15, y, str(query.value(0)))
                    var.report.drawString(x + 46, y, str(query.value(1)))
                    var.report.drawCentredString(x + 145, y, str(query.value(2)))

                    operacion = query.value(3)
                    operacion = operacion.replace("[", "").replace("]", "").replace("'", "").replace('"', "")

                    var.report.drawCentredString(x + 215, y, str (operacion))

                    alquiler = str(query.value(4))

                    if alquiler == '':
                        alquiler = '-'
                        var.report.drawRightString(x + 335, y, str(alquiler))

                    alquiler = alquiler + " €"
                    var.report.drawRightString(x + 335, y, str(alquiler))

                    venta = str(query.value(5))

                    if venta == '':
                        venta = '-'
                        var.report.drawRightString(x + 450, y, str(venta))

                    venta = venta + " €"
                    var.report.drawRightString(x + 450, y, str(venta))
                    y -= 20
            else:
                print(query.lastError().text())

            var.report.save()
            rootPath = '.\\informes'

            for file in os.listdir(rootPath):
                if file.endswith(nomepdfcli):
                    os.startfile(pdf_path)
        except Exception as e:
            print(e)

    def topInformePropiedades(titulo):
        """

        Método para generar la cabecera de un informe de propiedades

        :param titulo: Título del informe
        :type titulo: str
        :return: None
        :rtype: None


        """
        try:
            ruta_logo = '.\\img\\inmoteis.ico'
            logo = Image.open(ruta_logo)

            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'InmoTeis')
                var.report.drawString(230, 680, titulo)
                var.report.line(50, 665, 525, 665)

                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Chapela, Vigo - 36320 - España')
                var.report.drawString(55, 725, 'Teléfono: 654 333 979')
                var.report.drawString(55, 710, 'e-mail: evanchapela@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)

    def footInformePropiedades(titulo, paginas):
        """

        Método para generar el pie de un informe de propiedades

        :param titulo: Título del informe
        :type titulo: str
        :param paginas: Número de páginas del informe
        :type paginas: int
        :return: None
        :rtype: None

        """
        try:
            total_pages = 0
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber() + '/' + str(paginas)))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

