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
from service.versionService import VersionService

productService = ProductoService()
versionService = VersionService()
codigoProducto = None
idVersion = None

def inicializarProductoYVersion():
    nuevoProducto = {"Nombre": "Producto Para Test"}
    
    productService.crearProducto(nuevoProducto)
    codigoProducto = productService.getLastCodigoProductoAdded()
    nuevaVersion = {
        "CodigoVersion": "2.0",
        "CodigoProducto": codigoProducto,
        "Estado": "Nuevo"
    }
    
    versionService.crearVersion(nuevaVersion)


def eliminarProductoYVersion():
    idVersion = versionService.getLastIdVersionAdded()
    codigoProducto = productService.getLastCodigoProductoAdded()
    versionService.deleteVersion(idVersion)
    productService.deleteProducto(codigoProducto)

@given(u'una lista de prodcutos y versiones')
def step_impl(context):
    inicializarProductoYVersion()

@when(u'quiera conocer los productos y sus versiones disponibles')
def step_impl(context):
    idVersion = versionService.getLastIdVersionAdded()
    codigoProducto = productService.getLastCodigoProductoAdded()
    assert(productService.getProducto(codigoProducto) != None)
    assert(versionService.getVersion(idVersion) != None)


@then(u'se me informaran todos los productos con sus versiones disponibles')
def step_impl(context):
    codigoProducto = productService.getLastCodigoProductoAdded()
    assert((productService.getProducto(codigoProducto)).Nombre == 
          ("Producto Para Test"))
    eliminarProductoYVersion()
   