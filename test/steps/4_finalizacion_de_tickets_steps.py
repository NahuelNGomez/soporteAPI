from behave import *
from selenium import webdriver
from models.models import tickets
from typing import Dict
from datetime import date

from schemes.ticket import Ticket
from schemes.version import Version
from schemes.producto import Producto
from schemes.cliente import Cliente
from service.ticketService import TicketService

ticketService = TicketService()

# Finalzacion de un ticket
@given('Ticket con "{estado_curso}" "En curso"')
def ticket_con_estado_en_curso(context, estado_curso):
    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": estado_curso,
                "Severidad":"S1",
                "idVersion":1,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }
    ticketService.crearTicket(context.ticket1)
    context.ticket1 = {"id": ticketService.getLastIdTicketAdded(),
                       "FechaDeCreacion": date.today,
                  "Nombre":"TICKET_PRUEBA",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": estado_curso,
                "Severidad":"S1",
                "idVersion":1,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
            }
    pass

@when(u'Se resuelva el problema')
def step_impl(context):
    update_data: Dict[str, str] = {
        "Estado": "Cerrado"
    }
    
    ticketService.updateTicket(context.ticket1["id"], update_data)
    pass


@then(u'Ticket debera tener el "{estado_cerrado}" "Cerrado"')
def step_impl(context, estado_cerrado):
    assert(ticketService.getTicketByID(context.ticket1["id"]).Estado == estado_cerrado)
    ticketService.deleteTicket(context.ticket1["id"])