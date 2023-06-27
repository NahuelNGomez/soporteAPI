from datetime import date
from pydantic import BaseModel, root_validator, validator, Field
from typing import Optional
from uuid import UUID, uuid4
import requests
urlRecursos = "https://rrhh-squad6-1c2023.onrender.com/recursos"

class Ticket(BaseModel):
    #id: Optional[int]
    #id: UUID = Field(default_factory=uuid4) #@Autogenerate
    id: int = Field(default_factory=int) #@Autogenerate 
    FechaDeCreacion: Optional[date]
    FechaDeFinalizacion: date
    Nombre: str
    Descripcion: str
    Escenario: str
    Estado: str = Field(default_factory="Nuevo")
    Severidad: str
    idVersion: int
    CUIT: str
    RecursoAsignado: int

    class Config:
        use_enum_values = True
        allow_population_by_field_name = True
        validate_assigment = True

    @validator("Estado", pre=True, always=True)
    def set_estado(cls, Estado):
        return Estado or "Nuevo"

    @root_validator(pre=True)
    def set_default_fecha_creacion(cls, values):
        if not values.get('FechaDeCreacion'):
            values['FechaDeCreacion'] = date.today()
        return values
    
    def asignar(self,Nombre, Descripcion, Escenario, Estado, Severidad, idVersion, CUIT, RecursoAsignado):
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.Escenario = Escenario
        self.Estado = Estado
        self.Severidad = Severidad
        self.idVersion = idVersion
        self.CUIT = CUIT
        self.RecursoAsignado =  RecursoAsignado

    def verificarEstado(self):
        return ((self.Estado == "Nuevo") or (self.Estado == "En progreso") or (self.Estado == "Cerrado"))
    
    def verificarSeveridad(self):
        return ((self.Severidad == "S1") or (self.Severidad == "S2") or (self.Severidad == "S3") or (self.Severidad == "S4"))

    def verificarFechas(self):
        return (((self.FechaDeFinalizacion - self.FechaDeCreacion).days) >= 0)
    
    def verificarFechaDeCreacion(self):
        return self.FechaDeCreacion <= date.today()

    def verificarError(self):
        excepcion = None
        if (not self.verificarEstado()):
            excepcion = "Estado Invalido (Nuevo - En progreso - Cerrado)"
        if (not self.verificarSeveridad()):
            excepcion = "Severidad Invalida (S1 - S2 - S3 - S4)"
        if (not self.verificarFechas()):
            excepcion = "La fecha de finalizacion no puede ser anterior a la fecha de creacion"
        if (not self.verificarFechaDeCreacion()):
            excepcion = "La fecha de creacion no puede ser posterior al día de hoy"       

        return excepcion

    def estaCerrado(self):
        return self.Estado == "Cerrado"