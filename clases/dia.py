from clases.baseDatos import BaseDatos
from datetime import date, datetime
import time
class Dia():
    def __init__(self, empleado):
        self.__idDia = None
        self.__Fecha = None
        self.__horaApertura = None
        self.__horaCierre = None
        self.__empleadoApertura = None
        self.__empleadoCierre = None
        diaAbierto = self.getDiaAbierto()
        if(diaAbierto == False):
            self.setFecha()
            self.setHoraApertura()
            self.setEmpleadoApertura(empleado)
    @staticmethod
    def checkDia():
        __bd = BaseDatos()
        # Query para guardar venta en tabla venta
        sql = "select idDia, fecha, horaApertura, empleadoApertura from dia where horaCierre is null and empleadoCierre is null order by idDia desc limit 1"
        __bd.cursor.execute(sql)
        dia = __bd.cursor.fetchone()
        if(dia == None):
            return False
        else:
            return dia
    def setFecha(self):
        self.__Fecha= date.today()
    def setHoraApertura(self):
        self.__horaApertura = time.strftime("%H:%M:%S")
    def setEmpleadoApertura(self, empleado):
        self.__empleadoApertura=empleado
    def cierreDia(self, empleado):
        self.__horaCierre = time.strftime("%H:%M:%S")
        self.__empleadoCierre = empleado
    def abrirDia(self):
        __bd = BaseDatos()
        # Query para guardar venta en tabla venta
        sql = f"INSERT INTO dia (fecha, horaApertura, date_creation,date_update, empleadoApertura) values ('{self.__Fecha}','{self.__horaApertura}',NOW(),NOW(),  {self.__empleadoApertura})"
        __bd.cursor.execute(sql)
        __bd.commit()
    def getDiaAbierto(self):
            __bd = BaseDatos()
            # Query para guardar venta en tabla venta
            sql = "select idDia, fecha, horaApertura, empleadoApertura from dia where horaCierre is null and empleadoCierre is null order by idDia desc limit 1"
            __bd.cursor.execute(sql)
            dia = __bd.cursor.fetchone()
            if(dia == None):
                return False
            else:
                self.__idDia = dia[0]
                self.__Fecha = str(dia[1])
                self.__horaApertura = str(dia[2])
                self.__empleadoApertura = dia[3]
    def cierreDia(self, empleado):
        cierre = time.strftime("%H:%M:%S")
        __bd = BaseDatos()
        # Query para guardar venta en tabla venta
        sql = f"UPDATE dia SET horaCierre = '{cierre}', empleadoCierre = {empleado} where idDia={self.__idDia}"
        __bd.cursor.execute(sql)
        __bd.commit()

