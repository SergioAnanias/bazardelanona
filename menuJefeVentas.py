from clases.ventas import Venta
from clases.dia import Dia
from clases.productos import Product

def menuJefeVentas(empleado):
    empleadoDict= empleado.__dict__
    seleccion= int(input('Seleccione la opción con la que desea continuar:\n1 = Abrir día\n2 = Cerrar Dia\n3 = Gestionar Inventario\n4 = Registrar nuevo usuario\n0 = Salir'))
    if(seleccion == 1):
        diaAbierto = Dia.checkDia()
        if(diaAbierto):
            print('Ya existe un día abierto, debe cerrar primero el anterior')
            return menuJefeVentas(empleado)
        else:
            dia = Dia(empleadoDict['_Empleado__idEmpleado'])
            dia.abrirDia()
            return menuJefeVentas(empleado)
    elif(seleccion==2):
        diaAbierto = Dia.checkDia()
        if(diaAbierto):
            dia = Dia(empleadoDict['_Empleado__idEmpleado'])
            dia.cierreDia(empleadoDict['_Empleado__idEmpleado'])
        return menuJefeVentas(empleado)
    elif(seleccion==3):
        seleccion= int(input('Seleccione la opción con la que desea continuar:\n1 = Listar inventario\n2 = Agregar Item a inventario\n3 = Editar Item\n4 = Borrar item\n0 = Salir'))
        if(seleccion == 1):
            Product.getAllProduct()
            return menuJefeVentas(empleado)
        if(seleccion == 2):
            sku=input('Ingrese el SKU del producto')
            descProducto=input('Ingrese el nombre del producto')
            precioUnitario=int(input('Ingrese el valor unitario del producto'))
            producto = Product(sku,descProducto, precioUnitario)
            producto.createProduct(empleadoDict['_Empleado__idEmpleado'])
            return menuJefeVentas(empleado)
        if(seleccion == 3):
            Product.getAllProduct()
            idProducto = input('Ingrese el id del producto que desea editar\n')
            producto = Product.selectProductById(idProducto, cantidad=0)
            seleccion = input('¿Que valor desea editar?\n1 = SKU\n2 = Nombre del Producto\n3 = Precio unitario\n0 = Salir')
            if(producto == False):
                print('El id ingresado no es valido')
                return menuJefeVentas(empleado)
            if(seleccion=='1'):
                newSku=input('Ingrese el nuevo SKU\n')
                producto.setSku(newSku)
            elif(seleccion=='2'):
                newNombre=input('Ingrese el nuevo nombre')
                producto.setdescProducto(newNombre)
            elif(seleccion=='3'):
                newPrecio=int(input('Ingrese el nuevo precio unitario'))
                producto.setPrecioUnitario(newPrecio)
            elif(seleccion=='0'):
                return menuJefeVentas(empleado)
            producto.updateProduct(idProducto, empleadoDict['_Empleado__idEmpleado'])
            return menuJefeVentas(empleado)
        if(seleccion == 4):
            Product.getAllProduct()
            idProducto = input('Ingrese el id del producto que desea elimionar\n')
            producto = Product.selectProductById(idProducto, cantidad=0)
            producto.deleteProduct(idProducto,empleadoDict['_Empleado__idEmpleado'])
            return menuJefeVentas(empleado)
        if(seleccion == 0):
            pass
    elif(seleccion==4):
        rut = input('Ingrese el rut del nuevo empleado\n')
        checkUser=Empleado.getUser(rut)
        if(checkUser!= None):
            nombreEmpleado= input('Ingrese el nombre completo del nuevo empleado\n')
            password = input('Ingrese una contraseña para el nuevo empleado\n')
            cargo = input('Seleccione el cargo a tener el nuevo empleado:\n 1 = Administrador Global\n 2 = Vendedor\n 3 = Jefe de Ventas\n')
            Empleado.createUser(rut, nombreEmpleado, password, cargo)
        else:
            print('Ya se encuentra en base de datos, se procederá a dar de alta')
            Empleado.darAltaUsuario(rut)
    elif(seleccion==0):
        return
    else:
        print('Menu invalido')