from pydantic import BaseModel
from typing import Optional

class Version(BaseModel):
    idVersion: Optional[int]
    CodigoVersion: str
    CodigoProducto: int
    Estado: str
    
    def verificarEstado(self):
        return ((self.Estado == "Nuevo") or (self.Estado == "En desarrollo") or (self.Estado == "Terminado"))
