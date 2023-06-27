
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
                PromedioS1=versionService.getPromedioTickets("S1"),
                PromedioS2=versionService.getPromedioTickets("S2"),
                PromedioS3=versionService.getPromedioTickets("S3"),
                PromedioS4=versionService.getPromedioTickets("S4")
            )
         return reporte
