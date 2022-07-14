from clases.trabajador import Empleado, Cargo
from menuVendedor import menuVendedor
from menuJefeVentas import menuJefeVentas
def login():
    rut=input('Ingrese su nombre de usuario o deje en blanco para salir:\n')
    password = input('Ingrese su password:\n')
    if(rut == ''):
        print('Adios')
        return
    empleado = Empleado.loginUser(rut, password)
    if(empleado == False):
        print("Los datos ingresados son incorrectos, porfavor intente nuevamente")
        login()
    if(empleado.__dict__['_Empleado__primerLogin'] == True):
        newPassword = input('Ingrese una nueva contraseña')
        empleado.changePassword(newPassword)
        menu(empleado)
    else:
        menu(empleado)

def menu(empleado):
    if(empleado.__dict__['_Empleado__cargo'] == Cargo.VENDEDOR):
        menuVendedor(empleado)
    elif(empleado.__dict__['_Empleado__cargo'] == Cargo.JEFE_DE_VENTAS):
        menuJefeVentas(empleado)
    elif(empleado.__dict__['_Empleado__cargo']== Cargo.ADMINISTRADOR_GLOBAL):
        menuAdminGlobal(empleado)

def register():
    rut = input('Ingrese el rut del nuevo empleado\n')
    checkUser=Empleado.getUser(rut)
    if(checkUser!= None):
        nombreEmpleado= input('Ingrese el nombre completo del nuevo empleado\n')
        password = input('Ingrese una contraseña para el nuevo empleado\n')
        cargo = input('Seleccione el cargo a tener el nuevo empleado:\n 1 = Administrador Global\n 2 = Vendedor\n 3 = Jefe de Ventas\n')
        Empleado.createUser(rut, nombreEmpleado, password, cargo)
        login()
    else:
        print('Ya se encuentra en base de datos, se procederá a dar de alta')
        Empleado.darAltaUsuario(rut)



if(Empleado.checkUsers()):    
    login()
else:
    register()