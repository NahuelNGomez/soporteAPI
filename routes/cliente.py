from fastapi import APIRouter, HTTPException, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import clientes
from schemes.cliente import Cliente
from sqlalchemy.exc import IntegrityError
import requests
import json


cliente = APIRouter()



@cliente.get('/clientes', response_model=List[Cliente], tags=["Clientes"])
def get_clientes():
    return conn.execute(clientes.select()).fetchall()

@cliente.post('/clientes', response_model=Cliente, tags=["Clientes"])
def create_cliente(cliente: Cliente):
    new_cliente = {"CUIT": cliente.CUIT,
                   "Nombre": cliente.Nombre
                   }
    try: 
        conn.execute(clientes.insert().values(new_cliente))
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error en parámetros")
    return new_cliente

def add_clientes():

    r = requests.get("https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes")
    if r.status_code == 200:
        print()
        try: 
            for i in range(0,len(r.json())):
                cliente = {"CUIT": r.json()[i]["CUIT"],
                        "Nombre": r.json()[i]["razon social"]
                    }
                conn.execute(clientes.insert().values(cliente))
        except:
            print("el cliente ya estaba agregado")
