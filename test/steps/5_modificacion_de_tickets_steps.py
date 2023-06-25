from behave import *
from selenium import webdriver
from models.models import tickets
from typing import Dict
from datetime import date

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

# Se modifica un ticket existente
@given(u'un ticket cargado')
def step_impl(context):
    inicializarProductoYVersion()
    idVersion = versionService.getLastIdVersionAdded()
    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S3",
                "idVersion":idVersion,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }
    ticketService.crearTicket(context.ticket1)
    context.ticket1 = {"id": ticketService.getLastIdTicketAdded(),
                       "FechaDeCreacion": date.today,
                  "Nombre":"TICKET_PRUEBA",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S3",
                "idVersion":idVersion,
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
            }
    pass

@when(u'busque un ticket por alguno de los filtros disponibles')
def step_impl(context):
    assert(context.ticket1["id"] != None)
    pass

@then(u'podre realizarle alguna modificacion de: "{nombre_ticket}", "{severidad}", "{des_problema}", "{des_escenario}", "{estado}"')
def step_impl(context, nombre_ticket, severidad, des_problema, des_escenario, estado):
    update_data: Dict[str, str] = {
        "Nombre": nombre_ticket,
        "Descripcion": des_problema,
        "Escenario": des_escenario,
        "Estado": estado,
        "Severidad": severidad
    }
    
    ticketService.updateTicket(context.ticket1["id"], update_data)
    ticket1 = ticketService.getTicketByID(context.ticket1["id"])

    assert(ticket1.Nombre == nombre_ticket)
    assert(ticket1.Descripcion == des_problema)
    assert(ticket1.Escenario == des_escenario)
    assert(ticket1.Estado == estado)
    assert(ticket1.Severidad == severidad)

    ticketService.deleteTicket(context.ticket1["id"])
    eliminarProductoYVersion()
    