from fastapi import HTTPException
from config.db import conn
from models.models import tareasAsignadas
from schemes.tareaAsignada import TareaAsignada


class TareaAsignadaService():

    def verificaTareaNoAsignada(self, tarea):
        query = tareasAsignadas.select().where(tareasAsignadas.c.idTarea == tarea["idTarea"])
        result_proxy = conn.execute(query)
        rows = result_proxy.fetchall()
        for row in rows:
            if (row.id == tarea["id"]):
                return False
        return True    

    def getTareasAsignadas(self):
        return conn.execute(tareasAsignadas.select()).fetchall()
    
    def crearTareaAsignada(self, nuevaTarea):
        if(self.verificaTareaNoAsignada(nuevaTarea)):
            return conn.execute(tareasAsignadas.insert().values(nuevaTarea))
        raise HTTPException(status_code=500, detail="Error en parámetros")
    

    def getTareasAsignadasByIdTarea(self, idTarea):

        query = tareasAsignadas.select().where(tareasAsignadas.c.idTarea == idTarea)
        result_proxy = conn.execute(query)
        rows = result_proxy.fetchall()
    
        tarea_list = []
        for row in rows:
            tareaAsignada = TareaAsignada(
                codigoDeAsignacion = row.codigoDeAsignacion,
                idTarea=row.idTarea,
               id=row.id
            )
            tarea_list.append(tareaAsignada)
         
        return tarea_list


    def getTareasAsignadasByIdTicket(self, idTicket):
        query = tareasAsignadas.select().where(tareasAsignadas.c.id == idTicket)
        result_proxy = conn.execute(query)
        rows = result_proxy.fetchall()
    
        tarea_list = []

        # Deberia devolver una lista de tareas (con toda la info), a partir de un get del id de la tarea.
        for row in rows:
            tareaAsignada = TareaAsignada(
                codigoDeAsignacion = row.codigoDeAsignacion,
                idTarea=row.idTarea,
                id=row.id
            )
            tarea_list.append(tareaAsignada)
        
        return tarea_list

    def deleteTareaAsignada(self, codigoDeAsignacion):
        return conn.execute(tareasAsignadas.delete().where(tareasAsignadas.c.codigoDeAsignacion == codigoDeAsignacion))
    
    def getLastCodigoDeAsignacionAdded(self):
        return conn.execute(tareasAsignadas.select()).fetchall()[-1].codigoDeAsignacion