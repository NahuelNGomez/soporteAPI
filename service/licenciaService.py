from config.db import conn
from models.models import licencias
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

class LicenciaService():

    def getLicencias(self):
        return conn.execute(licencias.select()).fetchall()
    
    def crearLicencia(self, nuevaLicencia):
        return conn.execute(licencias.insert().values(nuevaLicencia))