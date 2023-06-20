from pydantic import BaseModel
from typing import Optional

class Reporte(BaseModel):
    idVersion: int
    NombreProducto: str
    CodigoVersion: str
    PromedioS1: int
    PromedioS2: int
    PromedioS3: int
    PromedioS4: int