
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
                PromedioS1=versionService.getPromedioTickets("S1", version.idVersion),
                PromedioS2=versionService.getPromedioTickets("S2", version.idVersion),
                PromedioS3=versionService.getPromedioTickets("S3", version.idVersion),
                PromedioS4=versionService.getPromedioTickets("S4", version.idVersion)
            )
         return reporte
