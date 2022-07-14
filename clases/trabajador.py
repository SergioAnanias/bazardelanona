from clases.baseDatos import BaseDatos
from enum import Enum
import bcrypt
from datetime import datetime

class Cargo(Enum):
    ADMINISTRADOR_GLOBAL = 1
    VENDEDOR = 2
    JEFE_DE_VENTAS = 3

class Empleado():
    def __init__(self, idEmpleado, nombreEmpleado, cargo, primerLogin):
        self.__idEmpleado = idEmpleado
        self.__nombreEmpleado = nombreEmpleado
        self.__cargo = Cargo(cargo)
        self.__primerLogin = primerLogin
    @staticmethod
    def createUser(idEmpleado, nombreEmpleado,contraseña, cargo):
        password = str(contraseña)
        pw =  bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        today = datetime.now()
        sql = f"insert into empleado (idEmpleado, nombreEmpleado, contraseña, date_creation, date_update, idCargo, firstLogin, status) values ({idEmpleado}, '{nombreEmpleado}','{pw}', '{today}','{today}',{cargo}, true, 'A');"
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
                return Empleado(empleado['idEmpleado'], empleado['nombreEmpleado'], empleado['idCargo'], empleado['firstLogin'])
            return False
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
    @staticmethod
    def checkUsers():
        __bd = BaseDatos()
        sql = f"SELECT * FROM empleado where STATUS='A'"
        __bd.cursor.execute(sql)
        empleados = __bd.cursor.fetchall()
        fields = [field[0] for field in __bd.cursor.description]
        empleados = [dict(zip(fields,empleado)) for empleado in empleados]
        if(len(empleados)>0):
            return True
        return False
    @staticmethod
    def getUser(idEmpleado):
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
        sql = f"UPDATE empleado SET contraseña='{pw}', firstLogin = False where idEmpleado = {self.__idEmpleado} and status='A'"
        __bd.cursor.execute(sql)
        __bd.commit()
    def changePermission(self, idEmpleado, permission):
        __bd = BaseDatos()
        newPermission = permission.value
        sql = f"UPDATE empleado SET idcargo={newPermission} where idEmpleado = {idEmpleado}"
        __bd.cursor.execute(sql)
        __bd.commit()
    @staticmethod
    def darBajaUsuario(idUsuario):
        __bd = BaseDatos()
        sql=f"update empleado set status = 'B' where idEmpleado = {idUsuario}"
        __bd.cursor.execute(sql)
        __bd.commit()
    @staticmethod
    def darAltaUsuario(idUsuario):
        __bd = BaseDatos()
        sql=f"update empleado set status = 'A' where idEmpleado = {idUsuario}"
        __bd.cursor.execute(sql)
        __bd.commit()
