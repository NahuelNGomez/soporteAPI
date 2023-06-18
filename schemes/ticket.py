from pydantic import BaseModel
from typing import Optional

class Ticket(BaseModel):
    id: Optional[str]
    Nombre: str
    Descripcion: str
    Escenario: str
    Estado: str
    Severidad: str
    CodigoProducto: int
    CodigoVersion: int

    def verificarEstado(self):
        return ((self.Estado == "Nuevo") or (self.Estado == "En progreso") or (self.Estado == "Cerrado"))
    
    def verificarSeveridad(self):
        return ((self.Severidad == "S1") or (self.Severidad == "S2") or (self.Severidad == "S3") or (self.Severidad == "S4"))

    def verificarError(self):
        excepcion = None
        if (not self.verificarEstado()):
            excepcion = "Estado Invalido (Nuevo - En progreso - Cerrado)"
        if (not self.verificarSeveridad()):
            excepcion = "Severidad Invalida (S1 - S2 - S3 - S4)"
        return excepcion
