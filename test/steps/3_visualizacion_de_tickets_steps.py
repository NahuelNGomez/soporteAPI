from behave import *
from selenium import webdriver
from models.models import tickets

from schemes.ticket import Ticket
from schemes.version import Version
from schemes.producto import Producto
from schemes.cliente import Cliente
from service.productoService import ProductoService
from service.versionService import VersionService


@given(u'que debo encontrar un ticket')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que debo encontrar un ticket')


@then(u'quiera encontrarlo')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then quiera encontrarlo')


@when(u'podre filtrar los tickets por: "{cliente}", "{severidad}", "{producto}", "{id_ticket}"')
def step_impl(context, cliente, severidad, producto, id_ticket):
    raise NotImplementedError(u'STEP: When podre filtrar los tickets por: "{tipo_de_cliente}", "{cliente}", "{severidad}", "{producto}", "{id_ticket}"')
