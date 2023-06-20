
from schemes.reporte import Reporte
from service.productoService import ProductoService
from service.versionService import VersionService

versionService = VersionService()
productoService = ProductoService()

class ReporteService():

    def getReporte(self, idVersion):
         version = versionService.getVersion(idVersion)
         
         reporte = Reporte(
                idVersion=version.idVersion,
                NombreProducto=productoService.getProducto(version.CodigoProducto).Nombre,
                CodigoVersion=version.CodigoVersion,
                PromedioS1=0,
                PromedioS2=0,
                PromedioS3=0,
                PromedioS4=0,
            )
         return reporte
