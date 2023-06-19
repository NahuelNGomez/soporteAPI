from pydantic import BaseModel


class Licencia(BaseModel):
    CodigoVersion: int
    CodigoProducto: int
    CUIL: int