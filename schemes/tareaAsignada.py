from pydantic import BaseModel
from typing import Optional

class TareaAsignada(BaseModel):
    codigoDeAsignacion: Optional[int]
    idTarea: int
    id: int #Id de ticket