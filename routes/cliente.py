from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.ticket import clientes
from schemes.cliente import Cliente

cliente = APIRouter()

@cliente.get('/clientes', response_model=List[Cliente], tags=["Clientes"])
def get_clientes():
    return conn.execute(clientes.select()).fetchall()

@cliente.post('/clientes', response_model=Cliente, tags=["Clientes"])
def create_cliente(cliente: Cliente):
    new_cliente = {"CUIL": cliente.CUIL,
                   "Nombre": cliente.Nombre
                   }
    conn.execute(clientes.insert().values(new_cliente))
    return new_cliente