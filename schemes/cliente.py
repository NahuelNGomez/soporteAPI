from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    CUIL: int
    Nombre: str