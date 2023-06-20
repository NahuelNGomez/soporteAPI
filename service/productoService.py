from config.db import conn
from models.models import productos


class ProductoService():

    def getProductos(self):
        return conn.execute(productos.select()).fetchall()
    
    def crearProducto(self, nuevoProducto):
        return conn.execute(productos.insert().values(nuevoProducto))
    
    def getProducto(self, codigoProducto):
        return conn.execute(productos.select().where(productos.c.CodigoProducto == codigoProducto)).first()
        
    def getLastCodigoProductoAdded():
        return conn.execute(productos.select()).fetchall()[-1].CodigoProducto