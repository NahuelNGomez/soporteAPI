from fastapi import APIRouter, HTTPException, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.models import productos
from schemes.producto import Producto
from sqlalchemy.exc import IntegrityError

producto = APIRouter()


@producto.get('/productos', response_model=List[Producto], tags=["Productos"])
def get_producto():
    return conn.execute(productos.select()).fetchall()

@producto.post('/productos', response_model=Producto, tags=["Productos"])
def create_producto(producto: Producto):
    auxProducto = {"Nombre": producto.Nombre}
    try: 
        conn.execute(productos.insert().values(auxProducto))
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error en parámetros")
    conn.execute(productos.select()).fetchall()[-1].CodigoProducto
    return {"CodigoProducto": conn.execute(productos.select()).fetchall()[-1].CodigoProducto,
             "Nombre": producto.Nombre,
            }