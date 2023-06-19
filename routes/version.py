from fastapi import APIRouter, Response, status, HTTPException
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import versiones
from schemes.version import Version
from sqlalchemy.exc import IntegrityError
version = APIRouter()

@version.get('/versiones', response_model=List[Version], tags=["Versiones"])
def get_versiones():
    return conn.execute(versiones.select()).fetchall()

@version.post('/versiones', response_model=Version, tags=["Versiones"])
def create_version(version: Version):
    newVersion = {
    "CodigoVersion": version.CodigoVersion,
    "CodigoProducto": version.CodigoProducto,
    "Estado": version.Estado
}
    if(not version.verificarEstado()):
        raise HTTPException(status_code=500, detail="Estado invalido")
    try: 
        conn.execute(versiones.insert().values(newVersion))
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error en parámetros")
    return {"idVersion": conn.execute(versiones.select()).fetchall()[-1].idVersion,
                "CodigoVersion": version.CodigoVersion,
                "CodigoProducto": version.CodigoProducto,
                "Estado": version.Estado
            }