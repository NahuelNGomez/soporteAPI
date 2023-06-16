from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta, engine

tickets = Table("tickets", meta, Column(
    "id", Integer, primary_key=True),
      Column("Nombre", String(255)),
      Column("Descripcion", String(255)),
      Column("Escenario", String(255)),
      Column("Estado", String(255)),
      Column("Severidad", String(255)))


meta.create_all(engine)
