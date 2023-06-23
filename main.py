from msilib.schema import SelfReg
from typing import Self
import mysql.connector

# Clase Palabra_clave
class Palabra_clave:
    '''Palabra_clave esta formado por:
    palabra: string
    normativas: [int]
    '''
    # Constructor del objeto Palabra_clave
    def __init__(self, palabra):
        self.palabra = palabra
        self.normativas = []

    # Modificar una palabra
    def modificar_palabra(self, nueva_palabra):
        self.palabra = nueva_palabra
    
    # Agregar una Normativa a la palabra
    def agregar_normativa(self, normativa):
        self.normativas.append(normativa)


# Clase Normativa
class Normativa:
    '''Normativa esta formado por:
    tipo: string
    numero: int
    fecha: string
    descripcion: string
    categoria: string
    jurisdiccion: string
    organo: string
    p_claves: [string]
    '''
    # Constructor del objeto Normativa
    def __init__(self, tipo, numero, fecha, descripcion, categoria, jurisdiccion, organo):
        # Hacer verificaciones
        self.tipo = tipo
        self.numero = numero
        self.fecha = fecha
        self.descripcion = descripcion
        self.categoria = categoria
        self.jurisdiccion = jurisdiccion
        self.organo = organo
        self.p_claves = []

    # Muestra en formato texto del objeto
    def __str__(self):
        print(f"Normativa\n {self.tipo} N° {self.numero}")
        print(f"Jurisdicción {self.jurisdiccion}")
        print(f"Organo legislativo: {self.organo}")
        print(f"Fecha: {self.fecha}")
        print(f"Categoría: {self.categoria}")
        print(f"Palabras claves: {self.p_claves}")
        print(f"{self.descripcion}")

    # Modificar una Normativa
    def modificar(self):
        pass


# Clase Conexionbd
class Conexionbd:
    '''Conexionbd esta formado por:
    host: string
    user: string
    password: string
    database: string
    '''
    # Constructor del objeto Conexionbd
    def __init__(self, user, password):        
        self.host="localhost" 
        self.user=user, 
        self.password=password,
        self.database="bdnormativa"
    def conectarbd(self):
        #import mysql.connector
        miConexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  password="fernando",
                                  database="bdnormativa")
        if miConexion.is_connected:
           #micursor = miConexion.cursor()
#           print ('conexion ok')
           #return micursor
           return miConexion         
        else:
            print ('error de conexion a la base de datos')
    def cerrarconectarbd(self,miConexion ):        
        miConexion.close()
#        print ('conexion cerrada')


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

#Modificar

def __init__(self, user, password):        
        self.host="localhost" 
        self.user=user, 
        self.password=password,
        self.database="bdnormativa"
def conectarbd(self):
        #import mysql.connector
        miConexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  password="1234568",
                                  database="bdnormativa")
class Modificador:
    def __init__(self, user, password):
        self.conn = Conexionbd(user, password)
        self.conexion = self.conn.conectarbd()
        self.micursor = self.conexion.cursor()

    def modificar(self, tipo, numero, fecha, descripcion, categoria, jurisdiccion, organo):
        consulta = "UPDATE bdnormativa SET campo1 = %s, campo2 = %s, campo3 = %s, campo4 = %s, campo5 = %s, campo6 = %s WHERE id = %s"
        valores = (tipo, numero, fecha, descripcion, categoria, jurisdiccion, organo)
        self.micursor.execute(consulta, valores)
        self.conexion.commit()
        print("Valor modificado correctamente.")
        def cerrarconectarbd(self,miConexion ):
            miConexion.close()


#otro
import mysql.connector

class Conexionbd:
    def __init__(self, user, password):
        self.host = "localhost"
        self.user = "root"
        self.password = "1234568"
        self.database = "bdnormativa"

    def conectarbd(self):
        # import mysql.connector
        miConexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database)
        return miConexion

    def cerrarconectarbd(self):
        self.miConexion.close()

class Modificador:
    def __init__(self, user, password):
        self.conn = Conexionbd(user, password)
        self.conexion = self.conn.conectarbd()
        self.micursor = self.conexion.cursor()

    def modificar(self, tipo, numero, fecha, descripcion, categoria, jurisdiccion, organo):
        consulta = "UPDATE bdnormativa SET campo1 = %s, campo2 = %s, campo3 = %s, campo4 = %s, campo5 = %s, campo6 = %s WHERE id = %s"
        valores = (tipo, numero, fecha, descripcion, categoria, jurisdiccion, organo)
        self.micursor.execute(consulta, valores)
        self.conexion.commit()
        print("Valor modificado correctamente.")
def cerrarconectarbd(self):
            self.conn.cerrarconectarbd()





