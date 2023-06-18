from fastapi import APIRouter, HTTPException, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import clientes
from schemes.cliente import Cliente
from sqlalchemy.exc import IntegrityError

cliente = APIRouter()

@cliente.get('/clientes', response_model=List[Cliente], tags=["Clientes"])
def get_clientes():
    return conn.execute(clientes.select()).fetchall()

@cliente.post('/clientes', response_model=Cliente, tags=["Clientes"])
def create_cliente(cliente: Cliente):
    new_cliente = {"CUIL": cliente.CUIL,
                   "Nombre": cliente.Nombre
                   }
    try: 
        conn.execute(clientes.insert().values(new_cliente))
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error en parámetros")
    return new_cliente