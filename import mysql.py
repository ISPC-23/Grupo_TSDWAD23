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
            