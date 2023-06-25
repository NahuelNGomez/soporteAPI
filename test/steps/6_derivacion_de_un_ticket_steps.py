from behave import *
from selenium import webdriver
from models.models import tickets
from datetime import date

from schemes.ticket import Ticket
from schemes.version import Version
from schemes.producto import Producto
from schemes.cliente import Cliente
from service.ticketService import TicketService


ticketService = TicketService()

# se deriva un ticket
@given(u'una tarea necesaria para resolver un ticket')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given una tarea necesaria para resolver un ticket')


@when(u'se cree la tarea en el proyecto')
def step_impl(context):
    raise NotImplementedError(u'STEP: When se cree la tarea en el proyecto')


@then(u'se podra vincular la tarea con el ticket')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then se podra vincular la tarea con el ticket')




# se vinculan varias tareas con un ticket
@given(u'varias tareas necesarias para resolver un ticket')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given varias tareas necesarias para resolver un ticket')


@when(u'se creen las tareas en un proyecto')
def step_impl(context):
    raise NotImplementedError(u'STEP: When se creen las tareas en un proyecto')


@then(u'se podran vincular a un ticket')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then se podran vincular a un ticket')




# se vincula una tarea con varios tickets
@given(u'una tarea necesaria para resolver varios tickets')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given una tarea necesaria para resolver varios tickets')


@when(u'se cree la tarea en un proyecto')
def step_impl(context):
    raise NotImplementedError(u'STEP: When se cree la tarea en un proyecto')


@then(u'se podran vincular varios tickets con una tarea')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then se podran vincular varios tickets con una tarea')
