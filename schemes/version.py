from pydantic import BaseModel
from typing import Optional

class Version(BaseModel):
    CodigoVersion: int
    CodigoDeProducto: int
    Estado: str
    
    class Config:
        orm_mode = True
        fields = {"CodigoVersion": "CodigoVersion", "CodigoDeProducto": "CodigoDeProducto", "Estado": "Estado"}