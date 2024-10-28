import var


class Propiedades():

    def altaTipopropiedad(self):
        tipo = var.dlggestion.txtGestipoprop.text()
        print(tipo)

    def altaPropiedad(self):
        try:
            propiedad = [var.ui.txtAltaprop.text(), var.ui.txtBajaprop, var.ui.txtDirprop.text(),
                         var.ui.cmbProvprop.currentText(), var.ui.cmbMuniprop.currentText(), var.ui.cmbTipoprop.currentText(),
                         var.ui.spnHabprop.text(), var.ui.spnBanprop.text(), var.ui.txtSuperprop.text(),
                         var.ui.txtPrecioalquilerprop.text(), var.ui.txtPrecioventaprop.text(), var.ui.CPprop.text(),
                         var.ui.txtObservaprop.toPlainText(), var.ui.txtNomeprop.text(), var.ui.txtMovilprop.text()
                         ]
            print(propiedad)
        except Exception as e:
            print("Error en propiedades, altaPropiedad()")
