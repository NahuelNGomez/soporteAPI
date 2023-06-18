from pydantic import BaseModel
from typing import Optional

class Version(BaseModel):
    CodigoVersion: int
    CodigoProducto: int
    Estado: str
    
    class Config:
        orm_mode = True
        fields = {"CodigoVersion": "CodigoVersion", "CodigoProducto": "CodigoProducto", "Estado": "Estado"}

    def verificarEstado(self):
        return ((self.Estado == "Nuevo") or (self.Estado == "En desarrollo") or (self.Estado == "Terminado"))
