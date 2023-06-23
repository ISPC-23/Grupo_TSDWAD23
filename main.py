import mysql.connector
BD_USUARIO =""
BD_PASSWORD =""
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
        self.user= user
        self.password=password
        self.database="bdnormativa"
    def conectarbd(self):
        #import mysql.connector
        miConexion=mysql.connector.connect(host="localhost", 
                                  user= self.user, 
                                  password=self.password,
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

############################################################### Menu principal ###################################################
def menu_principal():
    continuar = True
    while(continuar):
        opcioncorrecta=False
        while(not opcioncorrecta):
            print("=============== MENU PRINCIPAL ================")
            print("1-> Consultar Normativa por su numero")
            print("2-> Consultar Normativa por palabra clave")
            print("3-> Agregar Normativa")
            print("4-> Eliminar Normativa")
            print("5-> Modificar Normativa")
            print("6-> Salir")
            print("===============================================")
            opcion = int(input("Seleccione una opcion:  "))


            if opcion < 1 or opcion > 6 : 
                print (" Opcion incorrecta, ingrese nuevamente... ")
            elif opcion == 6:
                continuar = False
                print ("¡ Gracias por elegir nuestro sistema !")
                break
            else:
                opcioncorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion (opcion):
    

    if opcion ==1:

    #agregar la funcion 
    
    elif opcion == 2:

        #La palabra clave es:
    elif opcion == 3:
        #print ("La normativa a agregar es: ")
        #insertar_normativa(usuario,password)
    
    elif opcion == 4:

        #"Eliminar normativa: "

    elif opcion == 5:
        
        #("Modificar normativa: ")

menu_principal()

 ######################################################## FIN MENU PRINCIPAL #########################################################
# Proceso principal
def __main__():
    pass
