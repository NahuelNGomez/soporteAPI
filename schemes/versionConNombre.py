from typing import Optional
from pydantic import BaseModel

class VersionConNombre(BaseModel):
    idVersion: int
    idProyecto: Optional[int]
    CodigoVersion: str
    CodigoProducto: int
    NombreProducto: str
    Estado: str