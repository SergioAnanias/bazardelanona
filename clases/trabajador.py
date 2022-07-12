from baseDatos import BaseDatos
from enum import Enum
import bcrypt
from datetime import datetime

class Cargo(Enum):
    ADMINISTRADOR_GLOBAL = 1
    VENDEDOR = 2
    JEFE_DE_VENTAS = 3

class Empleado():
    def __init__(self, idEmpleado, nombreEmpleado, cargo):
        self.__idEmpleado = idEmpleado
        self.__nombreEmpleado = nombreEmpleado
        self.__cargo = Cargo(cargo)
    def __repr__(self):
        return f'datos empleado {self.__idEmpleado},{self.__nombreEmpleado},{self.__cargo.name}'
    @staticmethod
    def createUser(idEmpleado, nombreEmpleado,contraseña, cargo):
        password = str(password)
        pw =  bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        today = datetime.now()
        sql = f"insert into empleado (idEmpleado, nombreEmpleado, contraseña, date_creation, date_update, idCargo) values ({idEmpleado}, '{nombreEmpleado}','{pw}', '{today}','{today}',{cargo});"
        __bd = BaseDatos()
        __bd.cursor.execute(sql)
        __bd.commit()
    @staticmethod
    def loginUser(idEmpleado, password):
        try:
            __bd = BaseDatos()
            sql = f"SELECT * FROM EMPLEADO where idEmpleado = {idEmpleado}"
            __bd.cursor.execute(sql)
            data = __bd.cursor.fetchall()
            fields = [field[0] for field in __bd.cursor.description]
            empleado = [dict(zip(fields,empleado)) for empleado in data]
            if(Empleado.validateUser(empleado[0], password)):
                empleado = empleado[0]
                return Empleado(empleado['idEmpleado'], empleado['nombreEmpleado'], empleado['idCargo'])
            return 'Los datos ingresados son incorrectos'
        finally:
            __bd.cursor.close()
            __bd.conexion.close()
    @staticmethod
    def validateUser(empleado, password):
        if (empleado != None):
            password = str(password)
            if bcrypt.checkpw(password.encode(), empleado['contraseña'].encode()):
                return True
        else:
            return False
    def getUser(self, idEmpleado):
        __bd = BaseDatos()
        sql = f"SELECT * FROM empleado where idEmpleado = {idEmpleado}"
        __bd.cursor.execute(sql)
        empleados = __bd.cursor.fetchall()
        fields = [field[0] for field in __bd.cursor.description]
        empleados = [dict(zip(fields,empleado)) for empleado in empleados]
        return empleados
    def changePassword(self, password):
        __bd = BaseDatos()
        pw =  bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        sql = f"UPDATE empleado SET contraseña='{pw}' where idEmpleado = {self.__idEmpleado}"
        __bd.cursor.execute(sql)
        __bd.commit()
    def changePermission(self, idEmpleado, permission):
        __bd = BaseDatos()
        newPermission = permission.value
        print(newPermission)
        sql = f"UPDATE empleado SET idcargo={newPermission} where idEmpleado = {idEmpleado}"
        __bd.cursor.execute(sql)
        __bd.commit()
    def deleteUser():
        pass

empleado = Empleado.loginUser(188758851,'asjld')
print(empleado)
empleado2=empleado.getUser(188758851)
print(empleado2[0])