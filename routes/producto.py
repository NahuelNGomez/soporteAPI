from fastapi import APIRouter
from typing import List
from schemes.producto import Producto
from schemes.ticket import Ticket
from schemes.ticketConNombre import TicketConNombre
from service.productoService import ProductoService
from sqlalchemy.exc import IntegrityError
from service.ticketService import TicketService
from fastapi import APIRouter, HTTPException, Response, status
from starlette.status import HTTP_204_NO_CONTENT

producto = APIRouter()
productoService = ProductoService()
ticketService = TicketService()

@producto.get('/productos', response_model=List[Producto], tags=["Productos"])
def get_producto():
    return productoService.getProductos()

@producto.post('/productos', response_model=Producto, tags=["Productos"])
def create_producto(producto: Producto):
    nuevoProducto = {"Nombre": producto.Nombre}
    try:
        productoService.crearProducto(nuevoProducto)
    except IntegrityError:
            raise HTTPException(status_code=500, detail="Error en parámetros")
    return {"CodigoProducto": productoService.getLastCodigoProductoAdded(),
             "Nombre": producto.Nombre,
            }

@producto.get('/productos/{CodigoProducto}', response_model=Producto, tags=["Productos"])
def get_producto(codigoProducto: int):
    return productoService.getProducto(codigoProducto)

@producto.delete('/productos/{CodigoProducto}', status_code= status.HTTP_204_NO_CONTENT, tags=["Productos"])
def delete_ticket(CodigoProducto:int):
    result = productoService.deleteProducto(CodigoProducto)
    return Response(status_code=HTTP_204_NO_CONTENT)