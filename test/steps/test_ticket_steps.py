from behave import *
from selenium import webdriver

@given('Ticket con estado "En curso"')
def ticket_con_estado_en_curso(context):
    raise NotImplementedError(u'STEP: Given Ticket con estado "En curso"')


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