from fastapi import APIRouter, HTTPException, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import licencias
from schemes.licencia import Licencia
from sqlalchemy.exc import IntegrityError
from service.licenciaService import LicenciaService
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

licencia = APIRouter()
licenciaService = LicenciaService()

@licencia.get('/licencias', response_model=List[Licencia], tags=["Licencias"])
def get_licencias():
    return licenciaService.getLicencias()

@licencia.post('/licencias', response_model=Licencia, tags=["Licencias"])
def create_licencia(licencia: Licencia):
    nuevaLicencia = {"CodigoVersion": licencia.CodigoVersion,
                   "CUIT": licencia.CUIT,
                   "CodigoProducto": licencia.CodigoProducto
                   }
    try:
        licenciaService.crearLicencia(nuevaLicencia)
    except IntegrityError:
            raise HTTPException(status_code=500, detail="Error en parámetros")    
    return nuevaLicencia