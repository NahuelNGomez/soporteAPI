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
from service.versionService import VersionService

productService = ProductoService()
versionService = VersionService()

@given(u'una lista de prodcutos y versiones')
def step_impl(context):
    # carga de productos:
    context.product1 = {
        "Nombre": "producto_1"
        }
    productService.crearProducto(context.product1)
    context.product1 = {
        "id": productService.getLastCodigoProductoAdded(),
        "Nombre": "producto_1"
        }

    # carga de versiones:
    context.version1 = {
        "CodigoVersion": "1.2.3",
        "CodigoProducto": (productService.getProducto(context.product1["id"])).CodigoProducto,
        "Estado": "Terminado"
        }
    versionService.crearVersion(context.version1)
    context.version1 = {
        "id": versionService.getLastIdVersionAdded(),
        "CodigoVersion": "1.2.3",
        "CodigoProducto": (productService.getProducto(context.product1["id"])).CodigoProducto,
        "Estado": "Terminado"
        }
    pass

@when(u'quiera conocer los productos y sus versiones disponibles')
def step_impl(context):
    assert(productService.getProducto(context.product1["id"]) != None)
    assert(versionService.getVersion(context.version1["id"]) != None)


@then(u'se me informaran todos los productos con sus versiones disponibles')
def step_impl(context):
  
   assert((productService.getProducto(context.product1["id"])).Nombre == 
          (context.product1["Nombre"]))
   assert((versionService.getVersion(context.version1["id"])).CodigoVersion == 
          context.version1["CodigoVersion"])

   productService.deleteProducto(context.product1["id"])
   versionService.deleteVersion(context.version1["id"])
   