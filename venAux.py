from datetime import datetime

import conexion
import informes
import propiedades
from dlgAbout import Ui_dlgAbout
from dlgCalendar import *
import var
import eventos
from dlgGestionprop import Ui_dlg_tipoprop
from dlgInformeProp import Ui_dlgInformeProp


class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.uicalendar = Ui_dlgCalendar()
        var.uicalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year

        var.uicalendar.Calendar.setSelectedDate((QtCore.QDate(ano,mes,dia)))
        var.uicalendar.Calendar.clicked.connect(eventos.Eventos.cargaFecha)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()

class dlgGestionprop(QtWidgets.QDialog):

    def __init__(self):
        super(dlgGestionprop, self).__init__()
        self.ui = Ui_dlg_tipoprop()
        self.ui.setupUi(self)
        self.ui.btnAltatipoprop.clicked.connect(propiedades.Propiedades.altaTipopropiedad)
        self.ui.btnDeltipoprop.clicked.connect(propiedades.Propiedades.bajaTipopropiedad)


class dlgAbout(QtWidgets.QDialog):

    def __init__(self):
        super(dlgAbout, self).__init__()
        self.ui = Ui_dlgAbout()
        self.ui.setupUi(self)
        self.ui.btnAbout.clicked.connect(self.close)

class dlgInformeProp(QtWidgets.QDialog):


    def __init__(self):
        super(dlgInformeProp, self).__init__()
        self.ui = Ui_dlgInformeProp()
        self.ui.setupUi(self)
        dlgInformeProp.cargarMuniPropInforme(self)
        completer = QtWidgets.QCompleter(conexion.Conexion.listarMunicipios(), self.ui.cmbInformProp)
        completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.ui.cmbInformProp.setCompleter(completer)

        self.ui.btnInformeProp.clicked.connect(informes.Informes.reportPropiedades)

    def cargarMuniPropInforme(self):
        self.ui.cmbInformProp.clear()
        municipios = conexion.Conexion.listarMunicipios()
        self.ui.cmbInformProp.addItems(municipios)





