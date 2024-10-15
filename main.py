import conexion
import conexionserver
import eventos

from venAux import *
from venPrincipal import *
import sys
import var
import styles
import clientes


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        var.uicalendar = Calendar()
        var.dlgAbrir = FileDialogAbrir()
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        eventos.Eventos.cargarProv(self)
        eventos.Eventos.cargarMuni(self)

        # conexionserver.ConexionServer()





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

        '''

        EVENTOS DE LOS BOTONES

        '''

        var.ui.btnGrabarcli.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnAltacli.clicked.connect(lambda:  eventos.Eventos.abrirCalendar(0))
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifCliente)


        '''

        EVENTOS DE CAJAS DE TEXTO

        '''

        var.ui.txtDnicli.editingFinished.connect(lambda: clientes.Clientes.checkDNI(var.ui.txtDnicli.text()))
        var.ui.txtEmailcli.editingFinished.connect(lambda: clientes.Clientes.checkEmail(var.ui.txtEmailcli.text()))


        '''
        
        EVENTOS DE LOS COMOBOX
        
        '''

        var.ui.cmbProvcli.currentIndexChanged.connect(eventos.Eventos.cargarMuni)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())