def load_stylesheet():

    '''

    Carga y devuelve el contenido de styles.qss como una cadena


    '''


    with open("dist/styles.qss", "r") as stylesheet:
        return stylesheet.read()