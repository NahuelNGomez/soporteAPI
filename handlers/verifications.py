
from typing import Dict
from datetime import date, datetime


def verificarEstado(estado, data):
    if ((estado != "Nuevo") and (estado != "En progreso") and (estado != "Cerrado")) :
        return  "Estado Invalido (Nuevo - En progreso - Cerrado)"
    if (estado == 'Cerrado'):
        data["FechaDeFinalizacion"] = (date.today())
        
    return None    

def verificarSeveridad(severidad):
    if ((severidad != "S1") and (severidad != "S2") and (severidad != "S3") and (severidad != "S4")):
        return "Severidad Invalida (S1 - S2 - S3 - S4)"
    
def verificarFechaDeFinalizacion(fechaDeFinalizacion):
    
    fecha_date = datetime.strptime(fechaDeFinalizacion, "%Y-%m-%d").date()
    
    return (fecha_date >= date.today())

def verificarDatosActualizados(data):
    error = None
    if ("FechaDeFinalizacion" in data):
        error = verificarFechaDeFinalizacion(data["FechaDeFinalizacion"])
    if ("Estado" in data):
        error = verificarEstado(data["Estado"], data)
    if ("Severidad" in data):
        error = verificarSeveridad(data["Severidad"])
    return error