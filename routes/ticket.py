from datetime import date
from fastapi import APIRouter, HTTPException, Response, status
from pydantic import Field
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import tickets
from schemes.ticket import Ticket
from sqlalchemy.exc import IntegrityError
from typing import Dict
from handlers.verifications import *
from service.ticketService import TicketService

ticket = APIRouter()

ticketService = TicketService()

@ticket.get('/tickets', response_model=List[Ticket], tags=["Tickets"])
def get_tickets():
    return ticketService.getTickets()
@ticket.post('/tickets', response_model=Ticket, tags=["Tickets"])
def create_ticket(ticket: Ticket):
    newTicket = {"Nombre": ticket.Nombre,
                  "Descripcion": ticket.Descripcion,
                  "Escenario": ticket.Escenario,
                  "Estado": ticket.Estado,
                  "Severidad": ticket.Severidad,
                  "idVersion": ticket.idVersion,
                  "CUIT": ticket.CUIT,
                  "RecursoAsignado": ticket.RecursoAsignado
                  }
    exception = ticket.verificarError()
    if (exception != None):
        raise HTTPException(status_code=500, detail=exception)
    try: 
        ticketService.crearTicket(newTicket)
    except IntegrityError:
       raise HTTPException(status_code=500, detail="Error en parámetros")
    return {"id": ticketService.getLastIdTicketAdded(),
            "FechaDeCreacion": date.today(),
                  "Nombre": ticket.Nombre,
                  "Descripcion": ticket.Descripcion,
                  "Escenario": ticket.Escenario,
                  "Estado": ticket.Estado,
                  "Severidad": ticket.Severidad,
                  "idVersion": ticket.idVersion,
                  "CUIT": ticket.CUIT,
                  "RecursoAsignado": ticket.RecursoAsignado
            }

@ticket.get('/tickets/{ticket_id}', response_model=Ticket, tags=["Tickets"])
def get_ticket(id:int):
    return ticketService.getTicketByID(id)

#@ticket.get('/tickets/CUIT/{CUIT}', response_model=List[Ticket], tags=["Tickets"])
#def get_ticket(CUIT:str):
 #   return ticketService.getTicketByCUIT(CUIT)

@ticket.delete('/tickets/{id}', status_code= status.HTTP_204_NO_CONTENT, tags=["Tickets"])
def delete_ticket(id:int):
    result = ticketService.deleteTicket(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@ticket.put('/tickets/{id}', response_model=Ticket, tags=["Tickets"])
def update_ticket(id: int, ticket: Dict):
    

    update_data = {k: v for k, v in ticket.items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No se incluyó ningún campo para actualizar")
    excepcion = verificarDatosActualizados(update_data)
    if (excepcion):
        raise HTTPException(status_code=500, detail=excepcion)
    try:
        ticketService.updateTicket(id, update_data)
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error updating ticket")

    return ticketService.getTicket(id)