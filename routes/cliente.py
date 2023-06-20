from fastapi import APIRouter, HTTPException, Response, status
from starlette.status import HTTP_204_NO_CONTENT

from typing import List
from service.clienteService import ClienteService
from schemes.cliente import Cliente
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

import json

cliente = APIRouter()

clienteService = ClienteService()

@cliente.get('/clientes', response_model=List[Cliente], tags=["Clientes"])
def get_clientes():
    return clienteService.getClientes()

@cliente.post('/clientes', response_model=Cliente, tags=["Clientes"])
def create_cliente(cliente: Cliente):
    new_cliente = {"CUIT": cliente.CUIT,
                   "Nombre": cliente.Nombre
                   }
    try:
        clienteService.crearCliente(new_cliente)
    except IntegrityError:
            raise HTTPException(status_code=500, detail="Error en parámetros")
    return new_cliente

def add_clientes():
    clienteService.addClientes()
