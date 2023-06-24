import mysql.connector

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
        return f"Normativa\n{self.tipo} N° {self.numero}\n\
Jurisdicción {self.jurisdiccion}\n\
Organo legislativo: {self.organo}\n\
Fecha: {self.fecha}\n\
Categoría: {self.categoria}\n\
Palabras claves: {self.p_claves}\n\
{self.descripcion}"


# Clase Conexionbd
class Conexionbd :
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
        miConexion=mysql.connector.connect(host=self.host, 
                                  user= self.user, 
                                  password=self.password,
                                  database=self.database)
        if miConexion.is_connected:
           return miConexion         
        else:
            print ('error de conexion a la base de datos')

    def cerrarconectarbd(self,miConexion ):        
        miConexion.close()


################################################# INICIO DE CONSULTAR POR PALABRA CLAVE #########################################
# Consultar Normativa por palabra clave
def consultar_clave(p_clave, usuario, password):
    normativas = []
    myBD = Conexionbd(usuario, password)
    bdConectada = myBD.conectarbd()
    bdCursor = bdConectada.cursor()
    bdCursor.execute("SELECT * FROM palabra_clave where descripcion=%s",(p_clave,))
    registros = bdCursor.fetchall()
    sql = "SELECT TP.descripcion, N.numero, N.fecha, N.descripcion, C.descripcion,\
            J.descripcion, OL.descripcoin\
        FROM normativa AS N, tipo_normativa AS TP, categoria AS C, jurisdiccion AS J,\
            organo_legislativo AS OL\
        WHERE N.id_tipo_normativa = TP.id_tipo_normativa AND\
            N.id_categoria = C.id_categoria AND\
            N.id_jurisdiccion = J.id_jurisdiccion AND\
            N.id_organo_legislativo = OL.id_organo_legislativo AND\
            id_normativa=%s"
    for registro in registros:
        #print(f"{registro[0]} - {registro[1]}: {registro[2]}")
        bdCursor.execute(sql, (registro[1],))
        registro_norm = bdCursor.fetchone()
        nueva_norm = Normativa(
            registro_norm[0],
            registro_norm[1],
            registro_norm[2],
            registro_norm[3],
            registro_norm[4],
            registro_norm[5],
            registro_norm[6]
        )
        normativas.append(nueva_norm)
    bdCursor.close()
    myBD.cerrarconectarbd(bdConectada)
    return normativas
################################################# FIN DE CONSULTAR POR PALABRA CLAVE #########################################

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
        normativa_tipo = int (input ('Ingrese el tipo de normativa: '))
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
################################################# FIN DE AGREGAR NORMATIVA ####################################

###################################################### MENU PRICIPAL ##########################################
def menu_principal(usuario, password):
    continuar = True
    while(continuar):
        opcioncorrecta=False
        while(not opcioncorrecta):
            print("\n=============== MENU PRINCIPAL ================")
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
                ejecutarOpcion(opcion,usuario, password)

def ejecutarOpcion (opcion, usuario, password):
    
    if opcion ==1:       
    #agregar la funcion 
       consultar_num(usuario, password)

    elif opcion == 2:
        palabra = input("\nIngrese la palabra clave: ")
        resultados = consultar_clave(palabra, usuario, password)
        if resultados == []:
            print("\nNo se encontraron normativas con esa palabra")
        else:
            print("\nSeleccione que normativa quiere visualizar")
            for i,resultado in enumerate(resultados):
                print(f"[{i}] - {resultado.tipo} {resultado.numero}" )
            indice = int(input("\nIngrese el número de la opción: "))
            print(f"\n{resultados[indice]}")

    elif opcion == 3:
        #print ("La normativa a agregar es: ")
        insertar_normativa(usuario, password)

    elif opcion == 4:
        eliminar_normativa(usuario, password)
        #"Eliminar normativa: "

    elif opcion == 5:
        modificar_normativa(usuario, password)
        #("Modificar normativa: ")

################################################# FIN MENU PRINCIPAL ##########################################

################################################# INICIO DE ELIMINAR ##########################################
def eliminar_normativa(usuario, password):
    conn = Conexionbd(usuario, password)
    conexion = conn.conectarbd()
    micursor = conexion.cursor()
    micursor.execute("SELECT numero FROM normativa")
    lista_normativas_numeros=micursor.fetchall()
    respUser = input("¿Que normavita desea eliminar(numero normativa)?")
    #verificamos si la respuesta del usuario se encuentra en la bdd
    if ((respUser,) in lista_normativas_numeros):
        micursor.execute("SELECT id_normativa FROM normativa WHERE numero = "+respUser)
        variable=micursor.fetchone()
        #print(variable[0])
        
        respuesta = input("¿Esta seguro que desea borrar la normativa N°" + respUser + " (Si/No).\n")
        
        if respuesta.lower() == "no":
            print("Eliminación cancelada.")
            exit() 
        else:
            print("Eliminando...")
            micursor.execute("DELETE FROM palabra_clave WHERE id_normativa = "+str(variable[0]))
            micursor.execute("DELETE FROM normativa WHERE numero =" + respUser)
            print("Se eliminó con exito.")
            conexion.commit()        
    else:
        print("error no se encuentra la normativa")

    conn.cerrarconectarbd (conexion)
    micursor.close()
############################################## FIN DE ELIMINAR ###############################################

####################################### INICIO DE CONSULTAR POR NUMERO #######################################
def consultar_num(usuario, password):
    # Código para buscar los tipos de normativas en la BD
    # Creo el Objeto Conexion
    conn = Conexionbd(usuario, password)
    # Abro la conexion instanciando el metodo conectarbd
    conexion = conn.conectarbd()
    # Decalro y asigno el cursor de la conexion a la BD
    micursor = conexion.cursor()
    
    normativa = input("Ingrese el número de la normativa: ")

# Ejecuto Consulta SQL
    micursor.execute ("SELECT tipo_normativa.descripcion, normativa.numero, normativa.fecha, normativa.descripcion, categoria.descripcion, jurisdiccion.descripcion, organo_legislativo.descripcoin FROM normativa inner join tipo_normativa using(id_tipo_normativa) inner join categoria using(id_categoria) inner join jurisdiccion using(id_jurisdiccion) inner join organo_legislativo using(id_organo_legislativo) WHERE normativa.numero = " + normativa )

# Obtener el resultado de la consulta
    resultado = micursor.fetchone()

    if resultado:
        print("La normativa consultada es: ")
        print(resultado[0], ": ", resultado[1])
        print("Fecha de sanción: ", resultado[2])
        print("Descripción: ", resultado[3])
        print("Categoria: ", resultado[4])
        print("Jurisdicción: ", resultado[5])
        print("Organo Lesgislativo: ", resultado[6])
    else:
        print("No se encontró ninguna coincidencia para la normativa", normativa)
    micursor.close()
    conn.cerrarconectarbd (conexion)
####################################### FIN DE CONSULTAR POR NUMERO #######################################

####################################### INICIO DE FUNCION MODIFICAR #######################################
def modificar_normativa(usuario, password):
    # Código para buscar los tipos de normativas en la BD
    # Creo el Objeto Conexion
    conn = Conexionbd(usuario, password)
    # Abro la conexion instanciando el metodo conectarbd
    conexion = conn.conectarbd()
    # Decalro y asigno el cursor de la conexion a la BD
    micursor = conexion.cursor()
    # Ejecuto la SQL para bucar tipos de normativas
    num_norm = input('Ingrese el número de normativa que desea modificar: ')
    micursor.execute("SELECT normativa.id_normativa, tipo_normativa.descripcion, normativa.numero, normativa.fecha, normativa.descripcion FROM normativa  inner join tipo_normativa using (id_tipo_normativa) WHERE normativa.numero =" + num_norm)
    # con el metodo fetchall() asigna una tupla a la variable lista_resultado
    lista_resultado=micursor.fetchall()
    # Recorro y muestro la lista
    print ('''
La normativa a modificar es:''')
    print(lista_resultado[0][1], ' N° ', lista_resultado[0][2] , ' con fecha de sanción: ', lista_resultado[0][3], ' Descripcion: ', lista_resultado[0][4])
    id_norm = int (lista_resultado[0][0])
#    micursor.close    
    nuevo_texto = input ('''
Ingrese el nuevo texto descriptivo: ''')
#    micursor = conexion.cursor()
    sql = "UPDATE normativa SET descripcion = '"+ nuevo_texto  + "' WHERE id_normativa =" +str(id_norm) 
    micursor.execute(sql)
    conexion.commit()
    print ('''
La normativa fue modificar con éxito''')
    conn.cerrarconectarbd (conexion)
####################################### FIN DE FUNCION MODIFICAR #######################################

####################################### INICIO DE MAIN ####################################################
BD_USUARIO = "ispc"             #input ('Ingrese usuario de Base de Datos: ')
BD_PASSWORD = "Ispc*2023"       #input ("Ingrese la contraseña: ")
menu_principal (BD_USUARIO,BD_PASSWORD)

####################################### FIN DE MAIN #######################################################

