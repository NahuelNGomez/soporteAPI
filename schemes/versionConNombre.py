from pydantic import BaseModel

class VersionConNombre(BaseModel):
    idVersion: int
    CodigoVersion: str
    CodigoProducto: int
    NombreProducto: str
    Estado: str