from fastapi import APIRouter

from schemes.reporte import Reporte
from service.reporteService import ReporteService

reporte = APIRouter()

reporteService = ReporteService()

@reporte.get('/reportes/{idVersion}', response_model=Reporte, tags=["Reportes"])
def get_producto(idVersion: int):
    return reporteService.getReporte(idVersion)

