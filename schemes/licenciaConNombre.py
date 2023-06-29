from pydantic import BaseModel

class LicenciaConNombre(BaseModel):
    idVersion: int
    nombre: str
    CUIT: str