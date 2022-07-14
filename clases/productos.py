from clases.baseDatos import BaseDatos
from datetime import datetime
from tabulate import tabulate

class Product():
    def __init__(self, sku, descProducto, precioUnitario, cantidad = 0, id=0):
        self.__id=id
        self.__sku = sku
        self.__descProducto = descProducto
        self.__precioUnitario = precioUnitario
        self.__cantidad = cantidad
    def __repr__(self):
        return f'{self.__descProducto}'
    @staticmethod
    def getAllProduct():
        __bd = BaseDatos()
        sql = "SELECT idProducto, SKU, descProducto, precioUnitario, date_creation, date_update, user_register, user_update FROM PRODUCTO where status = 'A'"
        __bd.cursor.execute(sql)
        productos = __bd.cursor.fetchall()
        print (tabulate(productos, headers=["ID", "SKU", "Nombre", "Precio Unitario", "Fecha Creacion", "Fecha Actualizacion", "Usuario Creacion", "Usuario Actualizacion"]))
        return productos
    @staticmethod
    def selectProductBySKU(SKU,cantidad):
        __bd = BaseDatos()
        sql = f"SELECT * FROM PRODUCTO where SKU = {SKU}"
        __bd.cursor.execute(sql)
        producto = __bd.cursor.fetchall()
        print(producto)
        if(len(producto)>0):
            fields = [field[0] for field in __bd.cursor.description]
            producto = dict(zip(fields,producto[0]))
            return Product(producto['SKU'], producto['descProducto'], producto['precioUnitario'], cantidad)
    @staticmethod
    def selectProductById(id, cantidad):
        __bd = BaseDatos()
        sql = f"SELECT * FROM PRODUCTO where idProducto = {id} and status = 'A'"
        __bd.cursor.execute(sql)
        producto = __bd.cursor.fetchall()
        if(len(producto)>0):
            fields = [field[0] for field in __bd.cursor.description]
            producto = dict(zip(fields,producto[0]))
            return Product(producto['SKU'], producto['descProducto'], producto['precioUnitario'], cantidad,producto['idProducto'])
        else:
            print("no se ha encontrado nada")
            return False
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
    def updateProduct(self,  idProducto, userUpdate):
        dateUpdate =  datetime.now()
        __bd = BaseDatos()
        sql = f"UPDATE producto SET sku = {self.__sku}, descProducto = '{self.__descProducto}', precioUnitario = {self.__precioUnitario}, user_update = {userUpdate}, date_update = '{dateUpdate}' where idProducto = {idProducto}"
        __bd.cursor.execute(sql)
        __bd.commit()
    def setCantidadProducto(self, cantidad):
        self.__cantidad = cantidad
    def deleteProduct(self, idProducto, userUpdate):
        dateUpdate =  datetime.now()
        __bd = BaseDatos()
        sql = f"UPDATE producto SET status='B',date_update='{dateUpdate}', user_update={userUpdate} where idProducto = {idProducto}"
        __bd.cursor.execute(sql)
        __bd.commit()



