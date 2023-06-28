from pydantic import BaseModel
from typing import Optional

class TareaAsignadaCompleta(BaseModel):
    codigoDeAsignacion: Optional[int]
    idTarea: int
    id: int #Id de ticket
    nombre: str
    estado: str
    prioridad: str
    recursoAsignado: str
