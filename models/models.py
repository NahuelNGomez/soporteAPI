from sqlalchemy import ForeignKey, Table, Column, ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta, engine



productos = Table("productos", meta, 
    Column("CodigoProducto", Integer, primary_key=True),
    Column("Nombre", String(255))
)

versiones = Table(
    "versiones",
    meta,
    Column("CodigoVersion", Integer, primary_key=True),
    Column("CodigoProducto", Integer, ForeignKey("productos.CodigoProducto", ondelete="CASCADE"), nullable=False),
    Column("Estado", String(255)),
)

clientes = Table("clientes", meta, 
    Column("CUIL", Integer, primary_key=True),
    Column("Nombre", String(255))
)

tickets = Table("tickets", meta, 
    Column("id", Integer, primary_key=True),
    Column("Nombre", String(255)),
    Column("Descripcion", String(255)),
    Column("Escenario", String(255)),
    Column("Estado", String(255)),
    Column("Severidad", String(255)),
    Column("CodigoProducto", Integer, ForeignKey("productos.CodigoProducto", ondelete="CASCADE"), nullable=False),
    Column("CodigoVersion", Integer, ForeignKey("versiones.CodigoVersion", ondelete="CASCADE"), nullable=False)
)

meta.create_all(engine)