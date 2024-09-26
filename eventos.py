import sys

from PyQt6 import QtWidgets
from PyQt6.uic.properties import QtWidgets, QtGui


class eventos():
    def mensajeSalir(self=None):
        mbox = QtWidgets.QMessageBox()
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setIconWindow(QtGui.QIcon('./img/inmoteis.ico'))
        mbox.setWindowTitle('Salir')
        mbox.setText('¿Desea usted salir?')
        mbox.setStandardButton(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.setDefaultButton(QtWidgets.QMessageBox.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Sí')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()

