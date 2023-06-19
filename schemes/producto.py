from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    CodigoProducto: Optional[int]
    Nombre: str