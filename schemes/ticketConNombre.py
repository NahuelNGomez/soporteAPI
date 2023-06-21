from pydantic import BaseModel

class TicketConNombre(BaseModel):
    id: int
    Nombre: str
    Descripcion: str
    Escenario: str
    Estado: str
    Severidad: str
    idVersion: int
    nombreProducto: str
    CUIT: str