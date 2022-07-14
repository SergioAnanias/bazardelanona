from clases.ventas import Venta
from clases.dia import Dia
from clases.productos import Product
def menuVendedor(empleado):
    empleadoDict = empleado.__dict__
    inputVenta= input('Presione 1 para comenzar una nueva venta\n')
    if (inputVenta=='1'):
        dia = Dia.checkDia()
        if(dia != None):
            venta = Venta(empleadoDict['_Empleado__idEmpleado'], dia[0])
            agregarProductos = True
            while(agregarProductos == True):
                inputProductos = input('Presione \n 1 = Para mostrar todos los productos\n2 = para buscar un producto su SKU\n 0=para salir\n')
                if(inputProductos == '1'):
                    Product.getAllProduct()
                    idProducto=input('Seleccione el ID del producto que desea agregar\n')
                    cantidad = int(input('Ingrese la cantidad de unidades\n'))
                    producto = Product.selectProductById(idProducto, cantidad)
                    venta.appendProduct(producto)
                    print(venta.__dict__)
                    continuar = input('Desea agregar más productos?\n1 = Si\n2 = No\n')
                    if(continuar=='1'):
                        continue
                    elif(continuar=='2'):
                        agregarProductos= False
                elif(inputProductos=='2'):
                    skuProducto = input('Ingrese el SKU del producto a agregar\n')
                    cantidad = int(input('Ingrese la cantidad de unidades\n'))
                    producto = Product.selectProductBySKU(skuProducto, cantidad)
                    confirmacion = input(f'Desea agregar {producto} al carrito?\n 1 = Si \n 2= No')
                    if(confirmacion == '1'):
                        venta.appendProduct(producto)
                    else:
                        continue
                elif(inputProductos=='0'):
                    menuVendedor(empleado)
            tipoDocumento = int(input('Elija el tipo de document\n 1 = Boleta\n 2 = Factura \n 0=Salir\n'))
            if(tipoDocumento == 1):
                venta.setDocumento(tipoDocumento)
                venta.mostrarBoleta()
                confirmacion = int(input('Desea cerrar la venta?\n 1 = Si\n 2 = No\n'))
                if(confirmacion==1):
                    venta.guardarVenta()
                    menuVendedor(empleado)
                elif(confirmacion== 2):
                    menuVendedor(empleado)
            elif(tipoDocumento==2):
                venta.setDocumento(tipoDocumento)
                razonSocial = input('Ingrese la razon social de la empresa\n')
                rutCliente = input('Ingrese el rut de la empresa\n')
                giro = input('Ingrese el giro de la empresa\n')
                direccion = input('Ingrese la dirección de la empresa\n')
                venta.setDatosFactura(razonSocial, rutCliente, giro,direccion)
                venta.guardarVenta()
                venta.mostrarFactura()
                confirmacion = int(input('Desea cerrar la venta?\n 1 = Si\n 2 = No\n'))
                if(confirmacion==1):
                    venta.guardarVenta()
                    menuVendedor(empleado)
                elif(confirmacion== 2):
                    menuVendedor(empleado)
            elif(tipoDocumento == 0):
                menuVendedor(empleado)
            else:
                print('Valor no valido')
        else:
            print('No existe un día abierto para realizar venta, consulte con su jefe de ventas')
            return False