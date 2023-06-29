from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class Version(BaseModel):
    idVersion: Optional[int]
    #idVersion: UUID = Field(default_factory=uuid4) #@Autogenerate
<<<<<<< HEAD
    idVersion: int = Field(default_factory=int) #@Autogenerate
    idProyecto: Optional[int]
=======
    #idVersion: int = Field(default_factory=int) #@Autogenerate
>>>>>>> tests
    CodigoVersion: str
    CodigoProducto: int
    Estado: str
    
    def verificarEstado(self):
        return ((self.Estado == "Nuevo") or (self.Estado == "En desarrollo") or (self.Estado == "Terminado"))


