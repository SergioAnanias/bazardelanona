from productos import Product
from baseDatos import BaseDatos

class Venta(BaseDatos):
    def __init__(self):
        self.bd = BaseDatos.__init__ 
        self.__productos =[Product]
        self.__valorNeto= 14
        self.__valorBruto = 123
        self.__vendedor = 1
        self.__idTipoDocumento = 2
        self.__idDia = 12
    def appendProduct(self,Producto):
        self.__productos.append(Product)
    def asignarDocumento(self, Documento):
        pass
    def mostrarBoleta(self):
        pass
    def mostrarFactura(self):
        pass