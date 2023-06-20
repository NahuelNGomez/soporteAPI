from config.db import conn
from models.models import versiones
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


class VersionService():

    def getVersiones(self):
        return conn.execute(versiones.select()).fetchall()
    
    def crearVersion(self, nuevaVersion):
        return conn.execute(versiones.insert().values(nuevaVersion))

    def getVersion(self, idVersion):
        return conn.execute(versiones.select().where(versiones.c.idVersion == idVersion)).first()
        
    def getLastIdVersionAdded(self):
        return conn.execute(versiones.select()).fetchall()[-1].idVersion