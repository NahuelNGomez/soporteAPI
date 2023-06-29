from config.db import conn
from models.models import licencias
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from schemes.licenciaConNombre import LicenciaConNombre
from service.clienteService import ClienteService

clienteService = ClienteService()

class LicenciaService():

    def getLicencias(self):
        return conn.execute(licencias.select()).fetchall()
    
    def crearLicencia(self, nuevaLicencia):
        return conn.execute(licencias.insert().values(nuevaLicencia))
    
    def getLicenciasByIdVersion(self, idVersion):
        query = licencias.select().where(licencias.c.idVersion == idVersion)
        result_proxy = conn.execute(query)
        rows = result_proxy.fetchall()
    
        licencias_list = []
        for row in rows:
            licencia = LicenciaConNombre(
                idVersion=row.idVersion,
                nombre=clienteService.getClienteByCUIT(row.CUIT).Nombre,
                CUIT=row.CUIT,
            )
            licencias_list.append(licencia)
        
        return licencias_list