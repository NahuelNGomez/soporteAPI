from behave import *
from selenium import webdriver
from models.models import tickets
from typing import Dict
from datetime import date, timedelta

from schemes.ticket import Ticket
from schemes.version import Version
from schemes.producto import Producto
from schemes.cliente import Cliente
from service.productoService import ProductoService
from service.ticketService import TicketService
from service.versionService import VersionService

ticketService = TicketService()
versionService = VersionService()
productoService = ProductoService()

#ASUMO QUE SIEMPRE EXISTE UNA PRODUCTO Y SU VERSION
codigoProducto = None
idVersion = None
def inicializarProductoYVersion():
    nuevoProducto = {"Nombre": "Producto Para Test"}
    
    productoService.crearProducto(nuevoProducto)
    codigoProducto = productoService.getLastCodigoProductoAdded()
    nuevaVersion = {
        "CodigoVersion": "2.0",
        "CodigoProducto": codigoProducto,
        "Estado": "Nuevo"
    }
    
    versionService.crearVersion(nuevaVersion)

def eliminarProductoYVersion():
    idVersion = versionService.getLastIdVersionAdded()
    codigoProducto = productoService.getLastCodigoProductoAdded()
    versionService.deleteVersion(idVersion)
    productoService.deleteProducto(codigoProducto)


# Finalzacion de un ticket
@given('Ticket con "{estado_curso}" "En curso"')
def ticket_con_estado_en_curso(context, estado_curso):
    inicializarProductoYVersion()
    idVersion = versionService.getLastIdVersionAdded()
    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": estado_curso,
                "Severidad":"S1",
                "idVersion":1,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2,
                "FechaDeFinalizacion": date.today() + timedelta(days=15)
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
                "RecursoAsignado": 2,
                "FechaDeFinalizacion": date.today() + timedelta(days=15)
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
    eliminarProductoYVersion()