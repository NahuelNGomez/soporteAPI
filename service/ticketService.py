from dataclasses import asdict
from config.db import conn
from models.models import tickets
from schemes.ticket import Ticket
from schemes.ticketConNombre import TicketConNombre
from service.productoService import ProductoService
from sqlalchemy import and_

productoService = ProductoService()

class TicketService():

    def getTickets(self):
        return conn.execute(tickets.select()).fetchall()
    
    def crearTicket(self, nuevoTicket):
        return conn.execute(tickets.insert().values(nuevoTicket))
    
    def getLastIdTicketAdded(self):
        return conn.execute(tickets.select()).fetchall()[-1].id
    
    def getTicketByID(self, id):
        return conn.execute(tickets.select().where(tickets.c.id == id)).first()

    def getTicketBySeveridad(self, severidad, idVersion):
        query = tickets.select().where(and_(tickets.c.Severidad == severidad, tickets.c.idVersion == idVersion))
        result_proxy = conn.execute(query)
        rows = result_proxy.fetchall()
        tickets_list = []
        for row in rows:
            ticket = Ticket(
                id=row.id,
                FechaDeCreacion= row.FechaDeCreacion,
                FechaDeFinalizacion= row.FechaDeFinalizacion,
                Nombre=row.Nombre,
                Descripcion=row.Descripcion,
                Escenario=row.Escenario,
                Estado=row.Estado,
                Severidad=row.Severidad,
                idVersion=row.idVersion,
                CUIT=row.CUIT,
                RecursoAsignado=row.RecursoAsignado
            )
            
            tickets_list.append(ticket)
        
        return tickets_list
        
    #def getTicketByProducto(self, nombreProducto):
        # se busca el codigo del producto:
        codigoProducto = productoService.getCodigoProductoByNombre(nombreProducto)
        if codigoProducto == None:
           return None
        
        # se busca sus idVersion:
        versiones_list = versionService.getVersionsByCodigoProducto(codigoProducto)

        # busco los tickets por idVersion:
        tickets_list = []
        for version in versiones_list:
            query = tickets.select().where(tickets.c.idVersion == version)
            result_proxy = conn.execute(query)
            rows = result_proxy.fetchall()
            
            for row in rows:
                ticket = Ticket(
                    id=row.id,
                    FechaDeCreacion= row.FechaDeCreacion,
                    FechaDeFinalizacion= row.FechaDeFinalizacion,
                    Nombre=row.Nombre,
                    Descripcion=row.Descripcion,
                    Escenario=row.Escenario,
                    Estado=row.Estado,
                    Severidad=row.Severidad,
                    idVersion=row.idVersion,
                    CUIT=row.CUIT,
                    RecursoAsignado=row.RecursoAsignado
                )
                tickets_list.append(ticket)
        
        return tickets_list


    def getTicketByCUIT(self, CUIT):
        query = tickets.select().where(tickets.c.CUIT == str(CUIT))
        result_proxy = conn.execute(query)
        rows = result_proxy.fetchall()
    
        tickets_list = []
        for row in rows:
            ticket = Ticket(
                id=row.id,
                FechaDeCreacion= row.FechaDeCreacion,
                FechaDeFinalizacion= row.FechaDeFinalizacion,
                Nombre=row.Nombre,
                Descripcion=row.Descripcion,
                Escenario=row.Escenario,
                Estado=row.Estado,
                Severidad=row.Severidad,
                idVersion=row.idVersion,
                CUIT=row.CUIT,
                RecursoAsignado=row.RecursoAsignado
            )
            tickets_list.append(ticket)
        
        return tickets_list
    
    def deleteTicket(self, id):
        return conn.execute(tickets.delete().where(tickets.c.id == id))
    
    def updateTicket(self, id, update_data):
        return conn.execute(tickets.update().values(**update_data).where(tickets.c.id == int(id)))
    
    def getTicketsByIdVersion(self, idVersion):
        query = tickets.select().where(tickets.c.idVersion == idVersion)
        result_proxy = conn.execute(query)
        rows = result_proxy.fetchall()
        tickets_list = []
        for row in rows:
            ticket = Ticket(
                id=row.id,
                FechaDeCreacion= row.FechaDeCreacion,
                FechaDeFinalizacion= row.FechaDeFinalizacion,
                Nombre=row.Nombre,
                Descripcion=row.Descripcion,
                Escenario=row.Escenario,
                Estado=row.Estado,
                Severidad=row.Severidad,
                idVersion=row.idVersion,
                CUIT=row.CUIT,
                RecursoAsignado=row.RecursoAsignado
            )
            tickets_list.append(ticket)
        
        return tickets_list