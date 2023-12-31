from config.db import conn
from models.models import versiones
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from schemes.versionConNombre import VersionConNombre

from service.productoService import ProductoService
from service.tareaAsignadaService import TareaAsignadaService
from service.ticketService import TicketService

productoService = ProductoService()
ticketService = TicketService()
tareaAsignadaService = TareaAsignadaService()

class VersionService():

    def getVersiones(self):
        versiones_query = conn.execute(versiones.select()).fetchall()
        versiones_list = []
        for row in versiones_query:
            newVersion = VersionConNombre(
                idVersion= row.idVersion,
                idProyecto= row.idProyecto,
                CodigoVersion=row.CodigoVersion,
                CodigoProducto=row.CodigoProducto,
                NombreProducto= productoService.getProducto(row.CodigoProducto).Nombre,
                Estado=row.Estado
            )
            versiones_list.append(newVersion)
        
        return versiones_list

    def crearVersion(self, nuevaVersion):
        return conn.execute(versiones.insert().values(nuevaVersion))
    
    def calcularTiempo(self, ticket):
        return ((ticket.FechaDeFinalizacion - ticket.FechaDeCreacion).days)
    
    def getPromedioTickets(self, severidad, idVersion):
        tickets = ticketService.getTicketBySeveridad(severidad, idVersion)
        sumaTiempo = 0
        promedioTotal = 0
        cerrados = 0
        for ticket in tickets:
            if(ticket.estaCerrado()):
                cerrados += 1
                sumaTiempo += self.calcularTiempo(ticket)
        if(cerrados != 0):
            promedioTotal = sumaTiempo/cerrados
        return promedioTotal
    def getProductoByIdVersion(self, idVersion):
        version = conn.execute(versiones.select().where(versiones.c.idVersion == idVersion)).first()
        return productoService.getProducto(version.CodigoProducto)

    def getVersionsByCodigoProducto(self, codigoProducto):
        versiones_query = conn.execute(versiones.select().where(versiones.c.CodigoProducto == codigoProducto))
        versiones_list = []
        for row in versiones_query:
            versiones_list.append(row.idVersion)
        return versiones_list

    def getVersion(self, idVersion):
        query = conn.execute(versiones.select().where(versiones.c.idVersion == idVersion)).first()
        return VersionConNombre(
                idVersion= query.idVersion,
                idProyecto= query.idProyecto,
                CodigoVersion=query.CodigoVersion,
                CodigoProducto=query.CodigoProducto,
                NombreProducto= productoService.getProducto(query.CodigoProducto).Nombre,
                Estado=query.Estado
        )
    
    def updateVersion(self, idVersion, update_data):
        return conn.execute(versiones.update().values(**update_data).where(versiones.c.idVersion == int(idVersion)))
        
    def getLastIdVersionAdded(self):
        return conn.execute(versiones.select()).fetchall()[0].idVersion

    def deleteVersion(self, id):
        return conn.execute(versiones.delete().where(versiones.c.idVersion == id))
    
    def deleteProyecto(self, id):
        tareaAsignadaService.eliminarByIdVersion(id)
        update_data = {"idProyecto": None}
        return conn.execute(versiones.update().values(**update_data).where(versiones.c.idVersion == int(id)))