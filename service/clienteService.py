from config.db import conn
from models.models import clientes
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import requests


class ClienteService():

    def getClientes(self):
        return conn.execute(clientes.select()).fetchall()
    
    def getClienteByCUIT(self, CUIT):
        return conn.execute(clientes.select().where(clientes.c.CUIT == CUIT)).first()

    def crearCliente(self, new_cliente):
        return conn.execute(clientes.insert().values(new_cliente))
        
    def addClientes(self):
        r = requests.get("https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes")
        if r.status_code == 200:
            try: 
                for i in range(0,len(r.json())):
                    cliente = {"CUIT": r.json()[i]["CUIT"],
                            "Nombre": r.json()[i]["razon social"]
                        }
                    conn.execute(clientes.insert().values(cliente))
            except:
                print("el cliente ya estaba agregado")    