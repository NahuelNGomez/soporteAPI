from fastapi import FastAPI
from routes.ticket import ticket
from routes.producto import producto
from routes.version import version
from routes.cliente import cliente, add_clientes
from routes.licencia import licencia


app = FastAPI()
app.include_router(ticket)
app.include_router(producto)
app.include_router(version)
app.include_router(cliente)
app.include_router(licencia)

add_clientes()
