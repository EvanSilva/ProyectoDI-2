import conexion
import eventos
from venPrincipal import *
import sys
import var
import styles

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        self.setStyleSheet(styles.load_stylesheet())
        conexion.Conexion.db_conexion(self)
        eventos.Eventos.cargarProv(self)


        '''
        
        ZONA DE EVENTOS DEL MENUBAR
        
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.mensajeSalir)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())

