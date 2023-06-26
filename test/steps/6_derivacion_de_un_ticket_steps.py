from behave import *
from selenium import webdriver
from models.models import tickets
from datetime import date

from schemes.ticket import Ticket
from schemes.version import Version
from schemes.tareaAsignada import TareaAsignada
from service.ticketService import TicketService
from service.tareaAsignadaService import TareaAsignadaService

ticketService = TicketService()
tareaService = TareaAsignadaService()

# se deriva un ticket
@given(u'una tarea necesaria para resolver un ticket')
def step_impl(context):

    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA_6",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": 2,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }
    ticketService.crearTicket(context.ticket1)
    context.ticket1.update({"id": ticketService.getLastIdTicketAdded()})
    
    context.tarea1 = {
        "id": context.ticket1["id"],
        "idTarea": 0
        }
    tareaService.crearTareaAsignada(context.tarea1)
    context.tarea1.update({"codigoDeAsignacion": tareaService.getLastCodigoDeAsignacionAdded()})
    
    pass


@when(u'se asigne la tarea al ticket')
def step_impl(context):
    assert(len(tareaService.getTareasAsignadasByIdTarea(context.tarea1["idTarea"])) >= 1)


@then(u'se vinculara el ticket con la tarea')
def step_impl(context):
    assert(tareaService.getTareasAsignadasByIdTicket(context.ticket1["id"]) != None)
    
    # limpio
    ticketService.deleteTicket(context.ticket1["id"])
    tareaService.deleteTareaAsignada(context.tarea1["codigoDeAsignacion"])




# se vinculan varias tareas con un ticket
@given(u'varias tareas necesarias para resolver un ticket')
def step_impl(context):
    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA_6",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": 2,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }
    ticketService.crearTicket(context.ticket1)
    context.ticket1.update({"id": ticketService.getLastIdTicketAdded()})
    
    context.tarea1 = {
        "id": context.ticket1["id"],
        "idTarea": 0
        }
    tareaService.crearTareaAsignada(context.tarea1)
    context.tarea1.update({"codigoDeAsignacion": tareaService.getLastCodigoDeAsignacionAdded()})
    
    context.tarea2 = {
        "id": context.ticket1["id"],
        "idTarea": 6
        }
    tareaService.crearTareaAsignada(context.tarea2)
    context.tarea2.update({"codigoDeAsignacion": tareaService.getLastCodigoDeAsignacionAdded()})
    pass


@when(u'se asignen las tareas al ticket')
def step_impl(context):
    assert(len(tareaService.getTareasAsignadasByIdTarea(context.tarea1["idTarea"])) == 1)
    assert(len(tareaService.getTareasAsignadasByIdTarea(context.tarea2["idTarea"])) == 1)


@then(u'se vinculara el ticket con las tareas')
def step_impl(context):
    assert(len(tareaService.getTareasAsignadasByIdTicket(context.ticket1["id"])) == 2)

    # limpio
    ticketService.deleteTicket(context.ticket1["id"])
    tareaService.deleteTareaAsignada(context.tarea1["codigoDeAsignacion"])
    tareaService.deleteTareaAsignada(context.tarea2["codigoDeAsignacion"])



# se vincula una tarea con varios tickets
@given(u'una tarea necesaria para resolver varios tickets')
def step_impl(context):
    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA_6",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": 2,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }
    ticketService.crearTicket(context.ticket1)
    context.ticket1.update({"id": ticketService.getLastIdTicketAdded()})
    
    context.ticket2 ={
                "Nombre":"TICKET_PRUEBA_6",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": 2,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }
    ticketService.crearTicket(context.ticket2)
    context.ticket2.update({"id": ticketService.getLastIdTicketAdded()})

    # se asigna el primer ticket
    context.tarea1 = {
        "id": context.ticket1["id"],
        "idTarea": 0
        }
    tareaService.crearTareaAsignada(context.tarea1)
    context.tarea1.update({"codigoDeAsignacion": tareaService.getLastCodigoDeAsignacionAdded()})

    # se asigna el segundo ticket
    context.tarea2 = {
        "id": context.ticket2["id"],
        "idTarea": 0
        }
    tareaService.crearTareaAsignada(context.tarea2)
    context.tarea2.update({"codigoDeAsignacion": tareaService.getLastCodigoDeAsignacionAdded()})

    pass


@when(u'se asigne la tarea a los tickets necesarios')
def step_impl(context):
    assert(len(tareaService.getTareasAsignadasByIdTarea(context.tarea1["idTarea"])) == 2)


@then(u'se vincularan los tickets con la tarea')
def step_impl(context):
    assert(len(tareaService.getTareasAsignadasByIdTicket(context.ticket1["id"])) == 1)
    assert(len(tareaService.getTareasAsignadasByIdTicket(context.ticket2["id"])) == 1)

    # limpio
    ticketService.deleteTicket(context.ticket1["id"])
    ticketService.deleteTicket(context.ticket2["id"])
    tareaService.deleteTareaAsignada(context.tarea1["codigoDeAsignacion"])
    tareaService.deleteTareaAsignada(context.tarea2["codigoDeAsignacion"])
