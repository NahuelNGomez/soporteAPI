from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.ticket import tickets
from schemes.ticket import Ticket
ticket = APIRouter()

@ticket.get('/tickets', response_model=List[Ticket], tags=["Tickets"])
def get_tickets():
    return conn.execute(tickets.select()).fetchall()
@ticket.post('/tickets', response_model=Ticket, tags=["Tickets"])
def create_ticket(ticket: Ticket):
    newTicket = {"Nombre": ticket.Nombre,
                  "Descripcion": ticket.Descripcion,
                  "Escenario": ticket.Escenario,
                  "Estado": ticket.Estado,
                  "Severidad": ticket.Severidad
                  }
    conn.execute(tickets.insert().values(newTicket))
    return newTicket

@ticket.get('/tickets/{id}', response_model=Ticket, tags=["Tickets"])
def get_ticket(id:str):
    return conn.execute(tickets.select().where(tickets.c.id == id)).first()

@ticket.delete('/tickets/{id}', status_code= status.HTTP_204_NO_CONTENT, tags=["Tickets"])
def delete_ticket(id:str):
    result = conn.execute(tickets.delete().where(tickets.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@ticket.put('/tickets/{id}', response_model=Ticket, tags=["Tickets"])
def update_ticket(id:str, ticket: Ticket):
    result = conn.execute(tickets.update().values(Nombre = ticket.Nombre,
                                                   Descripcion = ticket.Descripcion,
                                                   Escenario = ticket.Escenario,
                                                   Estado = ticket.Estado,
                                                   Severidad = ticket.Severidad).where(tickets.c.id == id))
    return conn.execute(tickets.select().where(tickets.c.id == id)).first()