import math
from datetime import datetime

from PIL.ImageColor import colormap
from PyQt6 import QtSql
from reportlab.pdfgen import canvas
from PIL import Image
import os, shutil

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
                        var.report.drawString(450, 70, "Pagina siguiente")
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
            query.prepare(
                'select codigo, dirprop, tipoprop, tipooper, prealquiprop, prevenprop from propiedades where muniprop = :muniprop order by codigo')
            municipio = var.dlgInformeProp.ui.cmbInformProp.currentText()
            query.bindValue(":muniprop", municipio)

            if query.exec():
                x = 55
                y = 635
                while query.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=9)
                        var.report.drawString(450, 70, "Pagina siguiente")
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

                    var.report.drawCentredString(x + 215, y, str(operacion))

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

    ################################################### FACTURAS #########################################################

    @staticmethod
    def reportFacturaActual(facventa, subtotal, iva, total):
        """

        """
        try:
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.mkdirs(rootPath)
            numFactura = var.ui.txtNumFac.text()
            print(numFactura)
            titulo = "Listado Propiedades de la factura: " + numFactura
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
            Informes.topInformeFacturas(titulo)
            Informes.footInformeFacturas(titulo, paginas, subtotal, iva, total)
            items = ['ID VENTA', 'ID FACTURA', 'LOCALIDAD', 'TIPO', 'DIRECCION', 'PRECIO']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 650, str(items[0]))
            var.report.drawString(110, 650, str(items[1]))
            var.report.drawString(190, 650, str(items[2]))
            var.report.drawString(275, 650, str(items[3]))
            var.report.drawString(340, 650, str(items[4]))
            var.report.drawString(450, 650, str(items[5]))


            var.report.line(50, 645, 525, 645)

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
                x = 55
                y = 630
                while query.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=9)
                        var.report.drawString(450, 70, "Pagina siguiente")
                        var.report.showPage()
                        Informes.footInformeFacturas(titulo, paginas, subtotal, iva, total)
                        Informes.topInformeFacturas(titulo)
                        items = ['ID VENTA', 'ID FACTURA', 'LOCALIDAD', 'TIPO', 'DIRECCION', 'PRECIO']
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 650, str(items[0]))
                        var.report.drawString(100, 650, str(items[1]))
                        var.report.drawString(190, 650, str(items[2]))
                        var.report.drawString(310, 650, str(items[3]))
                        var.report.drawString(360, 650, str(items[4]))
                        var.report.drawString(450, 650, str(items[5]))

                        var.report.line(50, 645, 525, 645)
                        x = 55
                        y = 625

                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(x + 20, y, str(query.value(0)))
                    var.report.drawString(x + 80, y, str(query.value(1)))
                    var.report.drawCentredString(x + 163, y, str(query.value(2)))
                    var.report.drawCentredString(x + 235, y, str(query.value(3)))
                    var.report.drawCentredString(x + 312, y, str(query.value(4)))
                    var.report.drawCentredString(x + 415, y, str(query.value(5)) + " €")


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


    def topInformeFacturas(titulo):
        """

        """
        try:
            ruta_logo = '.\\img\\inmoteis.ico'
            logo = Image.open(ruta_logo)

            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'InmoTeis')
                var.report.drawString(160, 680, titulo)
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


    def footInformeFacturas(titulo, paginas, subtotal, iva, total):
        """

        """
        try:

            total_pages = 0
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber() + '/' + str(paginas)))

            var.report.drawString(50, 70, 'Subtotal: ' + str(subtotal) + ' €')
            var.report.drawString(50, 90, 'IVA: ' + str(iva) + ' €')
            var.report.drawString(50, 110, 'Total: ' + str(total) + ' €')



        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    ################################################### ALQUILERES #########################################################


    # colocar los valores y lo termino

    @staticmethod
    def reportMensualidadActual(idMensualidad):
        """
        Método para generar un informe con los datos de la mensualidad.
        """

        print("AWA AWA ----------------- ")
        try:
            rootPath = '.\\informes'
            if not os.path.exists(rootPath):
                os.mkdirs(rootPath)
            numAlquiler = var.ui.txtNumFac.text()
            print(idMensualidad)
            titulo = "Datos de la mensualidad: " + idMensualidad
            fecha = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
            nomepdfcli = fecha + "_listadopropiedades.pdf"
            query0 = QtSql.QSqlQuery()
            pdf_path = os.path.join(rootPath, nomepdfcli)
            var.report = canvas.Canvas(pdf_path)
            Informes.topInformeMensualidad(titulo)
            print("Hace el top")
            Informes.footInformeMensualidad(titulo)
            print("Hace el footer")

            # Lista de títulos
            items = ['Id mensualidad - ', 'Mes de la mensualidad - ', 'Precio - ', 'DNI cliente - ', 'Nombre del Cliente - ',
                     'Apellidos del cliente - ', "Direccion de facturacion - ", "Localidad de la propiedad - "]

            var.report.setFont('Helvetica-Bold', size=10)
            y = 625  # Empezamos desde la parte superior

            # Dibujar los títulos en negrita en la primera columna
            for i, item in enumerate(items):
                var.report.drawString(55, y, item)  # Títulos a la izquierda
                y -= 30  # Espacio entre títulos

            print("pre-query")
            query = QtSql.QSqlQuery()
            query.prepare("""
                                            SELECT    m.ID  as "idMensualidad",
                                                      m.Mes as "mesMensualidad",
                                                      m.Precio as "precioMensualidad",
                                                      c.dnicli as "dniCliente",
                                                      c.nomecli as "nombreCliente",
                                                      c.apelcli as "apellidosCliente",
                                                      c.dircli as "direccionCliente",
                                                      p.muniprop as "localidadPropiedad",
                                                      m.Abono as "Abono"

                                        FROM mensualidades AS m
                                        INNER JOIN alquileres AS a
                                            ON m.AlquilerAsociado = a.ID
                                                INNER JOIN clientes AS c
                                                    ON a.Cliente_DNI = c.dnicli
                                                        INNER JOIN propiedades as p
                                                            ON a.Propiedad_ID = p.codigo
                                            WHERE m.ID = :idMensualidad;
                                            """)
            query.bindValue(":idMensualidad", idMensualidad)
            if query.exec():
                x = 55
                y = 625
                print("Pre-while")
                while query.next():
                    if y <= 90:
                        var.report.setFont('Helvetica-Oblique', size=9)
                        var.report.drawString(450, 70, "Pagina siguiente")
                        var.report.showPage()
                        Informes.footInformeMensualidad(titulo)
                        Informes.topInformeMensualidad(titulo)

                        x = 55
                        y = 625

                    var.report.setFont('Helvetica', size=9)
                    # Ahora intercalamos los datos con los títulos, de modo que la información va a la derecha
                    var.report.drawString(135, y, str(query.value(0)))  # ID MENSUALIDAD
                    var.report.drawString(175, y - 30, str(query.value(1)).title())  # MES MENSUALIDAD
                    var.report.drawString(98, y - 60, str(query.value(2)) + " €")  # PRECIO MENSUALIDAD
                    var.report.drawString(117, y - 90, str(query.value(3)))  # DNI CLIENTE
                    var.report.drawString(155, y - 120, str(query.value(4)))  # NOMBRE CLIENTE
                    var.report.drawString(160, y - 150, str(query.value(5)))  # APELLIDOS CLIENTE
                    var.report.drawString(180, y - 180, str(query.value(6)))  # DIRECCIÓN CLIENTE
                    var.report.drawString(190, y - 210, str(query.value(7)))  # LOCALIDAD DE LA PROPIEDAD
                    var.report.line(50, y - 240, 525, y - 240)  # Línea justo después de la última fila

                    abonadobbdd = query.value(8)
                    abono = "NO ABONADO"

                    if abonadobbdd == "True":
                        abono = "ABONADO"

                    var.report.setFont('Helvetica-Bold', size=40)  # Fuente más grande para ABONO
                    var.report.setFillColorRGB(1, 0, 0)
                    var.report.drawString(65, y - 300, str(abono).upper())  # ABONO en mayúsculas y grande
                    var.report.line(50, y - 330, 525, y - 330)  # Línea justo después de la última fila

                    var.report.setFont('Helvetica', size=8)  # Fuente más pequeña para la retaila
                    var.report.setFillColorRGB(0, 0, 0)  # Color negro para el texto

                    # Retaila de texto legal
                    retaila = """
                                            INFORMACIÓN LEGAL:
                                            1. Este informe sigue la Ley 22/2023 sobre la Protección de Datos. Si no te gusta, reinicia el sistema.
                                            2. Los datos están protegidos por el RGPD. Los hackers no están invitados.
                                            3. En caso de error, solo presiona F5 y todo volverá a la normalidad.
                                            4. No es necesario un antivirus para leer este informe... a menos que se imprima en papel.
                                            5. La divulgación está prohibida, pero si lo compartes con un bot, está bien (siempre que sea un bot de confianza).
                                            6. Si ves un error, no te preocupes, el código es todavía "beta".
                                            7. No necesitas ser un administrador de red para entender esto, solo un humano.
                                            8. Este informe es solo un "placeholder" para el contrato real que llegará pronto.
                                            9. Las disputas se resolverán en los tribunales, no en una consola de comandos.
                                            10. Nuestra política de privacidad está más segura que un servidor SSH con dos factores.
                                            11. La información puede ser más larga que un log de servidor. Toma un descanso.
                                            12. Para acceso, contacta con nuestro "admin" o simplemente pide a tu asistente virtual.
                                            13. El acceso está restringido, pero si tienes un script autorizado, adelante.
                                            14. Este informe no es un contrato, solo un "README" preliminar.
                                            15. Las modificaciones se rastrean como commits en nuestro repositorio.
                                            16. Si no entiendes algo, prueba con Google, o con "man página".
                                            17. El informe se guardó en formato PDF, no en un floppy de 1.44MB.
                                            18. Los cambios se reflejarán en el próximo "push" de la política de privacidad.
                                            19. Este informe es válido solo si se lee en la terminal de un sistema UNIX.
                                            20. Cualquier error se corregirá con un parche rápido y un café.
                                            21. Si ves "404", es que el informe no está disponible... o no tienes permisos.
                                          
                    """

                    # Dibujamos la retaila en líneas separadas
                    lines = retaila.strip().split('\n')
                    line_y = y - 350  # Comenzamos justo después de la línea de ABONO

                    for line in lines:
                        var.report.drawString(50, line_y, line.strip())  # Dibuja cada línea
                        line_y -= 10  # Espaciado entre líneas




            else:

                print(query.lastError().text())

            var.report.save()
            rootPath = '.\\informes'

            for file in os.listdir(rootPath):
                if file.endswith(nomepdfcli):
                    os.startfile(pdf_path)
        except Exception as e:
            print(e)

    def topInformeMensualidad(titulo):
        """

        """
        try:
            ruta_logo = '.\\img\\inmoteis.ico'
            logo = Image.open(ruta_logo)

            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'InmoTeis')
                var.report.drawString(200, 680, titulo)
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

    def footInformeMensualidad(titulo):
        """

        """
        try:

            total_pages = 0
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)