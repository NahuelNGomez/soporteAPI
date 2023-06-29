from behave import *
from selenium import webdriver
from models.models import tickets
from datetime import date

from schemes.ticket import Ticket
from schemes.version import Version
from schemes.producto import Producto
from schemes.cliente import Cliente
from service.ticketService import TicketService
from service.productoService import ProductoService
from service.versionService import VersionService

ticketService = TicketService()
productService = ProductoService()
versionService = VersionService()

@given(u'una lista de tickets, una lista de productos con nombre: "{producto}" y una lista de sus versiones')
def step_impl(context, producto):
    # carga de producto
    context.producto1 = {
        "Nombre": producto
        }
    productService.crearProducto(context.producto1)
    context.producto1 = {
        "id": productService.getLastCodigoProductoAdded(),
        "Nombre": producto
        }

    assert(productService.getCodigoProductoByNombre(producto) != None)
    
    # carga de versiones
    context.version1 = {
        "CodigoVersion": "1.2.3",
        "CodigoProducto": (productService.getProducto(context.producto1["id"])).CodigoProducto,
        "Estado": "Terminado"
        }
    versionService.crearVersion(context.version1)
    context.version1 = {
        "id": versionService.getLastIdVersionAdded(),
        "CodigoVersion": "1.2.3",
        "CodigoProducto": (productService.getProducto(context.producto1["id"])).CodigoProducto,
        "Estado": "Terminado"
        }

    context.version2 = {
        "CodigoVersion": "1.2.4",
        "CodigoProducto": (productService.getProducto(context.producto1["id"])).CodigoProducto,
        "Estado": "Terminado"
        }
    versionService.crearVersion(context.version2)
    context.version2 = {
        "id": versionService.getLastIdVersionAdded(),
        "CodigoVersion": "1.2.4",
        "CodigoProducto": (productService.getProducto(context.producto1["id"])).CodigoProducto,
        "Estado": "Terminado"
        }

    assert(versionService.getVersion(context.version1["id"]) != None)
    assert(versionService.getVersion(context.version2["id"]) != None)
    assert(versionService.getVersion(context.version2["id"]) != 
           versionService.getVersion(context.version1["id"]))

    # carga de tickets
    context.ticket1 ={
                "Nombre":"TICKET_PRUEBA",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": context.version1["id"],
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }
    ticketService.crearTicket(context.ticket1)
    context.ticket1 = {
                "id": ticketService.getLastIdTicketAdded(),
                "FechaDeCreacion": date.today,
                "Nombre":"TICKET_PRUEBA",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S1",
                "idVersion": context.version1["id"],
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
            }

    context.ticket2 ={
                "Nombre":"TICKET_PRUEBA_2",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S2",
                "idVersion": context.version2["id"],
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }
    ticketService.crearTicket(context.ticket2)
    context.ticket2 ={
                "id": ticketService.getLastIdTicketAdded(),
                "FechaDeCreacion": date.today,
                "Nombre":"TICKET_PRUEBA_2",
                "Descripcion":"DESCRIPCION",
                "Escenario":"ESCENARIO",
                "Estado": "Nuevo",
                "Severidad":"S2",
                "idVersion": context.version2["id"],
                "CUIT":"20-12345678-3",
                "RecursoAsignado": 2
                  }

    assert(context.ticket1["id"] != context.ticket2["id"])

    
@when(u'quiera encontrar un ticket')
def step_impl(context):
    assert(ticketService.getTicketByID(context.ticket1["id"]) != None)
    assert(ticketService.getTicketByID(context.ticket2["id"]) != None)



@then(u'podre filtrar los tickets por: "{cliente}", "{severidad}", "{producto}", "{id_ticket}", "{id_version}"')
def step_impl(context, cliente, severidad, producto, id_ticket, id_version):
    # por id:
    # se fuerza el id, porque depende de la carga real de la base de datos:
    id_ticket = context.ticket1["id"]
    assert(ticketService.getTicketByID(id_ticket) != None)

    # por version:
    # se fuerza el id, porque depende de la carga real de la base de datos:
    id_version = context.ticket1["id"]
    #assert(len(ticketService.getTicketsByIdVersion(id_version)) == 1)

    # por nombre producto:
    #print(str(len(ticketService.getTicketByProducto(producto))))
    assert(len(ticketService.getTicketByProducto(producto)) == 2)

    # por cliente:
    assert(len(ticketService.getTicketByCUIT(context.ticket1["CUIT"])) >= 2)

    # por severidad:
    assert(len(ticketService.getTicketBySeveridad(context.ticket1["Severidad"])) >= 2)

    # se borran tickets:
    ticketService.deleteTicket(context.ticket1["id"])
    ticketService.deleteTicket(context.ticket2["id"])

    # se borran productos:
    productService.deleteProducto(context.producto1["id"])

    # se borran versiones:
    versionService.deleteVersion(context.version1["id"])
    versionService.deleteVersion(context.version2["id"])
