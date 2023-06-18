from fastapi import APIRouter, HTTPException, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import tickets
from schemes.ticket import Ticket
from sqlalchemy.exc import IntegrityError
from typing import Dict
from handlers.verifications import *

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
                  "Severidad": ticket.Severidad,
                  "CodigoProducto": ticket.CodigoProducto,
                  "CodigoVersion": ticket.CodigoVersion
                  }
    exception = ticket.verificarError()
    if (exception != None):
        raise HTTPException(status_code=500, detail=exception)
    try: 
        conn.execute(tickets.insert().values(newTicket))
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error en parámetros")
    return {"id": conn.execute(tickets.select()).fetchall()[-1].id,
                  "Nombre": ticket.Nombre,
                  "Descripcion": ticket.Descripcion,
                  "Escenario": ticket.Escenario,
                  "Estado": ticket.Estado,
                  "Severidad": ticket.Severidad,
                  "CodigoProducto": ticket.CodigoProducto,
                  "CodigoVersion": ticket.CodigoVersion
            }

@ticket.get('/tickets/{id}', response_model=Ticket, tags=["Tickets"])
def get_ticket(id:str):
    return conn.execute(tickets.select().where(tickets.c.id == id)).first()

@ticket.delete('/tickets/{id}', status_code= status.HTTP_204_NO_CONTENT, tags=["Tickets"])
def delete_ticket(id:str):
    result = conn.execute(tickets.delete().where(tickets.c.id == id))
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
        conn.execute(tickets.update().values(**update_data).where(tickets.c.id == int(id)))
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error updating user")

    return conn.execute(tickets.select().where(tickets.c.id == int(id))).first()