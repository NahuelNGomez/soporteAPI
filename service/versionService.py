from config.db import conn
from models.models import versiones
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from schemes.versionConNombre import VersionConNombre

from service.productoService import ProductoService

productoService = ProductoService()

class VersionService():

    def getVersiones(self):
        versiones_query = conn.execute(versiones.select()).fetchall()
        versiones_list = []
        for row in versiones_query:
            newVersion = VersionConNombre(
                idVersion= row.idVersion,
                CodigoVersion=row.CodigoVersion,
                CodigoProducto=row.CodigoProducto,
                NombreProducto= productoService.getProducto(row.CodigoProducto).Nombre,
                Estado=row.Estado
            )
            versiones_list.append(newVersion)
        
        return versiones_list

    def crearVersion(self, nuevaVersion):
        return conn.execute(versiones.insert().values(nuevaVersion))

    def getVersion(self, idVersion):
        return conn.execute(versiones.select().where(versiones.c.idVersion == idVersion)).first()
        
    def getLastIdVersionAdded(self):
        return conn.execute(versiones.select()).fetchall()[-1].idVersion