from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class Version(BaseModel):
    idVersion: Optional[int]
    #idVersion: UUID = Field(default_factory=uuid4) #@Autogenerate
    #idVersion: int = Field(default_factory=int) #@Autogenerate
    idProyecto: Optional[int]
    CodigoVersion: str
    CodigoProducto: int
    Estado: str
    
    def verificarEstado(self):
        return ((self.Estado == "Nuevo") or (self.Estado == "En desarrollo") or (self.Estado == "Terminado"))


