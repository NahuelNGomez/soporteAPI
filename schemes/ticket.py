from pydantic import BaseModel
from typing import Optional

class Ticket(BaseModel):
    id: Optional[str]
    Nombre: str
    Descripcion: str
    Escenario: str
    Estado: str
    Severidad: str
