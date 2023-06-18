from typing import Dict


def verificarEstado(estado):
    if ((estado != "Nuevo") and (estado != "En progreso") and (estado != "Cerrado")) :
        return "Estado Invalido (Nuevo - En progreso - Cerrado)"

def verificarSeveridad(severidad):
    if ((severidad != "S1") and (severidad != "S2") and (severidad != "S3") and (severidad != "S4")):
        return "Severidad Invalida (S1 - S2 - S3 - S4)"

def verificarDatosActualizados(data):
    error = None
    if ("Estado" in data):
        error = verificarEstado(data["Estado"])
    if ("Severidad" in data):
        error = verificarSeveridad(data["Severidad"])
    return error