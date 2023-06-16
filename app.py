from fastapi import FastAPI
from routes.ticket import ticket
from routes.producto import producto

app = FastAPI()
app.include_router(ticket)
app.include_router(producto)
