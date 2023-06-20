from fastapi import APIRouter, HTTPException, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import licencias
from schemes.licencia import Licencia
from sqlalchemy.exc import IntegrityError

licencia = APIRouter()

@licencia.get('/licencias', response_model=List[Licencia], tags=["Licencias"])
def get_licencias():
    return conn.execute(licencias.select()).fetchall()

@licencia.post('/licencias', response_model=Licencia, tags=["Licencias"])
def create_licencia(licencia: Licencia):
    licencia_nueva = {"CodigoVersion": licencia.CodigoVersion,
                   "CUIT": licencia.CUIT,
                   "CodigoProducto": licencia.CodigoProducto
                   }
    try: 
        conn.execute(licencias.insert().values(licencia_nueva))
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error en parámetros")
    return licencia_nueva