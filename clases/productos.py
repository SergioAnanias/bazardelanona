from baseDatos import BaseDatos
from datetime import datetime
from tabulate import tabulate

class Product():
    def __init__(self, idProducto, sku, descProducto, precioUnitario):
        self.__idProducto = idProducto
        self.__sku = sku
        self.__descProducto = descProducto
        self.__precioUnitario = precioUnitario
    def __repr__(self):
        return f'{self.__sku}, {self.__descProducto}, {self.__precioUnitario}'
    @staticmethod
    def getAllProduct():
        __bd = BaseDatos()
        sql = "SELECT * FROM PRODUCTO"
        __bd.cursor.execute(sql)
        productos = __bd.cursor.fetchall()
        print (tabulate(productos, headers=["ID", "SKU", "Nombre", "Precio Unitario", "Fecha Creacion", "Fecha Actualizacion", "Usuario Creacion", "Usuario Actualizacion"]))
        return productos
    @staticmethod
    def getProductBySKU(SKU):
        __bd = BaseDatos()
        sql = f"SELECT * FROM PRODUCTO where SKU = {SKU}"
        __bd.cursor.execute(sql)
        productos = __bd.cursor.fetchall()
        return productos
    @staticmethod
    def selectProductById(id):
        __bd = BaseDatos()
        sql = f"SELECT * FROM PRODUCTO where idProducto = {id}"
        __bd.cursor.execute(sql)
        producto = __bd.cursor.fetchall()
        if(len(producto)>0):
            fields = [field[0] for field in __bd.cursor.description]
            producto = dict(zip(fields,producto[0]))
            return Product(producto['idProducto'], producto['SKU'], producto['descProducto'], producto['precioUnitario'])
        else:
            print("no se ha encontrado nada")
    def createProduct(self, userRegister):
        dateCreation =  datetime.now()
        __bd = BaseDatos()
        sql = f"INSERT INTO producto (SKU, descProducto, precioUnitario, date_creation, user_register) VALUES ('{self.__sku}','{self.__descProducto}', {self.__precioUnitario},'{dateCreation}','{userRegister}')"
        __bd.cursor.execute(sql)
        __bd.commit()
    def setSku(self, sku):
        self.__sku = sku
    def setdescProducto(self, descProducto):
        self.__descProducto= descProducto
    def setPrecioUnitario(self, precioUnitario):
        self.__precioUnitario = precioUnitario
    def updateProduct(self, userUpdate):
        dateUpdate =  datetime.now()
        __bd = BaseDatos()
        sql = f"UPDATE producto SET sku = {self.__sku}, descProducto = '{self.__descProducto}', precioUnitario = {self.__precioUnitario}, user_update = {userUpdate}, date_update = '{dateUpdate}' where idProducto = {self.__idProducto}"
        __bd.cursor.execute(sql)
        __bd.commit()
    def deleteProduct(self):
        pass



producto = Product.selectProductById(3)
print(producto)

