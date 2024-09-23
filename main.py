from PIL.ImageQt import qt_version

from venPrincipal import *
import sys

class main(QtWidgets.QMainWindow):

    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_venPrincipal()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = main()
    window.show()
    sys.exit(app.exec())