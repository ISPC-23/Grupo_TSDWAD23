#Menu_Principal

def menu_principal():
    continuar = True
    while(continuar):
        opcioncorrecta=False
        while(not opcioncorrecta):
            print("=============== MENU PRINCIPAL ================")
            print("1-> Consultar Normativa por numero")
            print("2-> Consultar Normativa por palabra clave")
            print("3-> Agregar Normativa")
            print("4-> Eliminar Normativa")
            print("5-> Modifical Normativa")
            print("6-> Salir")
            print("===============================================")
            opcion = int(input("Seleccione una opcion: "))


            if opcion < 1 or opcion > 6 : 
                print (" Opcion incorrecta, ingrese nuevamente... ")
            elif opcion == 6 :
                continuar = False
                print ("¡Gracias por elegir nuestro sistema!")
                break
            else:
                opcioncorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion (opcion):
    print(opcion)

menu_principal()



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
##############################################
class Conexionbd:
    # Constructor del objeto Conexionbd
    def __init__(self):        
        self.host="localhost" 
        self.user="root", 
        self.password="fernando",
        self.database="bdnormativa"
    def conectarbd(self):
        import mysql.connector
        miConexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  password="fernando",
                                  database="bdnormativa")
        if miConexion.is_connected:
           micursor = miConexion.cursor()
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

# Menu principal   >>>>>>>>>>>>> lo realice en la parte de arriba del codigo
# def menu_principal():
 #   pass

# Proceso principal
def __main__():
    pass