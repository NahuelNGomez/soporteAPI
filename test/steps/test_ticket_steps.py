from behave import *
from selenium import webdriver
from models.models import tickets

from schemes.ticket import Ticket
from schemes.producto import Producto
from schemes.cliente import Cliente


# Creacion de Ticket
@given('un cliente y un producto')
def un_cliente_y_un_producto(context):
    context.cliente1 = Cliente()  #"20-4548272-9", "cliente1")
    context.producto1 = Producto()

    #cliente1 = Cliente()
    #producto1 = Producto()

@When('quiera informar un nuevo ticket de un producto debere informar: {nombre:d}, {severidad:d}, {problema:d}, {escenario:d}')
def quiera_informar_un_nuevo_ticket_de_producto(context, nombre, severidad, problema, escenario):
    print(nombre)
    print(severidad)
    print(problema)
    print(escenario)


"""
@given('Ticket con estado "En curso"')
def ticket_con_estado_en_curso(context):
    ticket1 = Ticket()



@when(u'Se Completa un Ticket')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Se Completa un Ticket')


@then(u'Ticket no debe tener estado "En curso"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Ticket no debe tener estado "En curso"')


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