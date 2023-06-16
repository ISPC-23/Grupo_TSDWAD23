# Clase Palabras_claves

class Palabras_claves:
    # Constructor del objeto Palabras_claves
    def __init__(self):
        pass

    # Insertar una nueva palabra
    def insertar_palabra(self, palabra):
        pass


# Clase Normativa

class Normativa:
    # Constructor del objeto Normativa
    def __init__(self, tipo, numero, fecha, descripcion, categoria, jurisdiccion, organo, p_claves):
        # Hacer verificaciones
        self.tipo = tipo
        self.numero = numero
        self.fecha = fecha
        self.descripcion = descripcion
        self.categoria = categoria
        self.jurisdiccion = jurisdiccion
        self.organo = organo
        self.p_claves = p_claves

    # Muestra en formato texto del objeto
    def __str__(self):
        pass


    # Modificar una Normativa
    def modificar(self):
        pass

    # Eliminar una Normativa
    def eliminar(self):
        pass


# Consultar todas las Normativas
def consultar():
    pass

# Consultar Normativa por numero
def consultar_num(numero):
    pass

# Consultar Normativa por palabra clave
def consultar_clave(p_clave):
    pass

# Menu principal
def menu_principal():
    pass


# Proceso principal
def __main__():
    pass