from sqlalchemy import ForeignKey, PrimaryKeyConstraint, Table, Column, ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import UniqueConstraint

from config.db import meta, engine

meta.drop_all(engine)

productos = Table("productos", meta, 
    Column("CodigoProducto", Integer, primary_key=True),
    Column("Nombre", String(255)),
)

versiones = Table(
    "versiones",
    meta,
    Column("idVersion", Integer, nullable=False, primary_key=True),
    Column("CodigoVersion", String, nullable=False),
    Column("CodigoProducto", Integer, ForeignKey("productos.CodigoProducto", ondelete="CASCADE"), nullable=False),
    Column("Estado", String(255)),
)

clientes = Table("clientes", meta, 
    Column("CUIT", String, primary_key=True),
    Column("Nombre", String(255))
)

tickets = Table("tickets", meta, 
    Column("id", Integer, primary_key=True),
    Column("Nombre", String(255)),
    Column("Descripcion", String(255)),
    Column("Escenario", String(255)),
    Column("Estado", String(255)),
    Column("Severidad", String(255)),
    Column("idVersion", Integer, ForeignKey("versiones.idVersion",ondelete="CASCADE"), nullable=False),
    Column("CUIT", String, ForeignKey("clientes.CUIT", ondelete="CASCADE"), nullable=False),
    Column("RecursoAsignado", Integer)
)

licencias = Table("licencias", meta, 
    Column("idVersion", Integer, ForeignKey("versiones.idVersion",ondelete="CASCADE"), primary_key=True, nullable=False),
    Column("CUIT", String, ForeignKey("clientes.CUIT",ondelete="CASCADE"), primary_key=True, nullable=False),
)

meta.create_all(engine)