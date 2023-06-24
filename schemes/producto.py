from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class Producto(BaseModel):
    #CodigoProducto: Optional[int]
    CodigoProducto: UUID = Field(default_factory=uuid4) #@Autogenerate
    Nombre: str