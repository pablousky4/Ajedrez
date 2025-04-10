import sqlite3

class SQL:
    def __init__(self, nombre_bd):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()

    def ejecutar(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.conexion.commit()

    def consultar(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()

    def cerrar(self):
        self.conexion.close()

    def crear_tabla(self, tabla, columnas):
        consulta = f"CREATE TABLE IF NOT EXISTS {tabla} ({columnas})"
        self.ejecutar(consulta)

    def insertar(self, tabla, columnas, valores):

        marcadores = ", ".join(["?"] * len(valores))
        consulta = f"INSERT INTO {tabla} ({columnas}) VALUES ({marcadores})"
        self.ejecutar(consulta, valores)

    def obtener_todos(self, tabla):

        consulta = f"SELECT * FROM {tabla}"
        return self.consultar(consulta)
