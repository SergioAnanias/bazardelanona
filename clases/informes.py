from tabulate import tabulate
from baseDatos import BaseDatos

class Informes():
    @staticmethod
    def getInformesBoletaByDate(date):
        __bd = BaseDatos()
        sql = f'''select idEmpleado, nombreEmpleado, SUM(valorNeto) as 'Total Valor Neto', sum(valorBruto) as 'Total Valor Bruto', valorBruto-valorNeto as 'IVA', COUNT(idVenta) as 'Ventas con Boleta' from venta
        inner join empleado
        on empleado.idEmpleado = venta.idVendedor
        where idTipoDocumento=1 
        and venta.date_creation between '{date} 00:00:00' AND '{date} 23:59:59'
        group by empleado.idEmpleado;
        '''
        __bd.cursor.execute(sql)
        boletas = __bd.cursor.fetchall()
        print('-'*30+'Boletas'+'-'*30)

        print(tabulate(boletas, headers=["ID empleado", "Nombre Empleado", "Total Neto", "Total Bruto", "IVA", "Total boletas"]))
    @staticmethod
    def getInformesFacturaByDate(date):
        __bd = BaseDatos()
        sql = f'''select idEmpleado, nombreEmpleado, venta.valorNeto as 'Total Valor Neto', valorBruto as 'Total Valor Bruto', valorBruto-valorNeto as 'IVA' from venta
        inner join empleado
        on empleado.idEmpleado = venta.idVendedor
        where idTipoDocumento=2
        and venta.date_creation between "{date} 00:00:00" AND "{date} 23:59:59";
        '''
        __bd.cursor.execute(sql)
        boletas = __bd.cursor.fetchall()
        print('-'*30+'Facturas'+'-'*30)
        print(tabulate(boletas, headers=["ID empleado", "Nombre Empleado", "Total Neto", "Total Bruto", "IVA", "Total boletas"]))
    @staticmethod
    def getInformesBoletaByUser(idEmpleado):
        __bd = BaseDatos()
        sql = f'''select idEmpleado, nombreEmpleado, SUM(valorNeto) as 'Total Valor Neto', sum(valorBruto) as 'Total Valor Bruto', valorBruto-valorNeto as 'IVA', COUNT(idVenta) as 'Ventas con Boleta' from venta
        inner join empleado
        on empleado.idEmpleado = venta.idVendedor
        where idTipoDocumento=1 
        and empleado.idEmpleado ={idEmpleado}
        group by empleado.idEmpleado;
        '''
        __bd.cursor.execute(sql)
        boletas = __bd.cursor.fetchall()
        print('-'*30+'Boletas'+'-'*30)
        print(tabulate(boletas, headers=["ID empleado", "Nombre Empleado", "Total Neto", "Total Bruto", "IVA", "Total boletas"]))
    def getInformesFacturaByUser(idEmpleado):
        __bd = BaseDatos()
        sql = f'''select idEmpleado, nombreEmpleado, venta.valorNeto as 'Total Valor Neto', valorBruto as 'Total Valor Bruto', valorBruto-valorNeto as 'IVA' from venta
        inner join empleado
        on empleado.idEmpleado = venta.idVendedor
        where idTipoDocumento=
        and venta.date_creation between "{date} 00:00:00" AND "{date} 23:59:59";
        '''
        __bd.cursor.execute(sql)
        boletas = __bd.cursor.fetchall()
        print('-'*30+'Facturas'+'-'*30)
        print(tabulate(boletas, headers=["ID empleado", "Nombre Empleado", "Total Neto", "Total Bruto", "IVA", "Total boletas"]))
