from clases.productos import Product
from clases.baseDatos import BaseDatos
from enum import Enum


class Venta(BaseDatos):
    def __init__(self,vendedor,dia , productos = [], valorNeto = 0, valorBruto=0, TipoDocumento = 0, factura= {}):
        self.__idVenta = None
        self.__productos =productos
        self.__valorNeto= valorNeto
        self.__valorBruto = valorBruto
        self.__vendedor = vendedor
        self.__idTipoDocumento = TipoDocumento
        self.__idDia = dia
        self.__factura = factura
        self.setIdVenta()
    def appendProduct(self,producto):
        self.__productos.append(producto.__dict__)
        self.actualizarValores(producto.__dict__)
    def setDocumento(self, idDocumento):
        self.__idTipoDocumento = idDocumento
    def setDatosFactura(self, razonSocial, rutCliente, giro, direccion):
        self.__factura['Razon Social'] = razonSocial
        self.__factura['Rut Cliente'] = rutCliente
        self.__factura['Giro'] = giro
        self.__factura['Direccion'] = direccion
    def mostrarBoleta(self):
        print(f'''Boleta
        id venta {self.__idVenta}
        valor neto {self.__valorNeto}
        valor bruto {self.__valorBruto}
        iva {self.__valorNeto*0.19}
        id vendedor {self.__vendedor}
        id tipo documento {self.__idTipoDocumento}
        id dia {self.__idDia}
        ''')
    def mostrarFactura(self):
        print(f'''Factura
        id venta {self.__idVenta}
        detalle productos {self.__productos}
        valor neto {self.__valorNeto}
        valor bruto {self.__valorBruto}
        vendedor {self.__vendedor}
        tipo documento {self.__idTipoDocumento}
        id dia {self.__idDia}
        datos factura {self.__factura}
        ''')
    def actualizarValores(self, producto):
        cantidadProducto = producto['_Product__cantidad']
        precioUnitario = producto['_Product__precioUnitario']
        self.__valorNeto += cantidadProducto*precioUnitario
        self.__valorBruto = self.__valorNeto*1.19
    def setIdVenta(self):
        venta = self.getUltimaVenta()
        if(venta == None):
            self.__idVenta=1
        else:
            self.__idVenta=venta[0]+1
    def getUltimaVenta(self):
            __bd = BaseDatos()
            # Query para guardar venta en tabla venta
            sql = "select idVenta from venta order by idVenta desc limit 1"
            __bd.cursor.execute(sql)
            venta = __bd.cursor.fetchone()
            return venta
    def guardarVenta(self):
        __bd = BaseDatos()
        # Query para guardar venta en tabla venta
        sqlVenta = f"INSERT INTO venta (idVenta, idVendedor, valorNeto, valorBruto, date_creation, date_update, idTipoDocumento, idDia) values ({self.__idVenta},{self.__vendedor},{self.__valorNeto}, {self.__valorBruto}, NOW(), NOW(), {self.__idTipoDocumento}, {self.__idDia})"
        __bd.cursor.execute(sqlVenta)
        for producto in self.__productos:
            valorNeto = producto['_Product__precioUnitario'] * producto['_Product__cantidad']
            valorTotal = valorNeto*1.19
            sqlDetalle = f"INSERT INTO detalleventa (cantidadProducto, valorNeto, valorTotal, date_creation, date_update, idProducto, idVenta) values ({producto['_Product__cantidad']},{valorNeto}, {valorTotal}, NOW(), NOW(), {producto['_Product__idProducto']}, {self.__idVenta})"
            __bd.cursor.execute(sqlDetalle)
        __bd.commit()
