from fastapi import FastAPI
from routes.ticket import ticket
from routes.producto import producto
from routes.version import version
from routes.cliente import cliente, add_clientes
from routes.licencia import licencia
from routes.reporte import reporte
from routes.tareaAsignada import tareaAsignada
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(ticket)
app.include_router(producto)
app.include_router(version)
app.include_router(cliente)
app.include_router(licencia)
app.include_router(reporte)
app.include_router(tareaAsignada)

add_clientes()

origins = [
    "http://localhost:3000",  # Origen permitido (puedes añadir más si es necesario)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)