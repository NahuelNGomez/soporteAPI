<<<<<<< HEAD
from pydantic import BaseModel
=======
from pydantic import BaseModel, Field
>>>>>>> tests
from typing import Optional

class TareaAsignada(BaseModel):
    codigoDeAsignacion: Optional[int]
<<<<<<< HEAD
    idTarea: int
=======
    idTarea: int #= Field(default_factory=int) #@Autogenerate
>>>>>>> tests
    id: int #Id de ticket