from pydantic import BaseModel, Field
from typing import Optional

class TareaAsignada(BaseModel):
    codigoDeAsignacion: Optional[int]
    idTarea: int #= Field(default_factory=int) #@Autogenerate
    id: int #Id de ticket