from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    CUIT: str
    Nombre: str