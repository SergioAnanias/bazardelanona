from .baseDatos import BaseDatos

class Product():
    def __init__(self):
        self.__bd = BaseDatos()
        self.__id = 123
        self.__sku = 'dasj'
        self.__descProducto = 'dajslk'
        self.__precioUnitario = 213
    def getAllProduct(self):
        sql = "SELECT * FROM PRODUCTO"
        self.__bd.cursor.execute(sql)
        productos = self.__bd.cursor.fetchall()
        return productos