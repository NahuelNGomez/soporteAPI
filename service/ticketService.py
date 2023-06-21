from config.db import conn
from models.models import tickets
from schemes.ticket import Ticket
from schemes.ticketConNombre import TicketConNombre
from service.productoService import ProductoService
from service.versionService import VersionService

productoService = ProductoService()
versionService = VersionService()

class TicketService():

    def getTickets(self):
        return conn.execute(tickets.select()).fetchall()
    
    def crearTicket(self, nuevoTicket):
        return conn.execute(tickets.insert().values(nuevoTicket))
    
    def getLastIdTicketAdded(self):
        return conn.execute(tickets.select()).fetchall()[-1].id
    

    def getTicketByID(self, id):
        return conn.execute(tickets.select().where(tickets.c.id == id)).first()
    
    def getTicketByCUIT(self, CUIT):
        query = tickets.select().where(tickets.c.CUIT == str(CUIT))
        result_proxy = conn.execute(query)
        rows = result_proxy.fetchall()
    
        tickets_list = []
        for row in rows:
            ticket = Ticket(
                id=row.id,
                Nombre=row.Nombre,
                Descripcion=row.Descripcion,
                Escenario=row.Escenario,
                Estado=row.Estado,
                Severidad=row.Severidad,
                idVersion=row.idVersion,
                CUIT=row.CUIT
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
            ticket = TicketConNombre(
                id=row.id,
                Nombre=row.Nombre,
                Descripcion=row.Descripcion,
                Escenario=row.Escenario,
                Estado=row.Estado,
                Severidad=row.Severidad,
                idVersion=row.idVersion,
                nombreProducto= versionService.getProductoByIdVersion(idVersion).Nombre,
                CUIT=row.CUIT
            )
            tickets_list.append(ticket)
        
        return tickets_list