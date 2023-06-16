from pydantic import BaseModel
from typing import Optional

class Version(BaseModel):
    CodigoVersion: int
    CodigoProducto: int
    Estado: str
