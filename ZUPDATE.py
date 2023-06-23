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

####################################### INICIO DE FUNCION MODIFICAR #######################################
def modificar_normativa(BD_USUARIO,BD_PASSWORD):
    # Código para buscar los tipos de normativas en la BD
    # Creo el Objeto Conexion
    conn = Conexionbd(BD_USUARIO,BD_PASSWORD)
    # Abro la conexion instanciando el metodo conectarbd
    conexion = conn.conectarbd()
    # Decalro y asigno el cursor de la conexion a la BD
    micursor = conexion.cursor()
    # Ejecuto la SQL para bucar tipos de normativas
    num_norm = input('Ingrese el número de normativa que desea modificar: ')
    micursor.execute("SELECT normativa.id_normativa, tipo_normativa.descripcion, normativa.numero, normativa.fecha, normativa.descripcion FROM normativa  inner join tipo_normativa using (id_tipo_normativa) WHERE NORMATIVA.NUMERO =" + num_norm)
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

BD_USUARIO = input ('Ingrese usuario de Base de Datos: ')
BD_PASSWORD = input ("Ingrese la contraseña: ")
modificar_normativa(BD_USUARIO,BD_PASSWORD)