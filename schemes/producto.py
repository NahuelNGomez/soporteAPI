from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    CodigoProducto: Optional[str]
    Nombre: str