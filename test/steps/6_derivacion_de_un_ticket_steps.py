from behave import *
from selenium import webdriver
from models.models import tickets
from datetime import date, timedelta

from schemes.ticket import Ticket
from schemes.version import Version
from schemes.tareaAsignadaCompleta import TareaAsignadaCompleta
from service.productoService import ProductoService
from service.ticketService import TicketService
from service.tareaAsignadaService import TareaAsignadaService
from service.versionService import VersionService

ticketService = TicketService()
tareaService = TareaAsignadaService()
productoService = ProductoService()
versionService = VersionService()

# los test fallan porque en service, al crear la tarea, "title" genera una keyerror
# no puedo conectarme a la base de proyectos desde el back,
# la logica del test esta ok, con los metodos correctos.

# se deriva un ticket

codigoProducto = None
idVersion = None
def inicializarProductoYVersion():
    nuevoProducto = {"Nombre": "Producto Para Test"}
    
    productoService.crearProducto(nuevoProducto)
    codigoProducto = productoService.getLastCodigoProductoAdded()
    nuevaVersion = {
        "CodigoVersion": "2.0",
        "CodigoProducto": codigoProducto,
        "idProyecto": 1,
        "Estado": "Nuevo"
    }
    
    versionService.crearVersion(nuevaVersion)

def eliminarProductoYVersion():
    idVersion = versionService.getLastIdVersionAdded()
    codigoProducto = productoService.getLastCodigoProductoAdded()
    versionService.deleteVersion(idVersion)
    productoService.deleteProducto(codigoProducto)

@given(u'una tarea necesaria para resolver un ticket')
def step_impl(context):
    idVersion = versionService.getLastIdVersionAdded()

    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA_6",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": idVersion,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2,
                "FechaDeFinalizacion": date.today() + timedelta(days=15)
                  }
    ticketService.crearTicket(context.ticket1)
    context.ticket1.update({"id": ticketService.getLastIdTicketAdded()})
    
    context.tarea1 = {
        "id": context.ticket1["id"],
        "idTarea": 16,
        "title":"prueba-6"
        }
    tareaService.crearTareaAsignada(context.tarea1)
    context.tarea1.update({"codigoDeAsignacion": tareaService.getLastCodigoDeAsignacionAdded()})
    
    pass


@when(u'se asigne la tarea al ticket')
def step_impl(context):
    assert(len(tareaService.getTareasAsignadasByIdTicket(context.ticket1["id"])) >= 1)


@then(u'se vinculara el ticket con la tarea')
def step_impl(context):
    assert(tareaService.getTareasAsignadasByIdTicket(context.ticket1["id"]) != None)
    
    # limpio
    ticketService.deleteTicket(context.ticket1["id"])
    tareaService.deleteTareaAsignada(context.tarea1["codigoDeAsignacion"])




# se vinculan varias tareas con un ticket
@given(u'varias tareas necesarias para resolver un ticket')
def step_impl(context):
    idVersion = versionService.getLastIdVersionAdded()
    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA_6",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": idVersion,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2,
                "FechaDeFinalizacion": date.today() + timedelta(days=15)
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
    assert(len(tareaService.getTareasAsignadasByIdTicket(context.ticket1["id"])) == 1)
    assert(len(tareaService.getTareasAsignadasByIdTicket(context.ticket2["id"])) == 1)


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
    idVersion = versionService.getLastIdVersionAdded()
    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA_6",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": idVersion,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2,
                "FechaDeFinalizacion": date.today() + timedelta(days=15)
                  }
    ticketService.crearTicket(context.ticket1)
    context.ticket1.update({"id": ticketService.getLastIdTicketAdded()})
    
    context.ticket2 ={
                "Nombre":"TICKET_PRUEBA_6",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": idVersion,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2,
                "FechaDeFinalizacion": date.today() + timedelta(days=15)
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
    assert(len(tareaService.getTareasAsignadasByIdTicket(context.ticket1["id"])) == 2)


@then(u'se vincularan los tickets con la tarea')
def step_impl(context):
    assert(len(tareaService.getTareasAsignadasByIdTicket(context.ticket1["id"])) == 1)
    assert(len(tareaService.getTareasAsignadasByIdTicket(context.ticket2["id"])) == 1)

    # limpio
    ticketService.deleteTicket(context.ticket1["id"])
    ticketService.deleteTicket(context.ticket2["id"])
    tareaService.deleteTareaAsignada(context.tarea1["codigoDeAsignacion"])
    tareaService.deleteTareaAsignada(context.tarea2["codigoDeAsignacion"])
