import mysql.connector

class BaseDatos:
    def __init__ (self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="mydb"
        )
        self.cursor = self.conexion.cursor()
