from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import productos
from schemes.producto import Producto

producto = APIRouter()


@producto.get('/productos', response_model=List[Producto], tags=["Productos"])
def get_producto():
    return conn.execute(productos.select()).fetchall()

@producto.post('/productos', response_model=Producto, tags=["Productos"])
def create_producto(producto: Producto):
    auxProducto = {"Nombre": producto.Nombre}
    conn.execute(productos.insert().values(auxProducto))
    conn.execute(productos.select()).fetchall()[-1].CodigoProducto
    return {"CodigoProducto": conn.execute(productos.select()).fetchall()[-1].CodigoProducto,
             "Nombre": producto.Nombre,
            }