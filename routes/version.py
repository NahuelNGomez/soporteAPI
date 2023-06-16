from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import versiones
from schemes.version import Version

version = APIRouter()

@version.get('/versiones', response_model=List[Version], tags=["Versiones"])
def get_versiones():
    return conn.execute(versiones.select()).fetchall()

@version.post('/versiones', response_model=Version, tags=["Versiones"])
def create_version(version: Version):
    newVersion = {
    "CodigoVersion": version.CodigoVersion,
    "CodigoDeProducto": version.CodigoDeProducto,
    "Estado": version.Estado
}
    conn.execute(versiones.insert().values(newVersion))
    return newVersion