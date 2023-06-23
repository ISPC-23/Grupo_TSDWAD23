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
        return f"Normativa\n{self.tipo} N° {self.numero}\n\
Jurisdicción {self.jurisdiccion}\n\
Organo legislativo: {self.organo}\n\
Fecha: {self.fecha}\n\
Categoría: {self.categoria}\n\
Palabras claves: {self.p_claves}\n\
{self.descripcion}"

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
        self.user=user
        self.password=password
        self.database="bdnormativa"
    def conectarbd(self):
        #import mysql.connector
        miConexion=mysql.connector.connect(host=self.host, 
                                  user=self.user, 
                                  password=self.password,
                                  database=self.database)
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
    normativas = []
    myBD = Conexionbd("ispc","Ispc*2023")
    bdConectada = myBD.conectarbd()
    bdCursor = bdConectada.cursor()
    sql = "SELECT TP.descripcion, N.numero, N.fecha, N.descripcion, C.descripcion,\
            J.descripcion, OL.descripcoin\
        FROM normativa AS N, tipo_normativa AS TP, categoria AS C, jurisdiccion AS J,\
            organo_legislativo AS OL\
        WHERE N.id_tipo_normativa = TP.id_tipo_normativa AND\
            N.id_categoria = C.id_categoria AND\
            N.id_jurisdiccion = J.id_jurisdiccion AND\
            N.id_organo_legislativo = OL.id_organo_legislativo"
    bdCursor.execute(sql)
    registros = bdCursor.fetchall()
    for registro in registros:
        nueva_norm = Normativa(
            registro[0],
            registro[1],
            registro[2],
            registro[3],
            registro[4],
            registro[5],
            registro[6]
        )
        normativas.append(nueva_norm)
    bdCursor.close()
    myBD.cerrarconectarbd(bdConectada)
    return normativas

# Consultar Normativa por numero
def consultar_num(numero):
    pass

# Consultar Normativa por palabra clave
def consultar_clave(p_clave):
    normativas = []
    myBD = Conexionbd("ispc","Ispc*2023")
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

# Menu principal
def menu_principal():
    pass
