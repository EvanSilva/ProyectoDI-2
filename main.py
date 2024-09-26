import eventos
from venPrincipal import *
import sys
import var

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)


        '''
        
        ZONA DE EVENTOS DEL MENUBAR
        
        '''

        var.ui.actionSalir.triggered.connect(eventos.eventos.mensajeSalir)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())

