from fastapi import APIRouter
from typing import List
from schemes.tareaAsignada import TareaAsignada
from schemes.tareaAsignadaCompleta import TareaAsignadaCompleta

from schemes.ticket import Ticket
from schemes.ticketConNombre import TicketConNombre
from service.productoService import ProductoService
from sqlalchemy.exc import IntegrityError
from service.tareaAsignadaService import TareaAsignadaService
from service.ticketService import TicketService
from fastapi import APIRouter, HTTPException, Response, status
from starlette.status import HTTP_204_NO_CONTENT

tareaAsignada = APIRouter()
tareaAsignadaService = TareaAsignadaService()
ticketService = TicketService()




@tareaAsignada.get('/tareasAsignadas', response_model=List[TareaAsignada], tags=["Tareas Asignadas"])
def get_tareas_asignadas():
    return tareaAsignadaService.getTareasAsignadas()

@tareaAsignada.post('/tareasAsignadas', response_model=TareaAsignada, tags=["Tareas Asignadas"])
def create_tarea_asignada(tareaAsignada: TareaAsignada):
    nuevaTarea = {"idTarea": tareaAsignada.idTarea,
                     "id": tareaAsignada.id}
    try:
        tareaAsignadaService.crearTareaAsignada(nuevaTarea)
    except IntegrityError:
            raise HTTPException(status_code=500, detail="Error en parámetros")
    return { "codigoDeAsignacion": tareaAsignadaService.getLastCodigoDeAsignacionAdded(),
            "idTarea": tareaAsignada.idTarea,
            "id": tareaAsignada.id}

@tareaAsignada.get('/tareasAsignadas/{idTicket}', response_model=List[TareaAsignadaCompleta], tags=["Tareas Asignadas"])
def get_tarea_by_IdTicket(idTicket: int):
    return tareaAsignadaService.getTareasAsignadasByIdTicket(idTicket)

@tareaAsignada.delete('/tareasAsignadas/{codigoDeAsignacion}', status_code= status.HTTP_204_NO_CONTENT, tags=["Tareas Asignadas"])
def delete_asignada(codigoDeAsignacion:int):
    result = tareaAsignadaService.deleteTareaAsignada(codigoDeAsignacion)
    return Response(status_code=HTTP_204_NO_CONTENT)