import mysql.connector
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

####################################### INICIO DE CONSULTAR POR NUMERO #######################################
def consultar_num(BD_USUARIO,BD_PASSWORD):
    # Código para buscar los tipos de normativas en la BD
    # Creo el Objeto Conexion
    conn = Conexionbd(BD_USUARIO,BD_PASSWORD)
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

BD_USUARIO = input ('Ingrese usuario de Base de Datos: ')
BD_PASSWORD = input ("Ingrese la contraseña: ")
consultar_num(BD_USUARIO,BD_PASSWORD)