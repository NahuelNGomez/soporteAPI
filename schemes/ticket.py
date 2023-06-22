from pydantic import BaseModel
from typing import Optional

import requests
#Se utiliza la API del modulo de recursos
urlRecursos = "https://rrhh-squad6-1c2023.onrender.com/recursos"

class Ticket(BaseModel):
    id: Optional[int]
    Nombre: str
    Descripcion: str
    Escenario: str
    Estado: str
    Severidad: str
    idVersion: int
    CUIT: str
    RecursoAsignado: int

    def asignar(self,Nombre, Descripcion, Escenario, Estado, Severidad, idVersion, CUIT, RecursoAsignado):
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.Escenario = Escenario
        self.Estado = Estado
        self.Severidad = Severidad
        self.idVersion = idVersion
        self.CUIT = CUIT
        self.RecursoAsignado =  RecursoAsignado


    def verificarRecurso(self, recursoAsignado):

        empleados = requests.get(urlRecursos).json()
        ids = [int(empleado["legajo"]) for empleado in empleados]
        return (recursoAsignado in ids)

    def verificarEstado(self):
        return ((self.Estado == "Nuevo") or (self.Estado == "En curso") or (self.Estado == "Cerrado"))
    
    def verificarSeveridad(self):
        return ((self.Severidad == "S1") or (self.Severidad == "S2") or (self.Severidad == "S3") or (self.Severidad == "S4"))

    def verificarError(self):
        excepcion = None
        if (not self.verificarEstado()):
            excepcion = "Estado Invalido (Nuevo - En progreso - Cerrado)"
        if (not self.verificarSeveridad()):
            excepcion = "Severidad Invalida (S1 - S2 - S3 - S4)"
        if (not self.verificarRecurso(self.RecursoAsignado)):
            excepcion = "Recurso a asignar invalido"

        return excepcion
