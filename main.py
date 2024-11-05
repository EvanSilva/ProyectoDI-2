import conexion
import eventos
from propiedades import Propiedades
from venAux import *
from venPrincipal import *
import sys
import var
import styles
import clientes
import propiedades


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uicalendar = Calendar()
        var.dlgAbrir = FileDialogAbrir()
        var.dlggestion = dlgGestionprop()
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargarMuni(self)
        var.historico = 1
        # conexionserver.ConexionServer()

        eventos.Eventos.cargarTipoprop(self)
        propiedades.Propiedades.cargaTablaPropiedades(self)





        '''
        
        EVENTOS DE TABLAS
        '''

        clientes.Clientes.cargaTablaClientes(self)
        eventos.Eventos.resizeTablaClientes(self)
        var.ui.tablaClientes.clicked.connect(clientes.Clientes.cargaOneCliente)


        '''

        ZONA DE EVENTOS DEL MENUBAR

        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionCrearBackup.triggered.connect(eventos.Eventos.crearBackup)
        var.ui.actionRestaurar.triggered.connect(eventos.Eventos.restaurarBackup)
        var.ui.actionPropiedades.triggered.connect(eventos.Eventos.abrirTipoprop)

        '''

        EVENTOS DE LOS BOTONES

        '''

        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnAltacli.clicked.connect(lambda:  eventos.Eventos.abrirCalendar(0, 0))
        var.ui.btnBajacli.clicked.connect(lambda: eventos.Eventos.abrirCalendar(0, 1))
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCliente)
        var.ui.btnDelcli.clicked.connect(clientes.Clientes.bajaCliente)
        var.ui.btnGrabarprop.clicked.connect(propiedades.Propiedades.altaPropiedad)
        '''

        EVENTOS DE CAJAS DE TEXTO

        '''

        var.ui.txtDnicli.editingFinished.connect(lambda: clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text()))
        var.ui.txtMovilcli.editingFinished.connect(lambda: clientes.Clientes.checkNumero(var.ui.txtMovilcli.text()))

        '''
        
        EVENTOS DE LOS COMOBOX
        
        '''
        eventos.Eventos.cargarProv(self)
        var.ui.cmbProvcli.currentIndexChanged.connect(eventos.Eventos.cargarMuni)
        var.ui.cmbProvcli.currentIndexChanged.connect(eventos.Eventos.cargarMuni)

        '''

        EVENTOS TOOLBAR

        '''

        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mensajeSalir)
        var.ui.actionbarLimpiar.triggered.connect(eventos.Eventos.limpiarPanel)

        '''

        EVENTOS CHECKBOX

        '''

        var.ui.chkHistoriacli.stateChanged.connect(clientes.Clientes.historicoCli)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())