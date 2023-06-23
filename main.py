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





################################################# INICIO DE AGREGAR NORMATIVA #########################################
def insertar_normativa(usuario,password):
    # Código para buscar los tipos de normativas en la BD
    # Creo el Objeto Conexion
    conn = Conexionbd(usuario, password)
    # Abro la conexion instanciando el metodo conectarbd
    conexion = conn.conectarbd()
    # Decalro y asigno el cursor de la conexion a la BD
    micursor = conexion.cursor()
    # Ejecuto la SQL para bucar tipos de normativas
    micursor.execute("SELECT * FROM tipo_normativa")
    # con el metodo fetchall() asigna una tupla a la variable lista_resultado
    lista_resultado=micursor.fetchall()
    y=0
    x=0
    # Recorro y muestro la lista
    print ('''
Tipo de normativas''')
    for i in lista_resultado:
        print(lista_resultado[y][0],lista_resultado[y][1])
        y+=1
    # Verifico si la opción elegida es válida    
    bandera = True
    while bandera == True:
        normativa_tipo = int (input ('Ingrese el tipos de normativa: '))
        j=0
        for i in lista_resultado:
            if normativa_tipo == (lista_resultado[j][0]):
                bandera= False
                n_normativa_tipo = (lista_resultado[j][1])
            j+=1        
        if bandera == True:
            print ('Error: número incorrecto') 
    
    # Cierro el cursor
    micursor.close()    

    normativa_numero = input ('''
Ingrese el número de normativa: ''')
    normativa_fecha = input ('''
Ingrese la fecha de sanción (aaaa/mm/dd): ''')
    normativa_descripcion = input ('''
Ingrese la descripción (max 300 caracteres): ''')

   # Código para buscar las categorías en la BD
    micursor = conexion.cursor()
    micursor.execute("SELECT * FROM categoria")
    lista_resultado=micursor.fetchall()
    y=0
    x=0
    print ('''
Categorías''')
    for i in lista_resultado:
        print(lista_resultado[y][0],lista_resultado[y][1])
        y+=1
    # Verifico si la opción elegida es válida
    bandera = True
    while bandera == True:    
        normativa_categoria = int (input ('Seleccione la Categoría de la normativa: '))
        j=0
        for i in lista_resultado:
            if normativa_categoria == (lista_resultado[j][0]):
                bandera= False
                n_normativa_categoria = (lista_resultado[j][1])
            j+=1        
        if bandera == True:
            print ('Error: número incorrecto') 
    micursor.close()

    # Código para buscar las Jurisdicciones en la BD
    micursor = conexion.cursor()
    micursor.execute("SELECT * FROM jurisdiccion")
    lista_resultado=micursor.fetchall()
    y=0
    x=0
    print ('''
Jurisdicciones''')
    for i in lista_resultado:
        print(lista_resultado[y][0],lista_resultado[y][1])
        y+=1
    # Verifico si la opción elegida es válida
    bandera = True
    while bandera == True:
        normativa_jurisdiccion = int (input ('Seleccione la Jurisdicción: '))
        j=0
        for i in lista_resultado:
            if normativa_jurisdiccion == (lista_resultado[j][0]):
                bandera= False
                n_normativa_jurisdiccion = (lista_resultado[j][1])
            j+=1        
        if bandera == True:
            print ('Error: número incorrecto')    
    micursor.close()

    # Código para buscar las Organo Legislativo en la BD
    micursor = conexion.cursor()
    micursor.execute("SELECT * FROM organo_legislativo")
    lista_resultado=micursor.fetchall()
    y=0
    x=0
    print ('''
Órganos Legislativos''')
    for i in lista_resultado:
        print(lista_resultado[y][0],lista_resultado[y][1])
        y+=1
    # Verifico si la opción elegida es válida    
    bandera = True
    while bandera == True:    
        normativa_organo = int (input ('Seleccione Órgano Legislativo: '))
        j=0
        for i in lista_resultado:
            if normativa_organo == (lista_resultado[j][0]):
                bandera= False
                n_normativa_organo = (lista_resultado[j][1])
            j+=1        
        if bandera == True:
            print ('Error: número incorrecto')
    micursor.close()
    
    # Decalro y asigno el cursor de la conexion a la BD
    micursor = conexion.cursor()
    # Ejecuto la SQL
    sql = "INSERT INTO normativa (id_tipo_normativa, numero,fecha, descripcion, id_categoria, id_jurisdiccion, id_organo_legislativo) VALUES (%s, %s, %s, %s, %s ,%s,%s)"
    var = (normativa_tipo ,normativa_numero,normativa_fecha,normativa_descripcion, normativa_categoria, normativa_jurisdiccion, normativa_organo)
    micursor.execute(sql,var)
    conexion.commit ()
    # Cierro el cursor
    id_new_normativa = micursor.lastrowid
    micursor.close()
    conjunto_palabras = []
    ciclo = True
    while ciclo == True :
        sn =input ('''
Desea agregar una palabra clave asociada a la normativa S/N: ''')
        if sn.upper() == 'S':
            palabra_clave = input('''
Por favor agregue la palabra: ''')
            micursor = conexion.cursor()
            # Ejecuto la SQL        
            sql = "INSERT INTO palabra_clave (id_normativa, descripcion) VALUES (%s, %s)"
            var = (id_new_normativa ,palabra_clave)
            micursor.execute(sql,var)
            conexion.commit () 
            micursor.close()
            conjunto_palabras.append (palabra_clave)            
        else:
            ciclo = False    
    print ('''
Usted ha agregado una nueva normativa con éxito.
''') 

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
    menu_principal()

# Menu principal
#################################################### Menu principal ##############################################
def menu_principal():
    BD_USUARIO = input ('Ingrese usuario de Base de Datos: ')
    BD_PASSWORD = input ("Ingrese la contraseña: ")

def eliminar_normativa(user, password):
    miConexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  password="root",
                                  database="bdnormativa")
    micursor = miConexion.cursor()
    conn = Conexionbd(user, password)
    conexion = conn.conectarbd()
    micursor.execute("SELECT numero FROM normativa")
    lista_normativas_numeros=micursor.fetchall()
    respUser = input("¿Que normavita desea eliminar(numero normativa)?")
    #verificamos si la respuesta del usuario se encuentra en la bdd
    if ((respUser,) in lista_normativas_numeros):
        micursor.execute("SELECT id_normativa FROM normativa WHERE numero = "+respUser)
        variable=micursor.fetchone()
        #print(variable[0])
        micursor.execute("DELETE FROM palabra_clave WHERE id_normativa = "+str(variable[0]))
        micursor.execute("DELETE FROM normativa WHERE numero =" + respUser)
        print("Se elimino con exito")
    else:
        print("error no se encuentra la normativa")


    conexion.commit()
    conn.cerrarconectarbd (conexion)
    micursor.close()
