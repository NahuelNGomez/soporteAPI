from fastapi import APIRouter, Response, status, HTTPException
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import versiones
from schemes.ticketConNombre import TicketConNombre
from schemes.version import Version
from sqlalchemy.exc import IntegrityError
from schemes.versionConNombre import VersionConNombre
from service.ticketService import TicketService
from service.versionService import VersionService

version = APIRouter()
versionService = VersionService()
ticketService = TicketService()

@version.get('/versiones', response_model=List[VersionConNombre], tags=["Versiones"])
def get_versiones():
    return versionService.getVersiones()

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
        versionService.crearVersion(newVersion) 
    except IntegrityError:
            raise HTTPException(status_code=500, detail="Error en parámetros")
    
    return {"idVersion": versionService.getLastIdVersionAdded(),
                "CodigoVersion": version.CodigoVersion,
                "CodigoProducto": version.CodigoProducto,
                "Estado": version.Estado
            }

@version.get('/versiones/{idVersion}', response_model=Version, tags=["Versiones"])
def get_producto(idVersion: int):
    return versionService.getVersion(idVersion)

@version.get('/versiones/{idVersion}/tickets', response_model=List[TicketConNombre], tags=["Versiones"])
def get_tickets(idVersion: int):
    return ticketService.getTicketsByIdVersion(idVersion)