from pydantic import BaseModel


class Licencia(BaseModel):
    idVersion: int
    CUIT: str