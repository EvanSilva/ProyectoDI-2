from PIL.ImageQt import qt_version

from venPrincipal import *
import sys
import var

class main(QtWidgets.QMainWindow):

    def __init__(self):
        super(main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = main()
    window.show()
    sys.exit(app.exec())