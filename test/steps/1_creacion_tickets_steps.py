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

@when(u'quiera informar un nuevo ticket de un producto debere informar: "{nombre_ticket}", "{severidad}", "{des_problema}", "{des_escenario}"')
def step_impl(context, nombre_ticket, severidad, des_problema, des_escenario):
    
    context.ticket1 = {
        "Nombre": nombre_ticket,
        "Descripcion": des_problema,
        "Escenario": des_escenario,
        "Estado": "Nuevo",
        "Severidad": severidad,
        "idVersion": 1,
        "CUIT": "20-12345678-3",
        "RecursoAsignado": 2
    }
    ticketService.crearTicket(context.ticket1)
    context.ticket1 = {"id": ticketService.getLastIdTicketAdded(),
                    "Nombre": nombre_ticket,
                    "Descripcion": des_problema,
                    "Escenario": des_escenario,
                    "Estado": "Nuevo",
                    "Severidad": severidad,
                    "idVersion": 1,
                    "CUIT": "20-12345678-3",
                    "RecursoAsignado": 2
                     }
    pass

@Then(u'se creará un ticket con "{estado}" Nuevo')
def ticket_con_estado_nuevo(context, estado):
    assert(ticketService.getTicketByID(context.ticket1["id"]).Estado == estado) 
    ticketService.deleteTicket(context.ticket1["id"])


"""
# Creo un ticket para un empleado que no se encuentra en la empresa
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