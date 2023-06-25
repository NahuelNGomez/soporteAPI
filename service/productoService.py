from config.db import conn
from models.models import productos


class ProductoService():

    def getProductos(self):
        return conn.execute(productos.select()).fetchall()
    
    def crearProducto(self, nuevoProducto):
        return conn.execute(productos.insert().values(nuevoProducto))
    
    def getProducto(self, codigoProducto):
        return conn.execute(productos.select().where(productos.c.CodigoProducto == codigoProducto)).first()
    
    #def getProductoByIdVersion(self, idVersion):
    #    return conn.execute(productos.select().where(productos.c.idVersion == idVersion))

    def getCodigoProductoByNombre(self, nombre):
        prod = conn.execute(productos.select().where(productos.c.Nombre == nombre)).first()
        if prod != None:
            return prod.CodigoProducto
        return None

        
    def getLastCodigoProductoAdded(self):
        return conn.execute(productos.select()).fetchall()[-1].CodigoProducto
    
    def deleteProducto(self, id):
        return conn.execute(productos.delete().where(productos.c.CodigoProducto == id))