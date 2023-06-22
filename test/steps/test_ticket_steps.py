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
#ASUMO QUE SIEMPRE EXISTE UNA PRODUCTO Y  SU VERSION CON ID 2

# Creacion de Ticket
@given('un cliente y una version de producto')
def un_cliente_y_un_producto(context):
    pass

@when(u'quiera informar un nuevo ticket de un producto debere informar: <"nombre ticket">, <"severidad">, <"des problema">, <"des escenario">')
def step_impl(context):
    context.ticket1 = {
        "Nombre": "nombre ticket",
        "Descripcion": "des_problema",
        "Escenario": "des_escenario",
        "Estado": "Nuevo",
        "Severidad": "severidad",
        "idVersion": 2,
        "CUIT": "20-12345678-3",
        "RecursoAsignado": 2
    }
    ticketService.crearTicket(context.ticket1)
    context.ticket1 = {"id": ticketService.getLastIdTicketAdded(),
                    "Nombre": "nombre ticket",
                    "Descripcion": "des_problema",
                    "Escenario": "des_escenario",
                    "Estado": "Nuevo",
                    "Severidad": "severidad",
                    "idVersion": 2,
                    "CUIT": "20-12345678-3",
                    "RecursoAsignado": 2
                     }
    
@Then('se creará un ticket con estado "{unEstado}"')
def ticket_con_estado_nuevo(context, unEstado):
    assert(ticketService.getTicketByID(context.ticket1["id"]).Estado == unEstado) 
    ticketService.deleteTicket(context.ticket1["id"])


@given('Ticket con estado "En curso"')
def ticket_con_estado_en_curso(context):
    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado":"En curso",
                "Severidad":"S1",
                "idVersion":2,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }
    ticketService.crearTicket(context.ticket1)
    context.ticket1 = {"id": ticketService.getLastIdTicketAdded(),
                       "FechaDeCreacion": date.today,
                  "Nombre":"TICKET_PRUEBA",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado":"En curso",
                "Severidad":"S1",
                "idVersion":2,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
            }

@when(u'Se Completa un Ticket')
def step_impl(context):
    update_data: Dict[str, str] = {
    "Estado": "Cerrado"
}
    
    ticketService.updateTicket(context.ticket1["id"], update_data)


@then(u'Ticket debe tener estado "{unEstado}"')
def step_impl(context, unEstado):
    assert(ticketService.getTicketByID(context.ticket1["id"]).Estado == unEstado)
    ticketService.deleteTicket(context.ticket1["id"])



@given(u'Soy empleado de mesa de ayuda')
def step_impl(context):
    pass


@when(u'Creo un ticket con un responsable asignado con id "{unID}"')
def step_impl(context, unID):
    context.error = None
    ticket = Ticket(
                Nombre= "TicketPrueba",
                FechaDeCreacion= date.today,
                Descripcion="Decripcion",
                Escenario="escenario",
                Estado="En Curso",
                Severidad="S1",
                idVersion=2,
                CUIT="20-12345678-3",
                RecursoAsignado=unID
            )
    exception = ticket.verificarError()
    if (exception != None):
        context.error = exception
    else:
        ticketService.crearTicket(ticket)



@when(u'Ese responsable no se encuentra en el sistema')
def step_impl(context):
    pass


@then(u'Se emite un error')
def step_impl(context):
    assert(context.error != None)


@when(u'Creo un ticket sin alguno de los atributos obligatorios')
def step_impl(context):
    context.error = None
    try:
        ticket = Ticket(
                    Nombre= "TicketPrueba",
                    FechaDeCreacion= date.today,
                    Descripcion="Decripcion",
                    Estado="En Curso",
                    Severidad="S1",
                    idVersion=2,
                    CUIT="20-12345678-3",
                    RecursoAsignado=2
                )
        exception = ticket.verificarError()
        if (exception != None):
            context.error = exception
        else:
            ticketService.crearTicket(ticket)
    except Exception as error:
        context.error = error



@then(u'El ticket no es creado')
def step_impl(context):
    pass

"""
@given(u'una lista de clientes y un producto')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given una lista de clientes y un producto')


@when(u'quiera informar un nuevo ticket de un producto')
def step_impl(context):
    raise NotImplementedError(u'STEP: When quiera informar un nuevo ticket de un producto')


@then(u'deberé informar producto: versión de producto, cliente, severidad, descripción del problema, descripción del escenario')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then deberé informar producto: versión de producto, cliente, severidad, descripción del problema, descripción del escenario')


@then(u'se creara un ticket con estado "en curso"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then se creara un ticket con estado "en curso"')


@given(u'un producto en especifico')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given un producto en especifico')


@when(u'trato de crear un ticket sin especificar su estado')
def step_impl(context):
    raise NotImplementedError(u'STEP: When trato de crear un ticket sin especificar su estado')


@then(u'el ticket se creará con estado "nuevo".')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el ticket se creará con estado "nuevo".')
"""